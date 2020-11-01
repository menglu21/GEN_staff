import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from ROOT import TLine, TH1D, TLorentzVector, TCanvas, TPad, TLegend, kRed, kBlue, kFALSE

from math import hypot, pi, cos

events = Events (['./madspin.root'])
events2 = Events (['./nomadspin.root'])

lphi_mad = TH1D("lepton phi madspin","",30,-3,3)
lphi_mad.SetStats(0)
lphi_mad.Sumw2()
lphi_mad.GetYaxis().SetTitle("a.u.")
lphi_mad.GetYaxis().SetTitleSize(0.05)
lphi_mad.GetYaxis().SetTitleOffset(0.75)
lphi_mad.GetXaxis().SetLabelSize(0)
#lphi_mad.SetMaximum(1000)
lphi_mad.SetMinimum(0)
lphi_nomad = TH1D("lepton phi nomadspin","",30,-3,3)
lphi_nomad.SetStats(0)
lphi_nomad.Sumw2()

lpt_mad = TH1D("lepton pt madspin","",20,0,200)
lpt_mad.SetStats(0)
lpt_mad.Sumw2()
lpt_mad.GetYaxis().SetTitle("a.u.")
lpt_mad.GetYaxis().SetTitleSize(0.05)
lpt_mad.GetYaxis().SetTitleOffset(0.75)
lpt_mad.GetXaxis().SetLabelSize(0)
#lpt_mad.SetMaximum(1000)
lpt_mad.SetMinimum(0)
lpt_nomad = TH1D("lepton pt nomadspin","",20,0,200)
lpt_nomad.SetStats(0)
lpt_nomad.Sumw2()

leta_mad = TH1D("lepton eta madspin","",30,-3,3)
leta_mad.SetStats(0)
leta_mad.Sumw2()
leta_mad.GetYaxis().SetTitle("a.u.")
leta_mad.GetYaxis().SetTitleSize(0.05)
leta_mad.GetYaxis().SetTitleOffset(0.75)
leta_mad.GetXaxis().SetLabelSize(0)
#leta_mad.SetMaximum(1000)
leta_mad.SetMinimum(0)
leta_nomad = TH1D("lepton eta nomadspin","",30,-3,3)
leta_nomad.SetStats(0)
leta_nomad.Sumw2()

neuphi_mad = TH1D("neu phi madspin","",30,-3,3)
neuphi_mad.SetStats(0)
neuphi_mad.Sumw2()
neuphi_mad.GetYaxis().SetTitle("a.u.")
neuphi_mad.GetYaxis().SetTitleSize(0.05)
neuphi_mad.GetYaxis().SetTitleOffset(0.75)
neuphi_mad.GetXaxis().SetLabelSize(0)
#neuphi_mad.SetMaximum(1000)
neuphi_mad.SetMinimum(0)
neuphi_nomad = TH1D("neu phi nomadspin","",30,-3,3)
neuphi_nomad.SetStats(0)
neuphi_nomad.Sumw2()

neupt_mad = TH1D("neu pt madspin","",20,0,200)
neupt_mad.SetStats(0)
neupt_mad.Sumw2()
neupt_mad.GetYaxis().SetTitle("a.u.")
neupt_mad.GetYaxis().SetTitleSize(0.05)
neupt_mad.GetYaxis().SetTitleOffset(0.75)
neupt_mad.GetXaxis().SetLabelSize(0)
#neupt_mad.SetMaximum(1000)
neupt_mad.SetMinimum(0)
neupt_nomad = TH1D("neu pt nomadspin","",20,0,200)
neupt_nomad.SetStats(0)
neupt_nomad.Sumw2()

neueta_mad = TH1D("neu eta madspin","",30,-3,3)
neueta_mad.SetStats(0)
neueta_mad.Sumw2()
neueta_mad.GetYaxis().SetTitle("a.u.")
neueta_mad.GetYaxis().SetTitleSize(0.05)
neueta_mad.GetYaxis().SetTitleOffset(0.75)
neueta_mad.GetXaxis().SetLabelSize(0)
#neueta_mad.SetMaximum(1000)
neueta_mad.SetMinimum(0)
neueta_nomad = TH1D("neu eta nomadspin","",30,-3,3)
neueta_nomad.SetStats(0)
neueta_nomad.Sumw2()

