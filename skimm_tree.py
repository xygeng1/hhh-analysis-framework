#from utils import wps_years
import ROOT
import shutil
import sys, os, re, shlex
#from subprocess import Popen, PIPE
#ROOT.ROOT.EnableImplicitMT()
#os.environ["MKL_NUM_THREADS"] = "1"
#os.environ["OMP_NUM_THREADS"] = "1"
import shutil,subprocess
import time
import os.path
from os import path
#from root_numpy import tree2array, array2tree
#import numpy as np
#import pandas
import glob
import gc

#import tdrstyle,CMS_lumi

ROOT.gROOT.SetBatch(ROOT.kTRUE)

from utils import histograms_dict, wps_years, wps, tags, luminosities, hlt_paths, triggersCorrections, add_bdt, bdts_xml, hist_properties, init_mhhh, addMHHH, clean_variables

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--base_folder ", type="string", dest="base", help="Folder in where to look for the categories", default='/eos/user/m/mstamenk/CxAOD31run/hhh-6b/v25/2017/baseline_recomputedSF/')
parser.add_option("--category ", type="string", dest="category", help="Category to compute it. if no argument is given will do all", default='none')
parser.add_option("--skip_do_trees", action="store_true", dest="skip_do_trees", help="Write...", default=False)
parser.add_option("--skip_do_histograms", action="store_true", dest="skip_do_histograms", help="Write...", default=False)
parser.add_option("--skip_do_plots", action="store_true", dest="skip_do_plots", help="Write...", default=False)
parser.add_option("--do_SR", action="store_true", dest="do_SR", help="Write...", default=False)
parser.add_option("--do_CR", action="store_true", dest="do_CR", help="Write...", default=False)
parser.add_option("--process ", type="string", dest="process_to_compute", help="Process to compute it. if no argument is given will do all", default='none')
parser.add_option("--do_limit_tree ", type="string", dest="do_limit_tree", help="If given it will do the histograms only in that variable with all the uncertainties", default='none')
## separate SR_CR as an option, this option would add _SR and _CR to the subfolder name
## add option to enter a process and if that is given to make the trees and histos only to it
## add option to add BDT computation here -- or not, we leave this only to MVA input variables -- the prefit plots already do data/MC
(options, args) = parser.parse_args()

do_limit_tree      = options.do_limit_tree ## X: to implement
process_to_compute = options.process_to_compute
do_SR              = options.do_SR
do_CR              = options.do_CR
skip_do_trees      = options.skip_do_trees
skip_do_histograms = options.skip_do_histograms
skip_do_plots      = options.skip_do_plots
input_tree         = options.base
cat                = options.category

if do_SR and do_CR :
    print("You should chose to signal region OR control region")
    exit()

selections = {
    #"final_selection_jetMultiplicity" : "(nbtags > 4 && nfatjets == 0) || (nbtags > 2 && nfatjets > 0)",
    "gt5bloose_test"                : {
        "sel" : "(Nloosebtags > 5 )",
        "label" : "6L"
        },
    "gt5bloose_0PFfat"              : {
        "sel" : "(Nloosebtags > 5 && nprobejets == 0)",
        "label" : "Resolved 6L"
        },
    "gt5bloose_gt0medium_0PFfat"    : {
        "sel" : "(Nloosebtags > 5 && Nmediumbtags >0 && nprobejets == 0)",
        "label" : "Resolved 1M 5L"
        },
    "gt5bloose_gt1medium_0PFfat"    : {
        "sel" : "(Nloosebtags > 5 && Nmediumbtags >1 && nprobejets == 0)",
        "label" : "Resolved 2M 4L"
        },
    "gt5bloose_gt2medium_0PFfat"    : {
        "sel" : "(Nloosebtags > 5 && Nmediumbtags >2 && nprobejets == 0)",
        "label" : "Resolved 3M 3L"
        },
    "gt5bloose_gt3medium_0PFfat"    : {
        "sel" : "(Nloosebtags > 5 && Nmediumbtags >3 && nprobejets == 0)",
        "label" : "Resolved 4M 2L"
        },
    "gt5bloose_gt4medium_0PFfat"    : {
        "sel" : "(Nloosebtags > 5 && Nmediumbtags >4 && nprobejets == 0)",
        "label" : "Resolved 5M 1L"
        },
    "gt5bmedium_0PFfat"             : {
        "sel" : "(Nmediumbtags > 5 && nprobejets == 0)",
        "label" : "Resolved 6M"
        },
    "1PFfat"                        : {
        "sel" : "(nprobejets == 1)",
        "label" : "Boosted (1 PN fat jet)"
        },
    "gt1PFfat"                      : {
        "sel" : "(nprobejets > 1)",
        "label" : "Boosted (> 1 PN fat jet)"
        },
    "gt0PFfat"                      : {
        "sel" : "(nprobejets > 1)",
        "label" : "Boosted (> 0 PN fat jet)"
        },
    ## you can add here categories with PN score
}

