from ROOT import *
from array import array

path="/eos/atlas/atlascerngroupdisk/phys-top/toproperties/ttgamma/v010_march18/CR1S/"
signal = "*ttgamma*"
background="*ttbar*"
gStyle.SetOptStat(0); 
signal_chain = TChain("nominal")
background_chain = TChain("nominal")

channels=["ejets/","mujets/","ee/","emu/","mumu/"]
for i in channels:
  signal_chain.Add(path+i+signal)
  background_chain.Add(path+i+background)

canvas = TCanvas("canvas","",0,0,800,800);
canvas.SetFillColor(0);

# Upper histogram plot is pad1
# canvas.cd(1)
pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
pad1.SetBottomMargin(0)  # joins upper and lower plot
#pad1.SetGridx()
pad1.Draw()
# Lower ratio plot is pad2
pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
pad2.SetTopMargin(0.01)  # joins upper and lower plot
pad2.SetBottomMargin(0.2)
#pad2.SetGridx()
pad2.Draw()
pad1.cd()


bin_sizes = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
bin_sizes_array = array('d',bin_sizes)
binnum = 10
PPT_s_nocut = TH1D("PPT_s_nocut","PPT_s_nocut", binnum, bin_sizes_array);
PPT_b_nocut = TH1D("PPT_b_nocut","PPT_b_nocut", binnum, bin_sizes_array);
PPT_s_FCL = TH1D("PPT_s_FCL","PPT_s_FCL", binnum, bin_sizes_array);
PPT_b_FCL = TH1D("PPT_b_FCL","PPT_b_FCL", binnum, bin_sizes_array);
PPT_s_FCTCO = TH1D("PPT_s_FCTCO","PPT_s_FCTCO", binnum, bin_sizes_array);
PPT_b_FCTCO = TH1D("PPT_b_FCTCO","PPT_b_FCTCO", binnum, bin_sizes_array);
PPT_s_FCT = TH1D("PPT_s_FCT","PPT_s_FCT", binnum, bin_sizes_array);
PPT_b_FCT = TH1D("PPT_b_FCT","PPT_b_FCT", binnum, bin_sizes_array);


signal_chain.Draw("ph_HFT_MVA>>PPT_s_nocut","!(event_photonorigin == 10 || event_photonorigin == 20 )","norm")
background_chain.Draw("ph_HFT_MVA>>PPT_b_nocut","event_photonorigin == 10","norm")

signal_chain.Draw("ph_HFT_MVA>>PPT_s_FCL","!(event_photonorigin == 10 || event_photonorigin == 20 ) && ph_isoFCL","norm")
background_chain.Draw("ph_HFT_MVA>>PPT_b_FCL","event_photonorigin == 10 && ph_isoFCL","norm")

signal_chain.Draw("ph_HFT_MVA>>PPT_s_FCTCO","!(event_photonorigin == 10 || event_photonorigin == 20 ) && ph_isoFCTCO","norm")
background_chain.Draw("ph_HFT_MVA>>PPT_b_FCTCO","event_photonorigin == 10 && ph_isoFCTCO","norm")

signal_chain.Draw("ph_HFT_MVA>>PPT_s_FCT","!(event_photonorigin == 10 || event_photonorigin == 20 ) && ph_isoFCT","norm")
background_chain.Draw("ph_HFT_MVA>>PPT_b_FCT","event_photonorigin == 10 && ph_isoFCT","norm")

PPT_s_nocut.Draw("H")
PPT_b_nocut.Draw("same p")
PPT_s_FCT.Draw("same H")
PPT_b_FCT.Draw("same p")
PPT_s_FCL.Draw("same H")
PPT_b_FCL.Draw("same p")
PPT_s_FCTCO.Draw("same H")
PPT_b_FCTCO.Draw("same p")


PPT_s_nocut.SetTitle("")
y1 = PPT_s_nocut.GetYaxis()
y1.SetTitle("A.U.")
y1.SetRangeUser(0.,0.4)
x1 = PPT_s_nocut.GetXaxis()
x1.SetTitle("PPT output")
x1.SetLimits(0.,1)

PPT_s_nocut.SetLineColor(632)
PPT_b_nocut.SetLineColor(625)
PPT_b_nocut.SetMarkerColor(625)

PPT_s_FCT.SetLineColor(419)
PPT_b_FCT.SetLineColor(417)
PPT_b_FCT.SetMarkerColor(417)

