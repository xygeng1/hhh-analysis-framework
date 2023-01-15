import ROOT
import numpy as np
import pickle


#variables = ['h_fit_mass','h1_t3_mass','h2_t3_mass','h3_t3_mass','h1_t3_dRjets','h2_t3_dRjets','h3_t3_dRjets','bcand1Pt','bcand2Pt','bcand3Pt','bcand4Pt','bcand5Pt','bcand6Pt','bcand1Eta','bcand2Eta','bcand3Eta','bcand4Eta','bcand5Eta','bcand6Eta','bcand1Phi','bcand2Phi','bcand3Phi','bcand4Phi','bcand5Phi','bcand6Phi','bcand1DeepFlavB','bcand2DeepFlavB','bcand3DeepFlavB','bcand4DeepFlavB','bcand5DeepFlavB','bcand6DeepFlavB','fatJet1Mass','fatJet1Pt','fatJet1Eta','fatJet1PNetXbb','fatJet2Mass','fatJet2Pt','fatJet2Eta','fatJet2PNetXbb','fatJet3Mass','fatJet3Pt','fatJet3Eta','fatJet3PNetXbb','fatJet1PNetQCD','fatJet2PNetQCD','fatJet3PNetQCD','jet7Pt','jet7Eta','jet7Phi','jet7DeepFlavB','jet8Pt','jet8Eta','jet8Phi','jet8DeepFlavB','jet9Pt','jet9Eta','jet9Phi','jet9DeepFlavB','jet10Pt','jet10Eta','jet10Phi','jet10DeepFlavB','eventWeightBTagCorrected']
variables = ['h_fit_mass','h1_t3_mass','h2_t3_mass','h3_t3_mass','h1_t3_dRjets','h2_t3_dRjets','h3_t3_dRjets','bcand1Pt','bcand2Pt','bcand3Pt','bcand4Pt','bcand5Pt','bcand6Pt','bcand1Eta','bcand2Eta','bcand3Eta','bcand4Eta','bcand5Eta','bcand6Eta','bcand1Phi','bcand2Phi','bcand3Phi','bcand4Phi','bcand5Phi','bcand6Phi','bcand1DeepFlavB','bcand2DeepFlavB','bcand3DeepFlavB','bcand4DeepFlavB','bcand5DeepFlavB','bcand6DeepFlavB','fatJet1Mass','fatJet1Pt','fatJet1Eta','fatJet1PNetXbb','fatJet2Mass','fatJet2Pt','fatJet2Eta','fatJet2PNetXbb','fatJet3Mass','fatJet3Pt','fatJet3Eta','fatJet3PNetXbb','fatJet1PNetQCD','fatJet2PNetQCD','fatJet3PNetQCD','jet7Pt','jet7Eta','jet7Phi','jet7DeepFlavB','jet8Pt','jet8Eta','jet8Phi','jet8DeepFlavB','jet9Pt','jet9Eta','jet9Phi','jet9DeepFlavB','jet10Pt','jet10Eta','jet10Phi','jet10DeepFlavB']


def load_data(signal_filename, background_filename):
    # Read data from ROOT files
    data_sig = ROOT.RDataFrame("Events", signal_filename).AsNumpy()
    data_bkg = ROOT.RDataFrame("Events", background_filename).AsNumpy()

    # Convert inputs to format readable by machine learning tools
    x_sig = np.vstack([data_sig[var] for var in variables]).T
    x_bkg = np.vstack([data_bkg[var] for var in variables]).T
    x = np.vstack([x_sig, x_bkg])

    # Create labels
    num_sig = x_sig.shape[0]
    num_bkg = x_bkg.shape[0]
    y = np.hstack([np.ones(num_sig), np.zeros(num_bkg)])

    # Compute weights balancing both classes
    num_all = num_sig + num_bkg
    w = np.hstack([np.ones(num_sig) * num_all / num_sig, np.ones(num_bkg) * num_all / num_bkg])

    return x, y, w

if __name__ == "__main__":
    print("Starting training")
    year = '2018'
    # Load data
    x, y, w = load_data(year + '/' + "train_signal.root", year + '/' + "train_background.root")

    # Fit xgboost model
    from xgboost import XGBClassifier
    bdt = XGBClassifier(max_depth=3, n_estimators=500)
    bdt.fit(x, y, sample_weight=w)

    # Save model in TMVA format
    print("Training done on ",x.shape[0],"events. Saving model in xgboost_%s.root"%year)
    ROOT.TMVA.Experimental.SaveXGBoost(bdt, "myBDT", "xgboost_%s.root"%year, num_inputs=x.shape[1])


    #print("Starting testing")

    #x_test, y_test, w_test = load_data(year + '/' + "test_signal.root", year + '/' + "test_background.root")
    #bdt_file = "xgboost_%s.root"%year

    #bdt = ROOT.TMVA.Experimental.RBDT[""]("myBDT", File)
    #y_test_pred = bdt.Compute(x_test)

    #from sklearn.metrics import roc_curve, auc
    #fpr, tpr, _ = roc_curve(y_test, y_test_pred, sample_weight=w_test)
    #score = auc(fpr, tpr)

    #c = ROOT.TCanvas("roc", "", 600, 600)
    #g = ROOT.TGraph(len(fpr), fpr, tpr)
    #g.SetTitle("AUC = {:.2f}".format(score))
    #g.SetLineWidth(3)
    #g.SetLineColor(ROOT.kRed)
    #g.Draw("AC")
    #g.GetXaxis().SetRangeUser(0, 1)
    #g.GetYaxis().SetRangeUser(0, 1)
    #g.GetXaxis().SetTitle("False-positive rate")
    #g.GetYaxis().SetTitle("True-positive rate")
    #c.Draw()





