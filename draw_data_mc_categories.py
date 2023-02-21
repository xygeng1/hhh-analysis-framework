# Script to plot data / mc from processed files

import os
from utils import histograms_dict, hist_properties, addLabel_CMS_preliminary, luminosities

import ROOT

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.CloseFiles()
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = 2000;")
ROOT.gROOT.SetMustClean(True)
ROOT.gStyle.SetOptStat("0")
ROOT.gROOT.SetBatch(ROOT.kTRUE)

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--input_folder", type="string", dest="input_folder", help="Folder in where to look for the categories", default='/eos/user/m/mstamenk/CxAOD31run/hhh-6b/v25/2017/baseline_recomputedSF/')
parser.add_option("--output_folder", type="string", dest="output_folder", help="Folder in where to look for the categories", default='none')
parser.add_option("--log", action="store_true", dest="log", help="Write...", default=False)
parser.add_option("--save_pdf", action="store_true", dest="save_pdf", help="Write...", default=False)
parser.add_option("--plot_label", type="string", dest="plot_label", help="Text to add on top left of the plot", default='none')


(options, args) = parser.parse_args()

input_folder = options.input_folder
do_log       = options.log
save_pdf     = options.save_pdf
plot_label   = options.plot_label


# change into one liner....
output_folder=options.output_folder
if output_folder == "none" :
    output_folder = input_folder

for era in ['2016APV', '2016' '2017', '2018' ] :
    if era in input_folder.split("/") : year = era

labels = addLabel_CMS_preliminary(luminosities[year])

iPeriod = 0
c = ROOT.TCanvas()
c.SetCanvasSize(600, 700)
#c.SetBorderMode(0)
#c.SetTopMargin(0.5)
p1 = ROOT.TPad("c_1","",0,0,1,0.3)
p2 = ROOT.TPad("c_2","", 0,0.3,1,0.95)

datahist   = 'data_obs'
signalhist = 'GluGluToHHHTo6B_SM'
inputTree = 'Events'

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

file_data   = "{}/{}.root".format(input_folder, datahist)
file_signal = "{}/{}.root".format(input_folder, signalhist)

chunk_data   = ROOT.RDataFrame(inputTree, file_data)
chunk_signal = ROOT.RDataFrame(inputTree, file_signal)
variables = chunk_data.GetColumnNames()

#file_data = ROOT.TFile(input_folder + '/' + 'histograms_%s.root'%(datahist))
#variables = [v.GetName() for v in file_data.GetListOfKeys()]
#file_data.Close()

if do_log :
    scale_sig = 1.0
    ypos     = 0.095
else :
    scale_sig = 5000.0
    ypos     = 0.9

