#Get TH1Fs

``these codes are based on the output of NanoGEN. The output of the codes are TH1F histograms, which could be used to do comparison``

``step1:``

put all the output rootfile in one directory, e.g., 'MG273' in the code (each sample should have their own directory)

``step2:``

put the histo.sh and histo.py in the same directory of the 'MG273'

``step3:``

1)if you would like to ``run locally``: ```sh histo.sh -q LOCAL```

the output files will be in the 'MG273/Output'

2)if you would like to ``submit jobs``: ```sh histo.sh -q SUBMIT```

the output files will be in the 'MG273/Output', and the scripts will be in the  'MG273/CondorSub', the submit file 'condor.sub' will be in the same directory with 'histo.sh'

3)if you would like to ``run parallel locally``: ```sh histo.sh -q PARALLER```

the output files will be in the 'MG273/Output'

#Get Plots

``step1:``

add all the rootfiles using hadd, and name them as e.g.,  MG265.root, MG273.root, MG265_1j.root, MG265_2j.root, and put them in the directory

``step2:``

put the ``plot.sh`` and ``plot.py`` in the same directory with the rootfile in ``step1``

``step3:``

the code runs in two modes, 

1) comparsion between two MG versions, i.e., inclusive MG265 and inclusive MG273, or MG265_1j vs MG273_1j

2) inclusive vs stitched of the same MG version

for both modes, you need to provide the names and the cross-section of these samples, following the current setting in ``plot.sh``. 

``N.B.`` the first value in array xs should be the inclusive one

``step4:``

1) mode 1: run ``sh plot.sh -m TWOVERSION``

2) mode 2: run ``sh plot.sh -m INCVSSTIT``

