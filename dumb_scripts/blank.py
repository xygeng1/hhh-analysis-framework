law run PlotPullsAndImpacts \
--version post_preapp3 \
--pois r \
--datacards histograms_noVJets_3Higgs_all.txt \
--use-snapshot  \
--hh-model "model_dummy.model_dummy" \
--parameters-per-page 30  \
--left-margin 400 \
--label-size 16 \
--order-by-impact \
--PullsAndImpacts-custom-args=' --X-rtd MINIMIZER_no_analytic' \
--fetch-output 0,a,.,False


