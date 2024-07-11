import subprocess
import os,sys
import ROOT


bdt_cut_strings = ["divide_bdt_cut_0","divide_bdt_cut_0.1","divide_bdt_cut_0.2","divide_bdt_cut_0.3", "divide_bdt_cut_0.4","divide_bdt_cut_0.5","divide_bdt_cut_0.6","divide_bdt_cut_0.7"]
btag_cut_strings = ["gt5bloose_0PFfat_","gt5bloose_gt0medium_0PFfat_", "gt5bloose_gt1medium_0PFfat_", "gt5bloose_gt2medium_0PFfat_", "gt5bloose_gt3medium_0PFfat_", "gt5bloose_gt4medium_0PFfat_", "gt5bmedium_0PFfat_"]
process_strings = ["ZZZ", "WZZ", "WWZ", "WWW", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TTToHadronic","TTTo2L2Nu","TTToSemiLeptonic", "QCD", "QCD_bEnriched", "data_obs" , "GluGluToHHHTo6B_SM"]
year = '2016'
path = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output'



for bdt_cut in bdt_cut_strings:
    for btag_cut in btag_cut_strings:
        output_folder = "{}/2016_all/{}/{}/histograms".format(path,bdt_cut,btag_cut)

        output_folder1 = "{}/2016_all/".format(path)
        if not os.path.exists(output_folder1) :
            procs=subprocess.Popen(['mkdir %s' % output_folder1],shell=True,stdout=subprocess.PIPE)
            out = procs.stdout.read()
            print("made directory %s" % output_folder1)
            
        output_folder2 = "{}/2016_all/{}/".format(path,bdt_cut)
        if not os.path.exists(output_folder2) :
            procs=subprocess.Popen(['mkdir %s' % output_folder2],shell=True,stdout=subprocess.PIPE)
            out = procs.stdout.read()
            print("made directory %s" % output_folder2)

        output_folder3 = "{}/2016_all/{}/{}".format(path,bdt_cut,btag_cut)
        if not os.path.exists(output_folder3) :
            procs=subprocess.Popen(['mkdir %s' % output_folder3],shell=True,stdout=subprocess.PIPE)
            out = procs.stdout.read()
            print("made directory %s" % output_folder3)
        
        if not os.path.exists(output_folder) :
            procs=subprocess.Popen(['mkdir %s' % output_folder],shell=True,stdout=subprocess.PIPE)
            out = procs.stdout.read()
            print("made directory %s" % output_folder)
        for process in process_strings:
            os.system("hadd -f  %s/2016_all/%s/%s/%s.root  %s/2016/%s/%s/%s.root  %s/2016APV/%s/%s/%s.root"%(path,bdt_cut,btag_cut,process,path,bdt_cut,btag_cut,process,path,bdt_cut,btag_cut,process)) 


