# Utility to add calibrations
# git clone ssh://git@gitlab.cern.ch:7999/cms-nanoAOD/jsonpog-integration.git

import ROOT
import correctionlib
correctionlib.register_pyroot_binding()

def btag_init(year):
    sfDir = '/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_12_5_2/src/jsonpog-integration/POG/BTV/%s_UL/btagging.json.gz'%year
    ROOT.gInterpreter.Declare('auto btvjson = correction::CorrectionSet::from_file("%s");'%sfDir)
    ROOT.gInterpreter.Declare('auto btvjson_shape = btvjson->at("deepJet_shape");')
    ROOT.gInterpreter.Declare('auto btvjson_comb = btvjson->at("deepJet_comb");') # bc
    ROOT.gInterpreter.Declare('auto btvjson_incl = btvjson->at("deepJet_incl");') # light



def addBTagSF(df, f_in): # shape scale factors for MVA
    if 'JetHT' in f_in or 'BTagCSV' in f_in:
        df = df.Define('bcand1BTagSF', '1')
        df = df.Define('bcand2BTagSF', '1')
        df = df.Define('bcand3BTagSF', '1')
        df = df.Define('bcand4BTagSF', '1')
        df = df.Define('bcand5BTagSF', '1')
        df = df.Define('bcand6BTagSF', '1')
        df = df.Define('jet7BTagSF', '1')
        df = df.Define('jet8BTagSF', '1')
        df = df.Define('jet9BTagSF', '1')
        df = df.Define('jet10BTagSF', '1')
    else:
        df = df.Define('bcand1BTagSF', 'btvjson_shape->evaluate({"central",int(round(bcand1HadronFlavour)),std::abs(bcand1Eta),bcand1Pt,bcand1DeepFlavB})')
        df = df.Define('bcand2BTagSF', 'btvjson_shape->evaluate({"central",int(round(bcand2HadronFlavour)),std::abs(bcand2Eta),bcand2Pt,bcand2DeepFlavB})')
        df = df.Define('bcand3BTagSF', 'btvjson_shape->evaluate({"central",int(round(bcand3HadronFlavour)),std::abs(bcand3Eta),bcand3Pt,bcand3DeepFlavB})')
        df = df.Define('bcand4BTagSF', 'btvjson_shape->evaluate({"central",int(round(bcand4HadronFlavour)),std::abs(bcand4Eta),bcand4Pt,bcand4DeepFlavB})')
        df = df.Define('bcand5BTagSF', 'btvjson_shape->evaluate({"central",int(round(bcand5HadronFlavour)),std::abs(bcand5Eta),bcand5Pt,bcand5DeepFlavB})')
        df = df.Define('bcand6BTagSF', 'btvjson_shape->evaluate({"central",int(round(bcand6HadronFlavour)),std::abs(bcand6Eta),bcand6Pt,bcand6DeepFlavB})')
        df = df.Define('jet7BTagSF', 'btvjson_shape->evaluate({"central",int(round(jet7HadronFlavour)),std::abs(jet7Eta),jet7Pt,jet7DeepFlavB})')
        df = df.Define('jet8BTagSF', 'btvjson_shape->evaluate({"central",int(round(jet8HadronFlavour)),std::abs(jet8Eta),jet8Pt,jet8DeepFlavB})')
        df = df.Define('jet9BTagSF', 'btvjson_shape->evaluate({"central",int(round(jet9HadronFlavour)),std::abs(jet9Eta),jet9Pt,jet9DeepFlavB})')
        df = df.Define('jet10BTagSF', 'btvjson_shape->evaluate({"central",int(round(jet10HadronFlavour)),std::abs(jet10Eta),jet10Pt,jet10DeepFlavB})')

    return df


computeLooseBTAGSF = '''
    float computeLooseBTagsEffSFPerFlavour(int hadronFlavour, float eta, float pt){
        float sf;
        if (hadronFlavour == 0) { sf = btvjson_incl->evaluate({"central","L",hadronFlavour,eta,pt});  }
        else { sf = btvjson_comb->evaluate({"central","L",hadronFlavour,eta,pt});} 
        return sf;
    }
'''

