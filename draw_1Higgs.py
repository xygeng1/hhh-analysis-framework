import ROOT
import string
import vector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import array
from ROOT import TCanvas, TGraphErrors,TGraphAsymmErrors,TGraph
from ROOT import gROOT

path_to_histograms = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v31/2018'
do_limit_input = "ProbHHH"
higgs1_path = "{}/ProbHHH6b_1Higgs_inclusive_/histograms/histograms_{}.root".format(path_to_histograms,do_limit_input)
higgs2_path = "{}/ProbHHH6b_2Higgs_inclusive_/histograms/histograms_{}.root".format(path_to_histograms,do_limit_input)


file_1Higgs = ROOT.TFile(higgs1_path)
file_2Higgs = ROOT.TFile(higgs2_path)


# ==== Reading original distributions
Hist_Data_1Higgs = file_1Higgs.Get("data_obs").Clone()
Hist_Data_1Higgs.SetName("Hist_Data_1Higgs")
Hist_Data_2Higgs = file_2Higgs.Get("data_obs").Clone()
Hist_Data_2Higgs.SetName("Hist_Data_2Higgs")

Hist_BKG_1Higgs = file_1Higgs.Get("QCD_datadriven_data").Clone()
Hist_BKG_1Higgs.SetName("Hist_BKG_1Higgs")
Hist_BKG_2Higgs = file_2Higgs.Get("QCD_datadriven_data").Clone()
Hist_BKG_2Higgs.SetName("Hist_BKG_2Higgs")

Hist_ratio_1Higgs = Hist_Data_1Higgs.Clone()
Hist_ratio_1Higgs.SetName("Hist_ratio_1Higgs")
Hist_ratio_1Higgs.SetTitle('Hist_ratio_1Higgs')


Hist_ratio_2Higgs = Hist_Data_2Higgs.Clone()
Hist_ratio_2Higgs.SetName("Hist_ratio_2Higgs")
Hist_ratio_2Higgs.SetTitle('Hist_ratio_2Higgs')

Hist_ratio_1Higgs_2Higgs = Hist_Data_2Higgs.Clone()
Hist_ratio_1Higgs_2Higgs.SetName("Hist_ratio_1Higgs_2Higgs")
Hist_ratio_1Higgs_2Higgs.SetTitle('Hist_ratio_1Higgs_2Higgs')

for i in range(1, Hist_Data_1Higgs.GetNbinsX()+1):
        # read value and error
        data_1Higgs = Hist_Data_1Higgs.GetBinContent(i)
        data_2Higgs = Hist_Data_2Higgs.GetBinContent(i)
        qcd_1Higgs  = Hist_BKG_1Higgs.GetBinContent(i)
        qcd_2Higgs  = Hist_BKG_2Higgs.GetBinContent(i)

        e_data_1Higgs = Hist_Data_1Higgs.GetBinError(i)
        e_data_2Higgs = Hist_Data_2Higgs.GetBinError(i)
        e_qcd_1Higgs  = Hist_BKG_1Higgs.GetBinError(i)
        e_qcd_2Higgs  = Hist_BKG_2Higgs.GetBinError(i)

        # Correction : Hist_BKG_2Higgs * (Hist_Data_1Higgs / Hist_BKG_1Higgs)
        ratio_1Higgs = data_1Higgs / qcd_1Higgs
        Hist_ratio_1Higgs.SetBinContent(i, ratio_1Higgs)

        ratio_2Higgs = data_2Higgs / qcd_2Higgs
        Hist_ratio_2Higgs.SetBinContent(i, ratio_2Higgs)

        ratio_1Higgs_2Higgs = (data_1Higgs / qcd_1Higgs) * (data_2Higgs / qcd_2Higgs)
        Hist_ratio_1Higgs_2Higgs.SetBinContent(i, ratio_1Higgs_2Higgs)


#==== Draw compared plot and save    
ytitle   = "Arbitray scale"
xtitle   = do_limit_input
y_min = 0.0
y_max = 200
y_M_min = 0.2
y_M_max = 1.8
# Hist_Data_2Higgs.GetYaxis().SetRangeUser(Hist_Data_2Higgs.GetMinimum(), Hist_Data_2Higgs.GetMaximum())
# Hist_Data_2Higgs.GetXaxis().SetRangeUser(Hist_Data_2Higgs.GetXaxis().GetXmin(), Hist_Data_2Higgs.GetXaxis().GetXmax())

ROOT.gROOT.SetBatch(True)

cc = ROOT.TCanvas("cc", "cc", 1000, 800)
cc.Divide(1,2,0,0,0) 

