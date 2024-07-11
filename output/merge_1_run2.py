import subprocess
import os,sys
import ROOT

# process_strings = ["DYJetsToLL","GluGluToHHHTo4B2Tau_SM","GluGluToHHTo2B2Tau","GluGluToHHTo4B_cHHH1","TTToSemiLeptonic","WJetsToLNu_0J","WJetsToLNu_1J","WJetsToLNu_2J", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TTToHadronic","TTTo2L2Nu", "QCD", "data_obs" , "GluGluToHHHTo6B_SM"]

year = '2018'
path = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33_new/sample_cut'
# path2 = '/eos/user/m/mstamenk/CxAOD31run/hhh-6b/v26'

var = 'ProbMultiH'
cat = 'ProbHHH6b'
option = '_CR'
btag_cut_strings = ['%s_2bh0h_inclusive%s','%s_1bh1h_inclusive%s','%s_0bh2h_inclusive%s','%s_3bh0h_inclusive%s','%s_2bh1h_inclusive%s','%s_1bh2h_inclusive%s','%s_0bh3h_inclusive%s','%s_3Higgs_inclusive%s','%s_2Higgs_inclusive%s','%s_1Higgs_inclusive%s','%s_0bh0h_inclusive%s']
# btag_cut_strings = ['%s_3Higgs_inclusive_']

for btag_cut in btag_cut_strings:
    btag_cut = btag_cut%(cat,option)
    output_folder = "{}/run2/{}/histograms".format(path,btag_cut)
    
    output_folder3 = "{}/run2/{}".format(path,btag_cut)
    if not os.path.exists(output_folder3) :
        procs=subprocess.Popen(['mkdir %s' % output_folder3],shell=True,stdout=subprocess.PIPE)
        out = procs.stdout.read()
        print("made directory %s" % output_folder3)
    
    if not os.path.exists(output_folder) :
        procs=subprocess.Popen(['mkdir %s' % output_folder],shell=True,stdout=subprocess.PIPE)
        out = procs.stdout.read()
        print("made directory %s" % output_folder)

    os.system("hadd -f  {}/run2/{}/histograms/histograms_{}.root \
                        {}/2016/{}/histograms/histograms_{}.root \
                        {}/2016APV/{}/histograms/histograms_{}.root \
                        {}/2017/{}/histograms/histograms_{}.root \
                        {}/2018/{}/histograms/histograms_{}.root \
                        ".format(path,btag_cut,var,path,btag_cut,var,path,btag_cut,var,path,btag_cut,var,path,btag_cut,var))
    