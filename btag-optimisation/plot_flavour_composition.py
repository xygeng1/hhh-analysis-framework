import os, ROOT
import tdrstyle,CMS_lumi

#ROOT.gROOT.SetBatch(ROOT.kFALSE)
ROOT.gROOT.SetBatch(ROOT.kTRUE)

# Set CMS style

# Set tdr style
#tdrstyle.setTDRStyle()

#change the CMS_lumi variables (see CMS_lumi.py)
#CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
#CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
#CMS_lumi.writeExtraText = 1
#CMS_lumi.extraText = "Internal"


labels = {
          'h1_mass' : 'm(H1)', 
          'h2_mass' : 'm(H2)', 
          'h3_mass' : 'm(H3)', 

          'h1_pt' : 'p_{T}(H1)', 
          'h2_pt' : 'p_{T}(H2)', 
          'h3_pt' : 'p_{T}(H3)', 

          'h1_eta' : '#eta(H1)', 
          'h2_eta' : '#eta(H2)', 
          'h3_eta' : '#eta(H3)', 

          'h1_phi' : '#phi(H1)', 
          'h2_phi' : '#phi(H2)', 
          'h3_phi' : '#phi(H3)', 

          'fatJet1Mass' : 'm(H1)', 
          'fatJet2Mass' : 'm(H2)', 
          'fatJet3Mass' : 'm(H3)', 

          'fatJet1Pt' : 'p_{T}(H1)', 
          'fatJet2Pt' : 'p_{T}(H2)', 
          'fatJet3Pt' : 'p_{T}(H3)', 

          'fatJet1Eta' : '#eta(H1)', 
          'fatJet2Eta' : '#eta(H2)', 
          'fatJet3Eta' : '#eta(H3)', 

          'fatJet1Phi' : '#phi(H1)', 
          'fatJet2Phi' : '#phi(H2)', 
          'fatJet3Phi' : '#phi(H3)', 

          'fatJet1PNetXbb' : 'PNet Xbb(H1)', 
          'fatJet2PNetXbb' : 'PNet Xbb(H2)', 
          'fatJet3PNetXbb' : 'PNet Xbb(H3)', 

          'fatJet1PNetXjj' : 'PNet Xjj(H1)', 
          'fatJet2PNetXjj' : 'PNet Xjj(H2)', 
          'fatJet3PNetXjj' : 'PNet Xjj(H3)', 

          'fatJet1PNetQCD' : 'PNet QCD(H1)', 
          'fatJet2PNetQCD' : 'PNet QCD(H2)', 
          'fatJet3PNetQCD' : 'PNet QCD(H3)', 

          'hhh_resolved_mass': 'm(HHH)',
          'hhh_resolved_pt': 'p_{T}(HHH)',

          'hhh_mass': 'm(HHH)',
          'hhh_pt': 'p_{T}(HHH)',

          'nfatjets' : 'N fat-jets',
          'nbtags' : 'N b-tags',

        }

binnings = {
          'h1_mass' : '(30,0,300)', 
          'h2_mass' : '(30,0,300)', 
          'h3_mass' : '(30,0,300)', 

          'h1_pt' : '(50,0,500)', 
          'h2_pt' : '(50,0,500)', 
          'h3_pt' : '(50,0,500)', 

          'h1_eta' : '(50,-5,5)', 
          'h2_eta' : '(50,-5,5)', 
          'h3_eta' : '(50,-5,5)', 

          'h1_phi' : '(60,-3.2,3.2)', 
          'h2_phi' : '(60,-3.2,3.2)', 
          'h3_phi' : '(60,-3.2,3.2)', 

          'fatJet1Mass' : '(30,0,300)', 
          'fatJet2Mass' : '(30,0,300)', 
          'fatJet3Mass' : '(30,0,300)', 

          'fatJet1Pt' : '(85,150,1000)', 
          'fatJet2Pt' : '(85,150,1000)', 
          'fatJet3Pt' : '(85,150,1000)', 

          'fatJet1Eta' : '(50,-5,5)', 
          'fatJet2Eta' : '(50,-5,5)', 
          'fatJet3Eta' : '(50,-5,5)', 

          'fatJet1Phi' : '(60,-3.2,3.2)', 
          'fatJet2Phi' : '(60,-3.2,3.2)', 
          'fatJet3Phi' : '(60,-3.2,3.2)', 

          'fatJet1PNetXbb' : '(20,0,1)', 
          'fatJet2PNetXbb' : '(20,0,1)', 
          'fatJet3PNetXbb' : '(20,0,1)', 

          'fatJet1PNetXjj' : '(20,0,1)', 
          'fatJet2PNetXjj' : '(20,0,1)', 
          'fatJet3PNetXjj' : '(20,0,1)', 

          'fatJet1PNetQCD' : '(20,0,1)', 
          'fatJet2PNetQCD' : '(20,0,1)', 
          'fatJet3PNetQCD' : '(20,0,1)', 

          'hhh_resolved_mass': '(80,0,1600)',
          'hhh_resolved_pt': '(80,0,800)',

          'hhh_mass': '(155,400,3500)',
          'hhh_pt': '(80,0,800)',
 
          'nfatjets' : '(5,0,5)',
          'nbtags' : '(10,0,10)',

          'JetFlavComp': '(10,0,10)', 

        }