cc.cd(1)
gPad = cc.GetPad(1)
gPad.SetTopMargin(0.1)
gPad.SetBottomMargin(0.1)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.07)
gPad.SetPad(0.0,0.25,0.98,0.98)
gPad.SetGrid()
Hist_Data_1Higgs.SetLineColor(1)
Hist_Data_1Higgs.SetLineWidth(2)
Hist_Data_1Higgs.SetMarkerColor(1)
Hist_Data_1Higgs.SetMarkerStyle(23)
Hist_Data_1Higgs.SetXTitle(xtitle)
Hist_Data_1Higgs.GetXaxis().SetLabelSize(0.04)    
Hist_Data_1Higgs.GetXaxis().SetTitleOffset(0.9)
Hist_Data_1Higgs.SetYTitle(ytitle)
Hist_Data_1Higgs.SetAxisRange(y_min, y_max, "Y")
Hist_Data_1Higgs.GetYaxis().SetLabelSize(0.04)

Hist_BKG_1Higgs.SetLineColor(2)
Hist_BKG_1Higgs.SetLineWidth(2)
Hist_BKG_1Higgs.SetMarkerColor(2)
Hist_BKG_1Higgs.SetMarkerStyle(23)


leg = ROOT.TLegend(0.65, 0.67, 0.92, 0.87)
leg.AddEntry(Hist_Data_1Higgs , "Data - 1 Higgs", "epl")
leg.AddEntry(Hist_BKG_1Higgs , "BKG - 1 Higgs", "epl")    
Hist_Data_1Higgs.Draw()
Hist_BKG_1Higgs.Draw("same")    
leg.Draw("same")

ptext = ROOT.TPaveText(0.13, 0.58, 0.64, 0.86,"NDC")
ptext.SetTextFont(132)
ptext.AddText("#color[4]{Ratio (1 Higgs) = Data/BKG (1 Higgs) }")
ptext.AddText("#color[2]{Ratio (2 Higgs) = Data/BKG (2 Higgs) }")
ptext.AddText("#color[1]{Ratio (1 Higgs) * Ratio (2 Higgs)} ")
ptext.SetFillColor(ROOT.kWhite)
ptext.SetTextAlign(11)
ptext.Draw("same")

cc.cd(2)
gPad = cc.GetPad(2)
gPad.SetTopMargin(0.05)
gPad.SetBottomMargin(0.3)
gPad.SetLeftMargin(0.12)
gPad.SetRightMargin(0.07)
gPad.SetPad(0.0,0.06,0.98,0.25)

Hist_ratio_1Higgs.GetXaxis().SetTitleOffset(2.8)
Hist_ratio_1Higgs.SetLineColor(4)
Hist_ratio_1Higgs.SetLineWidth(2)
Hist_ratio_1Higgs.SetMarkerColor(4)
Hist_ratio_1Higgs.SetMarkerStyle(23)
Hist_ratio_1Higgs.GetXaxis().SetLabelSize(0.1)
Hist_ratio_1Higgs.GetYaxis().SetLabelSize(0.18)
# Hist_ratio_1Higgs.SetLabelSize(100,"X")
# Hist_ratio_1Higgs.SetLabelSize(100,"Y")
Hist_ratio_1Higgs.SetXTitle(xtitle)
Hist_ratio_1Higgs.GetXaxis().SetLabelSize(0.2)    
Hist_ratio_1Higgs.GetXaxis().SetTitleOffset(0.9)
Hist_ratio_1Higgs.SetYTitle(ytitle)
Hist_ratio_1Higgs.SetAxisRange(y_M_min, y_M_max, "Y")
Hist_ratio_1Higgs.GetYaxis().SetTitle("")
Hist_ratio_1Higgs.GetYaxis().SetLabelSize(0)
Hist_ratio_1Higgs.SetStats(0)
Hist_ratio_1Higgs.GetYaxis().SetLabelSize(0.15)
Hist_ratio_1Higgs.GetYaxis().SetNdivisions(505)
Hist_ratio_2Higgs.SetLineColor(2)
Hist_ratio_2Higgs.SetLineWidth(2)
Hist_ratio_1Higgs_2Higgs.SetLineColor(1)
Hist_ratio_1Higgs_2Higgs.SetLineWidth(2)

Hist_ratio_1Higgs.Draw("hist")
Hist_ratio_2Higgs.Draw("hist && same")
Hist_ratio_1Higgs_2Higgs.Draw("hist && same")




cc.SaveAs("1Higgs_2Higgs_check.pdf")


    
    