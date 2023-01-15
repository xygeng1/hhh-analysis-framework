# Script to compute histograms for  b-tagging efficiency maps per samples
# todo Add b-tag weights to get data efficiency

import os, ROOT
from utils import luminosities

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.ROOT.EnableImplicitMT()

wps = { 'loose' : {'2016APV': 0.0508, '2016': 0.0480, '2016PostAPV': 0.0480,'2017': 0.0532, '2018': 0.0490},
        'medium': {'2016APV': 0.2598, '2016': 0.2489, '2016PostAPV': 0.2489,'2017': 0.3040, '2018': 0.2783},
        'tight' : {'2016APV': 0.6502, '2016': 0.6377, '2016PostAPV': 0.6377,'2017': 0.7476, '2018': 0.7100}, 
        }

f_in = 'QCD'
year = '2017'
version = 'v24'

for year in ['2016APV','2016','2017','2018']:
    for f_in in ['QCD_bEnriched','GluGluToHHHTo6B_SM','QCD','TT','WJetsToQQ','WWTo4Q','WWW','WWZ','WZZ','ZJetsToQQ','ZZTo4Q','ZZZ']:
        print("Running on", f_in)

        f_out = ROOT.TFile(year+'/'+'EffMap_%s.root'%f_in,'recreate')

        repo = 'samples-%s-%s-nanoaod'%(version,year)
        path = '/isilon/data/users/mstamenk/eos-triple-h/' + repo + '/'

        df = ROOT.ROOT.RDataFrame('Events', path  +  '/' + f_in + '.root')


        lumi = luminosities[year]
        if 'BTagCSV' in f_in or 'JetHT' in f_in:
            cutWeight = '1'
        else:
            cutWeight = '(%f * weight * xsecWeight * l1PreFiringWeight * puWeight * genWeight)'%(lumi)

        df = df.Define('eventWeight',cutWeight)

        df = df.Define('jet1AbsEta', 'abs(jet1Eta)')
        df = df.Define('jet2AbsEta', 'abs(jet2Eta)')
        df = df.Define('jet3AbsEta', 'abs(jet3Eta)')
        df = df.Define('jet4AbsEta', 'abs(jet4Eta)')
        df = df.Define('jet5AbsEta', 'abs(jet5Eta)')
        df = df.Define('jet6AbsEta', 'abs(jet6Eta)')
        df = df.Define('jet7AbsEta', 'abs(jet7Eta)')
        df = df.Define('jet8AbsEta', 'abs(jet8Eta)')
        df = df.Define('jet9AbsEta', 'abs(jet9Eta)')
        df = df.Define('jet10AbsEta', 'abs(jet10Eta)')

        loose_wp = wps['loose'][year]
        medium_wp = wps['medium'][year]
        tight_wp = wps['tight'][year]


        df1_b = df.Filter('jet1HadronFlavour == 5')
        df1_c = df.Filter('jet1HadronFlavour == 4')
        df1_l = df.Filter('jet1HadronFlavour == 0')

        df2_b = df.Filter('jet2HadronFlavour == 5')
        df2_c = df.Filter('jet2HadronFlavour == 4')
        df2_l = df.Filter('jet2HadronFlavour == 0')

        df3_b = df.Filter('jet3HadronFlavour == 5')
        df3_c = df.Filter('jet3HadronFlavour == 4')
        df3_l = df.Filter('jet3HadronFlavour == 0')

        df4_b = df.Filter('jet4HadronFlavour == 5')
        df4_c = df.Filter('jet4HadronFlavour == 4')
        df4_l = df.Filter('jet4HadronFlavour == 0')

        df5_b = df.Filter('jet5HadronFlavour == 5')
        df5_c = df.Filter('jet5HadronFlavour == 4')
        df5_l = df.Filter('jet5HadronFlavour == 0')

        df6_b = df.Filter('jet6HadronFlavour == 5')
        df6_c = df.Filter('jet6HadronFlavour == 4')
        df6_l = df.Filter('jet6HadronFlavour == 0')

        df7_b = df.Filter('jet7HadronFlavour == 5')
        df7_c = df.Filter('jet7HadronFlavour == 4')
        df7_l = df.Filter('jet7HadronFlavour == 0')

        df8_b = df.Filter('jet8HadronFlavour == 5')
        df8_c = df.Filter('jet8HadronFlavour == 4')
        df8_l = df.Filter('jet8HadronFlavour == 0')

        df9_b = df.Filter('jet9HadronFlavour == 5')
        df9_c = df.Filter('jet9HadronFlavour == 4')
        df9_l = df.Filter('jet9HadronFlavour == 0')

        df10_b = df.Filter('jet10HadronFlavour == 5')
        df10_c = df.Filter('jet10HadronFlavour == 4')
        df10_l = df.Filter('jet10HadronFlavour == 0')


        # jet1
        df1_b_loose = df.Filter('jet1DeepFlavB > %f && jet1HadronFlavour == 5'%loose_wp)
        df1_b_medium = df.Filter('jet1DeepFlavB > %f && jet1HadronFlavour == 5'%medium_wp)
        df1_b_tight = df.Filter('jet1DeepFlavB > %f && jet1HadronFlavour == 5'%tight_wp)

        df1_c_loose = df.Filter('jet1DeepFlavB > %f && jet1HadronFlavour == 4'%loose_wp)
        df1_c_medium = df.Filter('jet1DeepFlavB > %f && jet1HadronFlavour == 4'%medium_wp)
        df1_c_tight = df.Filter('jet1DeepFlavB > %f && jet1HadronFlavour == 4'%tight_wp)

        df1_l_loose = df.Filter('jet1DeepFlavB > %f && jet1HadronFlavour == 0'%loose_wp)
        df1_l_medium = df.Filter('jet1DeepFlavB > %f && jet1HadronFlavour == 0'%medium_wp)
        df1_l_tight = df.Filter('jet1DeepFlavB > %f && jet1HadronFlavour == 0'%tight_wp)

        # jet2
        df2_b_loose = df.Filter('jet2DeepFlavB > %f && jet2HadronFlavour == 5'%loose_wp)
        df2_b_medium = df.Filter('jet2DeepFlavB > %f && jet2HadronFlavour == 5'%medium_wp)
        df2_b_tight = df.Filter('jet2DeepFlavB > %f && jet2HadronFlavour == 5'%tight_wp)

        df2_c_loose = df.Filter('jet2DeepFlavB > %f && jet2HadronFlavour == 4'%loose_wp)
        df2_c_medium = df.Filter('jet2DeepFlavB > %f && jet2HadronFlavour == 4'%medium_wp)
        df2_c_tight = df.Filter('jet2DeepFlavB > %f && jet2HadronFlavour == 4'%tight_wp)

        df2_l_loose = df.Filter('jet2DeepFlavB > %f && jet2HadronFlavour == 0'%loose_wp)
        df2_l_medium = df.Filter('jet2DeepFlavB > %f && jet2HadronFlavour == 0'%medium_wp)
        df2_l_tight = df.Filter('jet2DeepFlavB > %f && jet2HadronFlavour == 0'%tight_wp)

        #jet3
        df3_b_loose = df.Filter('jet3DeepFlavB > %f && jet3HadronFlavour == 5'%loose_wp)
        df3_b_medium = df.Filter('jet3DeepFlavB > %f && jet3HadronFlavour == 5'%medium_wp)
        df3_b_tight = df.Filter('jet3DeepFlavB > %f && jet3HadronFlavour == 5'%tight_wp)

        df3_c_loose = df.Filter('jet3DeepFlavB > %f && jet3HadronFlavour == 4'%loose_wp)
        df3_c_medium = df.Filter('jet3DeepFlavB > %f && jet3HadronFlavour == 4'%medium_wp)
        df3_c_tight = df.Filter('jet3DeepFlavB > %f && jet3HadronFlavour == 4'%tight_wp)

        df3_l_loose = df.Filter('jet3DeepFlavB > %f && jet3HadronFlavour == 0'%loose_wp)
        df3_l_medium = df.Filter('jet3DeepFlavB > %f && jet3HadronFlavour == 0'%medium_wp)
        df3_l_tight = df.Filter('jet3DeepFlavB > %f && jet3HadronFlavour == 0'%tight_wp)

        # jet4
        df4_b_loose = df.Filter('jet4DeepFlavB > %f && jet4HadronFlavour == 5'%loose_wp)
        df4_b_medium = df.Filter('jet4DeepFlavB > %f && jet4HadronFlavour == 5'%medium_wp)
        df4_b_tight = df.Filter('jet4DeepFlavB > %f && jet4HadronFlavour == 5'%tight_wp)

        df4_c_loose = df.Filter('jet4DeepFlavB > %f && jet4HadronFlavour == 4'%loose_wp)
        df4_c_medium = df.Filter('jet4DeepFlavB > %f && jet4HadronFlavour == 4'%medium_wp)
        df4_c_tight = df.Filter('jet4DeepFlavB > %f && jet4HadronFlavour == 4'%tight_wp)

        df4_l_loose = df.Filter('jet4DeepFlavB > %f && jet4HadronFlavour == 0'%loose_wp)
        df4_l_medium = df.Filter('jet4DeepFlavB > %f && jet4HadronFlavour == 0'%medium_wp)
        df4_l_tight = df.Filter('jet4DeepFlavB > %f && jet4HadronFlavour == 0'%tight_wp)

        # jet5
        df5_b_loose = df.Filter('jet5DeepFlavB > %f && jet5HadronFlavour == 5'%loose_wp)
        df5_b_medium = df.Filter('jet5DeepFlavB > %f && jet5HadronFlavour == 5'%medium_wp)
        df5_b_tight = df.Filter('jet5DeepFlavB > %f && jet5HadronFlavour == 5'%tight_wp)

        df5_c_loose = df.Filter('jet5DeepFlavB > %f && jet5HadronFlavour == 4'%loose_wp)
        df5_c_medium = df.Filter('jet5DeepFlavB > %f && jet5HadronFlavour == 4'%medium_wp)
        df5_c_tight = df.Filter('jet5DeepFlavB > %f && jet5HadronFlavour == 4'%tight_wp)

        df5_l_loose = df.Filter('jet5DeepFlavB > %f && jet5HadronFlavour == 0'%loose_wp)
        df5_l_medium = df.Filter('jet5DeepFlavB > %f && jet5HadronFlavour == 0'%medium_wp)
        df5_l_tight = df.Filter('jet5DeepFlavB > %f && jet5HadronFlavour == 0'%tight_wp)

        #jet6
        df6_b_loose = df.Filter('jet6DeepFlavB > %f && jet6HadronFlavour == 5'%loose_wp)
        df6_b_medium = df.Filter('jet6DeepFlavB > %f && jet6HadronFlavour == 5'%medium_wp)
        df6_b_tight = df.Filter('jet6DeepFlavB > %f && jet6HadronFlavour == 5'%tight_wp)

        df6_c_loose = df.Filter('jet6DeepFlavB > %f && jet6HadronFlavour == 4'%loose_wp)
        df6_c_medium = df.Filter('jet6DeepFlavB > %f && jet6HadronFlavour == 4'%medium_wp)
        df6_c_tight = df.Filter('jet6DeepFlavB > %f && jet6HadronFlavour == 4'%tight_wp)

        df6_l_loose = df.Filter('jet6DeepFlavB > %f && jet6HadronFlavour == 0'%loose_wp)
        df6_l_medium = df.Filter('jet6DeepFlavB > %f && jet6HadronFlavour == 0'%medium_wp)
        df6_l_tight = df.Filter('jet6DeepFlavB > %f && jet6HadronFlavour == 0'%tight_wp)

        #jet7
        df7_b_loose = df.Filter('jet7DeepFlavB > %f && jet7HadronFlavour == 5'%loose_wp)
        df7_b_medium = df.Filter('jet7DeepFlavB > %f && jet7HadronFlavour == 5'%medium_wp)
        df7_b_tight = df.Filter('jet7DeepFlavB > %f && jet7HadronFlavour == 5'%tight_wp)

        df7_c_loose = df.Filter('jet7DeepFlavB > %f && jet7HadronFlavour == 4'%loose_wp)
        df7_c_medium = df.Filter('jet7DeepFlavB > %f && jet7HadronFlavour == 4'%medium_wp)
        df7_c_tight = df.Filter('jet7DeepFlavB > %f && jet7HadronFlavour == 4'%tight_wp)

        df7_l_loose = df.Filter('jet7DeepFlavB > %f && jet7HadronFlavour == 0'%loose_wp)
        df7_l_medium = df.Filter('jet7DeepFlavB > %f && jet7HadronFlavour == 0'%medium_wp)
        df7_l_tight = df.Filter('jet7DeepFlavB > %f && jet7HadronFlavour == 0'%tight_wp)

        #jet8
        df8_b_loose = df.Filter('jet8DeepFlavB > %f && jet8HadronFlavour == 5'%loose_wp)
        df8_b_medium = df.Filter('jet8DeepFlavB > %f && jet8HadronFlavour == 5'%medium_wp)
        df8_b_tight = df.Filter('jet8DeepFlavB > %f && jet8HadronFlavour == 5'%tight_wp)

        df8_c_loose = df.Filter('jet8DeepFlavB > %f && jet8HadronFlavour == 4'%loose_wp)
        df8_c_medium = df.Filter('jet8DeepFlavB > %f && jet8HadronFlavour == 4'%medium_wp)
        df8_c_tight = df.Filter('jet8DeepFlavB > %f && jet8HadronFlavour == 4'%tight_wp)

        df8_l_loose = df.Filter('jet8DeepFlavB > %f && jet8HadronFlavour == 0'%loose_wp)
        df8_l_medium = df.Filter('jet8DeepFlavB > %f && jet8HadronFlavour == 0'%medium_wp)
        df8_l_tight = df.Filter('jet8DeepFlavB > %f && jet8HadronFlavour == 0'%tight_wp)

        #jet9
        df9_b_loose = df.Filter('jet9DeepFlavB > %f && jet9HadronFlavour == 5'%loose_wp)
        df9_b_medium = df.Filter('jet9DeepFlavB > %f && jet9HadronFlavour == 5'%medium_wp)
        df9_b_tight = df.Filter('jet9DeepFlavB > %f && jet9HadronFlavour == 5'%tight_wp)

        df9_c_loose = df.Filter('jet9DeepFlavB > %f && jet9HadronFlavour == 4'%loose_wp)
        df9_c_medium = df.Filter('jet9DeepFlavB > %f && jet9HadronFlavour == 4'%medium_wp)
        df9_c_tight = df.Filter('jet9DeepFlavB > %f && jet9HadronFlavour == 4'%tight_wp)

        df9_l_loose = df.Filter('jet9DeepFlavB > %f && jet9HadronFlavour == 0'%loose_wp)
        df9_l_medium = df.Filter('jet9DeepFlavB > %f && jet9HadronFlavour == 0'%medium_wp)
        df9_l_tight = df.Filter('jet9DeepFlavB > %f && jet9HadronFlavour == 0'%tight_wp)

        #jet10
        df10_b_loose = df.Filter('jet10DeepFlavB > %f && jet10HadronFlavour == 5'%loose_wp)
        df10_b_medium = df.Filter('jet10DeepFlavB > %f && jet10HadronFlavour == 5'%medium_wp)
        df10_b_tight = df.Filter('jet10DeepFlavB > %f && jet10HadronFlavour == 5'%tight_wp)

        df10_c_loose = df.Filter('jet10DeepFlavB > %f && jet10HadronFlavour == 4'%loose_wp)
        df10_c_medium = df.Filter('jet10DeepFlavB > %f && jet10HadronFlavour == 4'%medium_wp)
        df10_c_tight = df.Filter('jet10DeepFlavB > %f && jet10HadronFlavour == 4'%tight_wp)

        df10_l_loose = df.Filter('jet10DeepFlavB > %f && jet10HadronFlavour == 0'%loose_wp)
        df10_l_medium = df.Filter('jet10DeepFlavB > %f && jet10HadronFlavour == 0'%medium_wp)
        df10_l_tight = df.Filter('jet10DeepFlavB > %f && jet10HadronFlavour == 0'%tight_wp)

        # Histograms

        binx = 100
        xmin = 20.
        xmax = 1000.

        biny = 25
        ymin = 0.
        ymax = 2.5

        h1_b = df1_b.Histo2D(('jet1_b','jet1_b',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')
        h1_b_loose = df1_b_loose.Histo2D(('jet1_b_loose','jet1_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')
        h1_b_medium = df1_b_medium.Histo2D(('jet1_b_medium','jet1_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')
        h1_b_tight = df1_b_tight.Histo2D(('jet1_b_tight','jet1_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')

        h1_c = df1_c.Histo2D(('jet1_c','jet1_c',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')
        h1_c_loose = df1_c_loose.Histo2D(('jet1_c_loose','jet1_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')
        h1_c_medium = df1_c_medium.Histo2D(('jet1_c_medium','jet1_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')
        h1_c_tight = df1_c_tight.Histo2D(('jet1_c_tight','jet1_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')

        h1_l = df1_l.Histo2D(('jet1_l','jet1_l',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')
        h1_l_loose = df1_l_loose.Histo2D(('jet1_l_loose','jet1_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')
        h1_l_medium = df1_l_medium.Histo2D(('jet1_l_medium','jet1_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')
        h1_l_tight = df1_l_tight.Histo2D(('jet1_l_tight','jet1_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet1Pt','jet1AbsEta', 'eventWeight')

        h2_b = df2_b.Histo2D(('jet2_b','jet2_b',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')
        h2_b_loose = df2_b_loose.Histo2D(('jet2_b_loose','jet2_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')
        h2_b_medium = df2_b_medium.Histo2D(('jet2_b_medium','jet2_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')
        h2_b_tight = df2_b_tight.Histo2D(('jet2_b_tight','jet2_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')

        h2_c = df2_c.Histo2D(('jet2_c','jet2_c',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')
        h2_c_loose = df2_c_loose.Histo2D(('jet2_c_loose','jet2_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')
        h2_c_medium = df2_c_medium.Histo2D(('jet2_c_medium','jet2_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')
        h2_c_tight = df2_c_tight.Histo2D(('jet2_c_tight','jet2_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')

        h2_l = df2_l.Histo2D(('jet2_l','jet2_l',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')
        h2_l_loose = df2_l_loose.Histo2D(('jet2_l_loose','jet2_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')
        h2_l_medium = df2_l_medium.Histo2D(('jet2_l_medium','jet2_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')
        h2_l_tight = df2_l_tight.Histo2D(('jet2_l_tight','jet2_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet2Pt','jet2AbsEta', 'eventWeight')

        h3_b = df3_b.Histo2D(('jet3_b','jet3_b',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')
        h3_b_loose = df3_b_loose.Histo2D(('jet3_b_loose','jet3_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')
        h3_b_medium = df3_b_medium.Histo2D(('jet3_b_medium','jet3_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')
        h3_b_tight = df3_b_tight.Histo2D(('jet3_b_tight','jet3_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')

        h3_c = df3_c.Histo2D(('jet3_c','jet3_c',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')
        h3_c_loose = df3_c_loose.Histo2D(('jet3_c_loose','jet3_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')
        h3_c_medium = df3_c_medium.Histo2D(('jet3_c_medium','jet3_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')
        h3_c_tight = df3_c_tight.Histo2D(('jet3_c_tight','jet3_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')

        h3_l = df3_l.Histo2D(('jet3_l','jet3_l',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')
        h3_l_loose = df3_l_loose.Histo2D(('jet3_l_loose','jet3_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')
        h3_l_medium = df3_l_medium.Histo2D(('jet3_l_medium','jet3_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')
        h3_l_tight = df3_l_tight.Histo2D(('jet3_l_tight','jet3_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet3Pt','jet3AbsEta', 'eventWeight')

        h4_b = df4_b.Histo2D(('jet4_b','jet4_b',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')
        h4_b_loose = df4_b_loose.Histo2D(('jet4_b_loose','jet4_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')
        h4_b_medium = df4_b_medium.Histo2D(('jet4_b_medium','jet4_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')
        h4_b_tight = df4_b_tight.Histo2D(('jet4_b_tight','jet4_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')

        h4_c = df4_c.Histo2D(('jet4_c','jet4_c',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')
        h4_c_loose = df4_c_loose.Histo2D(('jet4_c_loose','jet4_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')
        h4_c_medium = df4_c_medium.Histo2D(('jet4_c_medium','jet4_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')
        h4_c_tight = df4_c_tight.Histo2D(('jet4_c_tight','jet4_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')

        h4_l = df4_l.Histo2D(('jet4_l','jet4_l',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')
        h4_l_loose = df4_l_loose.Histo2D(('jet4_l_loose','jet4_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')
        h4_l_medium = df4_l_medium.Histo2D(('jet4_l_medium','jet4_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')
        h4_l_tight = df4_l_tight.Histo2D(('jet4_l_tight','jet4_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet4Pt','jet4AbsEta', 'eventWeight')

        h5_b = df5_b.Histo2D(('jet5_b','jet5_b',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')
        h5_b_loose = df5_b_loose.Histo2D(('jet5_b_loose','jet5_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')
        h5_b_medium = df5_b_medium.Histo2D(('jet5_b_medium','jet5_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')
        h5_b_tight = df5_b_tight.Histo2D(('jet5_b_tight','jet5_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')

        h5_c = df5_c.Histo2D(('jet5_c','jet5_c',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')
        h5_c_loose = df5_c_loose.Histo2D(('jet5_c_loose','jet5_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')
        h5_c_medium = df5_c_medium.Histo2D(('jet5_c_medium','jet5_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')
        h5_c_tight = df5_c_tight.Histo2D(('jet5_c_tight','jet5_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')

        h5_l = df5_l.Histo2D(('jet5_l','jet5_l',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')
        h5_l_loose = df5_l_loose.Histo2D(('jet5_l_loose','jet5_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')
        h5_l_medium = df5_l_medium.Histo2D(('jet5_l_medium','jet5_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')
        h5_l_tight = df5_l_tight.Histo2D(('jet5_l_tight','jet5_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet5Pt','jet5AbsEta', 'eventWeight')

        h6_b = df6_b.Histo2D(('jet6_b','jet6_b',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')
        h6_b_loose = df6_b_loose.Histo2D(('jet6_b_loose','jet6_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')
        h6_b_medium = df6_b_medium.Histo2D(('jet6_b_medium','jet6_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')
        h6_b_tight = df6_b_tight.Histo2D(('jet6_b_tight','jet6_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')

        h6_c = df6_c.Histo2D(('jet6_c','jet6_c',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')
        h6_c_loose = df6_c_loose.Histo2D(('jet6_c_loose','jet6_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')
        h6_c_medium = df6_c_medium.Histo2D(('jet6_c_medium','jet6_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')
        h6_c_tight = df6_c_tight.Histo2D(('jet6_c_tight','jet6_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')

        h6_l = df6_l.Histo2D(('jet6_l','jet6_l',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')
        h6_l_loose = df6_l_loose.Histo2D(('jet6_l_loose','jet6_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')
        h6_l_medium = df6_l_medium.Histo2D(('jet6_l_medium','jet6_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')
        h6_l_tight = df6_l_tight.Histo2D(('jet6_l_tight','jet6_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet6Pt','jet6AbsEta', 'eventWeight')

        h7_b = df7_b.Histo2D(('jet7_b','jet7_b',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')
        h7_b_loose = df7_b_loose.Histo2D(('jet7_b_loose','jet7_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')
        h7_b_medium = df7_b_medium.Histo2D(('jet7_b_medium','jet7_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')
        h7_b_tight = df7_b_tight.Histo2D(('jet7_b_tight','jet7_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')

        h7_c = df7_c.Histo2D(('jet7_c','jet7_c',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')
        h7_c_loose = df7_c_loose.Histo2D(('jet7_c_loose','jet7_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')
        h7_c_medium = df7_c_medium.Histo2D(('jet7_c_medium','jet7_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')
        h7_c_tight = df7_c_tight.Histo2D(('jet7_c_tight','jet7_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')

        h7_l = df7_l.Histo2D(('jet7_l','jet7_l',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')
        h7_l_loose = df7_l_loose.Histo2D(('jet7_l_loose','jet7_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')
        h7_l_medium = df7_l_medium.Histo2D(('jet7_l_medium','jet7_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')
        h7_l_tight = df7_l_tight.Histo2D(('jet7_l_tight','jet7_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet7Pt','jet7AbsEta', 'eventWeight')

        h8_b = df8_b.Histo2D(('jet8_b','jet8_b',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')
        h8_b_loose = df8_b_loose.Histo2D(('jet8_b_loose','jet8_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')
        h8_b_medium = df8_b_medium.Histo2D(('jet8_b_medium','jet8_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')
        h8_b_tight = df8_b_tight.Histo2D(('jet8_b_tight','jet8_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')

        h8_c = df8_c.Histo2D(('jet8_c','jet8_c',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')
        h8_c_loose = df8_c_loose.Histo2D(('jet8_c_loose','jet8_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')
        h8_c_medium = df8_c_medium.Histo2D(('jet8_c_medium','jet8_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')
        h8_c_tight = df8_c_tight.Histo2D(('jet8_c_tight','jet8_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')

        h8_l = df8_l.Histo2D(('jet8_l','jet8_l',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')
        h8_l_loose = df8_l_loose.Histo2D(('jet8_l_loose','jet8_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')
        h8_l_medium = df8_l_medium.Histo2D(('jet8_l_medium','jet8_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')
        h8_l_tight = df8_l_tight.Histo2D(('jet8_l_tight','jet8_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet8Pt','jet8AbsEta', 'eventWeight')

        h9_b = df9_b.Histo2D(('jet9_b','jet9_b',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')
        h9_b_loose = df9_b_loose.Histo2D(('jet9_b_loose','jet9_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')
        h9_b_medium = df9_b_medium.Histo2D(('jet9_b_medium','jet9_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')
        h9_b_tight = df9_b_tight.Histo2D(('jet9_b_tight','jet9_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')

        h9_c = df9_c.Histo2D(('jet9_c','jet9_c',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')
        h9_c_loose = df9_c_loose.Histo2D(('jet9_c_loose','jet9_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')
        h9_c_medium = df9_c_medium.Histo2D(('jet9_c_medium','jet9_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')
        h9_c_tight = df9_c_tight.Histo2D(('jet9_c_tight','jet9_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')

        h9_l = df9_l.Histo2D(('jet9_l','jet9_l',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')
        h9_l_loose = df9_l_loose.Histo2D(('jet9_l_loose','jet9_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')
        h9_l_medium = df9_l_medium.Histo2D(('jet9_l_medium','jet9_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')
        h9_l_tight = df9_l_tight.Histo2D(('jet9_l_tight','jet9_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet9Pt','jet9AbsEta', 'eventWeight')

        h10_b = df10_b.Histo2D(('jet10_b','jet10_b',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')
        h10_b_loose = df10_b_loose.Histo2D(('jet10_b_loose','jet10_b_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')
        h10_b_medium = df10_b_medium.Histo2D(('jet10_b_medium','jet10_b_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')
        h10_b_tight = df10_b_tight.Histo2D(('jet10_b_tight','jet10_b_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')

        h10_c = df10_c.Histo2D(('jet10_c','jet10_c',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')
        h10_c_loose = df10_c_loose.Histo2D(('jet10_c_loose','jet10_c_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')
        h10_c_medium = df10_c_medium.Histo2D(('jet10_c_medium','jet10_c_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')
        h10_c_tight = df10_c_tight.Histo2D(('jet10_c_tight','jet10_c_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')

        h10_l = df10_l.Histo2D(('jet10_l','jet10_l',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')
        h10_l_loose = df10_l_loose.Histo2D(('jet10_l_loose','jet10_l_loose',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')
        h10_l_medium = df10_l_medium.Histo2D(('jet10_l_medium','jet10_l_medium',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')
        h10_l_tight = df10_l_tight.Histo2D(('jet10_l_tight','jet10_l_tight',binx,xmin,xmax,biny,ymin,ymax), 'jet10Pt','jet10AbsEta', 'eventWeight')

        h1_b.Draw()

        f_out.cd()
        h1_b.Write()
        h1_b_loose.Write()
        h1_b_medium.Write()
        h1_b_tight.Write()

        h1_c.Write()
        h1_c_loose.Write()
        h1_c_medium.Write()
        h1_c_tight.Write()

        h1_l.Write()
        h1_l_loose.Write()
        h1_l_medium.Write()
        h1_l_tight.Write()

        h2_b.Write()
        h2_b_loose.Write()
        h2_b_medium.Write()
        h2_b_tight.Write()

        h2_c.Write()
        h2_c_loose.Write()
        h2_c_medium.Write()
        h2_c_tight.Write()

        h2_l.Write()
        h2_l_loose.Write()
        h2_l_medium.Write()
        h2_l_tight.Write()

        h3_b.Write()
        h3_b_loose.Write()
        h3_b_medium.Write()
        h3_b_tight.Write()

        h3_c.Write()
        h3_c_loose.Write()
        h3_c_medium.Write()
        h3_c_tight.Write()

        h3_l.Write()
        h3_l_loose.Write()
        h3_l_medium.Write()
        h3_l_tight.Write()

        h4_b.Write()
        h4_b_loose.Write()
        h4_b_medium.Write()
        h4_b_tight.Write()

        h4_c.Write()
        h4_c_loose.Write()
        h4_c_medium.Write()
        h4_c_tight.Write()

        h4_l.Write()
        h4_l_loose.Write()
        h4_l_medium.Write()
        h4_l_tight.Write()

        h5_b.Write()
        h5_b_loose.Write()
        h5_b_medium.Write()
        h5_b_tight.Write()

        h5_c.Write()
        h5_c_loose.Write()
        h5_c_medium.Write()
        h5_c_tight.Write()

        h5_l.Write()
        h5_l_loose.Write()
        h5_l_medium.Write()
        h5_l_tight.Write()

        h6_b.Write()
        h6_b_loose.Write()
        h6_b_medium.Write()
        h6_b_tight.Write()

        h6_c.Write()
        h6_c_loose.Write()
        h6_c_medium.Write()
        h6_c_tight.Write()

        h6_l.Write()
        h6_l_loose.Write()
        h6_l_medium.Write()
        h6_l_tight.Write()

        h7_b.Write()
        h7_b_loose.Write()
        h7_b_medium.Write()
        h7_b_tight.Write()

        h7_c.Write()
        h7_c_loose.Write()
        h7_c_medium.Write()
        h7_c_tight.Write()

        h7_l.Write()
        h7_l_loose.Write()
        h7_l_medium.Write()
        h7_l_tight.Write()

        h8_b.Write()
        h8_b_loose.Write()
        h8_b_medium.Write()
        h8_b_tight.Write()

        h8_c.Write()
        h8_c_loose.Write()
        h8_c_medium.Write()
        h8_c_tight.Write()

        h8_l.Write()
        h8_l_loose.Write()
        h8_l_medium.Write()
        h8_l_tight.Write()

        h9_b.Write()
        h9_b_loose.Write()
        h9_b_medium.Write()
        h9_b_tight.Write()

        h9_c.Write()
        h9_c_loose.Write()
        h9_c_medium.Write()
        h9_c_tight.Write()

        h9_l.Write()
        h9_l_loose.Write()
        h9_l_medium.Write()
        h9_l_tight.Write()

        h10_b.Write()
        h10_b_loose.Write()
        h10_b_medium.Write()
        h10_b_tight.Write()

        h10_c.Write()
        h10_c_loose.Write()
        h10_c_medium.Write()
        h10_c_tight.Write()

        h10_l.Write()
        h10_l_loose.Write()
        h10_l_medium.Write()
        h10_l_tight.Write()

        f_out.Close()







