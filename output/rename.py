import ROOT

def rename_histogram(file_name, hist_name, new_hist_name):
    file = ROOT.TFile(file_name, "UPDATE")
    if not file or file.IsZombie():
        print("Error: Unable to open file", file_name)
        return
    hist_name_list=["%s_MUF_Up","%s_MUR_Up","%s_MUF_Down","%s_MUR_Down"]
    file_type_list=["GluGluToHHTo4B_cHHH1","GluGluToHHHTo6B_SM"]
    for hist_name in hist_name_list:
        for file_type in file_type_list:
            hist_name = hist_name%file_type
            hist = file.Get(hist_name)
            if not hist:
                print("Error: Unable to find histogram", hist_name, "in file", file_name)
                file.Close()
                return


            hist.SetName("%s_fourB_%s"%(file_type,hist_name))

            file.WriteTObject(hist, "", "Overwrite")

    # 关闭文件s
    file.Close()

if __name__ == "__main__":
    file_name = "Marko_sample/%s/histograms/histograms_ProbMultiH.root"
    cat_list  = ['ProbHHH6b_3bh0h_inclusive','ProbHHH6b_2bh1h_inclusive','ProbHHH6b_1bh2h_inclusive','ProbHHH6b_0bh3h_inclusive','ProbHHH6b_3Higgs_inclusive','ProbHHH6b_2Higgs_inclusive','ProbHHH6b_1Higgs_inclusive','ProbHHH6b_0bh0h_inclusive']

    for cat
    hist_name = "GluGluToHHTo4B_cHHH1_JER_Up"
    new_hist_name = "GluGluToHHTo4B_cHHH1_JER_4B_Up"

    rename_histogram(file_name, hist_name, new_hist_name)
