# Scritp to prepare jobs for plotting with make_histograms_rdataframe.py

import os 

#years = ['2016APV','2016','2017','2018']
years = ['run2']
nT = [str(200 * x + 200) for x in range(3)]
mD = [str(x + 2) for x in range(2)]
nC = [str(50 *x + 50) for x in range(5)]
minNS = [str(2*x + 1) for x in range(15)]
aBB = [str(0.2*x + 0.2) for x in range(5)]

current_path = '/isilon/data/users/mstamenk/hhh-6b-producer/master/CMSSW_12_5_2/src/hhh-master/hhh-analysis-framework/bdt-framework/'
script = current_path + '/' + 'train_bdt_resolved.py'

pwd = current_path + '/' + 'condor-run-resolved/'

jobs_path = 'jobs'



job_cmd = '#! /bin/bash\nsource /cvmfs/cms.cern.ch/cmsset_default.sh\ncmsrel CMSSW_12_5_2\ncd CMSSW_12_5_2/src\ncmsenv\nulimit -s unlimited\nexport PYTHONPATH=$PYTHONPATH:/isilon/data/users/mstamenk/hhh-6b-producer/master/CMSSW_12_5_2/src/hhh-master/hhh-analysis-framework/ \n%s'
submit="Universe   = vanilla\nrequest_memory = 7900\nExecutable = %s\nArguments  = $(ClusterId) $(ProcId)\nLog        = log/job.$(ClusterId).$(ProcId).log\nOutput     = output_%s/job.$(ClusterId).$(ProcId).out\nError      = error/job.$(ClusterId).$(ProcId).error\nQueue 1"
#job_cmd = '%s'


submit_all = 'submit_all.sh'
manual_all = 'manual_run_all.sh'

train = 'regular'

jobs = []
manual_jobs = []
for year in years:
    for tree in nT:
        for depth in mD:
            for cut in nC:
                for minNodeSize in minNS:
                    for adaBoostBeta in aBB:
                        filename = 'job_%s_%s_%s_%s_%s_%s_%s.sh'%(year,tree,depth,cut,minNodeSize,adaBoostBeta, train)
                        if 'regular' in train:
                            cmd = 'python3 %s --year %s --nTrees %s --maxDepth %s --nCuts %s --minNodeSize %s --adaBoostBeta %s --category nAK8_0_failLoose --region inclusive'%(script,year,tree,depth,cut,minNodeSize,adaBoostBeta)
                        else:
                            cmd = 'python3 %s --year %s --nTrees %s --maxDepth %s --nCuts %s --minNodeSize %s --adaBoostBeta %s --invertTrainTest --category nAK8_0_failLoose --region inclusive'%(script,year,tree,depth,cut,minNodeSize,adaBoostBeta)


                        print("Writing %s"%filename)
                        with open(jobs_path + '/' + filename, 'w') as f:
                            f.write(job_cmd%cmd)
                        manual_jobs.append(filename)

                        submit_file = 'submit_%s_%s_%s_%s_%s_%s_%s'%(year,tree,depth,cut,minNodeSize,adaBoostBeta,train)
                        print('Writing %s/%s'%(jobs_path, submit_file))
                        with open(jobs_path + '/' + submit_file, 'w') as f:
                            f.write(submit%(jobs_path+'/'+filename,'%s_%s'%(year,train)))
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
                        
