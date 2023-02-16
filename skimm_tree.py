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

from utils import labels, wps_years, binnings, cuts, wps, tags, luminosities, hlt_paths, triggersCorrections, add_bdt, bdts_xml, hist_properties

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--base_folder ", type="string", dest="base", help="Folder in where to look for the categories", default='/eos/user/m/mstamenk/CxAOD31run/hhh-6b/v25/2017/baseline_recomputedSF/')
parser.add_option("--category ", type="string", dest="category", help="Category to compute it. if no argument is given will do all", default='none')
## separate SR_CR
## skip do trees
## add option to add BDT computation here -- or not, we leave this only to MVA input variables -- the prefit plots already do data/MC
(options, args) = parser.parse_args()

skip_do_trees      = True
skip_do_histograms = False
input_tree         = options.base
cat                = options.category

selections = {
    #"final_selection_jetMultiplicity" : "(nbtags > 4 && nfatjets == 0) || (nbtags > 2 && nfatjets > 0)",
    "gt5bloose_test"                : "(Nloosebtags > 5 )",
    "gt5bloose_0PFfat"              : "(Nloosebtags > 5 && nprobejets == 0)",
    "gt5bloose_gt0medium_0PFfat"    : "(Nloosebtags > 5 && Nmediumbtags >0 && nprobejets == 0)",
    "gt5bloose_gt1medium_0PFfat"    : "(Nloosebtags > 5 && Nmediumbtags >1 && nprobejets == 0)",
    "gt5bloose_gt2medium_0PFfat"    : "(Nloosebtags > 5 && Nmediumbtags >2 && nprobejets == 0)",
    "gt5bloose_gt3medium_0PFfat"    : "(Nloosebtags > 5 && Nmediumbtags >3 && nprobejets == 0)", # need to redo signal / da
    "gt5bloose_gt4medium_0PFfat"    : "(Nloosebtags > 5 && Nmediumbtags >4 && nprobejets == 0)",
    "gt5bmedium_0PFfat"             : "(Nmediumbtags > 5 && nprobejets == 0)",
    "1PFfat"                        : "(nprobejets == 1)",
    "gt1PFfat"                      : "(nprobejets > 1)",
}

inputTree = 'Events'

