import ROOT

f = ROOT.TFile('bdt_2017_nT_200_mD_3_nC_50_mNS_5_aBB_0.15.root')
d = f.Get('dataset-nTrees-200-maxDepth-3-nCuts-50-minNodeSize-5-adaBoostBeta-0.15')


tree = d.Get('TrainTree')

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
print("Significance on TestTree: %.4f - limit: %.2f"%(z, 1+1.64*1./z))

