from os import listdir
from os.path import isfile, join

mypath = "huese"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with open("lattice.txt", "w") as outfile:
    outfile.write("\n/cygdrive/c/Users/Vikto/Project3/{}/".format(mypath).join(onlyfiles))
