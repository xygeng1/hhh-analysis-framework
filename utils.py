# Script to store labels and cut definitions


import random
import ROOT

q = random.uniform(0,1)

luminosities = {'2016' : 36330.0,
                '2016APV' : 19207.0,
                '2016PostAPV' : 17122.0,
                '2016' : 17122.0,
                '2017' : 41480.0,
                '2018' : 59830.0,
        }


hlt_paths = {
#        '2016' : '( HLT_QuadJet45_TripleBTagCSV_p087||  HLT_PFHT400_SixJet30_DoubleBTagCSV_p056||  HLT_PFHT450_SixJet40_BTagCSV_p056||  HLT_AK8PFJet360_TrimMass30||  HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20||  HLT_AK8PFJet450||  HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200||  HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20||  HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20||  HLT_PFJet450 ||  HLT_QuadJet45_DoubleBTagCSV_p087 )',
        '2016' : '( HLT_QuadJet45_TripleBTagCSV_p087)',
        '2016PostAPV' : '( HLT_QuadJet45_TripleBTagCSV_p087)',
#        '2016APV' : '( HLT_QuadJet45_TripleBTagCSV_p087||  HLT_PFHT400_SixJet30_DoubleBTagCSV_p056||  HLT_PFHT450_SixJet40_BTagCSV_p056||  HLT_AK8PFJet360_TrimMass30||  HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20||  HLT_AK8PFJet450||  HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200||  HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20||  HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20||  HLT_PFJet450||  HLT_PFMET120_BTagCSV_p067||  HLT_QuadJet45_DoubleBTagCSV_p087 )',
        '2016APV' : '( HLT_QuadJet45_TripleBTagCSV_p087)',
#        '2016PostAPV' : '( HLT_QuadJet45_TripleBTagCSV_p087||  HLT_PFHT400_SixJet30_DoubleBTagCSV_p056||  HLT_PFHT450_SixJet40_BTagCSV_p056||  HLT_AK8PFJet360_TrimMass30||  HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20||  HLT_AK8PFJet450||  HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200||  HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20||  HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20||  HLT_PFJet450||  HLT_QuadJet45_DoubleBTagCSV_p087 )',
#             '2017' : '(HLT_PFJet450 || HLT_PFJet500 || HLT_PFHT1050 || HLT_AK8PFJet550 || HLT_AK8PFJet360_TrimMass30 || HLT_AK8PFJet400_TrimMass30 || HLT_AK8PFHT750_TrimMass50 || HLT_AK8PFJet330_PFAK8BTagCSV_p17 || HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0 || HLT_PFMET100_PFMHT100_IDTight_CaloBTagCSV_3p1 || HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2 || HLT_PFHT380_SixPFJet32_DoublePFBTagDeepCSV_2p2 || HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5 || HLT_QuadPFJet98_83_71_15_DoubleBTagCSV_p013_p08_VBF1 || HLT_QuadPFJet98_83_71_15_BTagCSV_p013_VBF2 )',
             '2017' : '(HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0 )',
             #'2018' : '(HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5||HLT_PFHT1050||HLT_PFJet500||HLT_AK8PFJet500||HLT_AK8PFJet400_TrimMass30||HLT_AK8PFHT800_TrimMass50||HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4||HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1||HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2||HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94||HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59||HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17||HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1||HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2|| HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1)',
             '2018' : '(HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5)',
        }



