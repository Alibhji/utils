import os

# Create a new directory if it'sn't exist

def makeDirs_if_not_exists(dirPth ,  verbose = False):
    # if not os.path.exists(dirPth):  # also you can use os.path.isdir() instead
    #     os.makedirs(dirPth)
    #     if verbose:
    #         print(dirPth ,"  is created.")

    dirPth = dirPth.strip(' ')
    try:
        os.makedirs(dirPth)
        if verbose:
            print(dirPth ,"  is created.")
    except:
        return False