c1= TCanvas("lphi","lphi",800,600)
lphi_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
lphi_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
lphi_pad1.SetFillColor(0)
lphi_pad1.SetLineColor(0)
lphi_pad2.SetFillColor(0)
lphi_pad2.SetLineColor(0)
lphi_pad1.SetBottomMargin(0.03);
lphi_pad2.SetTopMargin(0.15);
lphi_pad2.SetBottomMargin(0.3);
lphi_pad1.Draw()
lphi_pad2.Draw()

c2= TCanvas("lpt","lpt",800,600)
lpt_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
lpt_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
lpt_pad1.SetFillColor(0)
lpt_pad1.SetLineColor(0)
lpt_pad2.SetFillColor(0)
lpt_pad2.SetLineColor(0)
lpt_pad1.SetBottomMargin(0.03);
lpt_pad2.SetTopMargin(0.15);
lpt_pad2.SetBottomMargin(0.3);
lpt_pad1.Draw()
lpt_pad2.Draw()

c3= TCanvas("leta","leta",800,600)
leta_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
leta_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
leta_pad1.SetFillColor(0)
leta_pad1.SetLineColor(0)
leta_pad2.SetFillColor(0)
leta_pad2.SetLineColor(0)
leta_pad1.SetBottomMargin(0.03);
leta_pad2.SetTopMargin(0.15);
leta_pad2.SetBottomMargin(0.3);
leta_pad1.Draw()
leta_pad2.Draw()

c4= TCanvas("neuphi","neuphi",800,600)
neuphi_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
neuphi_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
neuphi_pad1.SetFillColor(0)
neuphi_pad1.SetLineColor(0)
neuphi_pad2.SetFillColor(0)
neuphi_pad2.SetLineColor(0)
neuphi_pad1.SetBottomMargin(0.03);
neuphi_pad2.SetTopMargin(0.15);
neuphi_pad2.SetBottomMargin(0.3);
neuphi_pad1.Draw()
neuphi_pad2.Draw()

c5= TCanvas("neupt","neupt",800,600)
neupt_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
neupt_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
neupt_pad1.SetFillColor(0)
neupt_pad1.SetLineColor(0)
neupt_pad2.SetFillColor(0)
neupt_pad2.SetLineColor(0)
neupt_pad1.SetBottomMargin(0.03);
neupt_pad2.SetTopMargin(0.15);
neupt_pad2.SetBottomMargin(0.3);
neupt_pad1.Draw()
neupt_pad2.Draw()

c6= TCanvas("neueta","neueta",800,600)
neueta_pad1 = TPad("pad1", "", 0.00, 0.20, 0.99, 0.99)
neueta_pad2 = TPad("pad2", "", 0.00, 0.00, 0.99, 0.20)
neueta_pad1.SetFillColor(0)
neueta_pad1.SetLineColor(0)
neueta_pad2.SetFillColor(0)
neueta_pad2.SetLineColor(0)
neueta_pad1.SetBottomMargin(0.03);
neueta_pad2.SetTopMargin(0.15);
neueta_pad2.SetBottomMargin(0.3);
neueta_pad1.Draw()
neueta_pad2.Draw()

leg1 = TLegend(0.65,0.75,0.9,0.9)
leg2 = TLegend(0.65,0.75,0.9,0.9)
leg3 = TLegend(0.65,0.75,0.9,0.9)
leg4 = TLegend(0.65,0.75,0.9,0.9)
leg5= TLegend(0.65,0.75,0.9,0.9)
leg6 = TLegend(0.65,0.75,0.9,0.9)

geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"
handlePruned  = Handle ("LHEEventProduct")
labelPruned = ("externalLHEProducer")

madspin_TLorentzVector = []
madspin_pdgid_index = []
nomadspin_TLorentzVector = []
nomadspin_pdgid_index = []

# loop over events
count= 0