phi_bins = 5
eta_bins = 10
histograms_dict = {
        'h1_t3_mass'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 300, "label" : 'm(H1) (GeV)'},
        'h2_t3_mass'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 300, "label" : 'm(H2) (GeV)'},
        'h3_t3_mass'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 300, "label" : 'm(H3) (GeV)'},

        'h_fit_mass'  : { "nbins" : 30 , "xmin" : 0 , "xmax" : 300, "label" : 'm(H) fitted (GeV)'},

        'h1_t3_pt'  : { "nbins" : 25 , "xmin" : 0 , "xmax" : 500, "label" : 'p_{T}(H1)'},
        'h2_t3_pt'  : { "nbins" : 25 , "xmin" : 0 , "xmax" : 500, "label" : 'p_{T}(H2)'},
        'h3_t3_pt'  : { "nbins" : 25 , "xmin" : 0 , "xmax" : 500, "label" : 'p_{T}(H3)'},

        'h1_t3_eta'  : { "nbins" : 15 , "xmin" : 0 , "xmax" : 3, "label" : '#eta(H1)'},
        'h2_t3_eta'  : { "nbins" : 15 , "xmin" : 0 , "xmax" : 3, "label" : '#eta(H2)'},
        'h3_t3_eta'  : { "nbins" : 15 , "xmin" : 0 , "xmax" : 3, "label" : '#eta(H3)'},

        'h1_t3_phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : '#phi(H1)'},
        'h2_t3_phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : '#phi(H2)'},
        'h3_t3_phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : '#phi(H3)'},

        'h1_t3_dRjets'  : { "nbins" : 30 , "xmin" : 0 , "xmax" : 5.0, "label" : '#Delta R(j1,j2) H1'},
        'h2_t3_dRjets'  : { "nbins" : 30 , "xmin" : 0 , "xmax" : 5.0, "label" : '#Delta R(j3,j4) H2'},
        'h3_t3_dRjets'  : { "nbins" : 30 , "xmin" : 0 , "xmax" : 5.0, "label" : '#Delta R(j5,j6) H3'},

        'h1_t3_match'  : { "nbins" : 2 , "xmin" : 0 , "xmax" : 2, "label" : 'H1 truth matched'},
        'h2_t3_match'  : { "nbins" : 2 , "xmin" : 0 , "xmax" : 2, "label" : 'H2 truth matched'},
        'h3_t3_match'  : { "nbins" : 2 , "xmin" : 0 , "xmax" : 2, "label" : 'H3 truth matched'},

        'bcand1Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'b-candidate 1 p_{T} (GeV)'},
        'bcand2Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'b-candidate 2 p_{T} (GeV)'},
        'bcand3Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'b-candidate 3 p_{T} (GeV)'},
        'bcand4Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'b-candidate 4 p_{T} (GeV)'},
        'bcand5Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'b-candidate 5 p_{T} (GeV)'},
        'bcand6Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'b-candidate 6 p_{T} (GeV)'},

        'bcand1Eta'  : { "nbins" : eta_bins , "xmin" : 0 , "xmax" : 2.5, "label" : 'b-candidate  1 #eta'},
        'bcand2Eta'  : { "nbins" : eta_bins , "xmin" : 0 , "xmax" : 2.5, "label" : 'b-candidate  2 #eta'},
        'bcand3Eta'  : { "nbins" : eta_bins , "xmin" : 0 , "xmax" : 2.5, "label" : 'b-candidate  3 #eta'},
        'bcand4Eta'  : { "nbins" : eta_bins , "xmin" : 0 , "xmax" : 2.5, "label" : 'b-candidate  4 #eta'},
        'bcand5Eta'  : { "nbins" : eta_bins , "xmin" : 0 , "xmax" : 2.5, "label" : 'b-candidate  5 #eta'},
        'bcand6Eta'  : { "nbins" : eta_bins , "xmin" : 0 , "xmax" : 2.5, "label" : 'b-candidate  6 #eta'},

        'bcand1Phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : 'b-candidate  1 #phi'},
        'bcand2Phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : 'b-candidate  2 #phi'},
        'bcand3Phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : 'b-candidate  3 #phi'},
        'bcand4Phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : 'b-candidate  4 #phi'},
        'bcand5Phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : 'b-candidate  5 #phi'},
        'bcand6Phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : 'b-candidate  5 #phi'},

        #'bcand1DeepFlavB'  : { "nbins" : 40 , "xmin" : 0 , "xmax" : 1, "label" : 'Jet 1 b-tag score'},
        #'bcand2DeepFlavB'  : { "nbins" : 40 , "xmin" : 0 , "xmax" : 1, "label" : 'Jet 2 b-tag score'},
        #'bcand3DeepFlavB'  : { "nbins" : 40 , "xmin" : 0 , "xmax" : 1, "label" : 'Jet 3 b-tag score'},
        #'bcand4DeepFlavB'  : { "nbins" : 40 , "xmin" : 0 , "xmax" : 1, "label" : 'Jet 4 b-tag score'},
        #'bcand5DeepFlavB'  : { "nbins" : 40 , "xmin" : 0 , "xmax" : 1, "label" : 'Jet 5 b-tag score'},
        #'bcand6DeepFlavB'  : { "nbins" : 40 , "xmin" : 0 , "xmax" : 1, "label" : 'Jet 6 b-tag score'},

        #'bcand1HiggsMatched'  : { "nbins" : 2 , "xmin" : 0 , "xmax" : 2, "label" : 'Jet 1 truth matched'},
        #'bcand2HiggsMatched'  : { "nbins" : 2 , "xmin" : 0 , "xmax" : 2, "label" : 'Jet 2 truth matched'},
        #'bcand3HiggsMatched'  : { "nbins" : 2 , "xmin" : 0 , "xmax" : 2, "label" : 'Jet 3 truth matched'},
        #'bcand4HiggsMatched'  : { "nbins" : 2 , "xmin" : 0 , "xmax" : 2, "label" : 'Jet 4 truth matched'},
        #'bcand5HiggsMatched'  : { "nbins" : 2 , "xmin" : 0 , "xmax" : 2, "label" : 'Jet 5 truth matched'},
        #'bcand6HiggsMatched'  : { "nbins" : 2 , "xmin" : 0 , "xmax" : 2, "label" : 'Jet 6 truth matched'},

        'fatJet1Mass'  : { "nbins" : 30 , "xmin" : 0 , "xmax" : 300, "label" : 'fatJet1 mass regressed (GeV)'},
        'fatJet2Mass'  : { "nbins" : 30 , "xmin" : 0 , "xmax" : 300, "label" : 'fatJet2 mass regressed (GeV)'},
        'fatJet3Mass'  : { "nbins" : 30 , "xmin" : 0 , "xmax" : 300, "label" : 'fatJet3 mass regressed (GeV)'},

        'fatJet1Pt'  : { "nbins" : 50 , "xmin" : 150 , "xmax" : 1000, "label" : 'p_{T}(fatJet1) (GeV)'},
        'fatJet2Pt'  : { "nbins" : 50 , "xmin" : 150 , "xmax" : 1000, "label" : 'p_{T}(fatJet2) (GeV)'},
        'fatJet3Pt'  : { "nbins" : 50 , "xmin" : 150 , "xmax" : 1000, "label" : 'p_{T}(fatJet3) (GeV)'},

        'fatJet1Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : '#eta(fatJet1)'},
        'fatJet2Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : '#eta(fatJet2)'},
        'fatJet3Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : '#eta(fatJet3)'},

        'fatJet1Phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : '#phi(fatJet1)'},
        'fatJet2Phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : '#phi(fatJet2)'},
        'fatJet3Phi'  : { "nbins" : phi_bins , "xmin" : 0 , "xmax" : 3.2, "label" : '#phi(fatJet3)'},

        'fatJet1PNetXbb'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'PNet Xbb(fatJet1)'},
        'fatJet2PNetXbb'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'PNet Xbb(fatJet2)'},
        'fatJet3PNetXbb'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'PNet Xbb(fatJet3)'},

        'fatJet1PNetXjj'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'PNet Xjj(fatJet1)'},
        'fatJet2PNetXjj'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'PNet Xjj(fatJet2)'},
        'fatJet3PNetXjj'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'PNet Xjj(fatJet3)'},

        'fatJet1PNetQCD'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'PNet QCD(fatJet1)'},
        'fatJet2PNetQCD'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'PNet QCD(fatJet2)'},
        'fatJet3PNetQCD'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'PNet QCD(fatJet3)'},

        'HHH_mass'   : { "nbins" : 80 , "xmin" : 0 , "xmax" : 1600, "label" : 'm(HHH) (GeV)'},
        'HHH_pt'     : { "nbins" : 80 , "xmin" : 0 , "xmax" : 800, "label" : 'p_{T}(HHH) (GeV)'},
        'HHH_eta'    : { "nbins" : 15 , "xmin" : 0 , "xmax" : 2.5, "label" : '#eta(HHH) (GeV)'},

        #'nfatjets'    : { "nbins" : 5 , "xmin" : 0 , "xmax" : 5, "label" : 'N fat-jets'},
        'nprobejets'  : { "nbins" : 5 , "xmin" : 0 , "xmax" : 5, "label" : 'N fat-jets'},
        'nbtags'      : { "nbins" : 10 , "xmin" : 0 , "xmax" : 10, "label" : 'N b-tags'},

        'Nloosebtags'   : { "nbins" : 10 , "xmin" : 0 , "xmax" : 10, "label" : 'N loose b-tags'},
        'Nmediumbtags'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 10, "label" : 'N meidum b-tags'},
        'Ntightbtags'   : { "nbins" : 10 , "xmin" : 0 , "xmax" : 10, "label" : 'N tight b-tags'},

        'ht'   : { "nbins" : 200 , "xmin" : 0 , "xmax" : 2000, "label" : 'Event HT [GeV]'},
        'met'  : { "nbins" : 150 , "xmin" : 0 , "xmax" : 1500, "label" : 'E_{T}^{miss} [GeV]'},
        'bdt'  : { "nbins" : 20 , "xmin" : -1 , "xmax" : 1, "label" : 'BDT output score'},
        'mva'  : { "nbins" : 20 , "xmin" : -0.6 , "xmax" : 0.8, "label" : 'BDT output score'},

        'jet1DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 1 DeepJet b-score'},
        'jet2DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 2 DeepJet b-score'},
        'jet3DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 3 DeepJet b-score'},
        'jet4DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 4 DeepJet b-score'},
        'jet5DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 5 DeepJet b-score'},
        'jet6DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 6 DeepJet b-score'},
        'jet7DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 7 DeepJet b-score'},
        'jet8DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 8 DeepJet b-score'},
        'jet9DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 9 DeepJet b-score'},
        'jet10DeepFlavB'  : { "nbins" : 20 , "xmin" : 0 , "xmax" : 1, "label" : 'jet 10 DeepJet b-score'},

        'jet1Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 1 p_{T} (GeV)'},
        'jet2Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 2 p_{T} (GeV)'},
        'jet3Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 3 p_{T} (GeV)'},
        'jet4Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 4 p_{T} (GeV)'},
        'jet5Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 5 p_{T} (GeV)'},
        'jet6Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 6 p_{T} (GeV)'},
        'jet7Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 7 p_{T} (GeV)'},
        'jet8Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 8 p_{T} (GeV)'},
        'jet9Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 9 p_{T} (GeV)'},
        'jet10Pt'  : { "nbins" : 50 , "xmin" : 0 , "xmax" : 500, "label" : 'jet 10 p_{T} (GeV)'},

        'jet1Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 1 #eta'},
        'jet2Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 2 #eta'},
        'jet3Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 3 #eta'},
        'jet4Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 4 #eta'},
        'jet5Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 5 #eta'},
        'jet6Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 6 #eta'},
        'jet7Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 7 #eta'},
        'jet8Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 8 #eta'},
        'jet9Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 9 #eta'},
        'jet10Eta'  : { "nbins" : 10 , "xmin" : 0 , "xmax" : 2.5, "label" : 'Jet 10 #eta'},

        # skip phi up to put that more automatic

}


