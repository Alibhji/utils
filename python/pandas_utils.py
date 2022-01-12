import numpy as np
import pandas as pd
import os
from .os_utils import  makeDirsIfNotExist


# split a pandas dataframe into the n chunks
def pandas_splitter_and_save (df , numOfChunks , save = False , save_diretory = './', base_name = 'df_chunk'):
    if save:
        makeDirsIfNotExist(save_diretory)
    dfChunks = np.array_split(df , numOfChunks)

    for i , chunk in enumerate(dfChunks):
        path = os.path.join(save_diretory , f"{base_name}_{i:03d}.pkl")
        chunk.to_pickle(path)

    return dfChunks


