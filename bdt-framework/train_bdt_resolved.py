# Python script to train BDT

import ROOT,os

from utils import mva_variables

import argparse
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('--year', default='run2') # year
parser.add_argument('--nTrees', default = '200') 
parser.add_argument('--maxDepth', default = '3') 
parser.add_argument('--nCuts', default = '50') 
parser.add_argument('--minNodeSize', default = '5') 
parser.add_argument('--adaBoostBeta', default = '0.15') 
parser.add_argument('--Optimise', action = 'store_true') 
parser.add_argument('--invertTrainTest', action = 'store_true') 
parser.add_argument('--category', default = 'nAK8_0_failLoose') 
parser.add_argument('--region', default = 'inclusive') 
parser.add_argument('--pnet', default = 'inclusive') 
args = parser.parse_args()

ROOT.ROOT.EnableImplicitMT()
ROOT.gROOT.SetBatch(ROOT.kTRUE)

year = args.year

#variables = ['h_fit_mass','h1_t3_mass','h2_t3_mass','h3_t3_mass','h1_t3_dRjets','h2_t3_dRjets','h3_t3_dRjets','bcand1Pt','bcand2Pt','bcand3Pt','bcand4Pt','bcand5Pt','bcand6Pt','bcand1Eta','bcand2Eta','bcand3Eta','bcand4Eta','bcand5Eta','bcand6Eta','bcand1Phi','bcand2Phi','bcand3Phi','bcand4Phi','bcand5Phi','bcand6Phi','bcand1DeepFlavB','bcand2DeepFlavB','bcand3DeepFlavB','bcand4DeepFlavB','bcand5DeepFlavB','bcand6DeepFlavB','fatJet1Mass','fatJet1Pt','fatJet1Eta','fatJet1PNetXbb','fatJet2Mass','fatJet2Pt','fatJet2Eta','fatJet2PNetXbb','fatJet3Mass','fatJet3Pt','fatJet3Eta','fatJet3PNetXbb','fatJet1PNetQCD','fatJet2PNetQCD','fatJet3PNetQCD','jet7Pt','jet7Eta','jet7Phi','jet7DeepFlavB','jet8Pt','jet8Eta','jet8Phi','jet8DeepFlavB','jet9Pt','jet9Eta','jet9Phi','jet9DeepFlavB','jet10Pt','jet10Eta','jet10Phi','jet10DeepFlavB']
#variables = ['h_fit_mass','h1_t3_mass','h2_t3_mass','h3_t3_mass','h1_t3_dRjets','h2_t3_dRjets','h3_t3_dRjets','bcand1Pt','bcand2Pt','bcand3Pt','bcand4Pt','bcand5Pt','bcand6Pt','bcand1Eta','bcand2Eta','bcand3Eta','bcand4Eta','bcand5Eta','bcand6Eta','bcand1DeepFlavB','bcand2DeepFlavB','bcand3DeepFlavB','bcand4DeepFlavB','bcand5DeepFlavB','bcand6DeepFlavB','jet7Pt','jet7Eta','jet7DeepFlavB','jet8Pt','jet8Eta','jet8DeepFlavB','jet9Pt','jet9Eta','jet9DeepFlavB','jet10Pt','jet10Eta','jet10DeepFlavB']
#variables = ['h_fit_mass']

variables = ['h2_t3_mass','h3_t3_mass','h2_t3_dRjets','h3_t3_dRjets','fatJet1Mass','fatJet1Pt','fatJet1Eta','fatJet2Mass','fatJet2Pt','fatJet2Eta','fatJet2PNetXbb','fatJet3Mass','fatJet3Pt','fatJet3Eta','fatJet3PNetXbb','fatJet1PNetQCD','fatJet2PNetQCD','fatJet3PNetQCD','mHHH','nloosebtags','nmediumbtags','ntightbtags','ht','nsmalljets','nfatjets']

