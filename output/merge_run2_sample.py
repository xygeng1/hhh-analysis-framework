import subprocess
import os,sys
import ROOT

# process_strings = ["DYJetsToLL","GluGluToHHHTo4B2Tau_SM","GluGluToHHTo2B2Tau","GluGluToHHTo4B_cHHH1","TTToSemiLeptonic","WJetsToLNu_0J","WJetsToLNu_1J","WJetsToLNu_2J", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TTToHadronic","TTTo2L2Nu", "QCD", "data_obs" , "GluGluToHHHTo6B_SM"]

year = 'run2'
path = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v32'
# path2 = '/eos/user/m/mstamenk/CxAOD31run/hhh-6b/v26'

var = 'ProbMultiH'
cat = 'ProbHH4b'
option = '_CR'
# btag_cut_strings = ['%s_3bh0h_inclusive%s','%s_2bh1h_inclusive%s','%s_1bh2h_inclusive%s','%s_0bh3h_inclusive%s','%s_3Higgs_inclusive%s','%s_2Higgs_inclusive%s','%s_1Higgs_inclusive%s','%s_0bh0h_inclusive%s']
btag_cut_strings = ['%s_3Higgs_inclusive%s','%s_2Higgs_inclusive%s','%s_1Higgs_inclusive%s','%s_0bh0h_inclusive%s']
process_strings  = ["data_obs",'GluGluToHHTo4B_cHHH0','GluGluToHHTo4B_cHHH1','GluGluToHHTo4B_cHHH5','GluGluToHHTo2B2Tau_SM','GluGluToHHHTo4B2Tau_SM','GluGluToHHHTo6B_SM','QCD_datadriven']

# btag_cut_strings = ['%s_3Higgs_inclusive_']
for btag_cut in btag_cut_strings:
    btag_cut = btag_cut%(cat,option)
    
    output_folder3 = "{}/run2/{}".format(path,btag_cut)
    if not os.path.exists(output_folder3) :
        procs=subprocess.Popen(['mkdir %s' % output_folder3],shell=True,stdout=subprocess.PIPE)
        out = procs.stdout.read()
        print("made directory %s" % output_folder3)
    
    for pro in process_strings:
        input_files = ["%s/2016/%s/%s.root","%s/2016APV/%s/%s.root","%s/2017/%s/%s.root","%s/2018/%s/%s.root"]
        output_file = "{}/run2/{}/{}.root".format(path,btag_cut,pro)

        chain = ROOT.TChain("Events")

        for file in input_files:
            file = file%(path,btag_cut,pro)
            chain.Add(file)

        output = ROOT.TFile(output_file, "RECREATE")

        chain.SetBranchStatus("*", 0)  
        chain.SetBranchStatus("ProbHHH", 1)  
        chain.SetBranchStatus("ProbMultiH", 1) 
        chain.SetBranchStatus("nprobejets", 1) 
        chain.SetBranchStatus("*flavTagWeight*", 1) 
        chain.SetBranchStatus("flavTagWeight_LHEScaleWeight*", 1) 
        chain.SetBranchStatus("l1PreFiringWeight*", 1) 
        chain.SetBranchStatus("puWeight*", 1) 
        chain.SetBranchStatus("PSWeight", 1) 
        chain.SetBranchStatus("LHEScaleWeight", 1) 
        chain.SetBranchStatus("LHEPdfWeight", 1) 
        chain.SetBranchStatus("totalWeight", 1) 
        chain.SetBranchStatus("fatJetFlavTagWeight*", 1) 
    
        new_tree = chain.CloneTree(-1, "fast")
        new_tree.Write()

        output.Close()
    print("alread finish {}/run2/{}".format(path,btag_cut))
