# Script to make histograms using rdataframe

import os, ROOT
from utils_new import labels, binnings, cuts, wps, tags, luminosities, hlt_paths, triggersCorrections, add_bdt, bdts_xml
from calibrations import btag_init, addBTagSF, addBTagEffSF
from truthtagging import tt_init, addTTWeight
from array import array


# argument parser
import argparse
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('-v','--version', default='v25') # version of NanoNN production
parser.add_argument('--year', default='2018') # year
parser.add_argument('--region', default = 'inclusive') # region: nFJ0, nFJ1, nFJ2, inclsuive, nFJ1p(= 1+2+3 fatjets)
parser.add_argument('--tag', default = '6tag') # n b-tags on AK4 jets using DeepJet
parser.add_argument('--wp', default = 'loose') # b-tagging working point: loose, medium, tight
parser.add_argument('--f_in', default = 'GluGluToHHHTo6B_SM') # input samples
#parser.add_argument('--inputs_path', default = '/afs/cern.ch/work/m/mstamenk/public/forPKU/') # path of inputs after NanoNN
parser.add_argument('--inputs_path', default = '/eos/user/m/mstamenk/CxAOD31run/hhh-6b/v25/2017/baseline_recomputedSF/gt5bmedium_0PFfat') # path of inputs after NanoNN  /eos/user/m/mstamenk/CxAOD31run/hhh-6b/v25/2017/inclusive
parser.add_argument('--outputs_path', help='Please specify output path for histograms / mva inputs location to be stored', default = '/eos/user/x/xgeng/workspace/HHH/CMSSW_12_5_2/src/hhh-analysis-framework/output') # output path for histograms and mva inputs
parser.add_argument('--doMVAInputs', action = 'store_true') # store MVA inputs
parser.add_argument('--doHistograms', action = 'store_true') # store histograms
parser.add_argument('--addBDT', action = 'store_true') # store histograms

args = parser.parse_args()

if not args.outputs_path:
    print("Exitting script: error")
    print("Please provide output path --outputs_path /path/to/store/outputs/")
    exit()

# set batch to speed up the run
ROOT.gROOT.SetBatch(ROOT.kTRUE)
#ROOT.ROOT.EnableImplicitMT()


# get inputs 
version = args.version
#path = args.inputs_path + '/' + 'samples-%s-%s-nanoaod'%(version,args.year) 
path = args.inputs_path
#path = args.inputs_path + '/' + 'samples-%s-%s-%s-wp-%s-%s'%(version,args.region,args.wp,args.tag,args.year) + '/'
#path = args.inputs_path + '/' + 'mva-inputs-HLT-selection-%s-inclusive-loose-wp-0ptag-%s'%(version,args.year) + '/'
print(path)
f_in = args.f_in

# data frame with all the events 
df = ROOT.ROOT.RDataFrame('Events', path+'/' + f_in + '.root')


lumi = luminosities[args.year]
wp = args.wp
tag = args.tag
region = args.region
typename = 'gt5bmedium_0PFfat'

if args.doHistograms:
    print("Running doHistograms: preparing output folder")
    out_path = args.outputs_path + '/' + args.version + '/'  + 'histograms-%s-%s-%s-%s'%(typename,version,region,args.year)
    #out_path = args.outputs_path + '/' + args.version + '/'  + 'histograms-%s-%s-%s-%s-wp-%s-%s'%(typename,version,region,wp,tag,args.year)
    print("Histograms will be saved at: " + out_path)
    if not os.path.isdir(out_path):
        os.makedirs(out_path)

    f_out = ROOT.TFile(out_path + '/' + 'histograms_%s.root'%(f_in), 'recreate')
    print("Writing in %s"%(out_path + '/' + 'histograms_%s.root'%(f_in)))