#hhh_variables = ['massjet1jet2', 'massjet1jet3', 'massjet1jet4', 'massjet1jet5', 'massjet1jet6', 'massjet1jet7', 'massjet1jet8', 'massjet1jet9', 'massjet1jet10', 'massjet2jet3', 'massjet2jet4', 'massjet2jet5', 'massjet2jet6', 'massjet2jet7', 'massjet2jet8', 'massjet2jet9', 'massjet2jet10', 'massjet3jet4', 'massjet3jet5', 'massjet3jet6', 'massjet3jet7', 'massjet3jet8', 'massjet3jet9', 'massjet3jet10', 'massjet4jet5', 'massjet4jet6', 'massjet4jet7', 'massjet4jet8', 'massjet4jet9', 'massjet4jet10', 'massjet5jet6', 'massjet5jet7', 'massjet5jet8', 'massjet5jet9', 'massjet5jet10', 'massjet6jet7', 'massjet6jet8', 'massjet6jet9', 'massjet6jet10', 'massjet7jet8', 'massjet7jet9', 'massjet7jet10', 'massjet8jet9', 'massjet8jet10', 'massjet9jet10','ptjet1jet2', 'ptjet1jet3', 'ptjet1jet4', 'ptjet1jet5', 'ptjet1jet6', 'ptjet1jet7', 'ptjet1jet8', 'ptjet1jet9', 'ptjet1jet10', 'ptjet2jet3', 'ptjet2jet4', 'ptjet2jet5', 'ptjet2jet6', 'ptjet2jet7', 'ptjet2jet8', 'ptjet2jet9', 'ptjet2jet10', 'ptjet3jet4', 'ptjet3jet5', 'ptjet3jet6', 'ptjet3jet7', 'ptjet3jet8', 'ptjet3jet9', 'ptjet3jet10', 'ptjet4jet5', 'ptjet4jet6', 'ptjet4jet7', 'ptjet4jet8', 'ptjet4jet9', 'ptjet4jet10', 'ptjet5jet6', 'ptjet5jet7', 'ptjet5jet8', 'ptjet5jet9', 'ptjet5jet10', 'ptjet6jet7', 'ptjet6jet8', 'ptjet6jet9', 'ptjet6jet10', 'ptjet7jet8', 'ptjet7jet9', 'ptjet7jet10', 'ptjet8jet9', 'ptjet8jet10', 'ptjet9jet10','etajet1jet2', 'etajet1jet3', 'etajet1jet4', 'etajet1jet5', 'etajet1jet6', 'etajet1jet7', 'etajet1jet8', 'etajet1jet9', 'etajet1jet10', 'etajet2jet3', 'etajet2jet4', 'etajet2jet5', 'etajet2jet6', 'etajet2jet7', 'etajet2jet8', 'etajet2jet9', 'etajet2jet10', 'etajet3jet4', 'etajet3jet5', 'etajet3jet6', 'etajet3jet7', 'etajet3jet8', 'etajet3jet9', 'etajet3jet10', 'etajet4jet5', 'etajet4jet6', 'etajet4jet7', 'etajet4jet8', 'etajet4jet9', 'etajet4jet10', 'etajet5jet6', 'etajet5jet7', 'etajet5jet8', 'etajet5jet9', 'etajet5jet10', 'etajet6jet7', 'etajet6jet8', 'etajet6jet9', 'etajet6jet10', 'etajet7jet8', 'etajet7jet9', 'etajet7jet10', 'etajet8jet9', 'etajet8jet10', 'etajet9jet10','phijet1jet2', 'phijet1jet3', 'phijet1jet4', 'phijet1jet5', 'phijet1jet6', 'phijet1jet7', 'phijet1jet8', 'phijet1jet9', 'phijet1jet10', 'phijet2jet3', 'phijet2jet4', 'phijet2jet5', 'phijet2jet6', 'phijet2jet7', 'phijet2jet8', 'phijet2jet9', 'phijet2jet10', 'phijet3jet4', 'phijet3jet5', 'phijet3jet6', 'phijet3jet7', 'phijet3jet8', 'phijet3jet9', 'phijet3jet10', 'phijet4jet5', 'phijet4jet6', 'phijet4jet7', 'phijet4jet8', 'phijet4jet9', 'phijet4jet10', 'phijet5jet6', 'phijet5jet7', 'phijet5jet8', 'phijet5jet9', 'phijet5jet10', 'phijet6jet7', 'phijet6jet8', 'phijet6jet9', 'phijet6jet10', 'phijet7jet8', 'phijet7jet9', 'phijet7jet10', 'phijet8jet9', 'phijet8jet10', 'phijet9jet10']

