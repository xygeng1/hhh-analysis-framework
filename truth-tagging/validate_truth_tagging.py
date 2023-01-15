# Script to overlay direct and truth tagging comparison for each process
import os, ROOT
from utils import get_scans, labels, binnings, wps_years

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.ROOT.EnableImplicitMT()


path = '/isilon/data/users/mstamenk/eos-triple-h/' 
version = 'v24'


year = '2017'
f_in = 'TT'

for year in ['2016','2016APV','2017','2018']:
#for year in ['2017','2018']:
    scans = get_scans(year)
    if '2018' in year:
        samples_list = ['GluGluToHHHTo6B_SM','QCD','QCD6B','QCD_bEnriched','QCD6B_bEnriched','TT','WJetsToQQ','WWTo4Q','WWW','WWZ','WZZ','ZJetsToQQ','ZZTo4Q','ZZZ','JetHT']
    else:
        samples_list = ['GluGluToHHHTo6B_SM','QCD','QCD6B','QCD_bEnriched','QCD6B_bEnriched','TT','WJetsToQQ','WWTo4Q','WWW','WWZ','WZZ','ZJetsToQQ','ZZTo4Q','ZZZ','BTagCSV']
    if 'v23' in version:
        samples_list.remove('QCD_bEnriched')
        samples_list.remove('QCD6B_bEnriched')
    for f_in in samples_list:
        hist_rep = 'histograms-%s-optimised'%version
        if not os.path.isdir(hist_rep):           
            os.mkdir(hist_rep)
        name_out = '%s/%s_%s.root'%(hist_rep,f_in,year)
        f_out = ROOT.TFile(name_out,'recreate')

        eos_plots = 'plots_tt_validation_%s-normscaled-%s-optimised'%(year,version)
        if not os.path.isdir(eos_plots):
            os.mkdir(eos_plots)

        #repo = 'mva-inputs-HLT-TripleBTagCSV-MVAInputs-TTWeights-%s-inclusive-loose-wp-0ptag-%s-btagSF/'%(version,year)
        #if year == '2017':
        #    repo = 'mva-inputs-HLT-TripleBTagCSV-TTWeights-BDT-%s-inclusive-loose-wp-0ptag-%s-btagSF/'%(version,year)
        #else:
        #repo = 'mva-inputs-HLT-TripleBTagCSV-TTWeights-Optimal-BDT-%s-inclusive-loose-wp-0ptag-%s-btagSF/'%(version,year)
        repo = 'mva-inputs-HLT-fit-inputs-%s-inclusive-loose-wp-0ptag-%s'%(version,year)
        if 'v23' in version and '2018' in year:
            repo = 'mva-inputs-HLT-TripleBTagCSV-TTWeights-Optimal-BDT-2018-%s-inclusive-loose-wp-0ptag-%s-btagSF/'%(version,year)



        full_path = path + '/' + version + '/' + repo

        df = ROOT.ROOT.RDataFrame('Events', full_path  +  '/' + f_in + '.root')

        for s in ['LLLLLL','MMMMMM','TTTTTT']:
            scan = scans[s]
            cut = scan[0]
            weight = scan[1]
            tt_weight = scan[2]

            #tt_weight = tt_weight.replace('eventWeight','eventWeightBTagCorrected')
            #weight = weight.replace('eventWeight','eventWeightBTagCorrected')

            df_dt = df.Filter(cut)
            #df_dt = df
            df = df.Define('tt_weight_%s'%s,tt_weight)
            df_dt =  df_dt.Define('dt_weight_%s'%s, weight)
            #df_dt = df_dt.Define('dt_weight_%s'%s, 'eventWeight')

            var = 'mva'
            for var in ['mva','h_fit_mass']:
                binning = binnings[var].replace('(','').replace(')','').split(',')
                bins = int(binning[0])
                xmin = float(binning[1])
                xmax = float(binning[2])

                h_dt = df_dt.Histo1D((var,var,bins,xmin,xmax),var,'dt_weight_%s'%s) 
                h_tt = df.Histo1D((var,var,bins,xmin,xmax),var,'tt_weight_%s'%s)

                h_tt.Draw()

                h_tt.GetValue().SetStats(0)
                h_tt.GetValue().SetTitle('')
                h_tt.GetValue().GetYaxis().SetTitle('Events')
                h_tt.GetValue().SetLineColor(ROOT.kGreen + 2)
                h_tt.GetValue().GetXaxis().SetLabelOffset(999)
                h_tt.GetValue().GetXaxis().SetLabelSize(0)

                h_tt.GetValue().SetLineWidth(2)
                h_dt.GetValue().SetLineWidth(2)
                if h_tt.GetValue().Integral() > 0 :
                    h_tt.GetValue().Scale(h_dt.GetValue().Integral()/ h_tt.GetValue().Integral())

                maxi = max(h_tt.GetValue().GetMaximum(), h_dt.GetValue().GetMaximum())
                h_tt.GetValue().SetMaximum(1.5* maxi)
                h_dt.GetValue().SetMaximum(1.5* maxi)

                h_div = h_tt.GetValue().Clone('%s_%s_%s_div'%(f_in,var,year))
                h_div.Divide(h_dt.GetValue())
                h_div.GetYaxis().SetTitle('TT / DT')
                h_div.GetXaxis().SetTitle(labels[var])

                h_div.GetXaxis().SetTitleSize(0.11)
                h_div.GetXaxis().SetTitleOffset(1.35)
                h_div.GetXaxis().SetLabelSize(0.11)
                h_div.GetXaxis().SetLabelOffset(0.03)
                h_div.GetYaxis().SetTitleSize(0.11)
                h_div.GetYaxis().SetTitleOffset(0.35)
                h_div.GetYaxis().SetLabelSize(0.11)
                h_div.GetYaxis().SetLabelOffset(0.001)
                h_div.GetYaxis().SetMaxDigits(0)
                h_div.GetYaxis().SetNdivisions(4,8,0,ROOT.kTRUE)

                h_div.GetYaxis().SetRangeUser(0.1,2.)

                legend = ROOT.TLegend(0.6,0.6,0.9,0.9)
                legend.SetBorderSize(0)
                legend.AddEntry(h_tt.GetValue(),'Truth tagging')
                legend.AddEntry(h_dt.GetValue(),'Direct tagging')

                c = ROOT.TCanvas()
                p1 = ROOT.TPad("c_1","",0,0,1,0.3)
                p2 = ROOT.TPad("c_2","", 0,0.3,1,1)
                p1.Draw()
                p2.Draw()

                p1.SetBottomMargin(0.3)
                p1.SetTopMargin(0.05)
                p1.SetRightMargin(0.05)
                p2.SetTopMargin(0.05)
                p2.SetBottomMargin(0.02)
                p2.SetRightMargin(0.05)

                p2.cd()
                h_tt.Draw('hist e')
                h_dt.Draw('hist e same')
                legend.Draw()

                p1.cd()
                p1.SetGridy()
                h_div.Draw('hist e')
                c.Print(eos_plots + '/' + '%s_%s_%s.pdf'%(f_in,var,s))

                h_tt.GetValue().SetName('%s_%s_TT'%(var,s))
                h_dt.GetValue().SetName('%s_%s_DT'%(var,s))

                f_out.cd()
                h_tt.Write()
                h_dt.Write()

        f_out.Close()


