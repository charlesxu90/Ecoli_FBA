echo 'cold condition:'
python ./count_pvale.py ./rand_3sample/sampling_all.out 38 essential    # cold essential 
python ./count_pvale.py ./rand_3sample/sampling_all.out 73 dispensable  # cold dispensable
echo 'heat condition:'
python ./count_pvale.py ./rand_4sample/sampling_all.out 63 essential    # heat essential 
python ./count_pvale.py ./rand_4sample/sampling_all.out 38 dispensable  # heat dispensable
echo 'low pH condition:'
python ./count_pvale.py ./rand_4sample/sampling_all.out 42 essential    # low pH essential 
python ./count_pvale.py ./rand_4sample/sampling_all.out 4 dispensable   # low pH dispensable
echo 'high pH condition:'
python ./count_pvale.py ./rand_4sample/sampling_all.out 30 essential    # high pH essential 
python ./count_pvale.py ./rand_4sample/sampling_all.out 25 dispensable  # high pH dispensable

