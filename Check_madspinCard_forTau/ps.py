import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from ROOT import TLine, TH1D, TLorentzVector, TCanvas, TPad, TLegend, kRed, kBlue, kFALSE

from math import hypot, pi, cos

events = Events (['./madspin.root'])
events2 = Events (['./nomadspin.root'])

tauphi_mad = TH1D("tau phi madspin","",30,-3,3)
tauphi_mad.SetStats(0)
tauphi_mad.Sumw2()
tauphi_mad.GetYaxis().SetTitle("a.u.")
tauphi_mad.GetYaxis().SetTitleSize(0.05);
tauphi_mad.GetYaxis().SetTitleOffset(0.75);
tauphi_mad.GetXaxis().SetLabelSize(0)
tauphi_mad.SetMinimum(0)
tauphi_nomad = TH1D("tau phi nomadspin","",30,-3,3)
tauphi_nomad.SetStats(0)
tauphi_nomad.Sumw2()

taueta_mad = TH1D("tau eta madspin","",30,-3,3)
taueta_mad.SetStats(0)
taueta_mad.Sumw2()
taueta_mad.GetYaxis().SetTitle("a.u.")
taueta_mad.GetYaxis().SetTitleSize(0.05);
taueta_mad.GetYaxis().SetTitleOffset(0.75);
taueta_mad.GetXaxis().SetLabelSize(0)
taueta_mad.SetMinimum(0)
taueta_nomad = TH1D("tau eta nomadspin","",30,-3,3)
taueta_nomad.SetStats(0)
taueta_nomad.Sumw2()

taupt_mad = TH1D("tau pt madspin","",20,0,200)
taupt_mad.SetStats(0)
taupt_mad.Sumw2()
taupt_mad.GetYaxis().SetTitle("a.u.")
taupt_mad.GetYaxis().SetTitleSize(0.05);
taupt_mad.GetYaxis().SetTitleOffset(0.75);
taupt_mad.GetXaxis().SetLabelSize(0)
taupt_mad.SetMinimum(0)
taupt_nomad = TH1D("tau pt nomadspin","",20,0,200)
taupt_nomad.SetStats(0)
taupt_nomad.Sumw2()

nphi_mad = TH1D("neutrino cosphi madspin","",20,-1,1)
nphi_mad.SetStats(0)
nphi_mad.Sumw2()
nphi_mad.GetYaxis().SetTitle("a.u.")
nphi_mad.GetYaxis().SetTitleSize(0.05);
nphi_mad.GetYaxis().SetTitleOffset(0.75);
nphi_mad.GetXaxis().SetLabelSize(0)
nphi_mad.SetMinimum(0)
nphi_nomad = TH1D("neutrino cosphi nomadspin","",20,-1,1)
nphi_nomad.SetStats(0)
nphi_nomad.Sumw2()

elephi_mad = TH1D("ele cosphi madspin","",20,-1,1)
elephi_mad.SetStats(0)
elephi_mad.Sumw2()
elephi_mad.GetYaxis().SetTitle("a.u.")
elephi_mad.GetYaxis().SetTitleSize(0.05);
elephi_mad.GetYaxis().SetTitleOffset(0.75);
elephi_mad.GetXaxis().SetLabelSize(0)
elephi_mad.SetMinimum(0)
elephi_nomad = TH1D("ele cosphi nomadspin","",20,-1,1)
elephi_nomad.SetStats(0)
elephi_nomad.Sumw2()

muphi_mad = TH1D("mu cosphi madspin","",20,-1,1)
muphi_mad.SetStats(0)
muphi_mad.Sumw2()
muphi_mad.GetYaxis().SetTitle("a.u.")
muphi_mad.GetYaxis().SetTitleSize(0.05);
muphi_mad.GetYaxis().SetTitleOffset(0.75);
muphi_mad.GetXaxis().SetLabelSize(0)
muphi_mad.SetMinimum(0)
muphi_nomad = TH1D("mu cosphi nomadspin","",20,-1,1)
muphi_nomad.SetStats(0)
muphi_nomad.Sumw2()

