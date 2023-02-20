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




labels = {
          #'h1_mass' : 'm(H1)',
          #'h2_mass' : 'm(H2)',
          #'h3_mass' : 'm(H3)',

          #'h1_pt' : 'p_{T}(H1)',
          #'h2_pt' : 'p_{T}(H2)',
          #'h3_pt' : 'p_{T}(H3)',

          #'h1_eta' : '#eta(H1)',
          #'h2_eta' : '#eta(H2)',
          #'h3_eta' : '#eta(H3)',

          #'h1_phi' : '#phi(H1)',
          #'h2_phi' : '#phi(H2)',
          #'h3_phi' : '#phi(H3)',

          #'h1_t2_mass' : 'm(H1)',
          #'h2_t2_mass' : 'm(H2)',
          #'h3_t2_mass' : 'm(H3)',

          'h1_t3_mass' : 'm(H1)',
          'h2_t3_mass' : 'm(H2)',
          'h3_t3_mass' : 'm(H3)',


          'h_fit_mass' : 'm(H) fitted',

          #'h1_t2_pt' : 'p_{T}(H1)',
          #'h2_t2_pt' : 'p_{T}(H2)',
          #'h3_t2_pt' : 'p_{T}(H3)',

          #'h1_t2_eta' : '#eta(H1)',
          #'h2_t2_eta' : '#eta(H2)',
          #'h3_t2_eta' : '#eta(H3)',

          #'h1_t2_phi' : '#phi(H1)',
          #'h2_t2_phi' : '#phi(H2)',
          #'h3_t2_phi' : '#phi(H3)',

          #'h1_t2_match' : 'H1 truth matched',
          #'h2_t2_match' : 'H2 truth matched',
          #'h3_t2_match' : 'H3 truth matched',

          #'h1_t2_dRjets' : '#Delta R(j1,j2) H1',
          #'h2_t2_dRjets' : '#Delta R(j3,j4) H2',
          #'h3_t2_dRjets' : '#Delta R(j5,j6) H3',

          'h1_t3_pt' : 'p_{T}(H1)',
          'h2_t3_pt' : 'p_{T}(H2)',
          'h3_t3_pt' : 'p_{T}(H3)',

          'h1_t3_eta' : '#eta(H1)',
          'h2_t3_eta' : '#eta(H2)',
          'h3_t3_eta' : '#eta(H3)',

          'h1_t3_phi' : '#phi(H1)',
          'h2_t3_phi' : '#phi(H2)',
          'h3_t3_phi' : '#phi(H3)',

          'h1_t3_dRjets' : '#Delta R(j1,j2) H1',
          'h2_t3_dRjets' : '#Delta R(j3,j4) H2',
          'h3_t3_dRjets' : '#Delta R(j5,j6) H3',

          'h1_t3_match' : 'H1 truth matched',
          'h2_t3_match' : 'H2 truth matched',
          'h3_t3_match' : 'H3 truth matched',

          #'h1_match' : 'H1 truth matched',
          #'h2_match' : 'H2 truth matched',
          #'h3_match' : 'H3 truth matched',

          'bcand1Pt' : 'Jet 1 p_{T}',
          'bcand2Pt' : 'Jet 2 p_{T}',
          'bcand3Pt' : 'Jet 3 p_{T}',
          'bcand4Pt' : 'Jet 4 p_{T}',
          'bcand5Pt' : 'Jet 5 p_{T}',
          'bcand6Pt' : 'Jet 6 p_{T}',

          'bcand1Eta' : 'Jet 1 #eta',
          'bcand2Eta' : 'Jet 2 #eta',
          'bcand3Eta' : 'Jet 3 #eta',
          'bcand4Eta' : 'Jet 4 #eta',
          'bcand5Eta' : 'Jet 5 #eta',
          'bcand6Eta' : 'Jet 6 #eta',

          'bcand1Phi' : 'Jet 1 #phi',
          'bcand2Phi' : 'Jet 2 #phi',
          'bcand3Phi' : 'Jet 3 #phi',
          'bcand4Phi' : 'Jet 4 #phi',
          'bcand5Phi' : 'Jet 5 #phi',
          'bcand6Phi' : 'Jet 6 #phi',

          'bcand1DeepFlavB' : 'Jet 1 b-tag score',
          'bcand2DeepFlavB' : 'Jet 2 b-tag score',
          'bcand3DeepFlavB' : 'Jet 3 b-tag score',
          'bcand4DeepFlavB' : 'Jet 4 b-tag score',
          'bcand5DeepFlavB' : 'Jet 5 b-tag score',
          'bcand6DeepFlavB' : 'Jet 6 b-tag score',

          'bcand1HiggsMatched' : 'Jet 1 truth matched',
          'bcand2HiggsMatched' : 'Jet 2 truth matched',
          'bcand3HiggsMatched' : 'Jet 3 truth matched',
          'bcand4HiggsMatched' : 'Jet 4 truth matched',
          'bcand5HiggsMatched' : 'Jet 5 truth matched',
          'bcand6HiggsMatched' : 'Jet 6 truth matched',

          'fatJet1Mass' : 'm(H1)',
          'fatJet2Mass' : 'm(H2)',
          'fatJet3Mass' : 'm(H3)',

          'fatJet1Pt' : 'p_{T}(H1)',
          'fatJet2Pt' : 'p_{T}(H2)',
          'fatJet3Pt' : 'p_{T}(H3)',

          'fatJet1Eta' : '#eta(H1)',
          'fatJet2Eta' : '#eta(H2)',
          'fatJet3Eta' : '#eta(H3)',

          'fatJet1Phi' : '#phi(H1)',
          'fatJet2Phi' : '#phi(H2)',
          'fatJet3Phi' : '#phi(H3)',

          'fatJet1PNetXbb' : 'PNet Xbb(H1)',
          'fatJet2PNetXbb' : 'PNet Xbb(H2)',
          'fatJet3PNetXbb' : 'PNet Xbb(H3)',

          'fatJet1PNetXjj' : 'PNet Xjj(H1)',
          'fatJet2PNetXjj' : 'PNet Xjj(H2)',
          'fatJet3PNetXjj' : 'PNet Xjj(H3)',

          'fatJet1PNetQCD' : 'PNet QCD(H1)',
          'fatJet2PNetQCD' : 'PNet QCD(H2)',
          'fatJet3PNetQCD' : 'PNet QCD(H3)',

          'HHH_mass' : 'm(HHH)',
          'HHH_pt': 'p_{T}(HHH)',
          'HHH_eta': 'eta_{T}(HHH)',

          #'hhh_resolved_mass': 'm(HHH)',
          #'hhh_resolved_pt': 'p_{T}(HHH)',
          #'hhh_t3_pt': 'p_{T}(HHH)',

          #'hhh_mass': 'm(HHH)',
          #'hhh_pt': 'p_{T}(HHH)',

          #'nfatjets' : 'N fat-jets',
          'nprobejets' : 'N fat-jets',
          'nbtags' : 'N b-tags',

          'Nloosebtags' : 'N loose b-tags',
          'Nmediumbtags' : 'N medium b-tags',
          'Ntightbtags' : 'N tight b-tags',

          'ht' : 'Event HT [GeV]',
          #'tot' : 'Event HT [GeV]',
          #'pass' : 'Event HT [GeV]',
          'met' : 'E_{T}^{miss} [GeV]',
          'bdt' : 'BDT output score',
          'mva' : 'BDT output score',

          'jet1DeepFlavB' : 'jet 1 DeepJet b-score',
          'jet2DeepFlavB' : 'jet 2 DeepJet b-score',
          'jet3DeepFlavB' : 'jet 3 DeepJet b-score',
          'jet4DeepFlavB' : 'jet 4 DeepJet b-score',
          'jet5DeepFlavB' : 'jet 5 DeepJet b-score',
          'jet6DeepFlavB' : 'jet 6 DeepJet b-score',

        }