#doing this ordered dictionary to make sure of the drawing order
# [color, marker size, line size, legend label , add in legend]
hist_properties = {'JetHT' : [ROOT.kBlack, 0.8, 0, 'Data', True] ,
                   'JetHT-btagSF' : [ROOT.kBlack, 0.8, 0, 'Data', True],
                   'BTagCSV' : [ROOT.kBlack, 0.8, 0, 'Data', True],
                   'data_obs' : [ROOT.kBlack, 0.8, 0, 'Data', True],
                   'ZZZ' : [ROOT.kRed, 0, 2, 'VVV', True],
                   'WWW' : [ROOT.kRed, 0, 2, 'VVV', False],
                   'WZZ' : [ROOT.kRed, 0, 2, 'VVV', False],
                   'WWZ' : [ROOT.kRed, 0, 2, 'VVV', False],
                   'ZJetsToQQ'   : [ROOT.kCyan, 0, 2, 'V+jets', True],
                   'WJetsToQQ'   : [ROOT.kCyan, 0, 2, 'V+jets', False],
                   'ZZTo4Q' : [ROOT.kGray, 0, 2, 'VV', True],
                   'WWTo4Q' : [ROOT.kGray, 0, 2, 'VV', False],
                   'TT' : [ROOT.kBlue, 0,2, 't#bar{t}', True],
                   'QCD'   : [ROOT.kOrange, 0, 2, 'QCD', True],
                   'QCD6B'   : [ROOT.kOrange + 2, 0, 2, 'QCD6B', True],
                   'GluGluToHHHTo6B_SM' : [ROOT.kRed, 0,2, 'SM HHH x 100', True],
        }