PPT_s_FCL.SetLineColor(860)
PPT_b_FCL.SetLineColor(856)
PPT_b_FCL.SetMarkerColor(856)

PPT_s_FCTCO.SetLineColor(1)
PPT_b_FCTCO.SetLineColor(1)
PPT_b_FCTCO.SetMarkerColor(1)

# Line and marker width

PPT_s_nocut.SetLineWidth(2)
PPT_b_nocut.SetLineWidth(2)
PPT_b_nocut.SetMarkerStyle(20)

PPT_s_FCT.SetLineWidth(2)
PPT_b_FCT.SetLineWidth(2)
PPT_b_FCT.SetMarkerStyle(20)

PPT_s_FCL.SetLineWidth(2)
PPT_b_FCL.SetLineWidth(2)
PPT_b_FCL.SetMarkerStyle(20)

PPT_s_FCTCO.SetLineWidth(2)
PPT_b_FCTCO.SetLineWidth(2)
PPT_b_FCTCO.SetMarkerStyle(20)

lumi = TLatex();
lumi.SetNDC();
lumi.SetTextAlign(12);
lumi.SetTextFont(63);
lumi.SetTextSizePixels(19);
lumi.DrawLatex(0.2,0.85, "#it{#scale[1.2]{ATLAS}} #bf{Internal}");
lumi.DrawLatex(0.2,0.81, "#bf{#sqrt{s}=13 TeV}");

leg = TLegend(0.2,0.58,0.35,0.75);
leg.SetTextSize(0.02);
leg.AddEntry(PPT_s_nocut,"no requirement signal","l");
leg.AddEntry(PPT_b_nocut,"no requirement background","lep");

leg.AddEntry(PPT_s_FCL,"FixedCutLoose signal","l");
leg.AddEntry(PPT_b_FCL,"FixedCutLoose background","lep");

leg.AddEntry(PPT_s_FCTCO,"FixedCutTightCaloOnly signal","l");
leg.AddEntry(PPT_b_FCTCO,"FixedCutTightCaloOnly background","lep");

leg.AddEntry(PPT_s_FCT,"FixedCutTight signal","l");
leg.AddEntry(PPT_b_FCT,"FixedCutTight background","lep");


# leg.AddEntry(bkg_goodPh,"ph_ptcone20, 1 good, tight photon","l");


leg.SetBorderSize(0)
leg.Draw()
#################################
ratio1 = PPT_s_nocut.Clone("ratio")
#ratio1.SetMarkerStyle(20)
ratio1.SetMinimum(0)
ratio1.SetMaximum(2)
ratio1.Sumw2()
ratio1.SetStats(0)
ratio1.Divide(PPT_s_FCT)
ratio1.SetTitle("")
y = ratio1.GetYaxis()
y.SetTitle("Nominal / Isolation")
y.SetNdivisions(505)
y.SetTitleSize(20)
y.SetTitleFont(43)
y.SetTitleOffset(1.55)
y.SetLabelFont(43)
y.SetLabelSize(15)
x = ratio1.GetXaxis()
x.SetTitle("PPT Output")
x.SetTitleSize(20)
x.SetTitleFont(43)
x.SetTitleOffset(3.2)
x.SetLabelFont(43)
x.SetLabelSize(15)
pad2.cd()
ratio1.SetLineColor(419)
ratio1.SetMarkerStyle(20)
ratio1.SetMarkerColor(419)
ratio1.Draw("")

ratio2 = PPT_s_nocut.Clone("ratio")
ratio2.Divide(PPT_s_FCTCO)
ratio2.SetLineColor(1)
ratio2.SetMarkerStyle(20)
ratio2.SetMarkerColor(1)
ratio2.Draw("same")

ratio3 = PPT_s_nocut.Clone("ratio")
ratio3.Divide(PPT_s_FCL)
ratio3.SetLineColor(860)
ratio3.SetMarkerStyle(20)
ratio3.SetMarkerColor(860)
ratio3.Draw("same")

sig_ratio = TLatex();
sig_ratio.SetNDC();
sig_ratio.SetTextAlign(12);
sig_ratio.SetTextFont(63);
sig_ratio.SetTextSizePixels(18);
sig_ratio.DrawLatex(0.8,0.85, "#bf{signal}");

line = TF1("fa1","1",-1000,1000);
line.Draw("same")
line.SetLineColor(632);
###############################

canvas.SaveAs("PPT_isolation.eps")

