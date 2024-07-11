for prob  in  ProbHHH6b 
# for prob  in  ProbHH4b 
do
    # for year in  2018 2017 2016 2016APV
    for year in  2016APV201620172018

    do


        python apply_binning_cat_4.py --year $year --prob $prob --var ProbMultiH  --version v32 --doSyst &

        

    done
done