procstodo = ["ZZZ", "WZZ", "WWZ", "WWW", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TT", "QCD", "QCD6B", "data_obs" , "GluGluToHHHTo6B_SM"]
#procstodo = [  "data_obs" ]
#procstodo = [ "WWZ" ]



for era in [2016, 2017, 2018] :
    if str(era) in input_tree : year = str(2017)

wp_loose = wps_years['loose'][year]
wp_medium = wps_years['medium'][year]
wp_tight = wps_years['tight'][year]

csv_saved = False
for selection in selections.keys() :
  if not cat == 'none' :
      if not selection == cat :
          continue
  print("Doing tree skimmed for %s" % selection)
  print(selections[selection])
  output_folder = "{}/{}".format(input_tree,selection)
  if not path.exists(output_folder) :
      procs=subprocess.Popen(['mkdir %s' % output_folder],shell=True,stdout=subprocess.PIPE)
      out = procs.stdout.read()
      print("made directory %s" % output_folder)

  if not skip_do_trees :
   for proctodo in procstodo :

    if proctodo == "data_obs" :
        if not year == '2018' :
            datahist = 'BTagCSV'
        else:
            datahist = 'JetHT'
    else :
        datahist = proctodo

    outtree = "{}/{}/{}.root".format(input_tree,selection,proctodo)



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
        print("With selection: ", selections[selection])

        chunk_df = ROOT.RDataFrame(inputTree, proc)

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

        chunk_df = chunk_df.Filter(selections[selection])
        entries = int(chunk_df.Count().GetValue())

        #print("cut made, tree size: ", int(tree.GetEntries()), int(tree_cut.GetEntries()))
        print("cut made, tree size: ", entries_no_filter, entries)
        print("starting to construct calibrations")
        variables = list(chunk_df.GetColumnNames())


        print("Cleaning variables", len(variables))

        for testing in ["HLT", "LHE", "v_", "L1_", "l1PreFiringWeight", "trigger", "vbf", "lep",  "pu", "_Up", "_Down", 'passmetfilters', 'PSWeight', "boostedTau", "boostedTau_"] :
            for var in variables :
                if str(var).find(testing) != -1:
                    variables.remove(var)

        # remove variables based on 6 first btags to not confuse
        for var in ['nloosebtags', 'nmediumbtags', 'ntightbtags'] :
            variables.remove(var)

        for var in [ 'LHEScaleWeightNormNew', 'fatJet3PtOverMHH_JMS_Down', 'fatJet3PtOverMHH_MassRegressed_JMS_Down', 'genHiggs1Eta', 'genHiggs1Phi', 'genHiggs1Pt', 'genHiggs2Eta', 'genHiggs2Phi', 'genHiggs2Pt', 'genHiggs3Eta', 'genHiggs3Phi', 'genHiggs3Pt', 'genTtbarId', 'genWeight', "xsecWeight", "nfatjets", 'l1PreFiringWeightDown', 'lep1Id', 'lep1Pt', 'lep2Id', 'lep2Pt', "eventWeightBTagSF", "eventWeightBTagCorrected", "weight", "PV_npvs", "boostedTau_phi", "boostedTau_rawAntiEleCat2018", "boostedTau_eta", "boostedTau_idMVAoldDM2017v2", "boostedTau_leadTkDeltaPhi", "boostedTau_rawMVAoldDM2017v2", 'boostedTau_rawIsodR03', 'HLT_AK8PFHT800_TrimMass50', 'HLT_AK8PFHT900_TrimMass50', 'HLT_AK8PFJet200', 'HLT_AK8PFJet320', 'HLT_AK8PFJet330_PFAK8BTagCSV_p17', 'HLT_AK8PFJet380_TrimMass30', 'HLT_AK8PFJet400', 'HLT_AK8PFJet420_TrimMass30', 'HLT_AK8PFJet500', 'HLT_AK8PFJet60', 'HLT_AK8PFJetFwd140', 'HLT_AK8PFJetFwd260', 'HLT_AK8PFJetFwd40', 'HLT_AK8PFJetFwd450', 'HLT_AK8PFJetFwd60', 'HLT_Ele27_WPTight_Gsf', 'HLT_HT300PT30_QuadJet_75_60_45_40', 'HLT_PFHT380_SixPFJet32', 'HLT_PFHT380_SixPFJet32_DoublePFBTagDeepCSV_2p2', 'HLT_PFHT430_SixJet40_BTagCSV_p080', 'HLT_PFMET120_PFMHT120_IDTight_PFHT60', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_HFCleaned', 'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight', 'HLT_PFMETTypeOne100_PFMHT100_IDTight_PFHT60', 'HLT_PFMETTypeOne120_PFMHT120_IDTight', 'HLT_Ele32_WPTight_Gsf_L1DoubleEG', 'HLT_Ele38_WPTight_Gsf', 'HLT_IsoMu20', 'HLT_IsoMu24_eta2p1', 'HLT_IsoMu30', 'HLT_Mu55', 'HLT_PFHT180', 'HLT_PFHT300PT30_QuadPFJet_75_60_45_40', 'HLT_PFHT350', 'HLT_PFHT370', 'HLT_PFHT380_SixPFJet32_DoublePFBTagCSV_2p2', 'HLT_PFHT430', 'HLT_PFHT430_SixPFJet40_PFBTagCSV_1p5', 'HLT_PFHT500_PFMET110_PFMHT110_IDTight', 'HLT_PFHT590', 'HLT_PFHT700_PFMET85_PFMHT85_IDTight', 'HLT_PFHT780', 'HLT_PFHT800_PFMET85_PFMHT85_IDTight', 'HLT_PFJet140', 'HLT_PFJet260', 'HLT_PFJet40', 'HLT_PFJet450', 'HLT_PFJet550', 'HLT_PFJet80', 'HLT_PFJetFwd200', 'HLT_PFJetFwd320', 'HLT_PFJetFwd400', 'HLT_PFJetFwd500', 'HLT_PFJetFwd80', 'HLT_PFMET100_PFMHT100_IDTight_PFHT60', 'HLT_PFMET110_PFMHT110_IDTight_CaloBTagCSV_3p1', 'HLT_PFMET120_PFMHT120_IDTight_CaloBTagCSV_3p1', 'HLT_PFMET130_PFMHT130_IDTight', 'HLT_PFMET140_PFMHT140_IDTight', 'HLT_PFMET200_HBHECleaned', 'HLT_PFMET200_NotCleaned', 'HLT_PFMET300_HBHECleaned', 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight', 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60', 'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight', 'HLT_PFMETTypeOne110_PFMHT110_IDTight', 'HLT_PFMETTypeOne120_PFMHT120_IDTight_PFHT60', 'HLT_PFMETTypeOne140_PFMHT140_IDTight', 'HLT_Photon175', 'HLT_QuadPFJet103_88_75_15_BTagCSV_p013_VBF2', 'HLT_QuadPFJet105_88_76_15', 'HLT_QuadPFJet105_90_76_15_DoubleBTagCSV_p013_p08_VBF1', 'HLT_QuadPFJet111_90_80_15_BTagCSV_p013_VBF2', 'HLT_QuadPFJet98_83_71_15', 'HLT_QuadPFJet98_83_71_15_DoubleBTagCSV_p013_p08_VBF1', 'L1_HTT280er_QuadJet_70_55_40_35_er2p5', 'L1_HTT320er_QuadJet_70_55_40_40_er2p4', 'L1_HTT320er_QuadJet_70_55_45_45_er2p5', 'L1_HTT450er', 'nfatjets', 'ptj2_over_ptj1', 'ptj3_over_ptj1', 'ptj3_over_ptj2', 'rho', 'LHE_Vpt', 'fatJet2PtOverMHH_JMS_Down', 'fatJet2PtOverMHH_MassRegressed_JMS_Down', 'mva', 'nLHEReweightingWeight', 'nbtags',  'puWeightDown', 'triggerEffMC3DWeight', 'triggerEffWeight', 'l1PreFiringWeightDown', 'lep1Id', 'lep1Pt', 'lep2Id', 'lep2Pt', 'v_1', 'v_11', 'v_13', 'v_15', 'v_17', 'v_19', 'v_20', 'v_22', 'v_24', 'v_26', 'v_28', 'v_3', 'v_31', 'v_33', 'v_35', 'v_37', 'v_39', 'v_40', 'v_42', 'v_44', 'v_46', 'v_48', 'v_5', 'v_51', 'v_53', 'v_55', 'v_57', 'v_59', 'v_60', 'v_7', 'v_9', 'vbffatJet1PNetXbb', 'vbffatJet1Pt', 'vbffatJet2PNetXbb', 'vbffatJet2Pt', 'vbfjet1Mass', 'vbfjet1Pt', 'vbfjet2Mass', 'vbfjet2Pt', 'boostedTau_pt', 'boostedTau_idAntiMu', 'boostedTau_jetIdx', 'boostedTau_mass', 'h1h2_mass_squared', 'h2h3_mass_squared', 'deltaEta_j1j3', 'deltaPhi_j1j3', 'deltaR_j1j3', 'mj3_over_mj1', 'mj3_over_mj1_MassRegressed', 'deltaEta_j2j3', 'deltaPhi_j2j3', 'deltaR_j2j3', 'mj3_over_mj2', 'mj3_over_mj2_MassRegressed', 'isVBFtag', 'dijetmass', 'nsmalljets',  'jet7BTagSF', 'jet8BTagSF', 'jet9BTagSF', 'jet10BTagSF', 'ratioPerEvent', "LHEPdfWeightNorm", "LHEScaleWeight", 'hh_eta_JMS_Down', 'hh_eta_MassRegressed_JMS_Down', 'hh_mass_JMS_Down', 'hh_mass_MassRegressed_JMS_Down', 'hh_pt_JMS_Down', 'hh_pt_MassRegressed', 'hh_pt_MassRegressed_JMS_Down',  'hhh_eta_JMS_Down', 'hhh_eta_MassRegressed_JMS_Down', 'hhh_mass_JMS_Down', 'hhh_mass_MassRegressed_JMS_Down', 'fatJet1PtOverMHH_JMS_Down', 'fatJet1PtOverMHH_MassRegressed_JMS_Down',  'eventWeight', 'hhh_pt_JMS_Down', 'hhh_pt_MassRegressed', 'hhh_pt_MassRegressed_JMS_Down', 'mj2_over_mj1', 'mj2_over_mj1_MassRegressed'] :
            try :
                variables.remove(var)
            except:
                1 == 1

        for hhhvar in [ 'eta_MassRegressed', 'phi_MassRegressed', 'mass_MassRegressed'] :
            variables.remove('hhh_{}'.format(hhhvar))
            variables.remove('hh_{}'.format(hhhvar))

        for jet_number in range(1,11) :
            for jetvar in ['DeepFlavB', 'HiggsMatched', 'HasMuon', 'HasElectron', 'FatJetMatched', 'HiggsMatchedIndex', 'MatchedGenPt', 'JetId', 'PuId', 'HadronFlavour', 'FatJetMatchedIndex', 'RawFactor', 'LooseBTagEffSF', 'MediumBTagEffSF', 'TightBTagEffSF'] :
                try :
                    variables.remove('jet{}{}'.format(jet_number,jetvar))
                except:
                    1 == 1

        for jet_number in range(1,7) :
            for jetvar in ['DeepFlavB', 'BTagSF', 'TightTTWeight', 'MediumTTWeight', 'LooseTTWeight', 'HiggsMatched', 'HasMuon', 'HasElectron', 'FatJetMatched', 'HiggsMatchedIndex', 'MatchedGenPt', 'JetId', 'PuId', 'HadronFlavour', 'FatJetMatchedIndex', 'RawFactor'] :
                try :
                    variables.remove('bcand{}{}'.format(jet_number,jetvar))
                except:
                    1 == 1

        for jet_number in range(1,4) :
            variables.remove('h{}_t3_match'.format(jet_number))
            variables.remove('h{}_t2_dRjets'.format(jet_number))
            for hvar in ["pt", "eta", "phi", "mass", "match"] :
                variables.remove('h{}_t2_{}'.format(jet_number, hvar))
                variables.remove('h{}_{}'.format(jet_number, hvar))

            # MassRegressed is saved as Mass simply
            for fatvar in ["HasBJetCSVLoose", "MassSD", "HasMuon", "HasElectron", "HiggsMatched", "OppositeHemisphereHasBJet", "NSubJets", "HiggsMatchedIndex", "GenMatchIndex", "MassRegressed_UnCorrected", "PtOverMHH_MassRegressed", "PtOverMSD", "PtOverMRegressed", "MassSD_noJMS", "RawFactor", "MassRegressed_JMS_Down", "MassSD_JMS_Down", "MassRegressed", 'Tau3OverTau2', 'PtOverMHH', 'MatchedGenPt', "MassSD_UnCorrected"] :
                try :
                    variables.remove('fatJet{}{}'.format(jet_number,fatvar))
                except:
                    1 == 1

        print("Cleaned variables", len(variables))
        print(variables)
        ## symetrize angle variables
        for type_obj in ['bcand', 'fatJet', 'jet'] :
            for jet_number in range(1,11) :
                for angle in ['Eta', 'Phi'] :
                    obj = '{}{}{}'.format(type_obj,jet_number,angle)
                    if obj in variables :
                        #print("Take absolute of %s" % obj)
                        chunk_df = chunk_df.Redefine(obj, "abs(%s)" % obj)
                chunk_df = chunk_df.Redefine('hhh_eta', "abs(hhh_eta)")
                chunk_df = chunk_df.Redefine('hh_phi', "abs(hh_phi)")

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
  if not skip_do_histograms : # args.doHistograms:
   for proctodo in procstodo :
    if proctodo == "data_obs" :
        if not year == '2018' :
            datahist = 'BTagCSV'
        else:
            datahist = 'JetHT'
    else :
        datahist = proctodo
    outtree = "{}/{}/{}.root".format(input_tree,selection,proctodo) ## make better, to not have to call it twice
    ## do Histograms
    output_histos = "{}/{}/histograms".format(input_tree,selection)

    if not path.exists(output_histos) :
      procs=subprocess.Popen(['mkdir %s' % output_histos],shell=True,stdout=subprocess.PIPE)
      out = procs.stdout.read()

    chunk_df = ROOT.RDataFrame(inputTree, outtree)
    seconds0 = time.time()
    # Define histograms to be produced
    print(output_histos)
    f_out = ROOT.TFile(output_histos + '/' + 'histograms_%s.root'%(proctodo), 'recreate')
    print("Writing in %s"%(output_histos + '/' + 'histograms_%s.root'%(proctodo)))

    histograms = []
    variables = chunk_df.GetColumnNames()
    #print(labels.keys())
    #variables = [v for v in labels if 'h_fit_mass' not in v and 'match' not in v and 'Match' not in v] # can be done better
    print("Will produce histograms for following variables:")
    print(variables)

    # Rdataframes require first histogram to be produced and then the rest is nested in the loop of the first one
    binning = binnings['h_fit_mass'].replace('(','').replace(')','').split(',')
    bins = int(binning[0])
    xmin = float(binning[1])
    xmax = float(binning[2])

    print(bins,xmin,xmax)
    h = chunk_df.Histo1D(("h_fit_mass","h_fit_mass",bins,xmin,xmax),"h_fit_mass", "totalWeight") # booking the rdataframe loop

    # TH1DModel::TH1DModel(const char* name, const char* title, int nbinsx, double xlow, double xup)
    h.SetTitle('h_fit_mass')
    h.SetName('h_fit_mass')

    histograms.append(h)
    for var in variables: # booking all variables to be produced
        try :
            binnings[var]
        except :
            print("Skip doing histogram to %s, if you want to draw add the binning option in utils" % var)
            continue
        binning = binnings[var].replace('(','').replace(')','').split(',')
        bins = int(binning[0])
        xmin = float(binning[1])
        xmax = float(binning[2])
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

  # Draw the data/MC to this selection
  #for proctodo in procstodo :
  #file_data = ROOT.TFile(histo_path + '/' + 'histograms_%s.root'%(datahist))
        # python make_histograms_rdataframe_selection.py --version v25 --year 2017 --region gt5bloose_0PFfat --inputs_path /eos/user/m/mstamenk/CxAOD31run/hhh-6b/v25/2017/baseline/gt5bloose_0PFfat/ --outputs_path /eos/user/m/mstamenk/CxAOD31run/hhh-6b/v25/2017/baseline/gt5bloose_0PFfat/data_mc --doHistograms
