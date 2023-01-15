import ROOT
import pickle

from train_and_test import load_data, variables


year = '2018'

print("Starting testing")

x_test, y_test, w_test = load_data(year + '/' + "test_signal.root", year + '/' + "test_background.root")
File = "xgboost_%s.root"%year

bdt = ROOT.TMVA.Experimental.RBDT[""]("myBDT", File)
y_test_pred = bdt.Compute(x_test)

from sklearn.metrics import roc_curve, auc
fpr, tpr, _ = roc_curve(y_test, y_test_pred, sample_weight=w_test)
score = auc(fpr, tpr)

c = ROOT.TCanvas("roc", "", 600, 600)
g = ROOT.TGraph(len(fpr), fpr, tpr)
g.SetTitle("AUC = {:.2f}".format(score))
g.SetLineWidth(3)
g.SetLineColor(ROOT.kRed)
g.Draw("AC")
g.GetXaxis().SetRangeUser(0, 1)
g.GetYaxis().SetRangeUser(0, 1)
g.GetXaxis().SetTitle("False-positive rate")
g.GetYaxis().SetTitle("True-positive rate")
c.Draw()





