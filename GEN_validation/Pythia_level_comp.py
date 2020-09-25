import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from ROOT import TH1F, TLorentzVector, TCanvas, TLegend, kRed, kBlue

from math import hypot, pi

#compare mgg samples from sherpa224 and sherpa228
events = Events (['224/HIG-RunIIFall17GS-00010.root'])
events2 = Events (['228/SMP-RunIIFall17GS-00041.root'])

g1_pt = TH1F("leading photon pt","",20,0,200)
g1_pt.SetStats(0)
g2_pt = TH1F("subleading photon pt","",20,0,200)
g2_pt.SetStats(0)
mgg = TH1F("mgg","",16,20,100)
mgg.SetStats(0)
g1_pt_new = TH1F("leading photon pt new","",20,0,200)
g1_pt_new.SetStats(0)
g2_pt_new = TH1F("subleading photon pt new","",20,0,200)
g2_pt_new.SetStats(0)
mgg_new = TH1F("mgg new","",16,20,100)
mgg_new.SetStats(0)

c1= TCanvas("g1pt","g1pt",800,600)
c2= TCanvas("g2pt","g2pt",800,600)
c3= TCanvas("mgg","mgg",800,600)

l1 = TLegend(0.6,0.7,0.9,0.9)
l2 = TLegend(0.6,0.7,0.9,0.9)
l3 = TLegend(0.6,0.7,0.9,0.9)
geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("genParticles")

# loop over events
count= 0
countweighted = 0

for event in events:
    g1 = TLorentzVector(0,0,0,0)
    g2 = TLorentzVector(0,0,0,0)
    temp = TLorentzVector(0,0,0,0)

    gamma_num = 0
    count = count+1
    if count % 100 == 0:
        print "count = " + str(count)

    count +=1

    event.getByLabel(labelPruned, handlePruned)

    pruned = handlePruned.product()

    event.getByLabel(geninfoLabel,geninfo)
    
    for p in pruned :
        if abs(p.pdgId()) == 22 and p.pt() > 10 and abs(p.eta()) < 2.5 and (p.statusFlags().isPrompt()) and p.status() == 1  :
          gamma_num = gamma_num+1
          if g1.Pt()==0:
            g1.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
          elif g2.Pt==0:
            if p.pt()<g1.Pt():
                g2.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
            else:
                temp.SetPtEtaPhiE(g1.Pt(),g1.Eta(),g1.Phi(),g1.E())
                g1.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
                g2.SetPtEtaPhiE(temp.Pt(),temp.Eta(),temp.Phi(),temp.E())
          else:
            if p.pt()>g1.Pt():
                g2.SetPtEtaPhiE(g1.Pt(),g1.Eta(),g1.Phi(),g1.E())
                g1.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
            elif p.pt()>g2.Pt():
                g2.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
            else:
                continue
    if gamma_num<2: continue
    g1_pt.Fill(g1.Pt())
    g2_pt.Fill(g2.Pt())
    mgg.Fill((g1+g2).M())


# loop over events2
count2= 0

for event in events2:
    g1 = TLorentzVector(0,0,0,0)
    g2 = TLorentzVector(0,0,0,0)
    temp = TLorentzVector(0,0,0,0)

    gamma_num = 0
    count2 = count2+1
    if count2 % 100 == 0:
        print "count2 = " + str(count2)

    count2 +=1

    event.getByLabel(labelPruned, handlePruned)

    pruned = handlePruned.product()

    event.getByLabel(geninfoLabel,geninfo)

    for p in pruned :
        if abs(p.pdgId()) == 22 and p.pt() > 10 and abs(p.eta()) < 2.5 and (p.statusFlags().isPrompt()) and p.status() == 1  :
          gamma_num = gamma_num+1
          if g1.Pt()==0:
            g1.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
          elif g2.Pt==0:
            if p.pt()<g1.Pt():
                g2.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
            else:
                temp.SetPtEtaPhiE(g1.Pt(),g1.Eta(),g1.Phi(),g1.E())
                g1.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
                g2.SetPtEtaPhiE(temp.Pt(),temp.Eta(),temp.Phi(),temp.E())
          else:
            if p.pt()>g1.Pt():
                g2.SetPtEtaPhiE(g1.Pt(),g1.Eta(),g1.Phi(),g1.E())
                g1.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
            elif p.pt()>g2.Pt():
                g2.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
            else:
                continue
    if gamma_num<2: continue
    g1_pt_new.Fill(g1.Pt())
    g2_pt_new.Fill(g2.Pt())
    mgg_new.Fill((g1+g2).M())
c1.cd()
g1_pt.SetLineColor(kRed)
g1_pt.GetXaxis().SetTitle('leading photon pt')
g1_pt.Draw('pe')
g1_pt_new.SetLineColor(kBlue)
g1_pt_new.Draw('pe same')
l1.AddEntry(g1_pt,'sherpa 224')
l1.AddEntry(g1_pt_new,'sherpa 228')
l1.Draw()
c1.SaveAs('g1pt.png')

c2.cd()
g2_pt.SetLineColor(kRed)
g2_pt.GetXaxis().SetTitle('subleading photon pt')
g2_pt.Draw('pe')
g2_pt_new.SetLineColor(kBlue)
g2_pt_new.Draw('pe same')
l2.AddEntry(g2_pt,'sherpa 224')
l2.AddEntry(g2_pt_new,'sherpa 228')
l2.Draw()
c2.SaveAs('g2pt.png')

c3.cd()
mgg.SetLineColor(kRed)
mgg.GetXaxis().SetTitle('mgg')
mgg.Draw('pe')
mgg_new.SetLineColor(kBlue)
mgg_new.Draw('pe same')
l3.AddEntry(mgg,'sherpa 224')
l3.AddEntry(mgg_new,'sherpa 228')
l3.Draw()
c3.SaveAs('mgg.png')