cuts = {'resolved' : ROOT.TCut('nbtags == 6 && nfatjets == 0 && nbtags > 4'),
        'boosted'  : ROOT.TCut('nfatjets == 3 && nbtags > 4'),
        }


cuts_fatjets = {'nFJ0' : ROOT.TCut("nfatjets == 0"), 
                'nFJ1' : ROOT.TCut("nfatjets == 1"),
                'nFJ2' : ROOT.TCut("nfatjets == 2"),
                'nFJ3' : ROOT.TCut("nfatjets == 3"), 
        }

iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12

iPeriod = 0

eos_plots = 'plots_samples-vSignalStudy-nanoaod'

if not os.path.isdir(eos_plots):
    os.mkdir(eos_plots)

f_in = 'QCD.root'

path = 'samples/'

lumi = 41480.0

for f_in in ['GluGluToHHHTo6B_SM']:


    tree = ROOT.TChain('Events')
    tree.AddFile(path + '/' + f_in + '.root')


    for fj in cuts_fatjets:
        cut = cuts_fatjets[fj]
        cutWeight = ROOT.TCut('(%f * weight * xsecWeight * l1PreFiringWeight * puWeight * genWeight)'%(lumi))
        cutHLT = ROOT.TCut("(HLT_PFJet450 || HLT_PFJet500 || HLT_PFHT1050 || HLT_AK8PFJet550 || HLT_AK8PFJet360_TrimMass30 || HLT_AK8PFJet380_TrimMass30 || HLT_AK8PFJet400_TrimMass30 || HLT_AK8PFHT800_TrimMass50 || HLT_AK8PFHT750_TrimMass50 || HLT_AK8PFJet330_PFAK8BTagCSV_p17 || HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0)")

        cut_jet = ROOT.TCut('jet1Pt > 20 && jet1Eta < 2.5 && jet1Eta > -2.5')
        for i in range(2,11):
            cut_jet += ROOT.TCut('jet%dPt > 20 && jet%dEta < 2.5 && jet%dEta > -2.5'%(i,i,i))

        cuts_common = cut + cutHLT + cut_jet

        var = 'JetFlavComp'
        name = 'hist_%s'%var
        h = ROOT.THStack()
        h_b = ROOT.TH1F(var+'_b',var+'_b',11,0,11)
        h_c = ROOT.TH1F(var+'_c',var+'_c',11,0,11)
        h_l = ROOT.TH1F(var+'_l',var+'_l',11,0,11)

        i = 1

        for i in range(1,11):

            total = float(tree.GetEntries(((cuts_common)*cutWeight).GetTitle()))

            cut_jet_b = ROOT.TCut('jet%dHadronFlavour == 5 '%i)
            bjets = tree.GetEntries(((cuts_common + cut_jet_b)*cutWeight).GetTitle())
            h_b.SetBinContent(i+1,bjets / total * 100)

            cut_jet_c = ROOT.TCut('jet%dHadronFlavour == 4 '%i)
            cjets = tree.GetEntries(((cuts_common + cut_jet_c)*cutWeight).GetTitle())
            h_c.SetBinContent(i+1,cjets / total * 100)

            cut_jet_l = ROOT.TCut('jet%dHadronFlavour == 0 '%i)
            ljets = tree.GetEntries(((cuts_common + cut_jet_l)*cutWeight).GetTitle())
            h_l.SetBinContent(i+1,ljets / total * 100)


        h_b.GetXaxis().SetTitle('Jets ordered by pT')
        h_b.GetYaxis().SetTitle('Percentage of total events')

        h_b.SetFillColor(ROOT.kRed + 1)
        h_c.SetFillColor(ROOT.kGreen + 2)
        h_l.SetFillColor(ROOT.kBlue + 2)

        h_b.SetMarkerSize(0)
        h_c.SetMarkerSize(0)
        h_l.SetMarkerSize(0)


        legend = ROOT.TLegend(0.6,0.6,0.9,0.9)
        legend.SetBorderSize(0)
        legend.AddEntry(h_b, 'b-jets')
        legend.AddEntry(h_c, 'c-jets')
        legend.AddEntry(h_l, 'light-jets')

        h.Add(h_b)
        h.Add(h_c)
        h.Add(h_l)

        h.SetMaximum(h.GetMaximum()*1.8)

        c = ROOT.TCanvas()
        h.Draw("hist")
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)
        legend.Draw()
        c.cd()
        c.Update()
        c.RedrawAxis()
        c.Print(eos_plots + '/' + f_in.replace('.root','_') + '_%s'%fj + '.pdf')


