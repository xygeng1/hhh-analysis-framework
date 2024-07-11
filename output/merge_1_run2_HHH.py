import subprocess
import os,sys
import ROOT

# process_strings = ["DYJetsToLL","GluGluToHHHTo4B2Tau_SM","GluGluToHHTo2B2Tau","GluGluToHHTo4B_cHHH1","TTToSemiLeptonic","WJetsToLNu_0J","WJetsToLNu_1J","WJetsToLNu_2J", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TTToHadronic","TTTo2L2Nu", "QCD", "data_obs" , "GluGluToHHHTo6B_SM"]

year = '2018'
path = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output'
# path2 = '/eos/user/m/mstamenk/CxAOD31run/hhh-6b/v26'

var = 'ProbMultiH'
cat = 'ProbMultiH'
option = '_CR'
# btag_cut_strings = ['%s_3bh0h_inclusive%s','%s_2bh1h_inclusive%s','%s_1bh2h_inclusive%s','%s_0bh3h_inclusive%s','%s_3Higgs_inclusive%s','%s_2Higgs_inclusive%s','%s_1Higgs_inclusive%s','%s_0bh0h_inclusive%s']
btag_cut_strings = ['%s_3bh0h_inclusive%s']

for btag_cut in btag_cut_strings:
    btag_cut = btag_cut%(cat,option)
    output_folder = "{}/Marko_20162018/{}/histograms".format(path,btag_cut)
    
    output_folder3 = "{}/Marko_20162018/{}".format(path,btag_cut)
    if not os.path.exists(output_folder3) :
        procs=subprocess.Popen(['mkdir %s' % output_folder3],shell=True,stdout=subprocess.PIPE)
        out = procs.stdout.read()
        print("made directory %s" % output_folder3)
    
    if not os.path.exists(output_folder) :
        procs=subprocess.Popen(['mkdir %s' % output_folder],shell=True,stdout=subprocess.PIPE)
        out = procs.stdout.read()
        print("made directory %s" % output_folder)

    os.system("hadd -f  {}/Marko_20162018/{}/histograms/histograms_ProbMultiH.root \
                        {}/Marko_20162018/2016/histograms/histograms_ProbMultiH.root \
                        {}/Marko_20162018/2016APV/histograms/histograms_ProbMultiH.root \
                        {}/Marko_20162018/2018/histograms/histograms_ProbMultiH.root \
                        ".format(path,btag_cut,path,btag_cut,path,btag_cut,path,btag_cut))
    