if args.doMVAInputs:
    mva_training_samples = args.outputs_path + '/' + args.version + '/' + 'mva-inputs-%s-%s-%s-%s'%(typename,version,region,args.year)
    #mva_training_samples = args.outputs_path + '/' + args.version + '/' + 'mva-inputs-%s-%s-%s-%s-wp-%s-%s'%(typename,version,region,wp,tag,args.year)
    print("Running doMVAInputs: preparing folder")
    print("Writing in %s"%mva_training_samples)
    if not os.path.isdir(mva_training_samples):
        os.makedirs(mva_training_samples)

# Tagging selection
# cutTag = tags[tag]
# print(cutTag)

#if tag == '0ptag':
#    cutTag = tags[tag]
#    wp = 'noWP'
#else:
    #cutTag = tags[tag]%(wps[wp], wps[wp], wps[wp], wps[wp], wps[wp], wps[wp])

cutRegion = cuts[region]

# cutweight = 从文件中读出
# eventWeightBTagSF = 从文件中读出
# eventWeightBTagCorrected = 从文件中读出


df = df.Filter(cutRegion, "Pass region cut")


# # Define new variables
# if 'hhh_t3_pt' not in df.GetColumnNames():
#     df = df.Define('hhh_t3_pt','h1_t3_pt + h2_t3_pt + h3_t3_pt')
# if 'eventWeight' not in df.GetColumnNames():
#     df = df.Define('eventWeight',cutWeight)

# if 'eventWeightBTagSF' not in df.GetColumnNames():
#     df = df.Define('eventWeightBTagSF',cutWeightBTagSF)

# # Normalisation ratio
# weight_before = df.Sum('eventWeight')
# weight_after = df.Sum('eventWeightBTagSF')

# ratio = weight_before.GetValue() / weight_after.GetValue()
# df = df.Define('ratioPerEvent', '%f'%ratio)
# df = df.Define('eventWeightBTagCorrected', 'eventWeightBTagSF * ratioPerEvent')

print("This is f_in:")
print(f_in)




# if args.addBDT:
#      #xml = bdts_xml[args.year]
#      df = add_bdt(df,args.year)



# Print report on event selection
report = df.Report()
report.Print()

if args.doMVAInputs:
    df.Snapshot('Events', mva_training_samples + '/' + f_in + '.root')

if args.doHistograms:
    # Define histograms to be produced
    histograms = []
    variables = df.GetColumnNames()
    variables = [v for v in labels if 'h_fit_mass' not in v and 'match' not in v and 'Match' not in v] # can be done better
    print("Will produce histograms for following variables:")
    print(variables)

    # Rdataframes require first histogram to be produced and then the rest is nested in the loop of the first one
    binning = binnings['h_fit_mass'].replace('(','').replace(')','').split(',')
    bins = int(binning[0])
    xmin = float(binning[1])
    xmax = float(binning[2])

    h = df.Histo1D(('h_fit_mass','h_fit_mass',bins,xmin,xmax),"h_fit_mass", 'eventWeight') # booking the rdataframe loop
    h.SetTitle('h_fit_mass')
    h.SetName('h_fit_mass')

    histograms.append(h)
    for var in variables: # booking all variables to be produced
        binning = binnings[var].replace('(','').replace(')','').split(',')
        bins = int(binning[0])
        xmin = float(binning[1])
        xmax = float(binning[2])
        # print("This is var:")
        # print(var)
        #print("This is bins:")
        #print(bins)
        #print("This is eventweight:")
       # print('eventWeight')
        #print("This is xmin")
        #print(xmin)
        #print("This is xmax")
        #print(xmax)
        h_tmp = df.Histo1D((var,var,bins,xmin,xmax),var, 'eventWeight')
        h_tmp.SetTitle('%s'%(var))
        h_tmp.SetName('%s'%(var))
        histograms.append(h_tmp)
    h.Draw() # run one loop for all variables

    # writing output histograms
    f_out.cd()
    for h in histograms:
        h.Write()
    f_out.Close()

