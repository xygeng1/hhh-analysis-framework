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

# Necessary step: producing efficiency maps
Efficiency maps are necessary to create truth tagging, and to use b-tagging calibrations in the case of jets failing the b-tagging requirement. The maps need to be produced.
```
cd eff-maps
python compute_efficiency_maps.py # need to modify line 26 where path = '' is defined to use the nanoaod samples
python build_map.py
```

# Alternative getting started

Instead of CMSSW you can also just pick up python and RDataframes in lxplus8 with

```
source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_102 x86_64-centos7-gcc11-opt
```



# Running the framework

## Doing trees with baseline selection from nanoAOD (trigger and basic pt cuts)

@Marko, please add how you do the inclusive (with an explicit example of the options)

```
cd hhh-analysis-framework
python make_histograms_rdataframe_selection.py # see options
```

## Scripts to b-tag and fat-jet categorization

With the script bellow we redefine a couple of variables and construct trees, histograms and data/MC plots to different categories

- several btag and fat jet categories selections are implemented. There is also an option to make the results with SR/CR separation

- read the script [here](https://github.com/mstamenk/hhh-analysis-framework/blob/main/skimm_tree.py#L53) for the category implemented_category options. Implemented more as needed (eg PN categorization in boosted categories)

```
python3 skimm_tree.py --category implemented_category --base_folder /eos/user/m/mstamenk/CxAOD31run/hhh-6b/v25/2017/baseline
```

- The histograms options are [here]().
  - If you change the histogram binning and want to redo the plots, there is no need to re-do tress, just pass `--skip_do_trees` as argument to the `skimm_tree.py`

- The plotting options are [here]().
  - If you change just plotting options (eg color, stack ordering, ...) and want to redo the plots, there is no need to re-do tress, just pass `--skip_do_trees  --skip_do_histograms` as argument to the `skimm_tree.py`

Read the other options as necessary


One can also inspect the yields on the different categories with the bellow.

```
```


# MVA training

- XGBoost based training scripts are [here]()
- @Marko add instructions to TMVA

# Instructions to run TMVA
First step is to fetch the data samples and save a train / test for signal and background. 

This can be done in the `prepare_datasets_boosted.py` (also usable for resolved)

```
python prepare_datasets_boosted.py
```

In the script, one needs to specify the paths to the resolved or boosted samples and what selection to apply.

Once the training and testing sets a completed, one can use the script `train_bdt_resolved.py` to do the training. 

```
python train_bdt_resolved.py --year run2 --nTrees 200 --maxDepth 3 --nCuts 50 --minNodeSize 5
```


# Datacards maker

- See [here]()