# cut loose = 0.0532 = 91%, medium = 0.3040 = 79%, tight = 0.7476 = 61%

# 2017
#wps = { 'loose'  : '0.0532',
#        'medium' : '0.3040',
#        'tight'  : '0.7476',
#        }

# 2018
wps = { 'loose'  : '0.0490',
        'medium' : '0.2783',
        'tight'  : '0.7100',
        }

wps_years = { 'loose' : {'2016APV': 0.0508, '2016': 0.0480, '2016PostAPV': 0.0480, '2017': 0.0532, '2018': 0.0490},
              'medium': {'2016APV': 0.2598, '2016': 0.2489, '2016PostAPV': 0.2489, '2017': 0.3040, '2018': 0.2783},
              'tight' : {'2016APV': 0.6502, '2016': 0.6377, '2016PostAPV': 0.6377, '2017': 0.7476, '2018': 0.7100},
        }

label_dict = {'L': [wps_years['loose'],'Loose'],
              'M': [wps_years['medium'],'Medium'],
              'T': [wps_years['tight'],'Tight'],
              }

def get_scans(year):
    scans = {}
    for j1 in ['L','M','T']:
        for j2 in ['L','M','T']:
            for j3 in ['L','M','T']:
                for j4 in ['L','M','T']:
                    for j5 in ['L','M','T']:
                        for j6 in ['L','M','T']:
                            cut = '(bcand1DeepFlavB > %f && bcand2DeepFlavB > %f && bcand3DeepFlavB > %f && bcand4DeepFlavB > %f && bcand5DeepFlavB > %f && bcand6DeepFlavB > %f)'%(label_dict[j1][0][year],label_dict[j2][0][year],label_dict[j3][0][year],label_dict[j4][0][year],label_dict[j5][0][year],label_dict[j6][0][year])
                            weight = 'eventWeight * bcand1%sBTagEffSF * bcand2%sBTagEffSF * bcand3%sBTagEffSF * bcand4%sBTagEffSF * bcand5%sBTagEffSF * bcand6%sBTagEffSF'%(label_dict[j1][1],label_dict[j2][1],label_dict[j3][1],label_dict[j4][1],label_dict[j5][1],label_dict[j6][1])
                            weightTT = '%s * bcand1%sTTWeight * bcand2%sTTWeight * bcand3%sTTWeight * bcand4%sTTWeight * bcand5%sTTWeight * bcand6%sTTWeight'%(weight,label_dict[j1][1],label_dict[j2][1],label_dict[j3][1],label_dict[j4][1],label_dict[j5][1],label_dict[j6][1])
                            point = j1+j2+j3+j4+j5+j6
                            scans[point] = [cut,weight,weightTT]
    return scans

