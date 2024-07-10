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
from ROOT import Form

cat_list = ["HHH6b_0bh0h","HHH6b_1Higgs","HHH6b_2Higgs","HHH6b_3Higgs",
            "HHH6b_3bh0h","HHH6b_2bh1h","HHH6b_1bh2h","HHH6b_0bh3h",
            "HHH6b_2bh0h","HHH6b_1bh1h","HHH6b_0bh2h"]

sample_list = ["c3_0_d4_0","c3_0_d4_99","c3_0_d4_m1","c3_19_d4_19","c3_1_d4_0","c3_4_d4_9","c3_m1_d4_0","c3_m1_d4_m1","c3_m1p5_d4_m0p5"]
sample_list = ["ggHH_kl_5_kt_1","ggHH_kl_1_kt_1","ggHH_kl_0_kt_1"]
# sample_list = ["GluGluToHHHTo6B_SM","GluGluToHHTo4B_cHHH0", "GluGluToHHTo4B_cHHH1", "GluGluToHHTo4B_cHHH5","HHHTo6B_c3_0_d4_99","HHHTo6B_c3_0_d4_minus1","HHHTo6B_c3_19_d4_19","HHHTo6B_c3_1_d4_0","HHHTo6B_c3_1_d4_2","HHHTo6B_c3_2_d4_minus1","HHHTo6B_c3_4_d4_9","HHHTo6B_c3_minus1_d4_0","HHHTo6B_c3_minus1_d4_minus1","HHHTo6B_c3_minus1p5_d4_minus0p5"]
# sample_list = ["data_obs","QCD","GluGluToHHTo4B_cHHH1","GluGluToHHHTo6B_SM"]
path_for_plot = "/eos/home-x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/plots/kappa_compare"

year = ["HH_4B","HHH_HH","HHH_only","SM_only"]
year = ["HHH_HH"]
path = "/eos/user/x/xgeng/workspace/HHH/CMSSW_11_3_4/src/datacards_maker_hhh/teste_datacards/v33/kappa_run2"
for cat in cat_list:
    for sample in sample_list:
        file_kappa=ROOT.TFile("%s/HHH_HH/histograms_ProbMultiHProb%s.root"%(path,cat), "READ")
        file_SM=ROOT.TFile("%s/SM_only/histograms_ProbMultiHProb%s.root"%(path,cat), "READ")
                # print(file_kappa)
        diction_kappa = file_kappa.Get("HHH_kappa")
        diction_SM = file_SM.Get("HHH_kappa")
        hist_SM = diction_SM.Get("%s"%(sample))
        if sample == "GluGluToHHTo4B_cHHH1":
            sample_kappa = "ggHH_kl_1_kt_1"
        elif sample == "GluGluToHHHTo6B_SM":
            sample_kappa = "c3_0_d4_0"
        else :
            sample_kappa = sample

        hist_kappa = diction_kappa.Get("%s"%(sample_kappa))
        


        xtitle   = 'ProbMultiH'
        # y_max= hist_kappa.GetMaximum()+0.2*hist_kappa.GetMaximum()
        max_1 = hist_SM.GetMaximum()
        max_2 = hist_kappa.GetMaximum()
        y_max = max(max_1,max_2)*1.2
        y_min = 0.0
        ROOT.gROOT.SetBatch(True)
        cc = ROOT.TCanvas("cc", "cc", 1000, 800)
        cc.SetTopMargin(0.1)
        cc.SetBottomMargin(0.1)
        cc.SetLeftMargin(0.12)
        cc.SetRightMargin(0.07)
        cc.SetPad(0.0,0.02,0.98,0.98)
        cc.SetGrid()
        hist_SM.SetLineColor(1)
        hist_SM.SetLineWidth(2)
        hist_SM.SetMarkerColor(1)
        hist_SM.SetMarkerStyle(23)
        hist_SM.SetXTitle(xtitle)
        hist_SM.GetXaxis().SetLabelSize(0.04)    
        hist_SM.GetXaxis().SetTitleOffset(0.9)
        # hist_SM.SetYTitle(ytitle)
        hist_SM.SetAxisRange(y_min, y_max, "Y")
        hist_SM.GetYaxis().SetLabelSize(0.04)
        hist_SM.SetTitle("{}:{}".format(cat,sample))
        hist_SM.SetStats(0)

        hist_kappa.SetLineColor(2)
        hist_kappa.SetLineWidth(2)
        hist_kappa.SetMarkerColor(2)
        hist_kappa.SetMarkerStyle(23)
        hist_kappa.SetTitle("{}:{}".format(cat,sample))

        hist_kappa.SetStats(0)


        leg = ROOT.TLegend(0.60, 0.80, 0.999, 0.92)
        leg.AddEntry(hist_SM , "SM:{}".format(sample), "epl")
        leg.AddEntry(hist_kappa , "kappa:{}".format(sample_kappa), "epl")    
        leg.SetTextSize(0.03) 

        hist_kappa.Draw()    

        hist_SM.Draw("same")
        leg.Draw("same")


        cc.SaveAs("{}/Compare_{}_{}.pdf".format(path_for_plot,cat,sample))





