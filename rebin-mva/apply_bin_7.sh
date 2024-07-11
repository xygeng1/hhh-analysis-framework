for prob  in  ProbHHH6b 
# for prob  in  ProbHH4b 
do
    # for path_year in  2016  2018
    for path_year in  2016 2016APV 2017 2018
    # for year in  2017 2016 2016APV

    do


        # python apply_binning_cat.py --year $year --prob  $prob &
        python apply_binning_for_kappa_new.py --path_year $path_year --prob  $prob --year 2016APV201620172018 &

        

    done
done