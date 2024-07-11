import ROOT

path = "/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v25/"
file_list = [path+"histograms-gt5bloose_gt3medium_0PFfat-v25-CR-2017/"]
#file_list = ["/eos/user/x/xgeng/workspace/HHH/CMSSW_11_1_0_pre5_PY3/src/PhysicsTools/hhh-plotting/output/v21/histograms-HLT-selection-v21-nFJ23-loose-wp-0ptag-2017/","/eos/user/x/xgeng/workspace/HHH/CMSSW_11_1_0_pre5_PY3/src/PhysicsTools/hhh-plotting/output/v21/histograms-HLT-selection-v21-nFJ2-loose-wp-0ptag-2017/", "/eos/user/x/xgeng/workspace/HHH/CMSSW_11_1_0_pre5_PY3/src/PhysicsTools/hhh-plotting/output/v21/histograms-HLT-selection-v21-nFJ3-loose-wp-0ptag-2017/"]
for file_path in file_list:
    print(file_path)
    for str in ['BTagCSV','QCD6B','TT','ZJetsToQQ','GluGluToHHHTo6B_SM','WJetsToQQ','WWZ','ZZTo4Q','QCD','WWTo4Q','WZZ','ZZZ']: 
         #'WWW','QCD_bEnriched','QCD6B_bEnriched'
        f = ROOT.TFile(file_path + "histograms_%s.root"%(str),"READ")
        #f = ROOT.TFile(file_path + "histograms_%s.root"%(str))
        h1 = f.Get("eventWeight")
        # Get the number of entries in the histogram
        sum = h1.Integral()

        print(str)
        print(sum)
        
        #print("Integral of histogram:", integral)
    
        # Get the number of entries in the histogram

        
    
        f.Close()
     