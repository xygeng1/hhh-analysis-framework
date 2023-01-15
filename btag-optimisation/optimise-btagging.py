# Script to loop over all the b-tagging configurations and find the optimal one based on s / sqrt(s + b) in h_fit_mass

import os, ROOT
from utils import labels, binnings, wps_years

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.ROOT.EnableImplicitMT()


scale_sig = 1000

def get_sig(h_sig,h_bkg):
    ret = 0
    for i in range(h_sig.GetValue().GetNbinsX()):
        s = h_sig.GetValue().GetBinContent(i) * scale_sig
        b = h_bkg.GetValue().GetBinContent(i)
        if (s+b) > 0:
            ret += s*s / ((s+b)*(s+b))
        else:
            ret += 0

    return ROOT.TMath.Sqrt(ret)

# focus on 2017 that gives best data / mc
year = '2017'
path = 'samples'

signal_vector = ROOT.std.vector('string')()
background_vector = ROOT.std.vector('string')()

for f in ['GluGluToHHHTo6B_SM.root']:
    signal_vector.push_back(path + '/' + f)

signal_samples = [signal_vector, 'signal']

#for f in ['QCD.root','TT.root','WJetsToQQ.root','WWTo4Q.root','WWW.root','WWZ.root','WZZ.root','ZJetsToQQ.root','ZZTo4Q.root','ZZZ.root']:
for f in ['BTagCSV.root']:
    background_vector.push_back(path + '/' + f)

background_samples = [background_vector, 'background']

df_signal = ROOT.RDataFrame('Events',signal_vector)
df_bkg = ROOT.RDataFrame('Events',background_vector)

var = 'h_fit_mass'
binning = binnings[var].replace('(','').replace(')','').split(',')
bins = int(binning[0])
xmin = float(binning[1])
xmax = float(binning[2])

cutWeight = 'eventWeight'
cutRange = 'h_fit_mass > 80 && h_fit_mass < 150'

results = {}

h_sig_ref = df_signal.Histo1D((var,var,bins,xmin,xmax),var,cutWeight)
h_bkg_ref = df_bkg.Histo1D((var,var,bins,xmin,xmax),var,cutWeight)
sig_ref = get_sig(h_sig_ref,h_bkg_ref)

results['inclusive'] = sig_ref
print(results)


loose_wp = wps_years['loose'][year]
medium_wp = wps_years['medium'][year]
tight_wp = wps_years['tight'][year]

label_dict = {'L': [loose_wp,'Loose'],
              'M': [medium_wp,'Medium'],
              'T': [tight_wp,'Tight'],
              'N': [-1, 'NoTagging']
        }

scans = {}
for j1 in ['T','L']:
    for j2 in ['T','L']:
        for j3 in ['T','L']:
            for j4 in ['T','L']:
                for j5 in ['T','L']:
                    for j6 in ['T','L']:
                        #cut = '(jet1DeepFlavB > %f && jet2DeepFlavB > %f && jet3DeepFlavB > %f && jet4DeepFlavB > %f && jet5DeepFlavB > %f && jet6DeepFlavB > %f)'%(label_dict[j1][0],label_dict[j2][0],label_dict[j3][0],label_dict[j4][0],label_dict[j5][0],label_dict[j6][0])
                        cut = '(bcand1DeepFlavB > %f && bcand2DeepFlavB > %f && bcand3DeepFlavB > %f && bcand4DeepFlavB > %f && bcand5DeepFlavB > %f && bcand6DeepFlavB > %f)'%(label_dict[j1][0],label_dict[j2][0],label_dict[j3][0],label_dict[j4][0],label_dict[j5][0],label_dict[j6][0])

                        #weight = 'eventWeight * jet1%sBTagEffSF * jet2%sBTagEffSF * jet3%sBTagEffSF * jet4%sBTagEffSF * jet5%sBTagEffSF * jet6%sBTagEffSF'%(label_dict[j1][1],label_dict[j2][1],label_dict[j3][1],label_dict[j4][1],label_dict[j5][1],label_dict[j6][1])
                        weight = 'eventWeight' 
                        point = j1+j2+j3+j4+j5+j6
                        scans[point] = [cut, weight]


for scan in scans:
    cut, weight = scans[scan]
    new_weight = 'weight%s'%scan
    df_sig_tmp = df_signal.Filter(cut).Define(new_weight, weight)
    h_sig = df_sig_tmp.Histo1D((var,var,bins,xmin,xmax),var,new_weight)

    df_bkg_tmp = df_bkg.Filter(cut).Define(new_weight, weight)
    h_bkg = df_bkg_tmp.Histo1D((var,var,bins,xmin,xmax),var,new_weight)
    res = get_sig(h_sig,h_bkg)
    results[scan] = res
    print(scan,res)

print(results)

print(sorted(results.items(),key=lambda item : item[1], reverse = True))