tags = {'5tag' :  'bcand1DeepFlavB > %s && bcand2DeepFlavB > %s && bcand3DeepFlavB > %s && bcand4DeepFlavB > %s && bcand5DeepFlavB > %s && bcand6DeepFlavB < %s  ',
        '6tag' :  'bcand1DeepFlavB > %s && bcand2DeepFlavB > %s && bcand3DeepFlavB > %s && bcand4DeepFlavB > %s && bcand5DeepFlavB > %s && bcand6DeepFlavB > %s  ',
        '4tag' :  'bcand1DeepFlavB > %s && bcand2DeepFlavB > %s && bcand3DeepFlavB > %s && bcand4DeepFlavB > %s && bcand5DeepFlavB < %s && bcand6DeepFlavB < %s  ',
        '3tag' :  'bcand1DeepFlavB > %s && bcand2DeepFlavB > %s && bcand3DeepFlavB > %s && bcand4DeepFlavB < %s && bcand5DeepFlavB < %s && bcand6DeepFlavB < %s  ',
        '2tag' :  'bcand1DeepFlavB > %s && bcand2DeepFlavB > %s && bcand3DeepFlavB < %s && bcand4DeepFlavB < %s && bcand5DeepFlavB < %s && bcand6DeepFlavB < %s  ',
        '1tag' :  'bcand1DeepFlavB > %s && bcand2DeepFlavB < %s && bcand3DeepFlavB < %s && bcand4DeepFlavB < %s && bcand5DeepFlavB < %s && bcand6DeepFlavB < %s  ',
        '0tag' :  'bcand1DeepFlavB < %s && bcand2DeepFlavB < %s && bcand3DeepFlavB < %s && bcand4DeepFlavB < %s && bcand5DeepFlavB < %s && bcand6DeepFlavB < %s  ',
        '0ptag' :  '1',

        }

#tags = {'high': 'bcand1DeepFlavB > %s && bcand2DeepFlavB > %s && bcand3DeepFlavB > %s && bcand4DeepFlavB > %s && bcand5DeepFlavB > %s && bcand6DeepFlavB > %s'%(wps['tight'], wps['tight'], wps['tight'], wps['tight'], wps['tight'], wps['tight']),
#         'middle' : '(bcand1DeepFlavB < %s && bcand1DeepFlavB > %s) && (bcand2DeepFlavB < %s && bcand2DeepFlavB > %s) && (bcand3DeepFlavB < %s && bcand3DeepFlavB > %s) && (bcand4DeepFlavB < %s && bcand4DeepFlavB > %s) && (bcand5DeepFlavB < %s && bcand5DeepFlavB > %s) && (bcand6DeepFlavB < %s && bcand6DeepFlavB > %s)'%(wps['tight'], wps['medium'],wps['tight'], wps['medium'],wps['tight'], wps['medium'],wps['tight'], wps['medium'],wps['tight'], wps['medium'],wps['tight'], wps['medium']),
#         'low' : '(bcand1DeepFlavB < %s && bcand1DeepFlavB > %s) && (bcand2DeepFlavB < %s && bcand2DeepFlavB > %s) && (bcand3DeepFlavB < %s && bcand3DeepFlavB > %s) && (bcand4DeepFlavB < %s && bcand4DeepFlavB > %s) && (bcand5DeepFlavB < %s && bcand5DeepFlavB > %s) && (bcand6DeepFlavB < %s && bcand6DeepFlavB > %s)'%(wps['medium'], wps['loose'],wps['medium'], wps['loose'],wps['medium'], wps['loose'],wps['medium'], wps['loose'],wps['medium'], wps['loose'],wps['medium'], wps['loose']),
#
#        }

# 2016
# HLT_QuadJet45_TripleBTagCSV_p087                              36.47/36.47
# HLT_PFHT400_SixJet30_DoubleBTagCSV_p056
# HLT_PFHT450_SixJet40_BTagCSV_p056
# HLT_AK8PFJet360_TrimMass30
# HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20

# HLT_AK8PFJet450                                               33.64/36.47

# HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200                     25.36/36.47
# HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460                         25.36/36.47

# HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20               20.20/36.47
# HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20                  20.20/36.47

# HLT_PFJet450                                                  16.94/36.47
# HLT_PFMET120_BTagCSV_p067                                     16.94/36.47

# HLT_QuadJet45_DoubleBTagCSV_p087                              1.29/36.47

# 2017

# HLT_PFJet500
# HLT_PFHT1050
# HLT_AK8PFJet550

# HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0     36.67/41.48
# HLT_AK8PFJet400_TrimMass30                                    36.67/41.48

# HLT_AK8PFHT750_TrimMass50                                     30.90/41.48

# HLT_AK8PFJet360_TrimMass30                                    28.23/41.48
# HLT_PFMET100_PFMHT100_IDTight_CaloBTagCSV_3p1                 28.23/41.48

