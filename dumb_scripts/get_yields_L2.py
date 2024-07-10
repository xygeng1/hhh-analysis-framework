import ROOT
cat_list = ["HHH6b_0bh0h","HHH6b_1Higgs",
            "HHH6b_3bh0h","HHH6b_2bh1h","HHH6b_1bh2h","HHH6b_0bh3h",
            "HHH6b_2bh0h","HHH6b_1bh1h","HHH6b_0bh2h"]

# year_list = ["2016_merged","2017","2018"]
year_list = ["run2"]

# sample_list = ["GluGluToHHHTo6B_SM","GluGluToHHTo4B_cHHH0", "GluGluToHHTo4B_cHHH1", "GluGluToHHTo4B_cHHH5","HHHTo6B_c3_0_d4_99","HHHTo6B_c3_0_d4_minus1","HHHTo6B_c3_19_d4_19","HHHTo6B_c3_1_d4_0","HHHTo6B_c3_1_d4_2","HHHTo6B_c3_2_d4_minus1","HHHTo6B_c3_4_d4_9","HHHTo6B_c3_minus1_d4_0","HHHTo6B_c3_minus1_d4_minus1","HHHTo6B_c3_minus1p5_d4_minus0p5"]
sample_list = ["data_obs","GluGluToHHHTo6B_SM", "GluGluToHHTo4B_cHHH1", "GluGluToHHHTo4B2Tau_SM","GluGluToHHTo2B2Tau_SM","QCD"]

for cat in cat_list:
    for year in year_list:
        print("integral value for %s %s is "%(year,cat))

        for sample in sample_list:
            # path = "/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33_new/%s/Prob%s_inclusive_CR/histograms"%(year,cat)
            path = "/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33_new/sample_original_slim/%s/Prob%s_inclusive_CR/histograms"%(year,cat)
            file_kappa=ROOT.TFile("%s/histograms_ProbMultiH.root"%(path), "READ")
            hist = file_kappa.Get("%s"%(sample))
            integral = hist.Integral()
            # print(sample)
            print(integral)
