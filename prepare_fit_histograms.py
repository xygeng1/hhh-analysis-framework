# Script to prepare fit histograms for SR and CR

import os, ROOT

#categories = ['gt5bloose_0PFfat','1PNfatLoose','gt1PNfatLoose']
#categories = ['1PNfatMedium','1PNfatTight','gt1PNfatMedium','gt1PNfatTight']
#categories = ['1PFfat_cat1','1PFfat_cat2','1PFfat_cat3','1PFfat_cat4','gt1PFfat_cat1','gt1PFfat_cat2','gt1PFfat_cat3','gt1PFfat_cat4']
#categories = ['1PFfat_cat1','1PFfat_cat2','1PFfat_cat3','1PFfat_cat4','gt1PFfat_cat1','gt1PFfat_cat2','gt1PFfat_cat3','gt1PFfat_cat4']

#categories = ['gt0PFfat','gt0PFfat_PNetTight']
categories = ['1PFfat_cat1','1PFfat_cat2','1PFfat_cat3','gt1PFfat_cat1','gt1PFfat_cat2','gt1PFfat_cat3','gt0PFfat','gt0PFfat_PNetTight']
#categories = ['1PFfat_cat2','1PFfat_cat3','1PFfat_cat1']
#categories = ['gt1PFfat_cat1','gt1PFfat_cat2','gt1PFfat_cat3']

#regions = ['SR','CR']
regions = ['SR']

variables = ['fatJet1Mass']

for region in regions:
    for cat in categories:
        for var in variables:
            #cmd = 'python skimm_tree.py --category %s --do_%s --do_limit_input %s --skip_do_trees --skip_do_plots'%(cat,region,var)
            cmd = 'python3 skimm_tree.py --category %s --do_%s --do_limit_input %s --skip_do_trees'%(cat,region,var)
            print(cmd)
            os.system(cmd)