TrueMET_mad = TH1D("TrueMET madspin","",20,0,100)
TrueMET_mad.SetStats(0)
TrueMET_mad.Sumw2()
TrueMET_mad.GetYaxis().SetTitle("a.u.")
TrueMET_mad.GetYaxis().SetTitleSize(0.05);
TrueMET_mad.GetYaxis().SetTitleOffset(0.75);
TrueMET_mad.GetXaxis().SetLabelSize(0)
TrueMET_mad.SetMinimum(0)
TrueMET_nomad = TH1D("TrueMET nomadspin","",20,-1,1)
TrueMET_nomad.SetStats(0)
TrueMET_nomad.Sumw2()

CaloMET_mad = TH1D("CaloMET madspin","",20,0,100)
CaloMET_mad.SetStats(0)
CaloMET_mad.Sumw2()
CaloMET_mad.GetYaxis().SetTitle("a.u.")
CaloMET_mad.GetYaxis().SetTitleSize(0.05);
CaloMET_mad.GetYaxis().SetTitleOffset(0.75);
CaloMET_mad.GetXaxis().SetLabelSize(0)
CaloMET_mad.SetMinimum(0)
CaloMET_nomad = TH1D("CaloMET nomadspin","",20,-1,1)
CaloMET_nomad.SetStats(0)
CaloMET_nomad.Sumw2()

JetpT_mad = TH1D("JetpT madspin","",20,0,200)
JetpT_mad.SetStats(0)
JetpT_mad.Sumw2()
JetpT_mad.GetYaxis().SetTitle("a.u.")
JetpT_mad.GetYaxis().SetTitleSize(0.05);
JetpT_mad.GetYaxis().SetTitleOffset(0.75);
JetpT_mad.GetXaxis().SetLabelSize(0)
JetpT_mad.SetMinimum(0)
JetpT_nomad = TH1D("JetpT nomadspin","",20,0,200)
JetpT_nomad.SetStats(0)
JetpT_nomad.Sumw2()

NonuJetpT_mad = TH1D("NonuJetpT madspin","",20,0,200)
NonuJetpT_mad.SetStats(0)
NonuJetpT_mad.Sumw2()
NonuJetpT_mad.GetYaxis().SetTitle("a.u.")
NonuJetpT_mad.GetYaxis().SetTitleSize(0.05);
NonuJetpT_mad.GetYaxis().SetTitleOffset(0.75);
NonuJetpT_mad.GetXaxis().SetLabelSize(0)
NonuJetpT_mad.SetMinimum(0)
NonuJetpT_nomad = TH1D("NonuJetpT nomadspin","",20,0,200)
NonuJetpT_nomad.SetStats(0)
NonuJetpT_nomad.Sumw2()

c1= TCanvas("tauphi","tauphi",800,600)
tauphi_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
tauphi_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
tauphi_pad1.SetFillColor(0)
tauphi_pad1.SetLineColor(0)
tauphi_pad2.SetFillColor(0)
tauphi_pad2.SetLineColor(0)
tauphi_pad1.SetBottomMargin(0.03);
tauphi_pad2.SetTopMargin(0.15);
tauphi_pad2.SetBottomMargin(0.3);
tauphi_pad1.Draw()
tauphi_pad2.Draw()

c2= TCanvas("taueta","taueta",800,600)
taueta_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
taueta_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
taueta_pad1.SetFillColor(0)
taueta_pad1.SetLineColor(0)
taueta_pad2.SetFillColor(0)
taueta_pad2.SetLineColor(0)
taueta_pad1.SetBottomMargin(0.03);
taueta_pad2.SetTopMargin(0.15);
taueta_pad2.SetBottomMargin(0.3);
taueta_pad1.Draw()
taueta_pad2.Draw()

c3= TCanvas("taupt","taupt",800,600)
taupt_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
taupt_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
taupt_pad1.SetFillColor(0)
taupt_pad1.SetLineColor(0)
taupt_pad2.SetFillColor(0)
taupt_pad2.SetLineColor(0)
taupt_pad1.SetBottomMargin(0.03);
taupt_pad2.SetTopMargin(0.15);
taupt_pad2.SetBottomMargin(0.3);
taupt_pad1.Draw()
taupt_pad2.Draw()

c4= TCanvas("neuphi","neuphi",800,600)
nphi_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
nphi_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
nphi_pad1.SetFillColor(0)
nphi_pad1.SetLineColor(0)
nphi_pad2.SetFillColor(0)
nphi_pad2.SetLineColor(0)
nphi_pad1.SetBottomMargin(0.03);
nphi_pad2.SetTopMargin(0.15);
nphi_pad2.SetBottomMargin(0.3);
nphi_pad1.Draw()
nphi_pad2.Draw()

