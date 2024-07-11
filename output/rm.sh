for folder in  ProbHHH6b_0bh0h_inclusive_CR ProbHHH6b_1Higgs_inclusive_CR ProbHHH6b_2Higgs_inclusive_CR ProbHHH6b_3Higgs_inclusive_CR ProbHHH6b_3bh0h_inclusive_CR ProbHHH6b_2bh1h_inclusive_CR ProbHHH6b_1bh2h_inclusive_CR ProbHHH6b_0bh3h_inclusive_CR
do
    for year in 2016 2017 2018 2016APV run2
    
    do
        rm  v33/${year}/${folder}/histograms/histograms*
        
    done
done