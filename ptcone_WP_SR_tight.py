from ROOT import *
from array import array

rootfile = "ttbar_ttgamma_w_NNVar.root"
gStyle.SetOptStat(0); 
f = TFile(rootfile)
myttree = f.Get("nominal")
#  histogram = "histogram"+i

canvas = TCanvas("canvas","",0,0,800,800);
canvas.SetFillColor(0);
# # Upper histogram plot is pad1
# # canvas.cd(1)
# pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
# pad1.SetBottomMargin(0)  # joins upper and lower plot
# pad1.SetGridx()
# pad1.Draw()
# # Lower ratio plot is pad2
# pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
# pad2.SetTopMargin(0)  # joins upper and lower plot
# pad2.SetBottomMargin(0.2)
# pad2.SetGridx()
# pad2.Draw()

# pad1.cd()
bin_sizes = [0,5,10,15,20,30,60]
bin_sizes_array = array('d',bin_sizes)
binnum = 6
phHFTMVA01 = TH1F("phHFTMVA01","phHFTMVA01", binnum, bin_sizes_array);
phHFTMVA02 = TH1D("phHFTMVA02","phHFTMVA02", binnum, bin_sizes_array);
phHFTMVA03 = TH1D("phHFTMVA03","phHFTMVA03", binnum, bin_sizes_array);
phHFTMVA04 = TH1D("phHFTMVA04","phHFTMVA04", binnum, bin_sizes_array);
phHFTMVA05 = TH1D("phHFTMVA05","phHFTMVA05", binnum, bin_sizes_array);
phHFTMVA06 = TH1D("phHFTMVA06","phHFTMVA06", binnum, bin_sizes_array);
phHFTMVA07 = TH1D("phHFTMVA07","phHFTMVA07", binnum, bin_sizes_array);
#phisHFake = TH1D("phisHFake","phisHFake", binnum, bin_sizes_array);


myttree.Draw("ph_ptcone20/1e3>>phHFTMVA01","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_HFT_MVA > 0.3  && event_ngoodphotons==1 && ph_isTight)", "norm")

myttree.Draw("ph_ptcone20/1e3>>phHFTMVA02","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_HFT_MVA > 0.4  && event_ngoodphotons==1 && ph_isTight)", "norm")

myttree.Draw("ph_ptcone20/1e3>>phHFTMVA03","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_HFT_MVA > 0.5  && event_ngoodphotons==1 && ph_isTight)", "norm")

myttree.Draw("ph_ptcone20/1e3>>phHFTMVA04","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_HFT_MVA > 0.6  && event_ngoodphotons==1 && ph_isTight)", "norm")

myttree.Draw("ph_ptcone20/1e3>>phHFTMVA05","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_HFT_MVA > 0.7  && event_ngoodphotons==1 && ph_isTight)", "norm")

myttree.Draw("ph_ptcone20/1e3>>phHFTMVA06","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_HFT_MVA > 0.8  && event_ngoodphotons==1 && ph_isTight)", "norm")

myttree.Draw("ph_ptcone20/1e3>>phHFTMVA07","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_HFT_MVA > 0.9  && event_ngoodphotons==1 && ph_isTight)", "norm")

#myttree.Draw("ph_ptcone20/1e3>>phisHFake","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_isHFake)", "norm")


phHFTMVA01.Draw("H")
# histogram2.Draw("same H")
phHFTMVA02.Draw("same H")
phHFTMVA03.Draw("same H")
phHFTMVA04.Draw("same H")
phHFTMVA05.Draw("same H")
phHFTMVA06.Draw("same H")
phHFTMVA07.Draw("same H")
#phisHFake.Draw("same H")

# bkg_goodPh.Draw("same")
# signal.Draw("same")
phHFTMVA01.SetTitle("")
y1 = phHFTMVA01.GetYaxis()
y1.SetTitle("A.U.")
y1.SetRangeUser(0.,1)
x1 = phHFTMVA01.GetXaxis()
x1.SetLimits(0.,60.)
x1.SetTitle("p_{T}^{cone20}(#gamma) [GeV]")

phHFTMVA01.SetLineColor(633)
phHFTMVA02.SetLineColor(617)
phHFTMVA03.SetLineColor(601)
phHFTMVA04.SetLineColor(433)
phHFTMVA05.SetLineColor(417)
phHFTMVA06.SetLineColor(401)
phHFTMVA07.SetLineColor(kBlack)
#phisHFake.SetLineColor(kBlue)