c5= TCanvas("elephi","elephi",800,600)
elephi_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
elephi_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
elephi_pad1.SetFillColor(0)
elephi_pad1.SetLineColor(0)
elephi_pad2.SetFillColor(0)
elephi_pad2.SetLineColor(0)
elephi_pad1.SetBottomMargin(0.03);
elephi_pad2.SetTopMargin(0.15);
elephi_pad2.SetBottomMargin(0.3);
elephi_pad1.Draw()
elephi_pad2.Draw()

c6= TCanvas("muphi","muphi",800,600)
muphi_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
muphi_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
muphi_pad1.SetFillColor(0)
muphi_pad1.SetLineColor(0)
muphi_pad2.SetFillColor(0)
muphi_pad2.SetLineColor(0)
muphi_pad1.SetBottomMargin(0.03);
muphi_pad2.SetTopMargin(0.15);
muphi_pad2.SetBottomMargin(0.3);
muphi_pad1.Draw()
muphi_pad2.Draw()

c7= TCanvas("TrueMET","TrueMET",800,600)
TrueMET_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
TrueMET_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
TrueMET_pad1.SetFillColor(0)
TrueMET_pad1.SetLineColor(0)
TrueMET_pad2.SetFillColor(0)
TrueMET_pad2.SetLineColor(0)
TrueMET_pad1.SetBottomMargin(0.03);
TrueMET_pad2.SetTopMargin(0.15);
TrueMET_pad2.SetBottomMargin(0.3);
TrueMET_pad1.Draw()
TrueMET_pad2.Draw()

c8= TCanvas("CaloMET","CaloMET",800,600)
CaloMET_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
CaloMET_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
CaloMET_pad1.SetFillColor(0)
CaloMET_pad1.SetLineColor(0)
CaloMET_pad2.SetFillColor(0)
CaloMET_pad2.SetLineColor(0)
CaloMET_pad1.SetBottomMargin(0.03);
CaloMET_pad2.SetTopMargin(0.15);
CaloMET_pad2.SetBottomMargin(0.3);
CaloMET_pad1.Draw()
CaloMET_pad2.Draw()

c9= TCanvas("JetpT","JetpT",800,600)
JetpT_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
JetpT_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
JetpT_pad1.SetFillColor(0)
JetpT_pad1.SetLineColor(0)
JetpT_pad2.SetFillColor(0)
JetpT_pad2.SetLineColor(0)
JetpT_pad1.SetBottomMargin(0.03);
JetpT_pad2.SetTopMargin(0.15);
JetpT_pad2.SetBottomMargin(0.3);
JetpT_pad1.Draw()
JetpT_pad2.Draw()

c10= TCanvas("NonuJetpT","NonuJetpT",800,600)
NonuJetpT_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
NonuJetpT_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
NonuJetpT_pad1.SetFillColor(0)
NonuJetpT_pad1.SetLineColor(0)
NonuJetpT_pad2.SetFillColor(0)
NonuJetpT_pad2.SetLineColor(0)
NonuJetpT_pad1.SetBottomMargin(0.03);
NonuJetpT_pad2.SetTopMargin(0.15);
NonuJetpT_pad2.SetBottomMargin(0.3);
NonuJetpT_pad1.Draw()
NonuJetpT_pad2.Draw()

leg1 = TLegend(0.65,0.75,0.9,0.9)
leg2 = TLegend(0.65,0.75,0.9,0.9)
leg3 = TLegend(0.65,0.75,0.9,0.9)
leg4 = TLegend(0.65,0.75,0.9,0.9)
leg5= TLegend(0.65,0.75,0.9,0.9)
leg6 = TLegend(0.65,0.75,0.9,0.9)
leg7 = TLegend(0.65,0.75,0.9,0.9)
leg8 = TLegend(0.65,0.75,0.9,0.9)
leg9 = TLegend(0.65,0.75,0.9,0.9)
leg10 = TLegend(0.65,0.75,0.9,0.9)

geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("genParticles")
jetinfo,jetinfoLabel = Handle("std::vector<reco::GenJet>"), "ak4GenJets"
jetnonuinfo,jetinonunfoLabel = Handle("std::vector<reco::GenJet>"), "ak4GenJetsNoNu"
CaloMETinfo,CaloMETinfoLabel = Handle("std::vector<reco::GenMET>"), "genMetCalo"
TrueMETinfo,TrueMETinfoLabel = Handle("std::vector<reco::GenMET>"), "genMetTrue"

madspin_TLorentzVector = []
madspin_pdgid_index = []
nomadspin_TLorentzVector = []
nomadspin_pdgid_index = []

# loop over events
count= 0

for event in events:
    if count>5:break
    lep_mad = TLorentzVector(0,0,0,0)
    ele_mad = TLorentzVector(0,0,0,0)
    mu_mad = TLorentzVector(0,0,0,0)
    tau_mad = TLorentzVector(0,0,0,0)
    neu_mad = TLorentzVector(0,0,0,0)
    count = count+1
    if count%100==0: print "count = ", count
    event.getByLabel(labelPruned, handlePruned)
    pruned = handlePruned.product()
    event.getByLabel(geninfoLabel,geninfo)
    info_pruned = geninfo.product()
    weight_mad = info_pruned.weight()/abs(info_pruned.weight())
    neu_posi = -999
    ele_posi = -999
    mu_posi = -999
    for p in pruned :
        if (p.isDirectHardProcessTauDecayProductFinalState()):
		print 'ID:',p.pdgId()
                lep_mad.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
		madspin_TLorentzVector.append(lep_mad.Clone())
		madspin_pdgid_index.append(p.pdgId())
    for i in range(len(madspin_pdgid_index)):
	tau_mad = tau_mad+madspin_TLorentzVector[i]
    tauphi_mad.Fill(tau_mad.Phi(),weight_mad)
    taueta_mad.Fill(tau_mad.Eta(),weight_mad)
    taupt_mad.Fill(tau_mad.Pt(),weight_mad)
    tau_mad_boost = tau_mad.BoostVector()
    tau_mad.Boost(-tau_mad_boost)
    if -16 in madspin_pdgid_index: neu_posi = madspin_pdgid_index.index(-16)
    if 16 in madspin_pdgid_index: neu_posi = madspin_pdgid_index.index(16)
    neu_mad = madspin_TLorentzVector[neu_posi]
    neu_mad.Boost(-tau_mad_boost)
    nphi_mad.Fill(cos(neu_mad.Angle(tau_mad.Vect())),weight_mad)
    if -11 in madspin_pdgid_index: ele_posi = madspin_pdgid_index.index(-11)
    if 11 in madspin_pdgid_index: ele_posi = madspin_pdgid_index.index(11)
    if ele_posi!=-999:
	ele_mad = madspin_TLorentzVector[ele_posi]
	ele_mad.Boost(-tau_mad_boost)
	elephi_mad.Fill(cos(ele_mad.Angle(tau_mad.Vect())),weight_mad)
    if -13 in madspin_pdgid_index: mu_posi = madspin_pdgid_index.index(-13)
    if 13 in madspin_pdgid_index: mu_posi = madspin_pdgid_index.index(13)
    if mu_posi!=-999:
	mu_mad = madspin_TLorentzVector[mu_posi]
	mu_mad.Boost(-tau_mad_boost)
	muphi_mad.Fill(cos(mu_mad.Angle(tau_mad.Vect())),weight_mad)
    del madspin_TLorentzVector[:]
    del madspin_pdgid_index[:]
tauphi_mad.Scale(1./tauphi_mad.Integral())
taueta_mad.Scale(1./taueta_mad.Integral())
taupt_mad.Scale(1./taupt_mad.Integral())
nphi_mad.Scale(1./nphi_mad.Integral())
elephi_mad.Scale(1./elephi_mad.Integral())
muphi_mad.Scale(1./muphi_mad.Integral())
tauphi_mad.SetMaximum(1.4*tauphi_mad.GetMaximum())
taueta_mad.SetMaximum(1.4*taueta_mad.GetMaximum())
taupt_mad.SetMaximum(1.4*taupt_mad.GetMaximum())
nphi_mad.SetMaximum(1.4*nphi_mad.GetMaximum())
elephi_mad.SetMaximum(1.4*elephi_mad.GetMaximum())
muphi_mad.SetMaximum(1.4*muphi_mad.GetMaximum())
print 'event number of madspin:', count

