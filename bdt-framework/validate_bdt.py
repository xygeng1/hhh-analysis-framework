#  Script to plot the output of the TMVA training
import ROOT

ROOT.TMVA.Tools.Instance()

import argparse
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('--file', default='bdt_boosted_2016APV2016_nT_200_mD_3_nC_250_mNS_7_aBB_1.0_nAK8_1p_loose.root') 
parser.add_argument('--dataset', default='dataset-boosted-2016APV2016-nTrees-200-maxDepth-3-nCuts-250-minNodeSize-7-adaBoostBeta-1.0nAK8_1p-loose') 
args = parser.parse_args()

f_name = args.file
data_name = args.dataset
print(data_name)

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.TMVA.mvas(data_name,f_name,3)
ROOT.TMVA.correlations(data_name,f_name)
ROOT.TMVA.BDTControlPlots(data_name,f_name)
ROOT.TMVA.efficiencies(data_name,f_name,2)
ROOT.TMVA.variables(data_name,f_name)



ROOT.gROOT.SetBatch(ROOT.kFALSE)
ROOT.TMVA.mvaeffs(data_name,f_name) # only works without batch mode
