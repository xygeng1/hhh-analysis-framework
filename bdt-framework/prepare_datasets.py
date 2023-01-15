# Script to prepare data set for MVA training
import os, ROOT

from utils import get_scans

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.ROOT.EnableImplicitMT()

variables = ['h_fit_mass','h1_t3_mass','h2_t3_mass','h3_t3_mass','h1_t3_dRjets','h2_t3_dRjets','h3_t3_dRjets','bcand1Pt','bcand2Pt','bcand3Pt','bcand4Pt','bcand5Pt','bcand6Pt','bcand1Eta','bcand2Eta','bcand3Eta','bcand4Eta','bcand5Eta','bcand6Eta','bcand1Phi','bcand2Phi','bcand3Phi','bcand4Phi','bcand5Phi','bcand6Phi','bcand1DeepFlavB','bcand2DeepFlavB','bcand3DeepFlavB','bcand4DeepFlavB','bcand5DeepFlavB','bcand6DeepFlavB','fatJet1Mass','fatJet1Pt','fatJet1Eta','fatJet1PNetXbb','fatJet2Mass','fatJet2Pt','fatJet2Eta','fatJet2PNetXbb','fatJet3Mass','fatJet3Pt','fatJet3Eta','fatJet3PNetXbb','fatJet1PNetQCD','fatJet2PNetQCD','fatJet3PNetQCD','jet7Pt','jet7Eta','jet7Phi','jet7DeepFlavB','jet8Pt','jet8Eta','jet8Phi','jet8DeepFlavB','jet9Pt','jet9Eta','jet9Phi','jet9DeepFlavB','jet10Pt','jet10Eta','jet10Phi','jet10DeepFlavB','eventWeightBTagCorrected','eventWeight', 'bcand1BTagSF','bcand2BTagSF','bcand3BTagSF','bcand4BTagSF','bcand5BTagSF','bcand6BTagSF','jet7BTagSF','jet8BTagSF','jet9BTagSF','jet10BTagSF', 'ttWeight','dtWeight']

if __name__ == '__main__':
    year = '2016APV'
    #path = '/isilon/data/users/mstamenk/eos-triple-h/v23/mva-inputs-HLT-TripleBTagCSV-Calib-v23-inclusive-loose-wp-0ptag-%s-btagSF'%(year)
    #path = '/isilon/data/users/mstamenk/eos-triple-h/v23/mva-inputs-HLT-TripleBTagCSV-MVAInputs-v23-inclusive-loose-wp-0ptag-%s-btagSF'%year
    #path = '/isilon/data/users/mstamenk/eos-triple-h/v23/mva-inputs-HLT-TripleBTagCSV-MVAInputs-TTWeights-v23-inclusive-loose-wp-0ptag-%s-btagSF'%year
    path = '/isilon/data/users/mstamenk/eos-triple-h/v24/mva-inputs-HLT-inputs-for-MVA-training-v24-inclusive-loose-wp-0ptag-%s'%year
    signal_vector = ROOT.std.vector('string')()
    background_vector = ROOT.std.vector('string')()

    scans = get_scans(year)
    scan = scans['LLLLLL']

    for f in ['GluGluToHHHTo6B_SM.root']:
        signal_vector.push_back(path + '/' + f)

    signal_samples = [signal_vector, 'signal']

    for f in ['QCD.root','TT.root','WJetsToQQ.root','WWTo4Q.root','WWW.root','WWZ.root','WZZ.root','ZJetsToQQ.root','ZZTo4Q.root','ZZZ.root']:
    #for f in ['QCD.root','TT.root','WJetsToQQ.root','WWTo4Q.root','WWW.root','WZZ.root','ZJetsToQQ.root','ZZTo4Q.root','ZZZ.root']:
        background_vector.push_back(path + '/' + f)
    background_samples = [background_vector, 'background']

    for files, label in [signal_samples,background_samples]:
        print(">>> Extract the training and testing events for {} from the {} dataset.".format(label, files))
        df = ROOT.RDataFrame('Events',files)

        cut = scan[0]
        dt_weight = scan[1]

        df = df.Filter(cut, 'LLLLL cut')
        dt_weight = dt_weight.replace('eventWeight','eventWeightBTagCorrected')

        tt_weight = scan[2]
        tt_weight = tt_weight.replace('eventWeight','eventWeightBTagCorrected')
        print(cut)
        print(dt_weight)
        print(tt_weight)

        df = df.Define('dtWeight',dt_weight)
        df = df.Define('ttWeight',tt_weight)

        report = df.Report()

        columns = ROOT.std.vector["string"](variables)

        df.Filter("event % 2 == 0", "Select even events for training").Snapshot('Events', year + '/' + 'train_%s.root'%label,columns)
        df.Filter("event % 2 == 1", "Select even events for testing").Snapshot('Events', year + '/' + 'test_%s.root'%label,columns)
        report.Print()