hhh_variables = ['massjet1jet2', 'massjet1jet3', 'massjet1jet4', 'massjet1jet5', 'massjet1jet6', 'massjet1jet7', 'massjet1jet8', 'massjet1jet9', 'massjet1jet10', 'massjet2jet3', 'massjet2jet4', 'massjet2jet5', 'massjet2jet6', 'massjet2jet7', 'massjet2jet8', 'massjet2jet9', 'massjet2jet10', 'massjet3jet4', 'massjet3jet5', 'massjet3jet6', 'massjet3jet7', 'massjet3jet8', 'massjet3jet9', 'massjet3jet10', 'massjet4jet5', 'massjet4jet6', 'massjet4jet7', 'massjet4jet8', 'massjet4jet9', 'massjet4jet10', 'massjet5jet6', 'massjet5jet7', 'massjet5jet8', 'massjet5jet9', 'massjet5jet10', 'massjet6jet7', 'massjet6jet8', 'massjet6jet9', 'massjet6jet10', 'massjet7jet8', 'massjet7jet9', 'massjet7jet10', 'massjet8jet9', 'massjet8jet10', 'massjet9jet10','ptjet1jet2', 'ptjet1jet3', 'ptjet1jet4', 'ptjet1jet5', 'ptjet1jet6', 'ptjet1jet7', 'ptjet1jet8', 'ptjet1jet9', 'ptjet1jet10', 'ptjet2jet3', 'ptjet2jet4', 'ptjet2jet5', 'ptjet2jet6', 'ptjet2jet7', 'ptjet2jet8', 'ptjet2jet9', 'ptjet2jet10', 'ptjet3jet4', 'ptjet3jet5', 'ptjet3jet6', 'ptjet3jet7', 'ptjet3jet8', 'ptjet3jet9', 'ptjet3jet10', 'ptjet4jet5', 'ptjet4jet6', 'ptjet4jet7', 'ptjet4jet8', 'ptjet4jet9', 'ptjet4jet10', 'ptjet5jet6', 'ptjet5jet7', 'ptjet5jet8', 'ptjet5jet9', 'ptjet5jet10', 'ptjet6jet7', 'ptjet6jet8', 'ptjet6jet9', 'ptjet6jet10', 'ptjet7jet8', 'ptjet7jet9', 'ptjet7jet10', 'ptjet8jet9', 'ptjet8jet10', 'ptjet9jet10','etajet1jet2', 'etajet1jet3', 'etajet1jet4', 'etajet1jet5', 'etajet1jet6', 'etajet1jet7', 'etajet1jet8', 'etajet1jet9', 'etajet1jet10', 'etajet2jet3', 'etajet2jet4', 'etajet2jet5', 'etajet2jet6', 'etajet2jet7', 'etajet2jet8', 'etajet2jet9', 'etajet2jet10', 'etajet3jet4', 'etajet3jet5', 'etajet3jet6', 'etajet3jet7', 'etajet3jet8', 'etajet3jet9', 'etajet3jet10', 'etajet4jet5', 'etajet4jet6', 'etajet4jet7', 'etajet4jet8', 'etajet4jet9', 'etajet4jet10', 'etajet5jet6', 'etajet5jet7', 'etajet5jet8', 'etajet5jet9', 'etajet5jet10', 'etajet6jet7', 'etajet6jet8', 'etajet6jet9', 'etajet6jet10', 'etajet7jet8', 'etajet7jet9', 'etajet7jet10', 'etajet8jet9', 'etajet8jet10', 'etajet9jet10',]

