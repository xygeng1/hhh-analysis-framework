# Script to build the TH2D with the tagging efficiencies
import os, ROOT

year = '2017'

f_in = 'QCD'

for year in ['2016APV','2016','2017','2018']:
    for f_in in ['GluGluToHHHTo6B_SM','QCD', 'QCD_bEnriched','TT','WJetsToQQ','WWTo4Q','WWW','WWZ','WZZ','ZJetsToQQ','ZZTo4Q','ZZZ']:
        f = ROOT.TFile(year + '/' + 'EffMap_%s.root'%f_in)

        f_out = ROOT.TFile('mcEff'+ '/' + '%s_%s.root'%(f_in,year),'recreate')


        h_b = f.Get('jet1_b')
        h_b_loose = f.Get('jet1_b_loose')
        h_b_medium = f.Get('jet1_b_medium')
        h_b_tight = f.Get('jet1_b_tight')

        h_c = f.Get('jet1_c')
        h_c_loose = f.Get('jet1_c_loose')
        h_c_medium = f.Get('jet1_c_medium')
        h_c_tight = f.Get('jet1_c_tight')

        h_l = f.Get('jet1_l')
        h_l_loose = f.Get('jet1_l_loose')
        h_l_medium = f.Get('jet1_l_medium')
        h_l_tight = f.Get('jet1_l_tight')


        for j in ['jet2','jet3','jet4','jet5','jet6','jet7','jet8','jet9','jet10']:
            
            h_tmp_b = f.Get('%s_b'%j)
            h_tmp_b_loose = f.Get('%s_b_loose'%j)
            h_tmp_b_medium = f.Get('%s_b_medium'%j)
            h_tmp_b_tight = f.Get('%s_b_tight'%j)

            h_tmp_c = f.Get('%s_c'%j)
            h_tmp_c_loose = f.Get('%s_c_loose'%j)
            h_tmp_c_medium = f.Get('%s_c_medium'%j)
            h_tmp_c_tight = f.Get('%s_c_tight'%j)

            h_tmp_l = f.Get('%s_l'%j)
            h_tmp_l_loose = f.Get('%s_l_loose'%j)
            h_tmp_l_medium = f.Get('%s_l_medium'%j)
            h_tmp_l_tight = f.Get('%s_l_tight'%j)

            h_b.Add(h_tmp_b)
            h_b_loose.Add(h_tmp_b_loose)
            h_b_medium.Add(h_tmp_b_medium)
            h_b_tight.Add(h_tmp_b_tight)

            h_c.Add(h_tmp_c)
            h_c_loose.Add(h_tmp_c_loose)
            h_c_medium.Add(h_tmp_c_medium)
            h_c_tight.Add(h_tmp_c_tight)

            h_l.Add(h_tmp_l)
            h_l_loose.Add(h_tmp_l_loose)
            h_l_medium.Add(h_tmp_l_medium)
            h_l_tight.Add(h_tmp_l_tight)


        eff_b_loose = h_b_loose.Clone('eff_b_loose')
        eff_b_medium = h_b_medium.Clone('eff_b_medium')
        eff_b_tight = h_b_tight.Clone('eff_b_tight')

        eff_c_loose = h_c_loose.Clone('eff_c_loose')
        eff_c_medium = h_c_medium.Clone('eff_c_medium')
        eff_c_tight = h_c_tight.Clone('eff_c_tight')

        eff_l_loose = h_l_loose.Clone('eff_l_loose')
        eff_l_medium = h_l_medium.Clone('eff_l_medium')
        eff_l_tight = h_l_tight.Clone('eff_l_tight')

        eff_b_loose.Divide(h_b)
        eff_b_medium.Divide(h_b)
        eff_b_tight.Divide(h_b)

        eff_c_loose.Divide(h_c)
        eff_c_medium.Divide(h_c)
        eff_c_tight.Divide(h_c)

        eff_l_loose.Divide(h_l)
        eff_l_medium.Divide(h_l)
        eff_l_tight.Divide(h_l)

        f_out.cd()
        eff_b_loose.Write()
        eff_b_medium.Write()
        eff_b_tight.Write()

        eff_c_loose.Write()
        eff_c_medium.Write()
        eff_c_tight.Write()

        eff_l_loose.Write()
        eff_l_medium.Write()
        eff_l_tight.Write()

        f_out.Close()



