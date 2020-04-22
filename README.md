# Language-model-Group-C

The commands used for creating our LM's are in Guide.txt, with some expections this is how we ran it in most cases

### Guide.txt
1) First line creates a vocabulary file and an n-gram ditribution file 
2) Second line Takes these files and turns them into an n-gram LM 
3) Third line is used for testing perplexity 
4) Forth and fifth lines rescore the lattices and create a hypothesis file

For  the last step in "Guide.txt" we need two files

1) An in-lattice-list "lattice.txt" which has references to every lattice that needs to be rescored. You need to change the path in "lattice.txt" to match where these files are locally on your own machine
2) in-lattice-list "upLats.txt" which has references to the newly rescored lattices. We set the path for the previous step into a folder called Uplats, and had "uplats.txt" just reference every file in there. When we needed to redo this step we had to rename the upLats folder to something new

### Datasets
+ Pizza palace training set       provided by  *Andreas Søeborg Kirkedal*
+ Verizon                         provided by  *Andreas Søeborg Kirkedal*
+ Googles Taskmaster ([2019](https://research.google/tools/datasets/taskmaster-1/) -[2020](https://research.google/tools/datasets/taskmaster-2/)) dataset, we only used the food-ordering json files 
+ [Ubuntu Dialogue Corpus](https://www.kaggle.com/rtatman/ubuntu-dialogue-corpus)
+ [Santa Barbara Corpus of Spoken American English](https://www.linguistics.ucsb.edu/research/santa-barbara-corpus)
+ [MetaLWOZ](https://www.microsoft.com/en-us/research/project/metalwoz/) We only used the categories, Phone setting, Pizza ordering and Phone plans.


### Folders

* **pp.trains** contains different version of the pizza palace training set, according with what we saw fit after each itertation
* **models_lms** contains all the iterations of pizza palace project. Each iteration contains the LM's used, the hyphesis file both normalized and untouched, aswell as a folder called upLats with the updated lattices
* **Lattices** contains the starting lattices, that has not yet been scored

### Scripts

+ **ww.py** is an helper module we created to cleant the files. It contain the functions, "remove_filler" (this is actually caught by ourder silencewords.txt, which makes it redundant), "remove_confirmation" and "pickUp" (concatenates pick up into 1 word)
+ **normhyp.py** first step of normalization, which removes all the ektra information given the way we create our hypothesis file in Guide.txt. This step would allways be done before applying further normalization e.i. ww.py
+ **pathFinder.py** can be used to create the in-lattice-lists mentioned in Guide.txt

### Text normalization standard

1) We only work with lowercase words
2) No punctuation allowed
3) All numbers are written out, 3 = "three". numbers out of range 0-9 are listed as a sequence of wordsnumbers with spaces inbetween

### Jupyter notebooks
##### Every "clean" jupyter notebook is used to normalize data according to the above given rules as well as some extra requirements depending on what we saw fit during the iterations
##### Most of the files in the notebooks contain paths that will not work on a general setting. Make sure to check if paths are set correctly for your environment

+ **clean_pptrain.ipynb** used to clean pp.train.txt by removing "and" and "okay" if they are in the beginning of the sentences. It also changces occurences of "pizza pizza" to "pizza palace" aswell as concatanating "pick up" with using functionality from ww.py 

+ **clean2019-2020TM.ipynb** Cleans the Taskmaster data set from google. Some regex magic was need to fix timestamps and prices which contained "$", "." and ":" so we made sure do this before removing punctuation. We also found it fitting to remove ["no", "yes", "okay", "ok", "sure", "and", "yep"] if they occur in the beginning of the sentence. It does all of this for both files and concatenates them.  
  
+ **OOVTest.verizon.ipynb** calculates number of "Our of vocabulary words". This was required since SRILM was given us a wrong number.

+ **MetaLWOZ.pizza.ipynb** cleans the subset of MetaLWOZ that contains pizza delivery

+ **MetaLWOZ.phone.ipynb** cleans the subset of MetaLWOZ that contains Phone setting and Phone plans

+ **UbuntuClean.ipynb** cleans the smallest of the datasets of the datasets from Ubuntu Dialogue Corpus

+ **Clean_SBC.ipynb** cleans the Santa Barbara Corpus of Spoken American English