# loop over events2
count2= 0

for event in events2:
    if count2>1:break
    lep_nomad = TLorentzVector(0,0,0,0)
    ele_nomad = TLorentzVector(0,0,0,0)
    mu_nomad = TLorentzVector(0,0,0,0)
    tau_nomad = TLorentzVector(0,0,0,0)
    neu_nomad = TLorentzVector(0,0,0,0)
    count2 = count2+1
    if count2%100==0: print "count2 = ", count2
    event.getByLabel(labelPruned, handlePruned)
    pruned = handlePruned.product()
    event.getByLabel(geninfoLabel,geninfo)
    info_pruned = geninfo.product()
    weight_nomad = info_pruned.weight()/abs(info_pruned.weight())
    neu_nomad_posi = -999
    ele_nomad_posi = -999
    mu_nomad_posi = -999
    for p in pruned :
        if (p.isDirectHardProcessTauDecayProductFinalState()):
                lep_nomad.SetPtEtaPhiE(p.pt(),p.eta(),p.phi(),p.energy())
		nomadspin_TLorentzVector.append(lep_nomad.Clone())
		nomadspin_pdgid_index.append(p.pdgId())
    for i in range(len(nomadspin_pdgid_index)):
	tau_nomad = tau_nomad+nomadspin_TLorentzVector[i]
    tauphi_nomad.Fill(tau_nomad.Phi(),weight_nomad)
    taueta_nomad.Fill(tau_nomad.Eta(),weight_nomad)
    taupt_nomad.Fill(tau_nomad.Pt(),weight_nomad)
    tau_nomad_boost = tau_nomad.BoostVector()
    tau_nomad.Boost(-tau_nomad_boost)
    if -16 in nomadspin_pdgid_index: neu_nomad_posi = nomadspin_pdgid_index.index(-16)
    if 16 in nomadspin_pdgid_index: neu_nomad_posi = nomadspin_pdgid_index.index(16)
    neu_nomad = nomadspin_TLorentzVector[neu_nomad_posi]
    neu_nomad.Boost(-tau_nomad_boost)
    nphi_nomad.Fill(cos(neu_nomad.Angle(tau_nomad.Vect())),weight_nomad)
    if -11 in nomadspin_pdgid_index: ele_nomad_posi = nomadspin_pdgid_index.index(-11)
    if 11 in nomadspin_pdgid_index: ele_nomad_posi = nomadspin_pdgid_index.index(11)
    if ele_nomad_posi!=-999:
	ele_nomad = nomadspin_TLorentzVector[ele_nomad_posi]
	ele_nomad.Boost(-tau_nomad_boost)
	elephi_nomad.Fill(cos(ele_nomad.Angle(tau_nomad.Vect())),weight_nomad)
    if -13 in nomadspin_pdgid_index: mu_nomad_posi = nomadspin_pdgid_index.index(-13)
    if 13 in nomadspin_pdgid_index: mu_nomad_posi = nomadspin_pdgid_index.index(13)
    if mu_nomad_posi!=-999:
	mu_nomad = nomadspin_TLorentzVector[mu_nomad_posi]
	mu_nomad.Boost(-tau_nomad_boost)
	muphi_nomad.Fill(cos(mu_nomad.Angle(tau_nomad.Vect())),weight_nomad)
    del nomadspin_TLorentzVector[:]
    del nomadspin_pdgid_index[:]
tauphi_nomad.Scale(1./tauphi_nomad.Integral())
taueta_nomad.Scale(1./taueta_nomad.Integral())
taupt_nomad.Scale(1./taupt_nomad.Integral())
nphi_nomad.Scale(1./nphi_nomad.Integral())
elephi_nomad.Scale(1./elephi_nomad.Integral())
muphi_nomad.Scale(1./muphi_nomad.Integral())
tauphi_nomad.SetMaximum(1.4*tauphi_nomad.GetMaximum())
taueta_nomad.SetMaximum(1.4*taueta_nomad.GetMaximum())
taupt_nomad.SetMaximum(1.4*taupt_nomad.GetMaximum())
nphi_nomad.SetMaximum(1.4*nphi_nomad.GetMaximum())
elephi_nomad.SetMaximum(1.4*elephi_nomad.GetMaximum())
muphi_nomad.SetMaximum(1.4*muphi_nomad.GetMaximum())
print 'event number of nonomadspin:', count2

