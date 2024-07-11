# for prob  in  ProbHHH6b 
for prob  in  ProbHH4b 
do
    for year in  2018 
    # for year in  2017 2016 2016APV

    do


        # python apply_binning_cat.py --year $year --prob  $prob &
        python apply_binning_for_kappa.py --year $year --prob  $prob &

        

    done
done