# Script to store methods to compute truth tagging weigths

import os,ROOT


path_tt = '/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_12_5_2/src/eff-maps/mcEff/'

def tt_init(year, f_in):
    ttDir = path_tt + '%s_%s.root'%(f_in,year)
    ROOT.gInterpreter.Declare('TFile* tt_weight = new TFile("%s");'%ttDir)
    ROOT.gInterpreter.Declare(''' 

            auto h_b_loose = (TH2D*) tt_weight->Get("eff_b_loose");
            auto h_b_medium = (TH2D*) tt_weight->Get("eff_b_medium");
            auto h_b_tight = (TH2D*) tt_weight->Get("eff_b_tight");
            
            auto h_c_loose = (TH2D*) tt_weight->Get("eff_c_loose");
            auto h_c_medium = (TH2D*) tt_weight->Get("eff_c_medium");
            auto h_c_tight = (TH2D*) tt_weight->Get("eff_c_tight");

            auto h_l_loose = (TH2D*) tt_weight->Get("eff_l_loose");
            auto h_l_medium = (TH2D*) tt_weight->Get("eff_l_medium");
            auto h_l_tight = (TH2D*) tt_weight->Get("eff_l_tight");
  
            ''')


computeLooseTTWeight = '''
    float computeLooseTTWeight(int hadronFlavour, float eta, float pt){
        float sf;
        if (hadronFlavour == 5) { 
            //auto h = (TH2D*) tt_weight->Get("eff_b_loose"); 
            sf = h_b_loose->GetBinContent(h_b_loose->FindBin(pt,eta)); 
        }
        else if (hadronFlavour == 4) {
            //auto h = (TH2D*) tt_weight->Get("eff_c_loose");
            sf = h_c_loose->GetBinContent(h_c_loose->FindBin(pt,eta));  
        }
        else if (hadronFlavour == 0) {
            //auto h = (TH2D*) tt_weight->Get("eff_l_loose");
            sf = h_l_loose->GetBinContent(h_l_loose->FindBin(pt,eta)); 
        }
        return sf; 
    }
'''

computeMediumTTWeight = '''
    float computeMediumTTWeight(int hadronFlavour, float eta, float pt){
        float sf;
        if (hadronFlavour == 5) { 
            //auto h = (TH2D*) tt_weight->Get("eff_b_medium"); 
            sf = h_b_medium->GetBinContent(h_b_medium->FindBin(pt,eta)); 
        }
        else if (hadronFlavour == 4) {
            //auto h = (TH2D*) tt_weight->Get("eff_c_medium");
            sf = h_c_medium->GetBinContent(h_c_medium->FindBin(pt,eta));  
        }
        else if (hadronFlavour == 0) {
            //auto h = (TH2D*) tt_weight->Get("eff_l_medium");
            sf = h_l_medium->GetBinContent(h_l_medium->FindBin(pt,eta)); 
        }
        return sf; 
    }
'''

computeTightTTWeight = '''
    float computeTightTTWeight(int hadronFlavour, float eta, float pt){
        float sf;
        if (hadronFlavour == 5) { 
            //auto h = (TH2D*) tt_weight->Get("eff_b_tight"); 
            sf = h_b_tight->GetBinContent(h_b_tight->FindBin(pt,eta)); 
        }
        else if (hadronFlavour == 4) {
            //auto h = (TH2D*) tt_weight->Get("eff_c_tight");
            sf = h_c_tight->GetBinContent(h_c_tight->FindBin(pt,eta));  
        }
        else if (hadronFlavour == 0) {
            //auto h = (TH2D*) tt_weight->Get("eff_l_tight");
            sf = h_l_tight->GetBinContent(h_l_tight->FindBin(pt,eta)); 
        }
        return sf; 
    }
'''





