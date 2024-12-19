import pandas as pd
import numpy as np
import random
import os

def run_CreateRumorChunks():
    """Look, this function is shit because it can be, alright?
    Reads Rumors.csv (the raw dataframe) and shuffles it. That shuffled
    dataframe is then flattened into a list which is finally exported
    as a txt for other calls to read. The rumors are chunked in fours, 
    those chunks are delimitted via double newline characters.
    
    Input: None
    Output: flattened txt."""
    
    # fix directory issue due to segmentation of .pys
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "Rumors.csv")

    # read raw rumors csv in latin1 to avoid odd apostrophe encoding errors
    df = pd.read_csv(csv_path, encoding='latin1')

    # initialize a sampling frame
    shuff = df.sample(frac=1)

    # two layers of random bc im stupid
    li = shuff.to_numpy().flatten().tolist()
    li = random.sample(li, len(li))

    # initialize an output path
    output = 'DistributedRumors.txt'

    # write the rumors to a txt in 4-element chunks delimited by two \n
    with open(output, "w", encoding='utf-8') as file:
        for i in range(0, len(li), 4):
            batch = li[i:i+4]
            file.write("\n".join(batch) + "\n\n")
            
    return