additional_selection = ""
additional_label     = ""
if do_SR :
    additional_selection = " && (h_fit_mass > 80 && h_fit_mass < 150)"
    additional_label     = "SR"
if do_CR :
    additional_selection = " && !(h_fit_mass > 80 && h_fit_mass < 150)"
    additional_label     = "CR"

# define function to run on mHHH
init_mhhh()

inputTree = 'Events'

procstodo = ["ZZZ", "WZZ", "WWZ", "WWW", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TT", "QCD", "QCD6B", "data_obs" , "GluGluToHHHTo6B_SM"]
if not process_to_compute == 'none' :
    procstodo     = [process_to_compute]
    skip_do_plots = True

for era in [2016, 2017, 2018] :
    if str(era) in input_tree : year = str(era)

wp_loose = wps_years['loose'][year]
wp_medium = wps_years['medium'][year]
wp_tight = wps_years['tight'][year]

csv_saved = False
for selection in selections.keys() :
  if not cat == 'none' :
      if not selection == cat :
          continue

  final_selection = selections[selection]["sel"]
  if not additional_selection == "" :
      final_selection = "(%s %s)" % (selections[selection]["sel"], additional_selection)

  print("Doing tree skimmed for %s_%s" % (selection, additional_label))
  print(final_selection)
  output_folder = "{}/{}_{}".format(input_tree,selection,additional_label)
  if not path.exists(output_folder) :
      procs=subprocess.Popen(['mkdir %s' % output_folder],shell=True,stdout=subprocess.PIPE)
      out = procs.stdout.read()
      print("made directory %s" % output_folder)

  if not skip_do_trees :
   for proctodo in procstodo :

    ## do that in a utils function
    datahist = proctodo
    if proctodo == "data_obs" :
        if year == '2018' :
            datahist = 'JetHT'
        else:
            datahist = 'BTagCSV'

    outtree = "{}/{}_{}/{}.root".format(input_tree,selection,additional_label,proctodo)

    list_proc=glob.glob("{}/inclusive/{}.root".format(input_tree,datahist))
    print("Will create %s" % outtree)

    for proc in list_proc :
        #if not csv_saved :
        tlocal = time.localtime()
        current_time = time.strftime("%H:%M:%S", tlocal)
        print(current_time)
        seconds0 = time.time()
        print(proc)
        print("Cutting tree and saving it to ", outtree)
        print("With selection: ", final_selection)

        chunk_df = ROOT.RDataFrame(inputTree, proc)

        # add mHHH variable
        chunk_df = addMHHH(chunk_df)

        entries_no_filter = int(chunk_df.Count().GetValue())

        print("Redefine btag counting ")
        count_loose=[]
        count_medium=[]
        count_tight=[]
        for jet in range(1,11) :
             count_loose.append('int(jet%sDeepFlavB > %f)'%(jet,wp_loose))
             count_medium.append('int(jet%sDeepFlavB > %f)'%(jet,wp_medium))
             count_tight.append('int(jet%sDeepFlavB > %f)'%(jet,wp_tight))

        nloose = '+'.join(count_loose)
        nmedium = '+'.join(count_medium)
        ntight = '+'.join(count_tight)

        chunk_df = chunk_df.Define('Nloosebtags',nloose)
        chunk_df = chunk_df.Define('Nmediumbtags',nmedium)
        chunk_df = chunk_df.Define('Ntightbtags',ntight)

        chunk_df = chunk_df.Filter(final_selection)
        entries = int(chunk_df.Count().GetValue())

        #print("cut made, tree size: ", int(tree.GetEntries()), int(tree_cut.GetEntries()))
        print("cut made, tree size: ", entries_no_filter, entries)
        print("starting to construct calibrations")
        variables = list(chunk_df.GetColumnNames())

        print("Cleaning variables", len(variables))
        variables = clean_variables(variables)
        ## if to do limit the cleaning will be different
        print("Cleaned variables", len(variables))
        print(variables)
        ## cleaning is not working for all variables, even if explicitelly asking to remove all that name, and for some not cleaned variables will given
        ## Error in <TBranch::TBranch>: Illegal leaf: LHEReweightingWeight/LHEReweightingWeight[nLHEReweightingWeight]/F. If this is a variable size C array it's possible that the branch holding the size is not available
        ## Maybe because I do not source CMSSW

        ## symetrize angle variables
        for type_obj in ['bcand', 'fatJet', 'jet'] :
            for jet_number in range(1,11) :
                for angle in ['Eta', 'Phi'] :
                    obj = '{}{}{}'.format(type_obj,jet_number,angle)
                    if obj in variables :
                        #print("Take absolute of %s" % obj)
                        chunk_df = chunk_df.Redefine(obj, "abs(%s)" % obj)
                chunk_df = chunk_df.Redefine('hhh_eta', "abs(hhh_eta)")
                #chunk_df = chunk_df.Redefine('hh_phi', "abs(hh_phi)")

        print("2 - construct the eventWeight")
        to_multiply = []
        do_SF = True

        if selection == "gt5bloose_test" or selection == "gt5bloose_0PFfat" :
            nmedium_cut = 0
        elif selection == "gt5bloose_gt0medium_0PFfat" :
            nmedium_cut = 1
        elif selection == "gt5bloose_gt1medium_0PFfat" :
            nmedium_cut = 2
        elif selection == "gt5bloose_gt2medium_0PFfat" :
            nmedium_cut = 3
        elif selection == "gt5bloose_gt3medium_0PFfat" :
            nmedium_cut = 4
        elif selection == "gt5bloose_gt4medium_0PFfat" :
            nmedium_cut = 5
        elif selection == "gt5bmedium_0PFfat" :
            nmedium_cut = 6
        else :
            print("no SF ready to selection %s , we are ignoring it by the moment" % selection)
            do_SF = False

        if do_SF :
            for jet_number in range(1,nmedium_cut+1) :
                to_multiply = to_multiply + ['jet{}MediumBTagEffSF'.format(jet_number)]
            for jet_number in range(nmedium_cut+1,7) :
                to_multiply = to_multiply + ['jet{}LooseBTagEffSF'.format(jet_number)]
        string_multiply = 'eventWeight'
        for ss in to_multiply :
            string_multiply = string_multiply + ' * {}'.format(ss)

        print( "Redefine eventWeight = {}".format(string_multiply))
        chunk_df = chunk_df.Define('totalWeight', string_multiply)

        proc_yield = chunk_df.Sum('totalWeight')
        print("Yield:", proc_yield.GetValue())

        chunk_df.Snapshot(inputTree, outtree, variables + ['totalWeight'])

        gc.collect() # clean menory
        sys.stdout.flush() # extra clean

        seconds = time.time()
        print("Seconds to load : ", seconds-seconds0)
        print("Minutes to load : ", (seconds-seconds0)/60.0)

  ## do Histograms -- reorganize to do directly limits
  output_histos = "{}/{}_{}/histograms".format(input_tree,selection,additional_label)
  if not path.exists(output_histos) :
    procs=subprocess.Popen(['mkdir %s' % output_histos],shell=True,stdout=subprocess.PIPE)
    out = procs.stdout.read()

  if not skip_do_histograms : # args.doHistograms:
   for proctodo in procstodo :
    datahist = proctodo
    if proctodo == "data_obs" :
        if year == '2018' :
            datahist = 'JetHT'
        else:
            datahist = 'BTagCSV'


    outtree = "{}/{}_{}/{}.root".format(input_tree,selection,additional_label,proctodo) ## make better, to not have to call it twice

    chunk_df = ROOT.RDataFrame(inputTree, outtree)
    seconds0 = time.time()
    # Define histograms to be produced
    print(output_histos)
    f_out = ROOT.TFile(output_histos + '/' + 'histograms_%s.root'%(proctodo), 'recreate')
    print("Writing in %s"%(output_histos + '/' + 'histograms_%s.root'%(proctodo)))

    histograms = []
    variables = chunk_df.GetColumnNames()
    if not len(variables) > 0 :
        print("process %s has 0 entries, skipping doing the histogram" % proctodo)
        continue
    print("Will produce histograms for following variables:")
    print(variables)

    # Rdataframes require first histogram to be produced and then the rest is nested in the loop of the first one
    bins = histograms_dict['h_fit_mass']["nbins"]
    xmin = histograms_dict['h_fit_mass']["xmin"]
    xmax = histograms_dict['h_fit_mass']["xmax"]

    print(bins,xmin,xmax)
    h = chunk_df.Histo1D(("h_fit_mass","h_fit_mass",bins,xmin,xmax),"h_fit_mass", "totalWeight") # booking the rdataframe loop

    # TH1DModel::TH1DModel(const char* name, const char* title, int nbinsx, double xlow, double xup)
    h.SetTitle('h_fit_mass')
    h.SetName('h_fit_mass')

    histograms.append(h)
    for var in variables: # booking all variables to be produced
        if "Resolved" in selections[selection]["label"] and "fatJet" in var :
            continue
        try :
            histograms_dict[var]
        except :
            print("Skip doing histogram to %s, if you want to draw add the binning option in utils" % var)
            continue
        bins = histograms_dict[var]["nbins"]
        xmin = histograms_dict[var]["xmin"]
        xmax = histograms_dict[var]["xmax"]
        char_var = var.c_str()
        print(var,char_var,bins,xmin,xmax)
        h_tmp = chunk_df.Histo1D((char_var,char_var,bins,xmin,xmax),var, "totalWeight")
        h_tmp.SetTitle('%s'%(var))
        h_tmp.SetName('%s'%(var))
        if datahist == "GluGluToHHHTo6B_SM" :
            h_tmp.Scale(10)
        histograms.append(h_tmp)
    h.Draw() # run one loop for all variables

    # writing output histograms
    f_out.cd()
    for h in histograms:
        h.Write()
    f_out.Close()
    seconds = time.time()
    print("Seconds to load : ", seconds-seconds0)
    print("Minutes to load : ", (seconds-seconds0)/60.0)

  if not skip_do_plots :
      # Draw the data/MC to this selection
      command = "python3 draw_data_mc_categories.py --input_folder %s --plot_label '%s (%s)'" % (output_histos, selections[selection]["label"], additional_label)
      #if "0PFfat" in selection :
      #command = command + " --log"
      print(command)

      proc=subprocess.Popen([command],shell=True,stdout=subprocess.PIPE)
      out = proc.stdout.read()
