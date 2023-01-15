# HHH analysis framework
Framework to perform HHH analysis, run MVA tree inputs, histograms, apply calibrations and BDT evaluation and produce maps.

# Getting started
Requires CMSSW with python3 enabled.

```
cmsrel CMSSW_12_5_2
cd CMSSW_12_5_2/src
cmsenv
```

Then, get the repository:
```
git clone git@github.com:mstamenk/hhh-analysis-framework.git
cd hhh-analysis-framework
source setup.sh
```

Then every time in a new shell:
```
cd hhh-analysis-framework
source setup.sh
```

# Installing additional softwares
Need for calibrations:
```
git clone ssh://git@gitlab.cern.ch:7999/cms-nanoAOD/jsonpog-integration.git
```




