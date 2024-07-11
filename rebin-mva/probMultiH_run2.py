import ROOT
from math import *
import shutil
import sys, os, re, shlex
import shutil,subprocess
import time
import os.path
from os import path
import glob
import gc
import math
import numpy as np
from array import array
from ROOT import gPad, TMath, TRandom3
from ROOT import kWhite, kRed, kBlue, kGreen, kSolid, kViolet, kDashed
from ROOT import RDataFrame, gRandom, TCanvas, TPaveText, RooFit, RooRealVar, RooFormulaVar, RooAddPdf, RooCBShape, RooBreitWigner, RooDataSet, RooDataHist, RooCrystalBall, RooGaussian, RooBifurGauss, RooFFTConvPdf, RooArgSet, RooArgList, RooDstD0BG, RooChebychev, RooRandom

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.ROOT.EnableImplicitMT()

path = /eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33
year_list =
cat_list = ['ProbHHH6b_3bh0h_inclusive','ProbHHH6b_2bh1h_inclusive','ProbHHH6b_1bh2h_inclusive','ProbHHH6b_0bh3h_inclusive','ProbHHH6b_3Higgs_inclusive','ProbHHH6b_2Higgs_inclusive','ProbHHH6b_1Higgs_inclusive','ProbHHH6b_0bh0h_inclusive']
files = ["data_obs",'GluGluToHHTo4B_cHHH0','GluGluToHHTo4B_cHHH1','GluGluToHHTo4B_cHHH5','GluGluToHHTo2B2Tau_SM','GluGluToHHHTo4B2Tau_SM','GluGluToHHHTo6B_SM','QCD_datadriven','GluGluToHHHTo4B2Tau_SMJERDOWN','GluGluToHHHTo4B2Tau_SMJERUP','GluGluToHHHTo4B2Tau_SMJESDOWN','GluGluToHHHTo4B2Tau_SMJESUP','GluGluToHHHTo4B2Tau_SMJMRDOWN','GluGluToHHHTo4B2Tau_SMJMRUP','GluGluToHHHTo6B_SMJERDOWN','GluGluToHHHTo6B_SMJERUP','GluGluToHHHTo6B_SMJESDOWN','GluGluToHHHTo6B_SMJESUP','GluGluToHHHTo6B_SMJMRDOWN','GluGluToHHHTo6B_SMJMRUP','GluGluToHHTo2B2Tau_SMJERDOWN','GluGluToHHTo2B2Tau_SMJERUP','GluGluToHHTo2B2Tau_SMJESDOWN','GluGluToHHTo2B2Tau_SMJESUP','GluGluToHHTo2B2Tau_SMJMRDOWN','GluGluToHHTo2B2Tau_SMJMRUP','GluGluToHHTo4B_cHHH1JERDOWN','GluGluToHHTo4B_cHHH1JERUP','GluGluToHHTo4B_cHHH1JESDOWN','GluGluToHHTo4B_cHHH1JESUP','GluGluToHHTo4B_cHHH1JMRDOWN','GluGluToHHTo4B_cHHH1JMRUP']

# categories = 


