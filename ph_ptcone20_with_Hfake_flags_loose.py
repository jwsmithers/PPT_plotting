from ROOT import *
from array import array

rootfile = "ttbar_ttgamma_w_NNVar.root"
gStyle.SetOptStat(0); 
f = TFile(rootfile)
myttree = f.Get("nominal")
#  histogram = "histogram"+i

canvas = TCanvas("canvas","",0,0,800,800);
canvas.SetFillColor(0);
# Upper histogram plot is pad1
# canvas.cd(1)
pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
pad1.SetBottomMargin(0)  # joins upper and lower plot
pad1.SetGridx()
pad1.Draw()
# Lower ratio plot is pad2
pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
pad2.SetTopMargin(0)  # joins upper and lower plot
pad2.SetBottomMargin(0.2)
pad2.SetGridx()
pad2.Draw()

pad1.cd()
# myttree.Draw("ph_ptcone20>>signal","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((abs(ph_caloEta) < 2.37) && ph_pt>20000 && !( ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42 && ph_truthType == 16 ) && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410082)", "norm")
# myttree.Draw("ph_ptcone20>>bkg_goodPh","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 &&  event_ngoodphotons==1 && ph_isTight)", "norm")
bin_sizes = [0,5,10,15,20,30,60]
bin_sizes_array = array('d',bin_sizes)
binnum = 6
histogram1 = TH1F("histogram1","histogram1", binnum, bin_sizes_array);
# histogram2 = TH1F("histogram2","histogram2", binnum, bin_sizes_array);
histogram3 = TH1D("histogram3","histogram3", binnum, bin_sizes_array);
histogram4 = TH1D("histogram4","histogram4", binnum, bin_sizes_array);
histogram5 = TH1D("histogram5","histogram5", binnum, bin_sizes_array);
histogram6 = TH1D("histogram6","histogram6", binnum, bin_sizes_array);
histogram7 = TH1D("histogram7","histogram7", binnum, bin_sizes_array);
histogram8 = TH1D("histogram8","histogram8", binnum, bin_sizes_array);

myttree.Draw("ph_ptcone20/1e3>>histogram1","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_HFT_MVA < 0.1)", "norm")
# myttree.Draw("ph_ptcone20/1e3>>histogram2","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_HFT_MVA < 0.1 && event_ngoodphotons==1 && ph_isTight)", "norm")
myttree.Draw("ph_ptcone20/1e3>>histogram3","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_isHadronFakeFailedDeltaE == 1 && ph_HFT_MVA < 0.1)", "norm")
myttree.Draw("ph_ptcone20/1e3>>histogram4","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_isHadronFakeFailedERatio == 1 && ph_HFT_MVA < 0.1)", "norm")
myttree.Draw("ph_ptcone20/1e3>>histogram5","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_isHadronFakeFailedFside ==1&& ph_HFT_MVA < 0.1)", "norm")
myttree.Draw("ph_ptcone20/1e3>>histogram6","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_isHadronFakeFailedWs3 == 1 && ph_HFT_MVA < 0.1)", "norm")
myttree.Draw("ph_ptcone20/1e3>>histogram7","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_isHFake == 1 && ph_HFT_MVA < 0.1)", "norm")
myttree.Draw("ph_ptcone20/1e3>>histogram8","(weight_mc*weight_pileup*weight_leptonSF*weight_jvt*weight_bTagSF_77*event_norm * event_lumi )* ((ph_truthOrigin==23 || ph_truthOrigin==24 || ph_truthOrigin==25 || ph_truthOrigin==26 || ph_truthOrigin==27 || ph_truthOrigin==28 || ph_truthOrigin==29 || ph_truthOrigin==30 || ph_truthOrigin==31 || ph_truthOrigin==32 || ph_truthOrigin==33 || ph_truthOrigin==34 || ph_truthOrigin==35 || ph_truthOrigin==42) && ph_truthType == 16 && !( abs(ph_mc_pid)==11 || ( ph_mcel_dr<0.2 && ph_mcel_dr>=0 ) ) && mcChannelNumber==410501 && ph_pt > 20000 && ph_isHFake == 1)", "norm")


histogram1.Draw("H")
# histogram2.Draw("same H")
histogram3.Draw("same H")
histogram4.Draw("same H")
histogram5.Draw("same H")
histogram6.Draw("same H")
histogram7.Draw("same H")
histogram8.Draw("same H")