def addTTWeight(df,f_in,wp):
    if 'JetHT' in f_in or 'BTagCSV' in f_in:
        if wp == 'loose':
            df = df.Define('bcand1LooseTTWeight', '1')
            df = df.Define('bcand2LooseTTWeight', '1')
            df = df.Define('bcand3LooseTTWeight', '1')
            df = df.Define('bcand4LooseTTWeight', '1')
            df = df.Define('bcand5LooseTTWeight', '1')
            df = df.Define('bcand6LooseTTWeight', '1')
        elif wp == 'medium':
            df = df.Define('bcand1MediumTTWeight', '1')
            df = df.Define('bcand2MediumTTWeight', '1')
            df = df.Define('bcand3MediumTTWeight', '1')
            df = df.Define('bcand4MediumTTWeight', '1')
            df = df.Define('bcand5MediumTTWeight', '1')
            df = df.Define('bcand6MediumTTWeight', '1')
        elif wp == 'tight':
            df = df.Define('bcand1TightTTWeight', '1')
            df = df.Define('bcand2TightTTWeight', '1')
            df = df.Define('bcand3TightTTWeight', '1')
            df = df.Define('bcand4TightTTWeight', '1')
            df = df.Define('bcand5TightTTWeight', '1')
            df = df.Define('bcand6TightTTWeight', '1')
    else: 
        '''
        l_1 = ROOT.std.vector['std::string']()
        l_1.push_back('rdfslot_')
        l_1.push_back('bcand1HadronFlavour')
        l_1.push_back('bcand1Eta')
        l_1.push_back('bcand1Pt')

        l_2 = ROOT.std.vector['std::string']()
        l_2.push_back('int(round(bcand2HadronFlavour))')
        l_2.push_back('std::abs(bcand2Eta)')
        l_2.push_back('bcand2Pt')

        l_3 = ROOT.std.vector['std::string']()
        l_3.push_back('int(round(bcand3HadronFlavour))')
        l_3.push_back('std::abs(bcand3Eta)')
        l_3.push_back('bcand3Pt')

        l_4 = ROOT.std.vector['std::string']()
        l_4.push_back('int(round(bcand4HadronFlavour))')
        l_4.push_back('std::abs(bcand4Eta)')
        l_4.push_back('bcand4Pt')

        l_5 = ROOT.std.vector['std::string']()
        l_5.push_back('int(round(bcand5HadronFlavour))')
        l_5.push_back('std::abs(bcand5Eta)')
        l_5.push_back('bcand5Pt')

        l_6 = ROOT.std.vector['std::string']()
        l_6.push_back('int(round(bcand6HadronFlavour))')
        l_6.push_back('std::abs(bcand6Eta)')
        l_6.push_back('bcand6Pt')
        '''
        if wp == 'loose':
            ROOT.gInterpreter.Declare(computeLooseTTWeight)
            name = 'LooseTTWeight'
            script = 'computeLooseTTWeight'
            
            '''df = df.DefineSlot('bcand1%s'%name, ROOT.computeLooseTTWeight ,l_1)
            df = df.DefineSlot('bcand2%s'%name, ROOT.computeLooseTTWeight ,l_2)
            df = df.DefineSlot('bcand3%s'%name, ROOT.computeLooseTTWeight ,l_3)
            df = df.DefineSlot('bcand4%s'%name, ROOT.computeLooseTTWeight ,l_4)
            df = df.DefineSlot('bcand5%s'%name, ROOT.computeLooseTTWeight ,l_5)
            df = df.DefineSlot('bcand6%s'%name, ROOT.computeLooseTTWeight ,l_6)'''


        elif wp == 'medium':
            ROOT.gInterpreter.Declare(computeMediumTTWeight)
            name = 'MediumTTWeight'
            script = 'computeMediumTTWeight'

            '''df = df.DefineSlot('bcand1%s'%name, ROOT.computeMediumTTWeight ,l_1)
            df = df.DefineSlot('bcand2%s'%name, ROOT.computeMediumTTWeight ,l_2)
            df = df.DefineSlot('bcand3%s'%name, ROOT.computeMediumTTWeight ,l_3)
            df = df.DefineSlot('bcand4%s'%name, ROOT.computeMediumTTWeight ,l_4)
            df = df.DefineSlot('bcand5%s'%name, ROOT.computeMediumTTWeight ,l_5)
            df = df.DefineSlot('bcand6%s'%name, ROOT.computeMediumTTWeight ,l_6)'''


        elif wp == 'tight':
            ROOT.gInterpreter.Declare(computeTightTTWeight)
            name = 'TightTTWeight'
            script = 'computeTightTTWeight'

            '''df = df.DefineSlot('bcand1%s'%name, ROOT.computeTightTTWeight ,l_1)
            df = df.DefineSlot('bcand2%s'%name, ROOT.computeTightTTWeight ,l_2)
            df = df.DefineSlot('bcand3%s'%name, ROOT.computeTightTTWeight ,l_3)
            df = df.DefineSlot('bcand4%s'%name, ROOT.computeTightTTWeight ,l_4)
            df = df.DefineSlot('bcand5%s'%name, ROOT.computeTightTTWeight ,l_5)
            df = df.DefineSlot('bcand6%s'%name, ROOT.computeTightTTWeight ,l_6)'''

        df = df.Define('bcand1%s'%name, "%s(int(round(bcand1HadronFlavour)),std::abs(bcand1Eta),bcand1Pt)"%script)
        df = df.Define('bcand2%s'%name, "%s(int(round(bcand2HadronFlavour)),std::abs(bcand2Eta),bcand2Pt)"%script)
        df = df.Define('bcand3%s'%name, "%s(int(round(bcand3HadronFlavour)),std::abs(bcand3Eta),bcand3Pt)"%script)
        df = df.Define('bcand4%s'%name, "%s(int(round(bcand4HadronFlavour)),std::abs(bcand4Eta),bcand4Pt)"%script)
        df = df.Define('bcand5%s'%name, "%s(int(round(bcand5HadronFlavour)),std::abs(bcand5Eta),bcand5Pt)"%script)
        df = df.Define('bcand6%s'%name, "%s(int(round(bcand6HadronFlavour)),std::abs(bcand6Eta),bcand6Pt)"%script)


    return df



