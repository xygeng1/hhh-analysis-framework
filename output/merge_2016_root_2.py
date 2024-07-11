import subprocess
import os,sys
import ROOT


btag_cut_strings = ['%s_2Higgs_inclusive%s','%s_1Higgs_inclusive%s','%s_0bh0h_inclusive%s']
# btag_cut_strings = ['%s_2Higgs_inclusive%s','%s_1Higgs_inclusive%s','%s_0bh0h_inclusive%s']
process_list = ['GluGluToHHHTo4B2Tau_SMJERDOWN','GluGluToHHHTo4B2Tau_SMJERUP','GluGluToHHHTo4B2Tau_SMJESDOWN','GluGluToHHHTo4B2Tau_SMJESUP','GluGluToHHHTo4B2Tau_SMJMRDOWN','GluGluToHHHTo4B2Tau_SMJMRUP','GluGluToHHHTo6B_SMJERDOWN','GluGluToHHHTo6B_SMJERUP','GluGluToHHHTo6B_SMJESDOWN','GluGluToHHHTo6B_SMJESUP','GluGluToHHHTo6B_SMJMRDOWN','GluGluToHHHTo6B_SMJMRUP','GluGluToHHTo2B2Tau_SMJERDOWN','GluGluToHHTo2B2Tau_SMJERUP','GluGluToHHTo2B2Tau_SMJESDOWN','GluGluToHHTo2B2Tau_SMJESUP','GluGluToHHTo2B2Tau_SMJMRDOWN','GluGluToHHTo2B2Tau_SMJMRUP','GluGluToHHTo4B_cHHH1JERDOWN','GluGluToHHTo4B_cHHH1JERUP','GluGluToHHTo4B_cHHH1JESDOWN','GluGluToHHTo4B_cHHH1JESUP','GluGluToHHTo4B_cHHH1JMRDOWN','GluGluToHHTo4B_cHHH1JMRUP',"GluGluToHHTo4B_cHHH1","data_obs","GluGluToHHHTo6B_SM","GluGluToHHHTo4B2Tau_SM","GluGluToHHTo2B2Tau_SM","QCD_datadriven"]
# process_list = ["HHHTo6B_c3_0_d4_99","HHHTo6B_c3_0_d4_minus1","HHHTo6B_c3_19_d4_19","HHHTo6B_c3_1_d4_0","HHHTo6B_c3_1_d4_2","HHHTo6B_c3_2_d4_minus1","HHHTo6B_c3_4_d4_9","HHHTo6B_c3_minus1_d4_0","HHHTo6B_c3_minus1_d4_minus1","HHHTo6B_c3_minus1p5_d4_minus0p5"]
# btag_cut_strings = ['%s_3Higgs_inclusive_']

path = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33_new'


cat = 'ProbHHH6b'
option = '_CR'
for btag_cut in btag_cut_strings:
        btag_cut = btag_cut%(cat,option)
        output_folder = "{}/2016_all/{}/histograms".format(path,btag_cut)

        output_folder1 = "{}/2016_all/".format(path)
        if not os.path.exists(output_folder1) :
            procs=subprocess.Popen(['mkdir %s' % output_folder1],shell=True,stdout=subprocess.PIPE)
            out = procs.stdout.read()
            print("made directory %s" % output_folder1)
            
        output_folder2 = "{}/2016_all/{}/".format(path,btag_cut)
        if not os.path.exists(output_folder2) :
            procs=subprocess.Popen(['mkdir %s' % output_folder2],shell=True,stdout=subprocess.PIPE)
            out = procs.stdout.read()
            print("made directory %s" % output_folder2)

        
        if not os.path.exists(output_folder) :
            procs=subprocess.Popen(['mkdir %s' % output_folder],shell=True,stdout=subprocess.PIPE)
            out = procs.stdout.read()
            print("made directory %s" % output_folder)
        for process in process_list:
            os.system("hadd -f  %s/2016_all/%s/%s.root  %s/2016/%s/%s.root  %s/2016APV/%s/%s.root"%(path,btag_cut,process,path,btag_cut,process,path,btag_cut,process)) 