# bkg_goodPh.Draw("same")
# signal.Draw("same")
histogram1.SetTitle("")
y1 = histogram1.GetYaxis()
y1.SetTitle("A.U.")
y1.SetRangeUser(0.,0.7)
x1 = histogram1.GetXaxis()
x1.SetLimits(0.,60.)
x1.SetTitle("p_{T}^{cone20}(#gamma) [GeV]")

# signal.SetLineColor(kRed)
histogram1.SetLineColor(633)
# histogram2.SetLineColor(625)
histogram3.SetLineColor(617)
histogram4.SetLineColor(433)
histogram5.SetLineColor(417)
histogram6.SetLineColor(401)
histogram7.SetLineColor(kBlack)
histogram8.SetLineColor(kBlue)

histogram1.SetLineWidth(2)
# histogram2.SetLineWidth(2)
histogram3.SetLineWidth(2)
histogram4.SetLineWidth(2)
histogram5.SetLineWidth(2)
histogram6.SetLineWidth(2)
histogram7.SetLineWidth(2)
histogram8.SetLineWidth(2)

# bkg_goodPh.SetLineWidth(2)

lumi = TLatex();
lumi.SetNDC();
lumi.SetTextAlign(12);
lumi.SetTextFont(63);
lumi.SetTextSizePixels(19);
lumi.DrawLatex(0.28,0.8, "#it{#scale[1.2]{ATLAS}} #bf{Internal}");

leg = TLegend(0.58,0.58,0.82,0.88);
leg.SetTextSize(0.032);
leg.AddEntry(histogram1,"ph_HFT_MVA","l");
# leg.AddEntry(histogram2,"ph_HFT_MVA, 1 good photon","l");
leg.AddEntry(histogram3,"+FailedDeltaE","l");
leg.AddEntry(histogram4,"+FailedERatio","l");
leg.AddEntry(histogram5,"+FailedFside","l");
leg.AddEntry(histogram6,"+FailedWs3","l");
leg.AddEntry(histogram7,"+ph_isHFake","l");
leg.AddEntry(histogram8,"ph_isHFake","l");

# leg.AddEntry(bkg_goodPh,"ph_ptcone20, 1 good, tight photon","l");


leg.SetBorderSize(0)
leg.Draw()

ratio1 = histogram1.Clone("ratio")
#ratio1.SetMarkerStyle(20)
ratio1.SetMinimum(-4)
ratio1.SetMaximum(5)
ratio1.Sumw2()
ratio1.SetStats(0)
ratio1.Divide(histogram3)
ratio1.SetTitle("")
y = ratio1.GetYaxis()
y.SetTitle("ph_HFT_MVA/Y")
y.SetNdivisions(505)
y.SetTitleSize(20)
y.SetTitleFont(43)
y.SetTitleOffset(1.55)
y.SetLabelFont(43)
y.SetLabelSize(15)
x = ratio1.GetXaxis()
x.SetTitle("p_{T}^{cone20}(#gamma) [GeV]")
x.SetTitleSize(20)
x.SetTitleFont(43)
x.SetTitleOffset(3.2)
x.SetLabelFont(43)
x.SetLabelSize(15)
pad2.cd()
ratio1.SetLineColor(617)
ratio1.Draw("")

# ratio2 = histogram1.Clone("ratio")
# ratio2.Divide(histogram3)
# ratio2.SetLineColor(617)
# ratio2.Draw("same")

ratio2 = histogram1.Clone("ratio")
ratio2.Divide(histogram4)
ratio2.SetLineColor(433)
ratio2.Draw("same")

ratio3 = histogram1.Clone("ratio")
ratio3.Divide(histogram5)
ratio3.SetLineColor(417)
ratio3.Draw("same")

ratio4 = histogram1.Clone("ratio")
ratio4.Divide(histogram6)
ratio4.SetLineColor(401)
ratio4.Draw("same")

ratio5 = histogram1.Clone("ratio")
ratio5.Divide(histogram7)
ratio5.SetLineColor(kBlack)
ratio5.Draw("same")

ratio6 = histogram1.Clone("ratio")
ratio6.Divide(histogram8)
ratio6.SetLineColor(kBlue)
ratio6.Draw("same")


line = TF1("fa1","1",-1000,1000);
line.Draw("same")
line.SetLineColor(633);


#gPad.SetLogz();
canvas.SaveAs("ph_ptcone20_with_hfake_flags_loose.png")