for var in variables:
    if "Resolved" in plot_label and "fatJet" in var :
        continue

    try :
        histograms_dict[var]
    except :
        print("Will skip draw %s, if you want to draw the should be added in utils" % var)
        continue

    xpos = 0.05*(histograms_dict[var]["xmax"]-histograms_dict[var]["xmin"])

    try :
        binining = histograms_dict[var]
    except :
        print("Skip drawing %s, if you want to draw add the binning option in utils" % var)
        continue

    template = ROOT.TH1F("", "", histograms_dict[var]["nbins"], histograms_dict[var]["xmin"], histograms_dict[var]["xmax"])
    char_var = var.c_str()
    #file_data = ROOT.TFile(input_folder + '/' + 'histograms_%s.root'%(datahist))
    #file_signal = ROOT.TFile(input_folder + '/' + 'histograms_%s.root'%('GluGluToHHHTo6B_SM'))

    files_bkg = {}
    for bkg in ['ZZZ','WWW','WZZ','ZZTo4Q', 'WWTo4Q', 'WWTo4Q','ZJetsToQQ', 'WJetsToQQ', 'TT', 'QCD6B', 'QCD']:
        #f_tmp = ROOT.TFile(input_folder + '/' + 'histograms_%s.root'%bkg)
        f_tmp = "{}/{}.root".format(input_folder, bkg)
        if os.path.exists(f_tmp) :
            files_bkg[bkg] = f_tmp

    legend = ROOT.TLegend(0.62,0.65,.95,0.9)
    legend.SetBorderSize(0)

    h_data = template.Clone()
    h_data = chunk_data.Fill(template, [char_var])
    h_data.SetTitle(hist_properties[datahist][3])
    h_data.SetName(hist_properties[datahist][3])
    #h_data = file_data.Get(var)
    h_data.SetMarkerColor(ROOT.kBlack)
    h_data.SetLineColor(ROOT.kBlack)
    h_data.SetMarkerSize(100)
    h_data.SetLineWidth(2)
    h_data.SetStats(0)
    h_data.GetXaxis().SetTitle(histograms_dict[var]["label"])
    h_data.SetTitle('')
    legend.AddEntry( h_data.GetPtr(), h_data.GetName())

    if do_log :
        ymax      = 1000000.0*h_data.GetMaximum()
    else :
        ymax      = 1.5*h_data.GetMaximum()

    # blinding
    if 'mass' in var:
        for mass_value in [110,120,130]:
            bin_m = h_data.FindBin(mass_value)
            h_data.SetBinContent(bin_m,-3.0000001)
            h_data.SetBinError(bin_m,-3.0)

    if 'bdt' in var:
        blind_bdt = [x*0.05 + 0.5 for x in range(20)]
        for value in blind_bdt:
            bin_blind = h_data.FindBin(value)
            h_data.SetBinContent(bin_blind,-3.0000001)
            h_data.SetBinError(bin_m,0)

    h_signal = template.Clone()
    h_signal = chunk_signal.Fill(template, [char_var, 'totalWeight'])
    #h_signal = file_signal.Get(var)
    h_signal.SetDirectory(0)
    h_signal.SetMarkerColor(hist_properties[signalhist][0])
    h_signal.SetLineColor(hist_properties[signalhist][0])
    h_signal.SetMarkerSize(hist_properties[signalhist][1])
    h_signal.SetLineWidth(hist_properties[signalhist][2])
    h_signal.Scale(scale_sig)
    label_sig = hist_properties[signalhist][3]
    if not scale_sig == 1.0 :
        label_sig =  "%s (X %s)" % (label_sig, str(scale_sig))
    #legend.AddEntry(h_signal, label_sig, 'l')
    legend.AddEntry(h_signal.GetPtr(), label_sig, 'l')

    h_stack = ROOT.THStack()

    #h_bkg = ROOT.TH1F(var+"bkg", var+"bkg", h_data.GetXaxis().GetNbins(), h_data.GetXaxis().GetXmin(), h_data.GetXaxis().GetXmax())
    h_bkg = template.Clone()
    h_bkg.SetTitle('%s_bkg'%(var))
    h_bkg.SetName('%s_bkg'%(var))

    for bkg in files_bkg:
        chunk_bkg   = ROOT.RDataFrame(inputTree, files_bkg[bkg])
        h_tmp       = chunk_bkg.Fill(template, [char_var, 'totalWeight'])

        try:
            h_tmp.SetDirectory(0)
        except:
            continue

        dumb = h_bkg.Add(h_tmp.GetPtr())
        del dumb

        h_tmp.SetFillColor(hist_properties[bkg][0])
        h_tmp.SetMarkerSize(hist_properties[bkg][1])
        if hist_properties[bkg][4]:
            legend.AddEntry(h_tmp.GetPtr(), hist_properties[bkg][3], 'f')
        print("adding to stack", bkg)
        dumb = h_stack.Add(h_tmp.GetPtr())
        del dumb

    maxi = max(h_data.GetMaximum(), h_bkg.GetMaximum())

    h_data.SetMaximum(1.5*maxi)

    print("doing histo to divide")
    h_div = h_data.Clone(var+'_ratio')
    h_div.Divide(h_bkg)

    h_div.GetYaxis().SetTitle('Data / MC')

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

    h_div.GetYaxis().SetRangeUser(-1.0,3.)

    h_mc_stat = h_bkg.Clone(h_bkg.GetName()+'_mcstat')
    h_mc_stat.Divide(h_bkg)
    h_mc_stat.SetFillColor(ROOT.kBlue)
    h_mc_stat.SetFillStyle(3244)

    h_data.GetXaxis().SetLabelOffset(999)
    h_data.GetXaxis().SetLabelSize(0)
    print("opening canvas")
    c.cd()
    print("drawing pads")
    dumb = p1.Draw()
    dumb = p2.Draw()
    del dumb
    print("setting pads")
    p1.SetBottomMargin(0.3)
    p1.SetTopMargin(0.05)
    p1.SetRightMargin(0.05)
    p2.SetTopMargin(0.05)
    p2.SetBottomMargin(0.02)
    p2.SetRightMargin(0.05)

    h_data.SetMinimum(0.0001)
    h_data.SetMaximum(ymax)

    print("opening pads")
    gPad = p2.cd()
    if do_log :
        gPad.SetLogy()

    print("drawing histograms in upper  pads")
    dumb = h_data.Draw('e')
    dumb = h_stack.Draw('hist e same')
    dumb = h_signal.Draw('hist e same')
    dumb = h_data.Draw('e same')
    dumb = legend.Draw()

    print("adding text")
    plot_label_tpave = ROOT.TText(xpos , ypos*ymax, plot_label)
    plot_label_tpave.SetTextAlign(11)
    plot_label_tpave.SetTextSize(0.04)
    dumb = plot_label_tpave.Draw()

    for ll, label in enumerate(labels):
        dumb = label.Draw("same")
        del dumb

    # plot_label
    print("drawing histograms in down  pads")

    p1.cd()
    p1.SetGridy()
    dumb = h_div.Draw('e')
    dumb = h_mc_stat.Draw('e2 same')
    c.cd()
    print("drawing histograms in down  pads done")


    #c.Update()
    #print("updated canvas")
    #c.RedrawAxis()
    #print("redrawing canvas")

    plot_file = "%s/%s" % (output_folder,str(var))
    # var is 'cppyy.CPPExcInstance'
    if save_pdf :
        c.Print("%s/%s" % (plot_file, '.pdf') ) # save PDF only when we need to add to docs
    dumb = c.Print("%s/%s" % (plot_file, '.png'))
    del dumb
    print("did %s" % plot_file)

    bottomPad.IsA().Destructor(bottomPad)
    c.Flush()
    topPad.IsA().Destructor(topPad)
    c.IsA().Destructor(canvas)

    #file_data.Close()
    #file_signal.Close()
    #for fi in files_bkg:
    #    files_bkg[fi].Close()
