import subprocess
import os,sys
import ROOT

# process_strings = ["DYJetsToLL","GluGluToHHHTo4B2Tau_SM","GluGluToHHTo2B2Tau","GluGluToHHTo4B_cHHH1","TTToSemiLeptonic","WJetsToLNu_0J","WJetsToLNu_1J","WJetsToLNu_2J", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TTToHadronic","TTTo2L2Nu", "QCD", "data_obs" , "GluGluToHHHTo6B_SM"]

year = 'run2'
path = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33_new/sample_before_slim'
# path2 = '/eos/user/m/mstamenk/CxAOD31run/hhh-6b/v26'

var = 'ProbMultiH'
cat = 'ProbHHH6b'
option = '_CR'
# btag_cut_strings = ['%s_3bh0h_inclusive%s']
btag_cut_strings = ['%s_2bh1h_inclusive%s','%s_1bh2h_inclusive%s','%s_0bh3h_inclusive%s','%s_3Higgs_inclusive%s','%s_2Higgs_inclusive%s','%s_1Higgs_inclusive%s','%s_0bh0h_inclusive%s']
# btag_cut_strings = ['%s_3Higgs_inclusive%s','%s_2Higgs_inclusive%s','%s_1Higgs_inclusive%s','%s_0bh0h_inclusive%s']
process_strings  = ["data_obs",'GluGluToHHTo4B_cHHH1','GluGluToHHTo2B2Tau_SM','GluGluToHHHTo4B2Tau_SM','GluGluToHHHTo6B_SM','QCD_datadriven']
# process_strings  = ["data_obs"]

# btag_cut_strings = ['%s_3Higgs_inclusive_']
for btag_cut in btag_cut_strings:
    btag_cut = btag_cut%(cat,option)
    
    output_folder3 = "{}/run2/{}".format(path,btag_cut)
    if not os.path.exists(output_folder3) :
        procs=subprocess.Popen(['mkdir %s' % output_folder3],shell=True,stdout=subprocess.PIPE)
        out = procs.stdout.read()
        print("made directory %s" % output_folder3)
    
    for pro in process_strings:

        os.system("hadd -f  %s/run2/%s/%s.root  %s/2016/%s/%s.root  %s/2016APV/%s/%s.root %s/2017/%s/%s.root %s/2018/%s/%s.root"%(path,btag_cut,pro,path,btag_cut,pro,path,btag_cut,pro,path,btag_cut,pro,path,btag_cut,pro)) 
        
    print("already finish %s"%(btag_cut))