for event in events:
#    if count>10:break
    tau_mad = TLorentzVector(0,0,0,0)
    neu_mad = TLorentzVector(0,0,0,0)
    count = count+1
    event.getByLabel(labelPruned, handlePruned)
    pruned = handlePruned.product()
    event.getByLabel(geninfoLabel,geninfo)
    info_pruned = geninfo.product()
    weight_mad = info_pruned.weight()/abs(info_pruned.weight())
    if count%100==0: print "count = ", count, 'weight: ', weight_mad
    for i in range(pruned.hepeup().NUP):
	if abs(pruned.hepeup().IDUP[i])==15:
	   tau_mad.SetPxPyPzE(pruned.hepeup().PUP[i][0],pruned.hepeup().PUP[i][1],pruned.hepeup().PUP[i][2],pruned.hepeup().PUP[i][3])
	   lphi_mad.Fill(tau_mad.Phi(),weight_mad)
	   lpt_mad.Fill(tau_mad.Pt(),weight_mad)
	   leta_mad.Fill(tau_mad.Eta(),weight_mad)
	if abs(pruned.hepeup().IDUP[i])==16:
           neu_mad.SetPxPyPzE(pruned.hepeup().PUP[i][0],pruned.hepeup().PUP[i][1],pruned.hepeup().PUP[i][2],pruned.hepeup().PUP[i][3])
           neuphi_mad.Fill(neu_mad.Phi(),weight_mad)
           neupt_mad.Fill(neu_mad.Pt(),weight_mad)
           neueta_mad.Fill(neu_mad.Eta(),weight_mad)
lphi_mad.Scale(1./lphi_mad.Integral())
lpt_mad.Scale(1./lpt_mad.Integral())
leta_mad.Scale(1./leta_mad.Integral())
neuphi_mad.Scale(1./neuphi_mad.Integral())
neupt_mad.Scale(1./neupt_mad.Integral())
neueta_mad.Scale(1./neueta_mad.Integral())
lphi_mad.SetMaximum(1.4*lphi_mad.GetMaximum())
lpt_mad.SetMaximum(1.4*lpt_mad.GetMaximum())
leta_mad.SetMaximum(1.4*leta_mad.GetMaximum())
neuphi_mad.SetMaximum(1.4*neuphi_mad.GetMaximum())
neupt_mad.SetMaximum(1.4*neupt_mad.GetMaximum())
neueta_mad.SetMaximum(1.4*neueta_mad.GetMaximum())

# loop over events2
count2= 0

for event in events2:
#    if count2>10:break
    tau_nomad = TLorentzVector(0,0,0,0)
    neu_nomad = TLorentzVector(0,0,0,0)
    count2 = count2+1
    event.getByLabel(labelPruned, handlePruned)
    pruned = handlePruned.product()
    event.getByLabel(geninfoLabel,geninfo)
    info_pruned = geninfo.product()
    weight_nomad = info_pruned.weight()/abs(info_pruned.weight())
    if count2%100==0: print "count2 = ", count2, 'weight: ',weight_nomad
    for i in range(pruned.hepeup().NUP):
	if abs(pruned.hepeup().IDUP[i])==15:
	   tau_nomad.SetPxPyPzE(pruned.hepeup().PUP[i][0],pruned.hepeup().PUP[i][1],pruned.hepeup().PUP[i][2],pruned.hepeup().PUP[i][3])
	   lphi_nomad.Fill(tau_nomad.Phi(),weight_nomad)
	   lpt_nomad.Fill(tau_nomad.Pt(),weight_nomad)
	   leta_nomad.Fill(tau_nomad.Eta(),weight_nomad)
	if abs(pruned.hepeup().IDUP[i])==16:
           neu_nomad.SetPxPyPzE(pruned.hepeup().PUP[i][0],pruned.hepeup().PUP[i][1],pruned.hepeup().PUP[i][2],pruned.hepeup().PUP[i][3])
           neuphi_nomad.Fill(neu_nomad.Phi(),weight_nomad)
           neupt_nomad.Fill(neu_nomad.Pt(),weight_nomad)
           neueta_nomad.Fill(neu_nomad.Eta(),weight_nomad)
lphi_nomad.Scale(1./lphi_nomad.Integral())
lpt_nomad.Scale(1./lpt_nomad.Integral())
leta_nomad.Scale(1./leta_nomad.Integral())
neuphi_nomad.Scale(1./neuphi_nomad.Integral())
neupt_nomad.Scale(1./neupt_nomad.Integral())
neueta_nomad.Scale(1./neueta_nomad.Integral())
lphi_nomad.SetMaximum(1.4*lphi_nomad.GetMaximum())
lpt_nomad.SetMaximum(1.4*lpt_nomad.GetMaximum())
leta_nomad.SetMaximum(1.4*leta_nomad.GetMaximum())
neuphi_nomad.SetMaximum(1.4*neuphi_nomad.GetMaximum())
neupt_nomad.SetMaximum(1.4*neupt_nomad.GetMaximum())
neueta_nomad.SetMaximum(1.4*neueta_nomad.GetMaximum())

