import os

# Create a new directory if it'sn't exist

def makeDirs_if_not_exists(dirPth ,  verbose = False):
    if not os.path.exists(dirPth):
        os.makedirs(dirPth)
        if verbose:
            print(dirPth ,"  is created.")