#variables = mva_variables + hhh_variables
#variables = hhh_variables
variables += hhh_variables

variables = [v for v in variables if 'phi' not in v and 'Phi' not in v]
variables = [v for v in variables if 'etajet' not in v]


#variables = ['h_fit_mass']


nTrees = int(args.nTrees)
maxDepth = int(args.maxDepth)
nCuts = int(args.nCuts)
minNodeSize = int(args.minNodeSize)
adaBoostBeta = float(args.adaBoostBeta)

path = '/isilon/data/users/mstamenk/hhh-6b-producer/master/CMSSW_12_5_2/src/hhh-master/hhh-analysis-framework/bdt-framework/'
fname = 'bdt_boosted_%s_nT_%s_mD_%s_nC_%s_mNS_%s_aBB_%s.root'%(args.year,args.nTrees,args.maxDepth,args.nCuts,args.minNodeSize,args.adaBoostBeta)
fname = fname.replace('.root','_%s_loose.root'%args.category)
if args.invertTrainTest:
    fname = fname.replace('bdt_','bdt_inverted_')
f_out = ROOT.TFile(fname,'recreate')

ROOT.TMVA.Tools.Instance()

if not args.invertTrainTest:
    factory = ROOT.TMVA.Factory("TMVAClassification_%s_even"%year,f_out, "!V:!Silent:Color:DrawProgressBar:AnalysisType=Classification")
else:
    factory = ROOT.TMVA.Factory("TMVAClassification_%s_odd"%year,f_out, "!V:!Silent:Color:DrawProgressBar:AnalysisType=Classification")

datasetname = "dataset-boosted-%s-nTrees-%d-maxDepth-%d-nCuts-%d-minNodeSize-%s-adaBoostBeta-%s"%(year,nTrees,maxDepth,nCuts,args.minNodeSize,args.adaBoostBeta)

datasetname += args.category + '-loose'
if args.invertTrainTest:
    datasetname += '_inverted'
loader = ROOT.TMVA.DataLoader(datasetname)


for f in variables:
    loader.AddVariable(f)

treeS = ROOT.TChain('Events')
treeS.AddFile(path + '/' + 'v26_%s_%s_%s_%s'%(year,args.category,args.region,args.pnet) + '/' + 'train_signal.root')
#treeS.AddFile(year + '/' + 'train_signal.root')
treeB = ROOT.TChain('Events')
treeB.AddFile(path + '/' + 'v26_%s_%s_%s_%s'%(year,args.category,args.region,args.pnet) + '/' + 'train_background.root')
#treeB.AddFile(year + '/' + 'train_background.root')

testS = ROOT.TChain('Events')
testS.AddFile(path + '/' + 'v26_%s_%s_%s_%s'%(year,args.category,args.region,args.pnet) + '/' + 'test_signal.root')
#treeS.AddFile(year + '/' + 'train_signal.root')
testB = ROOT.TChain('Events')
testB.AddFile(path + '/' + 'v26_%s_%s_%s_%s'%(year,args.category,args.region,args.pnet) + '/' + 'test_background.root')
#treeB.AddFile(year + '/' + 'train_background.root')


#cutWeight = 'eventWeight * jet1BTagSF * jet2BTagSF * jet3BTagSF * jet4BTagSF * jet5BTagSF * jet6BTagSF * jet7BTagSF * jet8BTagSF * jet9BTagSF * jet10BTagSF'
#cutWeight = 'ttWeight'
cutWeight = 'eventWeight'

