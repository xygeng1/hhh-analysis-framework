# Script to filter output from NanoAOD-tools into inclusive_resolved and inclusive_boosted

import os, ROOT

import glob

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.ROOT.EnableImplicitMT()


version = 'v26'
year = '2018'
path = '/isilon/data/users/mstamenk/eos-triple-h/samples-%s-%s-nanoaod'%(version,year)

output = '/isilon/data/users/mstamenk/eos-triple-h/%s/mva-inputs-%s/'%(version,year)


inclusive_resolved = 'inclusive_resolved'
inclusive_boosted = 'inclusive_boosted'

cut_resolved = 'nsmalljets >= 6 && nprobejets == 0'
cut_boosted = 'nprobejets > 0'

if not os.path.isdir(output + '/' + inclusive_resolved):
    print("Creating %s"%(output + '/' + inclusive_resolved))
    os.makedirs(output + '/' + inclusive_resolved)

if not os.path.isdir(output + '/' + inclusive_boosted):
    print("Creating %s"%(output + '/' + inclusive_boosted))
    os.makedirs(output + '/' + inclusive_boosted)

files = glob.glob(path + '/' + '*.root')

for f_in in files:
    f_name = os.path.basename(f_in)
    print(f_name)

    df = ROOT.RDataFrame('Events',f_in)

    df_resolved = df.Filter(cut_resolved)
    df_boosted = df.Filter(cut_boosted)

    print("Running on %s"%f_in)
    print("Doing resolved")
    
    if not os.path.isfile( output + '/' + inclusive_resolved + '/' + f_name):
        df_resolved.Snapshot('Events', output + '/' + inclusive_resolved + '/' + f_name)
    print("Doing boosted")
    if not os.path.isfile( output + '/' + inclusive_boosted + '/' + f_name):
        df_boosted.Snapshot('Events', output + '/' + inclusive_boosted + '/' + f_name)


print("All done!")



