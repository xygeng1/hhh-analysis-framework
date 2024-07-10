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



import ROOT
from ROOT import RDF


# variables_to_save_vec = ROOT.std.vector('string')(variables_to_save)
path = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33'
# for era in ["2016","2016APV","2017","2018"]:
    # for cat in ['ProbHHH6b_2bh0h_inclusive_CR','ProbHHH6b_1bh1h_inclusive_CR','ProbHHH6b_0bh2h_inclusive_CR','ProbHHH6b_3bh0h_inclusive_CR','ProbHHH6b_2bh1h_inclusive_CR','ProbHHH6b_1bh2h_inclusive_CR','ProbHHH6b_0bh3h_inclusive_CR','ProbHHH6b_3Higgs_inclusive_CR','ProbHHH6b_2Higgs_inclusive_CR','ProbHHH6b_1Higgs_inclusive_CR','ProbHHH6b_0bh0h_inclusive_CR']:
for cat in ['ProbHHH6b_2bh0h_inclusive_CR','ProbHHH6b_1bh1h_inclusive_CR','ProbHHH6b_0bh2h_inclusive_CR','ProbHHH6b_3bh0h_inclusive_CR','ProbHHH6b_2bh1h_inclusive_CR','ProbHHH6b_1bh2h_inclusive_CR','ProbHHH6b_0bh3h_inclusive_CR','ProbHHH6b_1Higgs_inclusive_CR','ProbHHH6b_0bh0h_inclusive_CR','ProbHHH6b_2Higgs_inclusive_CR','ProbHHH6b_3Higgs_inclusive_CR']:
    for sample in ['HHHTo6B_c3_0_d4_99','HHHTo6B_c3_0_d4_minus1','HHHTo6B_c3_19_d4_19','HHHTo6B_c3_1_d4_0','HHHTo6B_c3_1_d4_2','HHHTo6B_c3_2_d4_minus1','HHHTo6B_c3_4_d4_9','HHHTo6B_c3_minus1_d4_0','HHHTo6B_c3_minus1_d4_minus1','HHHTo6B_c3_minus1p5_d4_minus0p5','data_obs','QCD_datadriven','GluGluToHHHTo6B_SM','GluGluToHHTo4B_cHHH0','GluGluToHHTo4B_cHHH1','GluGluToHHTo4B_cHHH5']:
        proc_list = ['%s/2016/%s/%s.root'%(path,cat,sample),'%s/2016APV/%s/%s.root'%(path,cat,sample),'%s/2017/%s/%s.root'%(path,cat,sample),'%s/2018/%s/%s.root'%(path,cat,sample)]
        df = ROOT.RDataFrame('Events', proc_list)
        
