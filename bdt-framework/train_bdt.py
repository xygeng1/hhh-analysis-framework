# Python script to train BDT

import ROOT,os

import argparse
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('--year', default='2017') # year
parser.add_argument('--nTrees', default = '200') 
parser.add_argument('--maxDepth', default = '3') 
parser.add_argument('--nCuts', default = '50') 
parser.add_argument('--minNodeSize', default = '5') 
parser.add_argument('--adaBoostBeta', default = '0.15') 
parser.add_argument('--Optimise', action = 'store_true') 
parser.add_argument('--invertTrainTest', action = 'store_true') 
args = parser.parse_args()

ROOT.ROOT.EnableImplicitMT()
ROOT.gROOT.SetBatch(ROOT.kTRUE)

year = args.year

variables = ['h_fit_mass','h1_t3_mass','h2_t3_mass','h3_t3_mass','h1_t3_dRjets','h2_t3_dRjets','h3_t3_dRjets','bcand1Pt','bcand2Pt','bcand3Pt','bcand4Pt','bcand5Pt','bcand6Pt','bcand1Eta','bcand2Eta','bcand3Eta','bcand4Eta','bcand5Eta','bcand6Eta','bcand1Phi','bcand2Phi','bcand3Phi','bcand4Phi','bcand5Phi','bcand6Phi','bcand1DeepFlavB','bcand2DeepFlavB','bcand3DeepFlavB','bcand4DeepFlavB','bcand5DeepFlavB','bcand6DeepFlavB','fatJet1Mass','fatJet1Pt','fatJet1Eta','fatJet1PNetXbb','fatJet2Mass','fatJet2Pt','fatJet2Eta','fatJet2PNetXbb','fatJet3Mass','fatJet3Pt','fatJet3Eta','fatJet3PNetXbb','fatJet1PNetQCD','fatJet2PNetQCD','fatJet3PNetQCD','jet7Pt','jet7Eta','jet7Phi','jet7DeepFlavB','jet8Pt','jet8Eta','jet8Phi','jet8DeepFlavB','jet9Pt','jet9Eta','jet9Phi','jet9DeepFlavB','jet10Pt','jet10Eta','jet10Phi','jet10DeepFlavB']
#variables = ['h_fit_mass','h1_t3_mass','h2_t3_mass','h3_t3_mass','h1_t3_dRjets','h2_t3_dRjets','h3_t3_dRjets','bcand1Pt','bcand2Pt','bcand3Pt','bcand4Pt','bcand5Pt','bcand6Pt','bcand1Eta','bcand2Eta','bcand3Eta','bcand4Eta','bcand5Eta','bcand6Eta','bcand1DeepFlavB','bcand2DeepFlavB','bcand3DeepFlavB','bcand4DeepFlavB','bcand5DeepFlavB','bcand6DeepFlavB','jet7Pt','jet7Eta','jet7DeepFlavB','jet8Pt','jet8Eta','jet8DeepFlavB','jet9Pt','jet9Eta','jet9DeepFlavB','jet10Pt','jet10Eta','jet10DeepFlavB']
#variables = ['h_fit_mass']

#variables = ['h_fit_mass']


nTrees = int(args.nTrees)
maxDepth = int(args.maxDepth)
nCuts = int(args.nCuts)
minNodeSize = int(args.minNodeSize)
adaBoostBeta = float(args.adaBoostBeta)

path = '/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_12_5_2/src/bdt-framework/'
fname = 'bdt_%s_nT_%s_mD_%s_nC_%s_mNS_%s_aBB_%s.root'%(args.year,args.nTrees,args.maxDepth,args.nCuts,args.minNodeSize,args.adaBoostBeta)
if args.invertTrainTest:
    fname = fname.replace('bdt_','bdt_inverted_')
f_out = ROOT.TFile(fname,'recreate')

ROOT.TMVA.Tools.Instance()

if not args.invertTrainTest:
    factory = ROOT.TMVA.Factory("TMVAClassification_%s_even"%year,f_out, "!V:!Silent:Color:DrawProgressBar:AnalysisType=Classification")
else:
    factory = ROOT.TMVA.Factory("TMVAClassification_%s_odd"%year,f_out, "!V:!Silent:Color:DrawProgressBar:AnalysisType=Classification")

datasetname = "dataset-%s-nTrees-%d-maxDepth-%d-nCuts-%d-minNodeSize-%s-adaBoostBeta-%s"%(year,nTrees,maxDepth,nCuts,args.minNodeSize,args.adaBoostBeta)
if args.invertTrainTest:
    datasetname += '_inverted'
loader = ROOT.TMVA.DataLoader(datasetname)


for f in variables:
    loader.AddVariable(f)

treeS = ROOT.TChain('Events')
treeS.AddFile(path + '/' + year + '/' + 'train_signal.root')
#treeS.AddFile(year + '/' + 'train_signal.root')
treeB = ROOT.TChain('Events')
treeB.AddFile(path + '/' + year + '/' + 'train_background.root')
#treeB.AddFile(year + '/' + 'train_background.root')

testS = ROOT.TChain('Events')
testS.AddFile(path + '/' + year + '/' + 'test_signal.root')
#treeS.AddFile(year + '/' + 'train_signal.root')
testB = ROOT.TChain('Events')
testB.AddFile(path + '/' + year + '/' + 'test_background.root')
#treeB.AddFile(year + '/' + 'train_background.root')


#cutWeight = 'eventWeight * jet1BTagSF * jet2BTagSF * jet3BTagSF * jet4BTagSF * jet5BTagSF * jet6BTagSF * jet7BTagSF * jet8BTagSF * jet9BTagSF * jet10BTagSF'
#cutWeight = 'ttWeight'
cutWeight = 'dtWeight'

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