binnings = {
          'h1_mass' : '(30,0,300)',
          'h2_mass' : '(30,0,300)',
          'h3_mass' : '(30,0,300)',

          'h1_pt' : '(50,0,500)',
          'h2_pt' : '(50,0,500)',
          'h3_pt' : '(50,0,500)',

          'h1_eta' : '(30,0,5)',
          'h2_eta' : '(30,0,5)',
          'h3_eta' : '(30,0,5)',

          'h1_phi' : '(30,0,3.2)',
          'h2_phi' : '(30,0,3.2)',
          'h3_phi' : '(30,0,3.2)',

          #'h1_match' : '(2,0,2)',
          #'h2_match' : '(2,0,2)',
          #'h3_match' : '(2,0,2)',

          'h_fit_mass' : '(30,0,300)',

          'h1_t3_dRjets' : '(40,0,4)',
          'h2_t3_dRjets' : '(40,0,4)',
          'h3_t3_dRjets' : '(40,0,4)',

          'h1_t3_mass' : '(30,0,300)',
          'h2_t3_mass' : '(30,0,300)',
          'h3_t3_mass' : '(30,0,300)',

          'h1_t3_pt' : '(50,0,500)',
          'h2_t3_pt' : '(50,0,500)',
          'h3_t3_pt' : '(50,0,500)',

          'h1_t3_eta' : '(30,0,5)',
          'h2_t3_eta' : '(30,0,5)',
          'h3_t3_eta' : '(30,0,5)',

          'h1_t3_phi' : '(30,0,3.2)',
          'h2_t3_phi' : '(30,0,3.2)',
          'h3_t3_phi' : '(30,0,3.2)',

          #'h1_t3_match' : '(2,0,2)',
          #'h2_t3_match' : '(2,0,2)',
          #'h3_t3_match' : '(2,0,2)',

          'fatJet1Mass' : '(30,0,300)',
          'fatJet2Mass' : '(30,0,300)',
          'fatJet3Mass' : '(30,0,300)',

          'fatJet1Pt' : '(85,150,1000)',
          'fatJet2Pt' : '(85,150,1000)',
          'fatJet3Pt' : '(85,150,1000)',

          'fatJet1Eta' : '(30,0,5)',
          'fatJet2Eta' : '(30,0,5)',
          'fatJet3Eta' : '(30,0,5)',

          'fatJet1Phi' : '(30,0,3.2)',
          'fatJet2Phi' : '(30,0,3.2)',
          'fatJet3Phi' : '(30,0,3.2)',

          'bcand1Pt' : '(85,0,500)',
          'bcand2Pt' : '(85,0,500)',
          'bcand3Pt' : '(85,0,500)',
          'bcand4Pt' : '(85,0,500)',
          'bcand5Pt' : '(85,0,500)',
          'bcand6Pt' : '(85,0,500)',

          'bcand1Eta' : '(30,0,5)',
          'bcand2Eta' : '(30,0,5)',
          'bcand3Eta' : '(30,0,5)',
          'bcand4Eta' : '(30,0,5)',
          'bcand5Eta' : '(30,0,5)',
          'bcand6Eta' : '(30,0,5)',

          #'bcand1Phi' : '(60,0,3.2)',
          #'bcand2Phi' : '(60,0,3.2)',
          #'bcand3Phi' : '(60,0,3.2)',
          #'bcand4Phi' : '(60,0,3.2)',
          #'bcand5Phi' : '(60,0,3.2)',
          #'bcand6Phi' : '(60,0,3.2)',

          #'bcand1DeepFlavB' : '(40,0,1)',
          #'bcand2DeepFlavB' : '(40,0,1)',
          #'bcand3DeepFlavB' : '(40,0,1)',
          #'bcand4DeepFlavB' : '(40,0,1)',
          #'bcand5DeepFlavB' : '(40,0,1)',
          #'bcand6DeepFlavB' : '(40,0,1)',


          #'bcand1HiggsMatched' : '(2,0,2)',
          #'bcand2HiggsMatched' : '(2,0,2)',
          #'bcand3HiggsMatched' : '(2,0,2)',
          #'bcand4HiggsMatched' : '(2,0,2)',
          #'bcand5HiggsMatched' : '(2,0,2)',
          #'bcand6HiggsMatched' : '(2,0,2)',

          'fatJet1PNetXbb' : '(20,0,1)',
          'fatJet2PNetXbb' : '(20,0,1)',
          'fatJet3PNetXbb' : '(20,0,1)',

          'fatJet1PNetXjj' : '(20,0,1)',
          'fatJet2PNetXjj' : '(20,0,1)',
          'fatJet3PNetXjj' : '(20,0,1)',

          'fatJet1PNetQCD' : '(20,0,1)',
          'fatJet2PNetQCD' : '(20,0,1)',
          'fatJet3PNetQCD' : '(20,0,1)',

          'HHH_mass' : '(80,0,1600)',
          'HHH_pt': '(80,0,800)',
          'HHH_eta': '(30,0,5)',

          #'hhh_resolved_mass': '(80,0,1600)',
          #'hhh_resolved_pt': '(80,0,800)',
          #'hhh_t3_pt': '(80,0,800)',

          #'hhh_mass': '(155,400,3500)',
          #'hhh_pt': '(80,0,800)',

          #'nfatjets' : '(5,0,5)',
          'nprobejets' : '(5,0,5)',
          'nbtags' : '(10,0,10)',

          'Nloosebtags' : '(10,0,10)',
          'Nmediumbtags' : '(10,0,10)',
          'Ntightbtags' : '(10,0,10)',

          'ht' : '(200,0,2000)',
          #'tot' : '(200,0,2000)',
          #'pass' : '(200,0,2000)',
          'met' : '(150,0,1500)',
          'bdt' : '(20,-1,1)',
          'mva' : '(20,-0.6,0.8)',

          'jet1DeepFlavB' : '(20,0,1)',
          'jet2DeepFlavB' : '(20,0,1)',
          'jet3DeepFlavB' : '(20,0,1)',
          'jet4DeepFlavB' : '(20,0,1)',
          'jet5DeepFlavB' : '(20,0,1)',
          'jet6DeepFlavB' : '(20,0,1)',

        }

