import ROOT
import shutil
import sys, os, re, shlex
from Correction import Unc_Shape
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

#import tdrstyle,CMS_lumi

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.ROOT.EnableImplicitMT()

from utils import histograms_dict, wps_years, wps, tags, luminosities, hlt_paths, triggersCorrections, hist_properties, init_mhhh, addMHHH, clean_variables, initialise_df, save_variables, init_get_max_prob, init_get_max_cat
from machinelearning import init_bdt, add_bdt, init_bdt_boosted, add_bdt_boosted
from calibrations import btag_init, addBTagSF, addBTagEffSF
from hhh_variables import add_hhh_variables

from optparse import OptionParser


## already doing plots, will do histogram file only to the chosen variable
seconds0 = time.time()
#histograms = []
procstodo = ["DYJetsToLL","GluGluToHHHTo4B2Tau_SM","GluGluToHHTo2B2Tau_SM","GluGluToHHTo4B_cHHH0","GluGluToHHTo4B_cHHH1","GluGluToHHTo4B_cHHH5","TTToSemiLeptonic", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TTToHadronic","TTTo2L2Nu", "QCD","QCD_datadriven_data", "data_obs" , "GluGluToHHHTo6B_SM","WWW","WWZ","WZZ","ZZZ"]

for proctodo in procstodo:
    output_tree = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v31/2018/ProbHH4b_2Higgs_inclusive_'
    outtree = "{}/{}.root".format(output_tree,proctodo)
    chunk_df = ROOT.RDataFrame('Events', outtree)
    variables = chunk_df.GetColumnNames()
    output_histos = "{}/histograms".format(output_tree)
    nameout = output_histos + '/' + 'histograms_%s.root'%(proctodo)
    f_out = ROOT.TFile(nameout, 'recreate')
    f_out.cd()
    print("Writing in %s" % nameout)


    print("Will produce histograms for following variables:")
    print(variables)
    for var in variables: # booking all variables to be produced   
        try :
            histograms_dict[var]
        except :
            # print("The binning options for the variable %s should be added in utils" % var)
            continue
        nbins = histograms_dict[var]["nbins"]
        xmin = histograms_dict[var]["xmin"]
        xmax = histograms_dict[var]["xmax"]
        # define_bins = histograms_dict[do_limit_input]["define_bins"]
        # print("11111111")

       
        

        

        f_out.cd()
        char_var = var.c_str()
        try:
            #h_tmp = chunk_df.Fill(template, [char_var, 'totalWeight'])
            f_out.cd()
            h_tmp = chunk_df.Filter("%s > %s"%(char_var,xmin)).Histo1D((char_var,char_var,nbins,xmin,xmax),char_var, 'totalWeight')
            if proctodo == "data_obs":
                data_value = h_tmp.Integral()
                print("already get the data value !!!!!!!!!!!!!")
                print(h_tmp.Integral())

            if proctodo == "QCD_datadriven_data":
                print(h_tmp.Integral())
                h_tmp.Scale(data_value/h_tmp.Integral())
                print("already scale the QCD !!!!!!!!!!!!!")
                print(h_tmp.Integral())


            h_tmp.SetTitle('%s'%(var))
            h_tmp.SetName('%s'%(var))
            h_tmp.Write()
            

        except:
            print("%s likely has 0 events"%proctodo)

    f_out.Close()
    seconds = time.time()
    print("Seconds to load : ", seconds-seconds0)
        #print("Minutes to load : ", (seconds-seconds0)/60.0)