tline1 = TLine(-1,1,1,1)
tline1.SetLineColor(kRed)
tline2 = TLine(-3,1,3,1)
tline2.SetLineColor(kRed)
tline3 = TLine(0,1,200,1)
tline3.SetLineColor(kRed)

tauphi_ratio = tauphi_nomad.Clone()
tauphi_ratio.Divide(tauphi_mad)
tauphi_ratio.SetMaximum(1.5)
tauphi_ratio.SetMinimum(0.5)
tauphi_ratio.GetYaxis().SetNdivisions(2,kFALSE);

tauphi_ratio.GetXaxis().SetTitle('tau phi')
tauphi_ratio.GetXaxis().SetTitleSize(0.15);
tauphi_ratio.GetXaxis().SetTitleOffset(0.75);
tauphi_ratio.GetXaxis().SetLabelSize(0.13);

tauphi_ratio.GetYaxis().SetTitle('wo/with')
tauphi_ratio.GetYaxis().SetTitleSize(0.18);
tauphi_ratio.GetYaxis().SetTitleOffset(0.14);
tauphi_ratio.GetYaxis().SetLabelSize(0.13);

tauphi_pad1.cd()
tauphi_mad.SetLineColor(kRed)
tauphi_mad.Draw('pe')
tauphi_nomad.SetLineColor(kBlue)
tauphi_nomad.Draw('pe same')
leg1.AddEntry(tauphi_mad,'with madspin')
leg1.AddEntry(tauphi_nomad,'without madspin')
leg1.Draw()

tauphi_pad2.cd()
tauphi_ratio.Draw()
tline2.Draw()

c1.SaveAs('tauphi.png')

taueta_ratio = taueta_nomad.Clone()
taueta_ratio.Divide(taueta_mad)
taueta_ratio.SetMaximum(1.5)
taueta_ratio.SetMinimum(0.5)
taueta_ratio.GetYaxis().SetNdivisions(2,kFALSE);

taueta_ratio.GetXaxis().SetTitle('tau eta')
taueta_ratio.GetXaxis().SetTitleSize(0.15);
taueta_ratio.GetXaxis().SetTitleOffset(0.75);
taueta_ratio.GetXaxis().SetLabelSize(0.13);

taueta_ratio.GetYaxis().SetTitle('wo/with')
taueta_ratio.GetYaxis().SetTitleSize(0.18);
taueta_ratio.GetYaxis().SetTitleOffset(0.14);
taueta_ratio.GetYaxis().SetLabelSize(0.13);

taueta_pad1.cd()
taueta_mad.SetLineColor(kRed)
taueta_mad.Draw('pe')
taueta_nomad.SetLineColor(kBlue)
taueta_nomad.Draw('pe same')
leg2.AddEntry(taueta_mad,'with madspin')
leg2.AddEntry(taueta_nomad,'without madspin')
leg2.Draw()

taueta_pad2.cd()
taueta_ratio.Draw()
tline2.Draw()

c2.SaveAs('taueta.png')

taupt_ratio = taupt_nomad.Clone()
taupt_ratio.Divide(taupt_mad)
taupt_ratio.SetMaximum(1.5)
taupt_ratio.SetMinimum(0.5)
taupt_ratio.GetYaxis().SetNdivisions(2,kFALSE);

taupt_ratio.GetXaxis().SetTitle('tau pt')
taupt_ratio.GetXaxis().SetTitleSize(0.15);
taupt_ratio.GetXaxis().SetTitleOffset(0.75);
taupt_ratio.GetXaxis().SetLabelSize(0.13);

taupt_ratio.GetYaxis().SetTitle('wo/with')
taupt_ratio.GetYaxis().SetTitleSize(0.18);
taupt_ratio.GetYaxis().SetTitleOffset(0.14);
taupt_ratio.GetYaxis().SetLabelSize(0.13);

taupt_pad1.cd()
taupt_mad.SetLineColor(kRed)
taupt_mad.Draw('pe')
taupt_nomad.SetLineColor(kBlue)
taupt_nomad.Draw('pe same')
leg3.AddEntry(taupt_mad,'with madspin')
leg3.AddEntry(taupt_nomad,'without madspin')
leg3.Draw()

