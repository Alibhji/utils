import json
import sys
import os
import numpy as np 
import pandas as pd
from tqdm.contrib.concurrent import process_map 

from multiprocessing import Pool


# read json files in parallel and create a pandas dataframe

def multi_proc_read_json(jsons_list):

    df = pd.DataFrame()
    jsons_list = np.load("<path_to_the_list_of_json_files>")

    def read_json_(ind):
        stp_input = jsons_list[ind]
        with open(stp_input) as json_file:
            stp_output = json.load(json_file)
        fnol = stp_output['fnol']
        return fnol

    indexes =[(itm,) for itm in range(len(jsons_list))]  
    output = process_map(read_json_, indexes ,max_workers = os.cpu_count()-2, chunksize = 10)
    df = pd.DataFrame(output)
    return df


def multi_procs_with_more_than_one_arg(args):

    def f_sum(a,b):
        return a +b

    process_pool =multiprocessing.Pool(3)
    data =[(1,1),(2,1),(3,1)]
    output =process_pool.starmap(f_sum,data)

    print(output)