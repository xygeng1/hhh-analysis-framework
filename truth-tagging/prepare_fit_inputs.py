# Script to prepare fit inputs

import os, ROOT

year = '2017'


scan = 'LLLLLL'
tagging = 'DT'
cat = '6tag'
version = 'v24'
path_in = 'histograms-%s-optimised'%version

for year in ['2016APV','2016','2017','2018']:
    samples = ['GluGluToHHHTo6B_SM','QCD','QCD6B','TT','WJetsToQQ','WWTo4Q','WWW','WWZ','WZZ','ZJetsToQQ','ZZTo4Q','ZZZ']
    if year == '2018':
        samples.append('JetHT')
    else:
        samples.append('BTagCSV')

    for tagging in ['DT','TT']:

        path_out = 'fit-inputs-%s-optimised/%s-%s/%s'%(version,cat,year,tagging)
        if not os.path.isdir(path_out):
            os.makedirs(path_out)

        for sample in samples:
            f_in = ROOT.TFile(path_in + '/' + '%s_%s.root'%(sample, year))
            if sample == 'BTagCSV':
                f_out = ROOT.TFile(path_out + '/' +'histograms_%s'%('JetHT') + '.root','recreate')
            else:
                f_out = ROOT.TFile(path_out + '/' +'histograms_%s'%sample + '.root','recreate')
            for var in ['h_fit_mass','mva']:

                var_name = '%s_%s_%s'%(var,scan,tagging)

                h = f_in.Get(var_name)
                h.SetTitle(var)
                h.SetName(var)

                print("Writing %s in %s"%(var,path_out + '/' + 'histograms_%s'%sample + '.root'))
                f_out.cd()
                h.Write()


            f_in.Close()
            f_out.Close()

