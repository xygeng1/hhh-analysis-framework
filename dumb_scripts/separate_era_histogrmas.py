import ROOT
import shutil
import sys, os, re, shlex
from Correction_new import Unc_Shape
from array import array
#from subprocess import Popen, PIPE
#ROOT.ROOT.EnableImplicitMT()
#os.environ["MKL_NUM_THREADS"] = "1"
#os.environ["OMP_NUM_THREADS"] = "1"
import shutil,subprocess
import time
import os.path
from os import path
#from root_numpy import tree2array, array2tree
#import numpy as np
#import pandas
import glob
import gc



# 定义要合并的年份和文件名
path = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33_new'

years = ["2016_all", "2017", "2018"]
# cat_list = ['ProbHHH6b_2bh0h_inclusive_CR','ProbHHH6b_1bh1h_inclusive_CR','ProbHHH6b_0bh2h_inclusive_CR','ProbHHH6b_3bh0h_inclusive_CR','ProbHHH6b_2bh1h_inclusive_CR','ProbHHH6b_1bh2h_inclusive_CR','ProbHHH6b_0bh3h_inclusive_CR','ProbHHH6b_3Higgs_inclusive_CR','ProbHHH6b_2Higgs_inclusive_CR','ProbHHH6b_1Higgs_inclusive_CR','ProbHHH6b_0bh0h_inclusive_CR']
cat_list = ['2bh0h','1bh1h','0bh2h','3bh0h','2bh1h','1bh2h','0bh3h','3Higgs','2Higgs','1Higgs','0bh0h']



process_list = ["GluGluToHHHTo6B_SM","GluGluToHHTo4B_cHHH1","GluGluToHHHTo4B2Tau_SM","GluGluToHHTo2B2Tau_SM"]
process_data = ["QCD","data_obs"]
# 循环读取每个年份的 ROOT 文件
for cat_simple in cat_list:
    cat  = 'ProbHHH6b_%s_inclusive_CR'%(cat_simple)
    output_file_path = "%s/separate_era_histograms/%s/histograms_ProbMultiH_sepa_era.root"%(path,cat)
    output_folder1 = "{}/separate_era_histograms/{}".format(path,cat)
    if not os.path.exists(output_folder1) :
        procs=subprocess.Popen(['mkdir %s' % output_folder1],shell=True,stdout=subprocess.PIPE)
        out = procs.stdout.read()
        print("made directory %s" % output_folder1)

    f_out = ROOT.TFile(output_file_path, 'recreate')
    

    for year in years:
        input_file_path = "%s/%s/%s/histograms/histograms_ProbMultiH_fixAsy.root"%(path,year,cat)
        input_file = ROOT.TFile(input_file_path)
        # file_o = ROOT.TFile(hist_path)
        
        for key in input_file.GetListOfKeys():
            hist_name = key.GetName()
            if any(process in hist_name for process in process_list):
                hist = input_file.Get(hist_name)
                f_out.cd() 

                hist.Write()
    input_data_path = "%s/run2/%s/histograms/histograms_ProbMultiH.root"%(path,cat)
    input_data = ROOT.TFile(input_data_path)
    hist_data = input_data.Get("data_obs")
    hist_QCD = input_data.Get("QCD")
    if cat_simple in ["2bh0h","1bh1h","0bh2h","3bh0h","2bh1h","1bh2h","0bh3h","3Higgs","2Higgs"]:

        hist_QCD_down = input_data.Get("QCD_DataDriven_Shape_%sDown"%(cat_simple))
        hist_QCD_up = input_data.Get("QCD_DataDriven_Shape_%sUp"%(cat_simple))
        f_out.cd() 

        hist_QCD_up.Write()
        hist_QCD_down.Write()
    f_out.cd() 
    
    hist_data.Write()
    hist_QCD.Write()

    
    


    f_out.Close()

# 关闭输出文件
