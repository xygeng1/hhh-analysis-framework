import ROOT
cat_list = ["HHH6b_0bh0h","HHH6b_1Higgs","HHH6b_2Higgs","HHH6b_3Higgs",
            "HHH6b_2bh0h","HHH6b_1bh1h","HHH6b_0bh2h",
            "HHH6b_3bh0h","HHH6b_2bh1h","HHH6b_1bh2h","HHH6b_0bh3h"]

year_list = ["2016","2017","2018"]

# sample_list = ["GluGluToHHHTo6B_SM","GluGluToHHTo4B_cHHH0", "GluGluToHHTo4B_cHHH1", "GluGluToHHTo4B_cHHH5","HHHTo6B_c3_0_d4_99","HHHTo6B_c3_0_d4_minus1","HHHTo6B_c3_19_d4_19","HHHTo6B_c3_1_d4_0","HHHTo6B_c3_1_d4_2","HHHTo6B_c3_2_d4_minus1","HHHTo6B_c3_4_d4_9","HHHTo6B_c3_minus1_d4_0","HHHTo6B_c3_minus1_d4_minus1","HHHTo6B_c3_minus1p5_d4_minus0p5"]
sample_list = ["GluGluToHHHTo6B_SM","GluGluToHHTo4B_cHHH1","QCD","data_obs"]
for cat in cat_list:
    print("integral value for %s is "%(cat))

    for sample in sample_list:
        
        sum_sample = 0
        

        for year in year_list:

            path = "/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33_new/separate_era_histograms/Prob%s_inclusive_CR/"%(cat)
            file_kappa=ROOT.TFile("%s/histograms_ProbMultiH_sepa_era.root"%(path), "READ")
            var = "%s_%s"%(sample,year)
            if sample == 'QCD' :
                var ='QCD'
            if sample == 'data_obs' :
                var ='data_obs'


            hist = file_kappa.Get(var)
            integral = hist.Integral()
            sum_sample = sum_sample + integral
            if sample == 'QCD' or sample == 'data_obs':
                sum_sample = integral

            print(var)
            print(integral)
            # print(sample)
        # print(sample)
        # print(sum_sample)