tline1 = TLine(-3,1,3,1)
tline1.SetLineColor(kRed)
tline2 = TLine(0,1,200,1)
tline2.SetLineColor(kRed)

lphi_ratio = lphi_nomad.Clone()
lphi_ratio.Divide(lphi_mad)
lphi_ratio.SetMaximum(1.5)
lphi_ratio.SetMinimum(0.5)
lphi_ratio.GetYaxis().SetNdivisions(2,kFALSE);

lphi_ratio.GetXaxis().SetTitle('lep phi')
lphi_ratio.GetXaxis().SetTitleSize(0.15);
lphi_ratio.GetXaxis().SetTitleOffset(0.75);
lphi_ratio.GetXaxis().SetLabelSize(0.13);

lphi_ratio.GetYaxis().SetTitle('wo/with')
lphi_ratio.GetYaxis().SetTitleSize(0.18);
lphi_ratio.GetYaxis().SetTitleOffset(0.14);
lphi_ratio.GetYaxis().SetLabelSize(0.13);

lphi_pad1.cd()
lphi_mad.SetLineColor(kRed)
lphi_mad.Draw('pe')
lphi_nomad.SetLineColor(kBlue)
lphi_nomad.Draw('pe same')
leg1.AddEntry(lphi_mad,'with madspin')
leg1.AddEntry(lphi_nomad,'without madspin')
leg1.Draw()

lphi_pad2.cd()
lphi_ratio.Draw()
tline1.Draw()
c1.SaveAs('lphi.png')

lpt_ratio = lpt_nomad.Clone()
lpt_ratio.Divide(lpt_mad)
lpt_ratio.SetMaximum(1.5)
lpt_ratio.SetMinimum(0.5)
lpt_ratio.GetYaxis().SetNdivisions(2,kFALSE);

lpt_ratio.GetXaxis().SetTitle('lep pt')
lpt_ratio.GetXaxis().SetTitleSize(0.15);
lpt_ratio.GetXaxis().SetTitleOffset(0.75);
lpt_ratio.GetXaxis().SetLabelSize(0.13);

lpt_ratio.GetYaxis().SetTitle('wo/with')
lpt_ratio.GetYaxis().SetTitleSize(0.18);
lpt_ratio.GetYaxis().SetTitleOffset(0.14);
lpt_ratio.GetYaxis().SetLabelSize(0.13);

lpt_pad1.cd()
lpt_mad.SetLineColor(kRed)
lpt_mad.Draw('pe')
lpt_nomad.SetLineColor(kBlue)
lpt_nomad.Draw('pe same')
leg2.AddEntry(lpt_mad,'with madspin')
leg2.AddEntry(lpt_nomad,'without madspin')
leg2.Draw()

lpt_pad2.cd()
lpt_ratio.Draw()
tline2.Draw()
c2.SaveAs('lpt.png')

leta_ratio = leta_nomad.Clone()
leta_ratio.Divide(leta_mad)
leta_ratio.SetMaximum(1.5)
leta_ratio.SetMinimum(0.5)
leta_ratio.GetYaxis().SetNdivisions(2,kFALSE);

leta_ratio.GetXaxis().SetTitle('lep eta')
leta_ratio.GetXaxis().SetTitleSize(0.15);
leta_ratio.GetXaxis().SetTitleOffset(0.75);
leta_ratio.GetXaxis().SetLabelSize(0.13);

leta_ratio.GetYaxis().SetTitle('wo/with')
leta_ratio.GetYaxis().SetTitleSize(0.18);
leta_ratio.GetYaxis().SetTitleOffset(0.14);
leta_ratio.GetYaxis().SetLabelSize(0.13);

leta_pad1.cd()
leta_mad.SetLineColor(kRed)
leta_mad.Draw('pe')
leta_nomad.SetLineColor(kBlue)
leta_nomad.Draw('pe same')
leg3.AddEntry(leta_mad,'with madspin')
leg3.AddEntry(leta_nomad,'without madspin')
leg3.Draw()

