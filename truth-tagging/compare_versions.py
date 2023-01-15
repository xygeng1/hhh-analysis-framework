# Script to compare version 

import os, ROOT
import glob

ROOT.gROOT.SetBatch(ROOT.kTRUE)

path_v1 = 'histograms-v23'
path_v2 = 'histograms-v24'

label_v1 = 'v23'
label_v2 = 'v24'

year = '2017'
sample = 'BTagCSV'

samples_list = ['GluGluToHHHTo6B_SM', 'QCD', 'QCD6B', 'TT','WJetsToQQ','WWTo4Q','WWW','WWZ','WZZ','ZJetsToQQ','ZZTo4Q','ZZZ']

for year in ['2017','2018']:
    if year == '2018':
        samples = samples_list + ['JetHT']
    else:
        samples = samples_list + ['BTagCSV']
    for sample in samples:
        eos_plots = 'comparison-%s-%s-%s'%(year,label_v1,label_v2)
        if not os.path.isdir(eos_plots):
            os.mkdir(eos_plots)
        f_in = '%s_%s'%(sample,year)

        f_v1 = ROOT.TFile(path_v1 + '/' + f_in + '.root')
        f_v2 = ROOT.TFile(path_v2 + '/' + f_in + '.root')

        histos = [h.GetName() for h in f_v1.GetListOfKeys()]

        print("Running over ", f_in)
        print(histos)

        #hist_name = histos[0]
        for hist_name in histos:

            h_v1 = f_v1.Get(hist_name)
            h_v1.SetStats(0)
            h_v2 = f_v2.Get(hist_name)

            h_v1.SetLineColor(ROOT.kBlack)
            h_v1.SetLineWidth(2)

            h_v1.GetXaxis().SetLabelOffset(999)
            h_v2.GetXaxis().SetLabelSize(0)

            maxi = max(h_v1.GetMaximum(), h_v2.GetMaximum())
            h_v1.SetMaximum(maxi*1.5)
            h_v2.SetMaximum(maxi*1.5)

            h_v2.SetLineColor(ROOT.kRed + 2)
            h_v2.SetLineWidth(2)

            h_div = h_v1.Clone(h_v1.GetName() + '_div')
            h_div.Divide(h_v2)

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

            h_div.GetYaxis().SetTitle('%s/%s'%(label_v1,label_v2))

            legend = ROOT.TLegend(0.6,0.6,0.9,0.9)
            legend.SetBorderSize(0)
            legend.AddEntry(h_v1,label_v1)
            legend.AddEntry(h_v2,label_v2)

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
            h_v1.Draw("hist e")
            h_v2.Draw("hist e same")
            legend.Draw()

            p1.cd()
            p1.SetGridy()
            h_div.Draw("hist e")

            c.Print(eos_plots + '/' + f_in + '_' + hist_name + '.pdf')