# HLT_PFHT380_SixPFJet32_DoublePFBTagDeepCSV_2p2                17.68/41.48

# HLT_PFJet450                                                  10.45/41.48

# HLT_AK8PFJet330_PFAK8BTagCSV_p17                              7.73/41.48
# HLT_QuadPFJet98_83_71_15_BTagCSV_p013_VBF2                    7.73/41.48

# HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2                    5.30/41.48
# HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5                          5.30/41.48
# HLT_QuadPFJet98_83_71_15_DoubleBTagCSV_p013_p08_VBF1          5.30/41.48

# 2018
# HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5 59.96/59.96
# HLT_PFHT1050
# HLT_PFJet500
# HLT_AK8PFJet500
# HLT_AK8PFJet400_TrimMass30
# HLT_AK8PFHT800_TrimMass50

# HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4            54.44/59.74
# HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1    54.44/59.74
# HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2              54.44/59.74

# HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94               42.28/59.96
# HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59                     42.28/59.96

# HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17               22.74/59.96

# HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1     9.25/59.96
# HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2               9.25/59.74

# HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1             1.41/59.96


hlt_sf_2016 = """
float getTriggerSF(int HLT_QuadJet45_TripleBTagCSV_p087, int HLT_PFHT400_SixJet30_DoubleBTagCSV_p056, int HLT_PFHT450_SixJet40_BTagCSV_p056, int HLT_AK8PFJet360_TrimMass30, int HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20, int HLT_AK8PFJet450, int HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200, int HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460, int HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20, int HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20, int HLT_PFJet450, int HLT_PFMET120_BTagCSV_p067, int HLT_QuadJet45_DoubleBTagCSV_p087 ){
    float triggerSF = 1;
        if (HLT_QuadJet45_TripleBTagCSV_p087 || HLT_PFHT400_SixJet30_DoubleBTagCSV_p056 || HLT_PFHT450_SixJet40_BTagCSV_p056 || HLT_AK8PFJet360_TrimMass30 || HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20) {triggerSF = 1;}
        else if (HLT_AK8PFJet450) {triggerSF = 33.64/36.47;}
        else if (HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200 || HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460) {triggerSF=25.36/36.47;}
        else if (HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20 || HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20) {triggerSF = 20.20/36.47;}
        else if (HLT_PFJet450 || HLT_PFMET120_BTagCSV_p067) {triggerSF = 16.94/36.47;}
        else if (HLT_QuadJet45_DoubleBTagCSV_p087) {triggerSF=1.29/36.47;}

    return triggerSF;
}
"""

hlt_sf_2017 = """
float getTriggerSF(int HLT_PFJet450, int HLT_PFJet500, int HLT_PFHT1050, int HLT_AK8PFJet550, int HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0, int HLT_AK8PFJet360_TrimMass30, int HLT_AK8PFHT750_TrimMass50, int HLT_AK8PFJet400_TrimMass30, int HLT_PFMET100_PFMHT100_IDTight_CaloBTagCSV_3p1, int HLT_PFHT380_SixPFJet32_DoublePFBTagDeepCSV_2p2, int HLT_AK8PFJet330_PFAK8BTagCSV_p17, int HLT_QuadPFJet98_83_71_15_BTagCSV_p013_VBF2, int HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2, int HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5, int HLT_QuadPFJet98_83_71_15_DoubleBTagCSV_p013_p08_VBF1 ){
    float triggerSF = 1;
        if (HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0) {triggerSF = 36.67/41.48;}
        //if (HLT_PFJet500 || HLT_PFHT1050 || HLT_AK8PFJet550) {triggerSF = 1;}
        //else if (HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0 || HLT_AK8PFJet400_TrimMass30 ) {triggerSF = 36.67/41.48;}
        //else if (HLT_AK8PFHT750_TrimMass50) {triggerSF=30.90/41.48;}
        //else if (HLT_AK8PFJet360_TrimMass30 || HLT_PFMET100_PFMHT100_IDTight_CaloBTagCSV_3p1) {triggerSF = 28.23/41.48;}
        //else if (HLT_PFHT380_SixPFJet32_DoublePFBTagDeepCSV_2p2) {triggerSF = 17.68/41.48;}
        //else if (HLT_PFJet450) {triggerSF=10.45/41.48;}
        //else if (HLT_AK8PFJet330_PFAK8BTagCSV_p17 || HLT_QuadPFJet98_83_71_15_BTagCSV_p013_VBF2) {triggerSF=7.73/41.48;}
        //else if (HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2 || HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5 || HLT_QuadPFJet98_83_71_15_DoubleBTagCSV_p013_p08_VBF1) {triggerSF=5.30/41.48;}

    return triggerSF;
}
"""