computeMediumBTAGSF = '''
    float computeMediumBTagsEffSFPerFlavour(int hadronFlavour, float eta, float pt){
        float sf;
        if (hadronFlavour == 0) { sf = btvjson_incl->evaluate({"central","M",hadronFlavour,eta,pt});  }
        else {sf = btvjson_comb->evaluate({"central","M",hadronFlavour,eta,pt});} 
        return sf;
    }
'''

computeTightBTAGSF = '''
    float computeTightBTagsEffSFPerFlavour(int hadronFlavour, float eta, float pt){
        float sf;
        if (hadronFlavour == 0) { sf = btvjson_incl->evaluate({"central","T",hadronFlavour,eta,pt});  }
        else {sf = btvjson_comb->evaluate({"central","T",hadronFlavour,eta,pt});} 
        return sf;
    }
'''



def addBTagEffSF(df,f_in,wp):

    if 'JetHT' in f_in or 'BTagCSV' in f_in:
        if wp == 'loose':
            df = df.Define('bcand1LooseBTagEffSF', '1')
            df = df.Define('bcand2LooseBTagEffSF', '1')
            df = df.Define('bcand3LooseBTagEffSF', '1')
            df = df.Define('bcand4LooseBTagEffSF', '1')
            df = df.Define('bcand5LooseBTagEffSF', '1')
            df = df.Define('bcand6LooseBTagEffSF', '1')
        elif wp == 'medium':
            df = df.Define('bcand1MediumBTagEffSF', '1')
            df = df.Define('bcand2MediumBTagEffSF', '1')
            df = df.Define('bcand3MediumBTagEffSF', '1')
            df = df.Define('bcand4MediumBTagEffSF', '1')
            df = df.Define('bcand5MediumBTagEffSF', '1')
            df = df.Define('bcand6MediumBTagEffSF', '1')
        elif wp == 'tight':
            df = df.Define('bcand1TightBTagEffSF', '1')
            df = df.Define('bcand2TightBTagEffSF', '1')
            df = df.Define('bcand3TightBTagEffSF', '1')
            df = df.Define('bcand4TightBTagEffSF', '1')
            df = df.Define('bcand5TightBTagEffSF', '1')
            df = df.Define('bcand6TightBTagEffSF', '1')
    else: 
        if wp == 'loose':
            ROOT.gInterpreter.Declare(computeLooseBTAGSF)
            name = 'LooseBTagEffSF'
            script = 'computeLooseBTagsEffSFPerFlavour'
        elif wp == 'medium':
            ROOT.gInterpreter.Declare(computeMediumBTAGSF)
            name = 'MediumBTagEffSF'
            script = 'computeMediumBTagsEffSFPerFlavour'
        elif wp == 'tight':
            ROOT.gInterpreter.Declare(computeTightBTAGSF)
            name = 'TightBTagEffSF'
            script = 'computeTightBTagsEffSFPerFlavour'
        df = df.Define('bcand1%s'%name, "%s(int(round(bcand1HadronFlavour)),std::abs(bcand1Eta),bcand1Pt)"%script)
        df = df.Define('bcand2%s'%name, "%s(int(round(bcand2HadronFlavour)),std::abs(bcand2Eta),bcand2Pt)"%script)
        df = df.Define('bcand3%s'%name, "%s(int(round(bcand3HadronFlavour)),std::abs(bcand3Eta),bcand3Pt)"%script)
        df = df.Define('bcand4%s'%name, "%s(int(round(bcand4HadronFlavour)),std::abs(bcand4Eta),bcand4Pt)"%script)
        df = df.Define('bcand5%s'%name, "%s(int(round(bcand5HadronFlavour)),std::abs(bcand5Eta),bcand5Pt)"%script)
        df = df.Define('bcand6%s'%name, "%s(int(round(bcand6HadronFlavour)),std::abs(bcand6Eta),bcand6Pt)"%script)
    return df



