for var in  BTagCSV  QCD6B  TT GluGluToHHHTo6B_SM   ZJetsToQQ   WJetsToQQ   ZZTo4Q   QCD  WZZ ZZZ WWW WWTo4Q WWZ
do
    python3 make_new.py --version v25 --year 2017 --region 1 --tag 6tag --wp loose --f_in $var --doMVAInputs --doHistograms  &
done


# QCD_bEnriched QCD6B_bEnriched 