leta_pad2.cd()
leta_ratio.Draw()
tline1.Draw()
c3.SaveAs('leta.png')

neuphi_ratio = neuphi_nomad.Clone()
neuphi_ratio.Divide(neuphi_mad)
neuphi_ratio.SetMaximum(1.5)
neuphi_ratio.SetMinimum(0.5)
neuphi_ratio.GetYaxis().SetNdivisions(2,kFALSE);

neuphi_ratio.GetXaxis().SetTitle('neu phi')
neuphi_ratio.GetXaxis().SetTitleSize(0.15);
neuphi_ratio.GetXaxis().SetTitleOffset(0.75);
neuphi_ratio.GetXaxis().SetLabelSize(0.13);

neuphi_ratio.GetYaxis().SetTitle('wo/with')
neuphi_ratio.GetYaxis().SetTitleSize(0.18);
neuphi_ratio.GetYaxis().SetTitleOffset(0.14);
neuphi_ratio.GetYaxis().SetLabelSize(0.13);

neuphi_pad1.cd()
neuphi_mad.SetLineColor(kRed)
neuphi_mad.Draw('pe')
neuphi_nomad.SetLineColor(kBlue)
neuphi_nomad.Draw('pe same')
leg4.AddEntry(lphi_mad,'with madspin')
leg4.AddEntry(lphi_nomad,'without madspin')
leg4.Draw()

neuphi_pad2.cd()
neuphi_ratio.Draw()
tline1.Draw()
c4.SaveAs('neuphi.png')

neupt_ratio = neupt_nomad.Clone()
neupt_ratio.Divide(neupt_mad)
neupt_ratio.SetMaximum(1.5)
neupt_ratio.SetMinimum(0.5)
neupt_ratio.GetYaxis().SetNdivisions(2,kFALSE);

neupt_ratio.GetXaxis().SetTitle('neu pt')
neupt_ratio.GetXaxis().SetTitleSize(0.15);
neupt_ratio.GetXaxis().SetTitleOffset(0.75);
neupt_ratio.GetXaxis().SetLabelSize(0.13);

neupt_ratio.GetYaxis().SetTitle('wo/with')
neupt_ratio.GetYaxis().SetTitleSize(0.18);
neupt_ratio.GetYaxis().SetTitleOffset(0.14);
neupt_ratio.GetYaxis().SetLabelSize(0.13);

neupt_pad1.cd()
neupt_mad.SetLineColor(kRed)
neupt_mad.Draw('pe')
neupt_nomad.SetLineColor(kBlue)
neupt_nomad.Draw('pe same')
leg5.AddEntry(lpt_mad,'with madspin')
leg5.AddEntry(lpt_nomad,'without madspin')
leg5.Draw()

neupt_pad2.cd()
neupt_ratio.Draw()
tline2.Draw()
c5.SaveAs('neupt.png')

neueta_ratio = neueta_nomad.Clone()
neueta_ratio.Divide(neueta_mad)
neueta_ratio.SetMaximum(1.5)
neueta_ratio.SetMinimum(0.5)
neueta_ratio.GetYaxis().SetNdivisions(2,kFALSE);

neueta_ratio.GetXaxis().SetTitle('neu eta')
neueta_ratio.GetXaxis().SetTitleSize(0.15);
neueta_ratio.GetXaxis().SetTitleOffset(0.75);
neueta_ratio.GetXaxis().SetLabelSize(0.13);

neueta_ratio.GetYaxis().SetTitle('wo/with')
neueta_ratio.GetYaxis().SetTitleSize(0.18);
neueta_ratio.GetYaxis().SetTitleOffset(0.14);
neueta_ratio.GetYaxis().SetLabelSize(0.13);

neueta_pad1.cd()
neueta_mad.SetLineColor(kRed)
neueta_mad.Draw('pe')
neueta_nomad.SetLineColor(kBlue)
neueta_nomad.Draw('pe same')
leg6.AddEntry(leta_mad,'with madspin')
leg6.AddEntry(leta_nomad,'without madspin')
leg6.Draw()

neueta_pad2.cd()
neueta_ratio.Draw()
tline1.Draw()
c6.SaveAs('neueta.png')