taupt_pad2.cd()
taupt_ratio.Draw()
tline3.Draw()

c3.SaveAs('taupt.png')

nphi_ratio = nphi_nomad.Clone()
nphi_ratio.Divide(nphi_mad)
nphi_ratio.SetMaximum(1.5)
nphi_ratio.SetMinimum(0.5)
nphi_ratio.GetYaxis().SetNdivisions(2,kFALSE);

nphi_ratio.GetXaxis().SetTitle('neutrino cos(phi)')
nphi_ratio.GetXaxis().SetTitleSize(0.15);
nphi_ratio.GetXaxis().SetTitleOffset(0.75);
nphi_ratio.GetXaxis().SetLabelSize(0.13);

nphi_ratio.GetYaxis().SetTitle('wo/with')
nphi_ratio.GetYaxis().SetTitleSize(0.18);
nphi_ratio.GetYaxis().SetTitleOffset(0.14);
nphi_ratio.GetYaxis().SetLabelSize(0.13);

nphi_pad1.cd()
nphi_mad.SetLineColor(kRed)
nphi_mad.Draw('pe')
nphi_nomad.SetLineColor(kBlue)
nphi_nomad.Draw('pe same')
leg4.AddEntry(nphi_mad,'with madspin')
leg4.AddEntry(nphi_nomad,'without madspin')
leg4.Draw()

nphi_pad2.cd()
nphi_ratio.Draw()
tline1.Draw()

c4.SaveAs('nphi.png')

elephi_ratio = elephi_nomad.Clone()
elephi_ratio.Divide(elephi_mad)
elephi_ratio.SetMaximum(1.5)
elephi_ratio.SetMinimum(0.5)
elephi_ratio.GetYaxis().SetNdivisions(2,kFALSE);

elephi_ratio.GetXaxis().SetTitle('electron cos(phi)')
elephi_ratio.GetXaxis().SetTitleSize(0.15);
elephi_ratio.GetXaxis().SetTitleOffset(0.75);
elephi_ratio.GetXaxis().SetLabelSize(0.13);

elephi_ratio.GetYaxis().SetTitle('wo/with')
elephi_ratio.GetYaxis().SetTitleSize(0.18);
elephi_ratio.GetYaxis().SetTitleOffset(0.14);
elephi_ratio.GetYaxis().SetLabelSize(0.13);

elephi_pad1.cd()
elephi_mad.SetLineColor(kRed)
elephi_mad.Draw('pe')
elephi_nomad.SetLineColor(kBlue)
elephi_nomad.Draw('pe same')
leg5.AddEntry(elephi_mad,'with madspin')
leg5.AddEntry(elephi_nomad,'without madspin')
leg5.Draw()

elephi_pad2.cd()
elephi_ratio.Draw()
tline1.Draw()

c5.SaveAs('elephi.png')

muphi_ratio = muphi_nomad.Clone()
muphi_ratio.Divide(muphi_mad)
muphi_ratio.SetMaximum(1.5)
muphi_ratio.SetMinimum(0.5)
muphi_ratio.GetYaxis().SetNdivisions(2,kFALSE);

muphi_ratio.GetXaxis().SetTitle('muon cos(phi)')
muphi_ratio.GetXaxis().SetTitleSize(0.15);
muphi_ratio.GetXaxis().SetTitleOffset(0.75);
muphi_ratio.GetXaxis().SetLabelSize(0.13);

muphi_ratio.GetYaxis().SetTitle('wo/with')
muphi_ratio.GetYaxis().SetTitleSize(0.18);
muphi_ratio.GetYaxis().SetTitleOffset(0.14);
muphi_ratio.GetYaxis().SetLabelSize(0.13);

muphi_pad1.cd()
muphi_mad.SetLineColor(kRed)
muphi_mad.Draw('pe')
muphi_nomad.SetLineColor(kBlue)
muphi_nomad.Draw('pe same')
leg6.AddEntry(muphi_mad,'with madspin')
leg6.AddEntry(muphi_nomad,'without madspin')
leg6.Draw()

muphi_pad2.cd()
muphi_ratio.Draw()
tline1.Draw()

c6.SaveAs('muphi.png')