if not args.invertTrainTest:
    loader.AddSignalTree(treeS,1.0,ROOT.TMVA.Types.kTraining)
    loader.AddBackgroundTree(treeB,1.0, ROOT.TMVA.Types.kTraining)
    loader.AddSignalTree(testS,1.0,ROOT.TMVA.Types.kTesting)
    loader.AddBackgroundTree(testB,1.0, ROOT.TMVA.Types.kTesting)
else:
    loader.AddSignalTree(treeS,1.0,ROOT.TMVA.Types.kTesting)
    loader.AddBackgroundTree(treeB,1.0, ROOT.TMVA.Types.kTesting)
    loader.AddSignalTree(testS,1.0,ROOT.TMVA.Types.kTraining)
    loader.AddBackgroundTree(testB,1.0, ROOT.TMVA.Types.kTraining)

loader.SetSignalWeightExpression(cutWeight)
loader.SetBackgroundWeightExpression(cutWeight)

cutS = ROOT.TCut("")
cutB = ROOT.TCut("")

#loader.PrepareTrainingAndTestTree(cutS,cutB,"SplitMode=random:!V")
loader.PrepareTrainingAndTestTree(cutS,cutB,"!V")


method =  "!H:!V:NTrees=%d:MinNodeSize=%d"%(nTrees,minNodeSize)+"%"+":MaxDepth=%d:BoostType=AdaBoost:AdaBoostBeta=%.2f:SeparationType=GiniIndex:nCuts=%d:PruneMethod=NoPruning"%(maxDepth,adaBoostBeta,nCuts)
print(method)
factory.BookMethod(loader, ROOT.TMVA.Types.kBDT, "BDT", method)

if args.Optimise:
    factory.OptimizeAllMethodsForClassification()
factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

f_out.Close()

# Calculate significance on test tree

f_result = ROOT.TFile(fname)
dir_result = f_result.Get(datasetname)
tree = dir_result.Get('TestTree')
tree_train = dir_result.Get('TrainTree')

binning = '(20,-1,1)' 

h_sig_name = 'h_sig'
tree.Draw("BDT>>%s%s"%(h_sig_name,binning),"(classID == 0)* weight")
h_sig = ROOT.gPad.GetPrimitive(h_sig_name)

h_bkg_name = 'h_bkg'
tree.Draw("BDT>>%s%s"%(h_bkg_name,binning),"(classID == 1)* weight")
h_bkg = ROOT.gPad.GetPrimitive(h_bkg_name)

z = 0.
for i in range(h_sig.GetNbinsX()):
    s = h_sig.GetBinContent(i)
    b = h_bkg.GetBinContent(i)
    if (s+b) > 0:
        z += s*s / (s+b)

z = ROOT.TMath.Sqrt(z)

h_sig_name = 'h_sig_train'
tree_train.Draw("BDT>>%s%s"%(h_sig_name,binning),"(classID == 0)* weight")
h_sig = ROOT.gPad.GetPrimitive(h_sig_name)

h_bkg_name = 'h_bkg_train'
tree_train.Draw("BDT>>%s%s"%(h_bkg_name,binning),"(classID == 1)* weight")
h_bkg = ROOT.gPad.GetPrimitive(h_bkg_name)

z_train = 0.
for i in range(h_sig.GetNbinsX()):
    s = h_sig.GetBinContent(i)
    b = h_bkg.GetBinContent(i)
    if (s+b) > 0:
        z_train += s*s / (s+b)

z_train = ROOT.TMath.Sqrt(z_train)

print("Significance on TestTree: %.4f - limit: %.2f - train-limit %.2f"%(z, 1+1.64*1./z, 1+1.64*1./z_train))
print('nTrees',int(args.nTrees))
print('maxDepth',int(args.maxDepth))
print('nCuts',int(args.nCuts))
print('minNodeSize',int(args.minNodeSize))
print('adaBoostBeta',float(args.adaBoostBeta))


