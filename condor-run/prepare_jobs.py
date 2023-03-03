# Scritp to prepare jobs for plotting with make_histograms_rdataframe.py

import os 

#categories = ['gt1PFfat_cat1','gt1PFfat_cat2','gt1PFfat_cat3','1PFfat_cat1','1PFfat_cat2','1PFfat_cat3','gt0PFfat','gt0PFfat_PNetTight']
categories = ['gt0PFfat_cat1','gt0PFfat_cat2','gt0PFfat_cat3']


regions = ['SR']
files = ["ZZZ", "WZZ", "WWZ", "WWW", "ZZTo4Q", "WWTo4Q", "ZJetsToQQ", "WJetsToQQ", "TTToHadronic","TTo2L2Nu","TTToSemiLeptonic", "QCD", "QCD6B", "data_obs" , "GluGluToHHHTo6B_SM"]
#files = ['data_obs']

current_path = '/isilon/data/users/mstamenk/hhh-6b-producer/master/CMSSW_12_5_2/src/hhh-master/hhh-analysis-framework/'
script = current_path + '/' + 'skimm_tree.py'

pwd = current_path + '/' + 'condor-run/'
jobs_path = 'jobs'

submit="Universe   = vanilla\nrequest_memory = 7900\nExecutable = %s\nArguments  = $(ClusterId) $(ProcId)\nLog        = log/job_%s_%s_%s.log\nOutput     = output/job_%s_%s_%s.out\nError      = error/job_%s_%s_%s.error\nQueue 1"
job_cmd = '#! /bin/bash\nsource /cvmfs/cms.cern.ch/cmsset_default.sh\ncmsrel CMSSW_12_5_2\ncd CMSSW_12_5_2/src\ncmsenv\nulimit -s unlimited\nexport MYROOT=$(pwd)\nexport PYTHONPATH=$PYTHONPATH:$MYROOT \n%s'
#job_cmd = '%s'


submit_all = 'submit_all.sh'
manual_all = 'manual_run_all.sh'

jobs = []
manual_jobs = []
#for year in ['2016','2016APV','2017','2018']:

for category in categories:
    for region in regions:
        for f_in in files:
            filename = 'job_%s_%s_%s.sh'%(f_in,region,category)
            cmd = 'python3 %s --process %s --do_%s --category %s --skip_do_plots --skip_do_histograms '%(script,f_in,region,category)

            print("Writing %s"%filename)
            with open(jobs_path + '/' + filename, 'w') as f:
                f.write(job_cmd%cmd)
            manual_jobs.append(filename)

            submit_file = 'submit_%s_%s_%s'%(f_in,region,category)
            print('Writing %s/%s'%(jobs_path, submit_file))
            with open(jobs_path + '/' + submit_file, 'w') as f:
                f.write(submit%(jobs_path+'/'+filename,f_in,category,region,f_in,category,region,f_in,category,region))
            jobs.append(submit_file)

cmd = '#!/bin/bash\n'
for j in jobs:
    cmd += 'condor_submit %s/%s \n'%(jobs_path, j)


with open(submit_all, 'w') as f:
    f.write(cmd)


cmd = '#!/bin/bash\n'
for f in manual_jobs:
    cmd += 'source %s/%s/%s\n'%(pwd,jobs_path,f)

with open(manual_all,'w') as f:
    f.write(cmd)
                        
