import ROOT
import string
import vector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import array
import random
from ROOT import TCanvas, TGraphErrors,TGraphAsymmErrors,TGraph
from ROOT import gROOT
from ROOT import Form


def get_random_color():
    color_index = random.randint(500, 999)
    while not ROOT.TColor.GetColor(color_index):
        color_index = random.randint(500, 999)
    return color_index

cat_list = ["HHH6b_0bh0h","HHH6b_1Higgs","HHH6b_2Higgs","HHH6b_3Higgs",
            "HHH6b_3bh0h","HHH6b_2bh1h","HHH6b_1bh2h","HHH6b_0bh3h",
            "HHH6b_2bh0h","HHH6b_1bh1h","HHH6b_0bh2h"]
# cat_list = ["HHH6b_0bh0h"]

# sample_list = ["c3_0_d4_0","c3_0_d4_99","c3_0_d4_m1","c3_19_d4_19","c3_1_d4_0","c3_4_d4_9","c3_m1_d4_0","c3_m1_d4_m1","c3_m1p5_d4_m0p5"]
sample_list = ["ggHH_kl_5_kt_1","ggHH_kl_1_kt_1","ggHH_kl_0_kt_1"]
# sample_list = ["GluGluToHHHTo6B_SM","GluGluToHHTo4B_cHHH0", "GluGluToHHTo4B_cHHH1", "GluGluToHHTo4B_cHHH5","HHHTo6B_c3_0_d4_99","HHHTo6B_c3_0_d4_minus1","HHHTo6B_c3_19_d4_19","HHHTo6B_c3_1_d4_0","HHHTo6B_c3_1_d4_2","HHHTo6B_c3_2_d4_minus1","HHHTo6B_c3_4_d4_9","HHHTo6B_c3_minus1_d4_0","HHHTo6B_c3_minus1_d4_minus1","HHHTo6B_c3_minus1p5_d4_minus0p5"]
# sample_list = ["data_obs","QCD","GluGluToHHTo4B_cHHH1","GluGluToHHHTo6B_SM"]
path_for_plot = "/eos/home-x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/plots/kappa_compare"
color_list = [1,2,210]
year = ["HH_4B","HHH_HH","HHH_only","SM_only"]
year = ["HHH_HH"]
path = "/eos/user/x/xgeng/workspace/HHH/CMSSW_11_3_4/src/datacards_maker_hhh/teste_datacards/v33/kappa_run2"

for cat in cat_list:
    file_kappa = ROOT.TFile("%s/HHH_HH/histograms_ProbMultiHProb%s.root" % (path, cat), "READ")
    diction_kappa = file_kappa.Get("HHH_kappa")

    

for cat in cat_list:
    global_min = float('inf')
    global_max = float('-inf')
    ROOT.gROOT.SetBatch(True)
    cc = ROOT.TCanvas("cc", "cc", 1000, 800)
    cc.SetTopMargin(0.1)
    cc.SetBottomMargin(0.1)
    cc.SetLeftMargin(0.12)
    cc.SetRightMargin(0.07)
    cc.SetPad(0.0,0.02,0.98,0.98)
    cc.SetGrid()
    leg = ROOT.TLegend(0.70, 0.82, 0.999, 0.95)
    # leg.SetNColumns(2)
    color_index = 0
    first_plot = 1
    file_kappa=ROOT.TFile("%s/HHH_HH/histograms_ProbMultiHProb%s.root"%(path,cat), "READ")
            # print(file_kappa)
    diction_kappa = file_kappa.Get("HHH_kappa") 
    for sample in sample_list:
        hist_kappa = diction_kappa.Get("%s" % (sample))
        integral = hist_kappa.Integral()
        if integral != 0:
            hist_kappa.Scale(1.0 / integral)
        
        min_bin = hist_kappa.GetMinimum()
        if  min_bin < global_min:
            global_min = min_bin
        
        max_bin = hist_kappa.GetMaximum()
        if max_bin > global_max:
            global_max = max_bin
    # hist_0_0 = diction_kappa.Get("c3_0_d4_0")
   
    for sample in sample_list:
        hist_kappa = diction_kappa.Get("%s"%(sample))
        integral = hist_kappa.Integral()
        if integral != 0:
            hist_kappa.Scale(1.0 / integral)
        
        xtitle   = 'ProbMultiH'
        min_bin = hist_kappa.GetMinimum()
        # if min_bin <= 0:
        #     print("0 bin in %s : %s"%(cat,sample))
        #     break
    
        y_max = global_max * 1.2
        y_min = global_min * 0.8
        # print (global_max)
        # print (global_min)
        
        hist_kappa.SetLineColor(color_list[color_index])
        hist_kappa.SetLineWidth(2)
        hist_kappa.SetMarkerColor(color_list[color_index])
        color_index = color_index +1
        hist_kappa.SetMarkerStyle(23)
        hist_kappa.SetXTitle(xtitle)
        hist_kappa.GetXaxis().SetLabelSize(0.04)    
        hist_kappa.GetXaxis().SetTitleOffset(0.9)
        hist_kappa.SetAxisRange(y_min, y_max, "Y")
        hist_kappa.GetYaxis().SetLabelSize(0.04)
        hist_kappa.SetTitle("{}".format(cat))
        hist_kappa.SetStats(0)
        leg.AddEntry(hist_kappa , "SM:{}".format(sample), "epl")
        leg.SetTextSize(0.03) 

        if first_plot:
            hist_kappa.Draw()    
            first_plot = 0
        else :
            hist_kappa.Draw("same")

    leg.Draw("same")
    # cc.SetLogy()
    cc.Update()
    cc.SaveAs("{}/Compare_{}_HH_norm.pdf".format(path_for_plot,cat))





