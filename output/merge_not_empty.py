import ROOT
import os

def is_non_empty_root_file(file_path):
    
    if not os.path.exists(file_path):
        return False

    file = ROOT.TFile(file_path)
    if file.IsZombie() or file.TestBit(ROOT.TFile.kRecovered):
        file.Close()
        return False

    keys = file.GetListOfKeys()
    file.Close()
    return len(keys) > 0

def get_non_empty_files(file_list):
    
    non_empty_files = [file for file in file_list if is_non_empty_root_file(file)]
    return non_empty_files
var = 'ProbMultiH'
cat = 'ProbHHH6b'
option = '_CR'
path = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/v33_new/sample_cut_slim'
btag_cut_strings = ['%s_2bh1h_inclusive%s','%s_1bh2h_inclusive%s','%s_0bh3h_inclusive%s','%s_3Higgs_inclusive%s','%s_2Higgs_inclusive%s','%s_1Higgs_inclusive%s','%s_0bh0h_inclusive%s']
process_strings  = ["data_obs",'GluGluToHHTo4B_cHHH1','GluGluToHHTo2B2Tau_SM','GluGluToHHHTo4B2Tau_SM','GluGluToHHHTo6B_SM','QCD_datadriven']
for btag_cut in btag_cut_strings:
    btag_cut = btag_cut%(cat,option)
    
    output_folder3 = "{}/run2/{}".format(path,btag_cut)
    if not os.path.exists(output_folder3) :
        procs=subprocess.Popen(['mkdir %s' % output_folder3],shell=True,stdout=subprocess.PIPE)
        out = procs.stdout.read()
        print("made directory %s" % output_folder3)
    
    for pro in process_strings:
        input_files = [
            "%s/2016/%s/%s.root" % (path, btag_cut, pro),
            "%s/2016APV/%s/%s.root" % (path, btag_cut, pro),
            "%s/2017/%s/%s.root" % (path, btag_cut, pro),
            "%s/2018/%s/%s.root" % (path, btag_cut, pro)
        ]

        non_empty_files = get_non_empty_files(input_files)
        print(input_files)

        if non_empty_files:
            output_file =  "%s/run2/%s/%s.root"%(path,btag_cut,pro)
            hadd_command = "hadd -f {} {}".format(output_file, " ".join(non_empty_files))
            os.system(hadd_command)
            print(f"Successfully merged into {output_file}")
        else:
            print("No non-empty ROOT files found to merge.")