hlt_sf_2018 = """
float getTriggerSF( int HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5, int HLT_PFHT1050, int HLT_PFJet500, int HLT_AK8PFJet500, int HLT_AK8PFJet400_TrimMass30, int HLT_AK8PFHT800_TrimMass50, int HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4, int HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1, int HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2, int HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94, int HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59, int HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17, int HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1, int HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2, int HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1 ){
    float triggerSF = 1;
        if (HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5 || HLT_PFHT1050 || HLT_PFJet500 || HLT_AK8PFJet500 || HLT_AK8PFJet400_TrimMass30 || HLT_AK8PFHT800_TrimMass50) {triggerSF = 1;}
        else if ( HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4 || HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1 || HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2) {triggerSF = 54.44/59.74;}
        else if (HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94 || HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59) {triggerSF=42.28/59.96;}
        else if (HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17) {triggerSF = 22.74/59.96;}
        else if (HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1 || HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2) {triggerSF = 9.25/59.96;}
        else if (HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1) {triggerSF=1.41/59.96;}

    return triggerSF;
}
"""




hlt_method_2016 = 'getTriggerSF( HLT_QuadJet45_TripleBTagCSV_p087,  HLT_PFHT400_SixJet30_DoubleBTagCSV_p056,  HLT_PFHT450_SixJet40_BTagCSV_p056,  HLT_AK8PFJet360_TrimMass30,  HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20,  HLT_AK8PFJet450,  HLT_QuadPFJet_BTagCSV_p016_p11_VBF_Mqq200,  HLT_QuadPFJet_BTagCSV_p016_VBF_Mqq460,  HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20,  HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV_p20,  HLT_PFJet450,  HLT_PFMET120_BTagCSV_p067,  HLT_QuadJet45_DoubleBTagCSV_p087 );'

hlt_method_2017 = ' getTriggerSF( HLT_PFJet450,  HLT_PFJet500,  HLT_PFHT1050,  HLT_AK8PFJet550,  HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0,  HLT_AK8PFJet360_TrimMass30,  HLT_AK8PFHT750_TrimMass50,  HLT_AK8PFJet400_TrimMass30,  HLT_PFMET100_PFMHT100_IDTight_CaloBTagCSV_3p1,  HLT_PFHT380_SixPFJet32_DoublePFBTagDeepCSV_2p2,  HLT_AK8PFJet330_PFAK8BTagCSV_p17,  HLT_QuadPFJet98_83_71_15_BTagCSV_p013_VBF2,  HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2,  HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5,  HLT_QuadPFJet98_83_71_15_DoubleBTagCSV_p013_p08_VBF1 );'

hlt_method_2018 = ' getTriggerSF(HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5,HLT_PFHT1050,HLT_PFJet500,HLT_AK8PFJet500,HLT_AK8PFJet400_TrimMass30,HLT_AK8PFHT800_TrimMass50,HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4,HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1,HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2,HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94,HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59,HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17,HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1,HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2, HLT_PFMET100_PFMHT100_IDTight_CaloBTagDeepCSV_3p1);'


triggersCorrections = {
                       '2016' : [hlt_sf_2016,hlt_method_2016],
                       '2017' : [hlt_sf_2017,hlt_method_2017],
                       '2018' : [hlt_sf_2018,hlt_method_2018],
        }


path_bdt_xml = '/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_12_5_2/src/data/bdt/'
bdts_xml = {
            '2016APV' : [path_bdt_xml+'TMVAClassification_2016APV_v24_regular.xml',path_bdt_xml+'TMVAClassification_2016APV_v24_inverted.xml'],
            '2016' : [path_bdt_xml+'TMVAClassification_2016_v24_regular.xml',path_bdt_xml+'TMVAClassification_2016_v24_inverted.xml'],
            '2017' : [path_bdt_xml+'TMVAClassification_2017_v24_regular.xml',path_bdt_xml+'TMVAClassification_2017_v24_inverted.xml'],
            '2018' : [path_bdt_xml+'TMVAClassification_2018_v24_regular.xml',path_bdt_xml+'TMVAClassification_2018_v24_inverted.xml'],
            #'2017' : ['/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_12_5_2/src/data/bdt/TMVAClassification_2017_BDT.weights.xml'],
            #'2018' : '/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_12_5_2/src/data/bdt/TMVAClassification_2018_optimal_BDT.weights.xml'
            }

# Keep old function
#def add_bdt(df, xmlpath):
#    ROOT.gInterpreter.ProcessLine('''TMVA::Experimental::RReader model("{}");'''.format(xmlpath))
#    nvars = ROOT.model.GetVariableNames().size()
#    ROOT.gInterpreter.ProcessLine('''auto computeModel = TMVA::Experimental::Compute<{}, float>(model);'''.format(nvars))
#
#    l_expr = ROOT.model.GetVariableNames()
#    l_varn = ROOT.std.vector['std::string']()
#    for i_expr, expr in enumerate(l_expr):
#        varname = 'v_{}'.format(i_expr)
#        l_varn.push_back(varname)
#
#        df=df.Define(varname, '(float)({})'.format(expr) )
#
#    df = df.Define('mva', ROOT.computeModel, l_varn)
#
#    return df