phHFTMVA01.SetLineWidth(2)
phHFTMVA02.SetLineWidth(2)
phHFTMVA03.SetLineWidth(2)
phHFTMVA04.SetLineWidth(2)
phHFTMVA05.SetLineWidth(2)
phHFTMVA06.SetLineWidth(2)
phHFTMVA07.SetLineWidth(2)
#phisHFake.SetLineWidth(2)

# bkg_goodPh.SetLineWidth(2)

lumi = TLatex();
lumi.SetNDC();
lumi.SetTextAlign(12);
lumi.SetTextFont(63);
lumi.SetTextSizePixels(19);
lumi.DrawLatex(0.28,0.8, "#it{#scale[1.2]{ATLAS}} #bf{Internal}");

leg = TLegend(0.52,0.58,0.82,0.88);
leg.SetTextSize(0.032);
leg.AddEntry(phHFTMVA01,"ph_HFT_MVA > 0.30","l");
leg.AddEntry(phHFTMVA02,"ph_HFT_MVA > 0.40","l");
leg.AddEntry(phHFTMVA03,"ph_HFT_MVA > 0.50","l");
leg.AddEntry(phHFTMVA04,"ph_HFT_MVA > 0.60","l");
leg.AddEntry(phHFTMVA05,"ph_HFT_MVA > 0.70","l");
leg.AddEntry(phHFTMVA06,"ph_HFT_MVA > 0.80","l");
leg.AddEntry(phHFTMVA07,"ph_HFT_MVA > 0.90","l");
#leg.AddEntry(phisHFake,"ph_isHFake","l");

# leg.AddEntry(bkg_goodPh,"ph_ptcone20, 1 good, tight photon","l");


leg.SetBorderSize(0)
leg.Draw()

# ratio1 = phisHFake.Clone("ratio")
# #ratio1.SetMarkerStyle(20)
# ratio1.SetMinimum(0)
# ratio1.SetMaximum(2)
# ratio1.Sumw2()
# ratio1.SetStats(0)
# ratio1.Divide(phHFTMVA01)
# ratio1.SetTitle("")
# y = ratio1.GetYaxis()
# y.SetTitle("isHFake/HFT_MVA")
# y.SetNdivisions(505)
# y.SetTitleSize(20)
# y.SetTitleFont(43)
# y.SetTitleOffset(1.55)
# y.SetLabelFont(43)
# y.SetLabelSize(15)
# x = ratio1.GetXaxis()
# x.SetTitle("p_{T}^{cone20}(#gamma) [GeV]")
# x.SetTitleSize(20)
# x.SetTitleFont(43)
# x.SetTitleOffset(3.2)
# x.SetLabelFont(43)
# x.SetLabelSize(15)
# pad2.cd()
# ratio1.SetLineColor(633)
# ratio1.Draw("")

# ratio2 = phisHFake.Clone("ratio")
# ratio2.Divide(phHFTMVA02)
# ratio2.SetLineColor(617)
# ratio2.Draw("same")

# ratio2 = phisHFake.Clone("ratio")
# ratio2.Divide(phHFTMVA03)
# ratio2.SetLineColor(601)
# ratio2.Draw("same")

# ratio3 = phisHFake.Clone("ratio")
# ratio3.Divide(phHFTMVA04)
# ratio3.SetLineColor(433)
# ratio3.Draw("same")

# ratio4 = phisHFake.Clone("ratio")
# ratio4.Divide(phHFTMVA05)
# ratio4.SetLineColor(417)
# ratio4.Draw("same")

# ratio5 = phisHFake.Clone("ratio")
# ratio5.Divide(phHFTMVA06)
# ratio5.SetLineColor(401)
# ratio5.Draw("same")

# ratio6 = phisHFake.Clone("ratio")
# ratio6.Divide(phHFTMVA07)
# ratio6.SetLineColor(kBlack)
# ratio6.Draw("same")



# line = TF1("fa1","1",-1000,1000);
# line.Draw("same")
# line.SetLineColor(kBlue);


#gPad.SetLogz();
canvas.SaveAs("ph_ptcone20_SR_tight.png")