#cuts = {#'resolved' : ROOT.TCut('nbtags == 6 && nfatjets == 0 && nbtags > 4',
#        #'boosted'  : 'nfatjets == 3 && nbtags > 4',
#        'nFJ0'  : 'nfatjets == 0',
#        'nFJ1'  : 'nfatjets == 1',
#        'nFJ2'  : 'nfatjets == 2',
#        'nFJ3'  : 'nfatjets == 3',
#        'inclusive' : '1'
#        }

cuts = {
        'nFJ0'  : 'nprobejets == 0',
        'nFJ1'  : 'nprobejets == 1',
        'nFJ2'  : 'nprobejets == 2',
        'nFJ3'  : 'nprobejets == 3',
        'inclusive' : '1',
        'nFJ1p' : 'nprobejets > 0',
        }

hist_properties = {'JetHT' : [ROOT.kBlack, 0.8, 0, 'Data', True] , # [color, marker size, line size, legend label , add in legend]
                   'JetHT-btagSF' : [ROOT.kBlack, 0.8, 0, 'Data', True],
                   'BTagCSV' : [ROOT.kBlack, 0.8, 0, 'Data', True],
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

# try to do this smarther == no triplicate computations
computeMHHH = '''
    float computeMHHH(int type, float h1_t3_mass, float h1_t3_pt, float h1_t3_eta, float h1_t3_phi,float h2_t3_mass, float h2_t3_pt, float h2_t3_eta, float h2_t3_phi, float h3_t3_mass, float h3_t3_pt, float h3_t3_eta, float h3_t3_phi) {
        TLorentzVector h1;
        TLorentzVector h2;
        TLorentzVector h3;

        h1.SetPtEtaPhiM(h1_t3_pt, h1_t3_eta, h1_t3_phi, h1_t3_mass);
        h2.SetPtEtaPhiM(h2_t3_pt, h2_t3_eta, h2_t3_phi, h2_t3_mass);
        h3.SetPtEtaPhiM(h3_t3_pt, h3_t3_eta, h3_t3_phi, h3_t3_mass);


        if (type == 0)
            return (h1+h2+h3).M();
        else if (type == 1)
            return (h1+h2+h3).Pt();
        else if (type == 2)
            return (h1+h2+h3).Eta();
        else return 0;
    }

'''

def init_mhhh():
    ROOT.gInterpreter.Declare(computeMHHH)

def addMHHH(df):
    df = df.Define('HHH_mass', 'computeMHHH(0, h1_t3_mass,h1_t3_pt,h1_t3_eta,h1_t3_phi,h2_t3_mass,h2_t3_pt,h2_t3_eta,h2_t3_phi,h3_t3_mass,h3_t3_pt,h3_t3_eta,h3_t3_phi)')
    df = df.Define('HHH_pt', 'computeMHHH(1, h1_t3_mass,h1_t3_pt,h1_t3_eta,h1_t3_phi,h2_t3_mass,h2_t3_pt,h2_t3_eta,h2_t3_phi,h3_t3_mass,h3_t3_pt,h3_t3_eta,h3_t3_phi)')
    df = df.Define('HHH_eta', 'computeMHHH(2, h1_t3_mass,h1_t3_pt,h1_t3_eta,h1_t3_phi,h2_t3_mass,h2_t3_pt,h2_t3_eta,h2_t3_phi,h3_t3_mass,h3_t3_pt,h3_t3_eta,h3_t3_phi)')
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
