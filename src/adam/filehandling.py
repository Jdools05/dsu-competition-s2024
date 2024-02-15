import os
import pandas as pd

file_name = "../../data/DSU_output_FINAL.csv"

def write_uniques(uniques):
    max_wvals = 100
    print("writing to unique")
    with open("unique.txt", "w") as f:
        f.write(f"Total of {len(uniques)} labels\n")
        f.write(",".join(list(uniques)) + "\n\n")
        useless = sum([ len(uniques[l]) <= 1 for l in uniques ] )
        f.write(f"Number of useless labels: {useless}/{len(uniques)}\n\n")
        for l in uniques:
            u = uniques[l]
            lnum = len(u)
            f.write(f"Label: \"{l}\" length {lnum}\n")
            for i in range( min( max_wvals, lnum ) ):
                f.write(f"    {u[i]}\n")
            if max_wvals < lnum:
                f.write(f"     ... {lnum - max_wvals} more ... \n")
            f.write("\n")
    print("finished writing to unique")
                    
def get_uniques(uniques):
    print(f"getting unique")
    df = pd.read_csv( file_name )
    labels = df.columns
    for l in labels:
        if not l in uniques:
            uniques[l] = df[l].unique()
                    
def get_uniques_accross_all():
    uniques = {}
    get_uniques(uniques)
    write_uniques( uniques )
            
            