# Script to compute the trigger efficiency curves

import os,ROOT
from utils import hlt_paths, luminosities, labels, binnings, wps_years

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.ROOT.EnableImplicitMT()

year = '2017'


f_in = 'TT'
version = 'v24'

for year in ['2016APV','2016','2017','2018']:
    path = '/isilon/data/users/mstamenk/eos-triple-h/samples-%s-%s-nanoaod'%(version,year)
    hlt = hlt_paths[year]
    lumi = luminosities[year]
    for f_in in ['QCD_bEnriched','GluGluToHHHTo6B_SM','QCD','TT','WJetsToQQ','WWTo4Q','WWW','WWZ','WZZ','ZJetsToQQ','ZZTo4Q','ZZZ','SingleMuon']:
        print(year,f_in)

        f_out = ROOT.TFile('histograms/%s_%s.root'%(f_in,year),'recreate')


        df = ROOT.ROOT.RDataFrame('Events', path + '/' + f_in + '.root')

        if f_in == 'SingleMuon':
            cutWeight = '1'
        else:
            cutWeight = '(%f * weight * xsecWeight * l1PreFiringWeight * puWeight * genWeight)'%(lumi)

        df = df.Filter('HLT_IsoMu24',"Pass reference trigger") # reference path (already selected in principle)
        df = df.Define('eventWeight',cutWeight)
        

        # Selection
        df = df.Filter("lep1Pt > 30 || lep2Pt > 30",'Lepton momentum cut')
        wp = wps_years['loose'][year]
        cut = 'jet1DeepFlavB > %f && jet2DeepFlavB > %f && jet3DeepFlavB > %f'%(wp,wp,wp)

        df = df.Filter(cut,'Pass b-tagging loose on 3 jets with highest score')

        df_hlt = df.Filter(hlt, 'Pass trigger to calibrate')

        report = df_hlt.Report()
        report.Print()


        var = 'ht'
        binning = binnings[var].replace('(','').replace(')','').split(',')
        bins = int(binning[0])
        xmin = float(binning[1])
        xmax = float(binning[2])

        href = df.Histo1D((var,var,bins,xmin,xmax),var,'eventWeight')
        h_hlt = df_hlt.Histo1D((var,var,bins,xmin,xmax),var,'eventWeight')

        href.Draw()

        href.GetValue().Rebin(2)
        h_hlt.GetValue().Rebin(2)

        href.SetName('tot')
        href.SetTitle('tot')

        h_hlt.SetName('pass')
        h_hlt.SetName('pass')

        f_out.cd()
        href.Write()
        h_hlt.Write()
        f_out.Close()


