
import ROOT
import shutil
import sys, os, re, shlex
import shutil,subprocess
import time
import os.path
from os import path
import gc

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--base_folder ", type="string", dest="base", help="Folder in where to look for the categories", default='/eos/user/m/mstamenk/CxAOD31run/hhh-6b/v25/2017/baseline')
parser.add_option("--category ", type="string", dest="category", help="Category to compute it. if no argument is given will do all", default='none')
(options, args) = parser.parse_args()

base_folder=options.base
cat=options.category

if not cat == 'none' :
    categories = [cat]
else :
    categories = [
    "gt5bloose_0PFfat_",
    # "gt5bloose_gt0medium_0PFfat_",
    # "gt5bloose_gt1medium_0PFfat_",
    # "gt5bloose_gt2medium_0PFfat_",
    # "gt5bloose_gt3medium_0PFfat_",
    # "gt5bloose_gt4medium_0PFfat_",
    # "gt5bmedium_0PFfat_",

    
    ]
    # "1PFfat",
    # "gt1PFfat"

procstodo = ["ZZZ", "WZZ", "WWZ", "WWW", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TT", "QCD", "QCD6B", "GluGluToHHHTo6B_SM", "data_obs" ]

inputTree = 'Events'

# Chalange:
# 1 - have an option to compute the yield with processes grouped as on the plotting
# 2 - make the script already output the yields in table format for all categories
#     tip: instead of print the values as you compute them do a dataframe to be fimming collumns and print at the end, or even save in a csv file

for category in categories :
    print("Computing for category: %s" % category )
    for proc in procstodo :
        input_file="{}/{}/{}.root".format(base_folder,category,proc)

        #tfile = ROOT.TFile(input_file)

        #try :
        #    tree = tfile.Get(inputTree)
        #except :
        #    #print("The file %s is not correctly done" % input_file)
        #    continue

        try :
            #chunk_arr = tree2array(tree)
            chunk_df = ROOT.RDataFrame(inputTree, input_file)
        except :
            print("{}: Yield  = {} | #events = {}".format(proc, 0, 0))
            continue
        try :
            proc_yield = chunk_df.Sum('totalWeight')
        except :
            print("{}: Yield  = {} | #events = {}".format(proc, 0, 0))
            continue
        entries = chunk_df.Count()
        print("{}: Yield  = {} | #events = {}".format(proc, proc_yield.GetValue(), entries.GetValue()))


        #output_folder = "/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output/after_cut/%s"%(category)
        # print("made directory %s" % output_folder)
            
        # if not os.path.isdir(output_folder):
        #     os.makedirs(output_folder)
        # # tfile = ROOT.TFile(input_file,"read")
        # # tree = tfile.Get('Events')

        #df = ROOT.ROOT.RDataFrame('Events',input_file)
        # Yield_cut = 1
        df =ROOT.RDataFrame(inputTree, input_file)
        # events_cut = 1

        


        for CR_min in range(200,50,-10):

       

            selection = "h_fit_mass < %s"%(CR_min)
            print(CR_min)

            #df_new = df.Filter(selection, "Pass h_fit_mass cut")
            try :
                df_new = df.Filter(selection, "Pass h_fit_mass cut")
            except:
                print("error")
                continue
                
                

            try :
                proc_yield_cut = df_new.Sum('totalWeight')
            except :
                print("error")
                continue

            entries_cut = df_new.Count()
            Yield_cut = proc_yield_cut.GetValue() 
            events_cut = entries_cut.GetValue()
            print("{}: Yield_cut  = {} | #events_cut = {}".format(proc, proc_yield_cut.GetValue(), entries_cut.GetValue()))
            #print("the CR_min in {} is {}".format(proc, CR_min))
                #print("still not end in CR_min")
                #print("{}: Yield_cut  = {} | #events_cut = {}".format(proc, proc_yield_cut.GetValue(), entries_cut.GetValue()))


            
                
                
                





        #output_file = ROOT.TFile(output_folder + '/' + '%s.root'%(proc), 'recreate')
        #df_new.Snapshot('Events',output_folder + '/' + '%s.root'%(proc))
            

        # tree_cut = tree.CopyTree(selection)
        # print("Number of entries in tree_cut: ", tree_cut.GetEntries())
        # print("yield of entries in tree_cut: ", tree_cut.Sum('eventWeight'))
        

        
        # print("Writing in %s"%(output_folder + '/' + '%s.root'%(proc)))
        # #tree_cut.Write()
        # tfile.Close()
        # output_file.Close()


        # try :
        # #chunk_arr = tree2array(tree)
        #     #chunk_df_cut = ROOT.RDataFrame(inputTree, output_folder + '/' + '%s.root'%(proc))
        #     df_new = df.Filter(selection, "Pass h_fit_mass cut")
        # except :
        #     print("{}: Yield_cut  = {} | #events_cut = {}".format(proc, 0, 0))
        #     continue
        # try :
        #     #proc_yield_cut = chunk_df_cut.Sum('eventWeight')
        #     proc_yield_cut = df_new.Sum('eventWeight')
        # except :
        #     print("{}: Yield_cut  = {} | #events_cut = {}".format(proc, 0, 0))
        #     continue
        # #entries_cut = chunk_df_cut.Count()
        # entries_cut = df_new.Count()
        # print("{}: Yield_cut  = {} | #events_cut = {}".format(proc, proc_yield_cut.GetValue(), entries_cut.GetValue()))