def add_bdt(df, year):
    xmlpath_odd, xmlpath_even = bdts_xml[year]


    ROOT.gInterpreter.ProcessLine('''TMVA::Experimental::RReader model_even("{}");'''.format(xmlpath_even))
    nvars = ROOT.model_even.GetVariableNames().size()
    #ROOT.gInterpreter.Declare('''auto computeModel_even = TMVA::Experimental::Compute<{}, float>(model_even);'''.format(nvars))

    ROOT.gInterpreter.ProcessLine('''TMVA::Experimental::RReader model_odd("{}");'''.format(xmlpath_odd))
    nvars = ROOT.model_odd.GetVariableNames().size()
    #ROOT.gInterpreter.Declare('''auto computeModel_odd = TMVA::Experimental::Compute<{}, float>(model_odd);'''.format(nvars))

    l_expr = ROOT.model_even.GetVariableNames()
    l_varn = ROOT.std.vector['std::string']()
    l_varn.push_back('event')

    ls_var = ['int event']
    ls_call = ['event']
    ls_bdt = []

    for i_expr, expr in enumerate(l_expr):
        varname = 'v_{}'.format(i_expr)
        l_varn.push_back(varname)
        df=df.Define(varname, '(float)({})'.format(expr) )
        ls_var.append('float ' + varname)
        ls_call.append(varname)
        ls_bdt.append(varname)

    method_all = ','.join(ls_var)
    method_bdt = ','.join(ls_bdt)
    method_call = ','.join(ls_call)

    # Split even and odd numbers and apply it different mva training
    #print(" auto computeModel(%s){if (event"%(method_all) + "%"+ " 2 == 0) { return model_even.Compute({%s});}else {return model_odd.Compute({%s});}}"%(method_bdt,method_bdt))
    ROOT.gInterpreter.Declare(" auto computeModel(%s){ auto prediction = model_odd.Compute({%s}); if (event"%(method_all,method_bdt) + "%"+ " 2 == 0) { prediction =  model_even.Compute({%s});} return prediction;}"%(method_bdt))
    #ROOT.gInterpreter.Declare(" auto computeModel(%s){if (event"%(method_all) + "%"+ " 2 == 0) { return model_even.Compute({%s});}}"%(method_bdt))
    #ROOT.gInterpreter.Declare(" auto computeModel(%s){if (event"%(method_all) + "%"+ " 2 == 0) { return model_even.Compute({%s});}}"%(method_bdt))
    #ROOT.gInterpreter.Declare(" float computeModel(%s){ float sf = 0; if (event"%(method_all) + "%"+ " 2 == 0) { sf = 0;} else {sf = 1;} return sf;}")
    #method_all = 'int eventnumber'
    #print(" auto computeModel(%s){if (eventnumber"%(method_all) + "%"+ " 2 == 0){ return computeModel_even(%s);}else {return computeModel_odd(%s);}}"%(method_bdt,method_bdt))
    #print("float computeModel(%s){if (eventnumber"%(method_all) + "%"+ " 2 == 0){ return 0;}else {return 1;}}")

    #df = df.Define('mva', ROOT.computeModel, l_varn)
    #df = df.Define('mva', 'computeModel(%s)'%method_call)
    df = df.Define('mva', 'computeModel(%s)'%method_call)

    return df

computeMHHH = '''
    float computeMHHH(float h1_t3_mass, float h1_t3_pt, float h1_t3_eta, float h1_t3_phi,float h2_t3_mass, float h2_t3_pt, float h2_t3_eta, float h2_t3_phi, float h3_t3_mass, float h3_t3_pt, float h3_t3_eta, float h3_t3_phi) {
        TLorentzVector h1;
        TLorentzVector h2;
        TLorentzVector h3;

        h1.SetPtEtaPhiM(h1_t3_pt, h1_t3_eta, h1_t3_phi, h1_t3_mass);
        h2.SetPtEtaPhiM(h2_t3_pt, h2_t3_eta, h2_t3_phi, h2_t3_mass);
        h3.SetPtEtaPhiM(h3_t3_pt, h3_t3_eta, h3_t3_phi, h3_t3_mass);

        return (h1+h2+h3).M();
    }

'''

def init_mhhh():
    ROOT.gInterpreter.Declare(computeMHHH)

def addMHHH(df):
    df = df.Define('mHHH', 'computeMHHH(h1_t3_mass,h1_t3_pt,h1_t3_eta,h1_t3_phi,h2_t3_mass,h2_t3_pt,h2_t3_eta,h2_t3_phi,h3_t3_mass,h3_t3_pt,h3_t3_eta,h3_t3_phi)')
    return df

def drawText(x, y, text, color = ROOT.kBlack, fontsize = 0.05, font = 42, doNDC = True, alignment = 12):
    tex = ROOT.TLatex()
    if doNDC:
        tex.SetNDC()
    ROOT.SetOwnership(tex, False)
    tex.SetTextAlign(alignment)
    tex.SetTextSize(fontsize)
    tex.SetTextFont(font)
    tex.SetTextColor(color)
    tex.DrawLatex(x, y, text)
