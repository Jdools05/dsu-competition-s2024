import os
import pandas as pd

file_name = "../../data/DSU_output_FINAL.csv"

# get unique values for each label
# and write a sample of those values for each label to
# a text file named unique.txt
def get_uniques( df ):

    unique_values = {}

    print(f"getting unique")

    # get unique values for each label
    labels = df.columns
    for label in labels:
        unique_values[label] = df[label].unique()

    
    max_write_vals = 100
    label_amount = len(labels)
    print("writing to unique")
    
    with open("unique.txt", "w") as fout:

        # write number of labels along with the list
        # of all labels
        fout.write( f"Total of { label_amount } labels\n" )
        fout.write( ",".join( labels ) + "\n\n" )

        # compute the amount of labels with only one value in the entire column
        # these are mostly all nans
        useless = sum([ len( unique_values[ label ] ) <= 1 for label in labels ] )
        fout.write( f"Number of useless labels: { useless }/{ label_amount }\n\n")
        
        for label in labels:
            
            total_values = unique_values[label]
            total_amount = len( total_values )

            # write the name of label and number of unique values in column
            fout.write(f"Label: \"{ label }\" length { total_amount }\n")

            #print a sample of those values up to max_write_vals
            for i in range( min( max_write_vals, total_amount ) ):
                fout.write(f"    { total_values[i] }\n")
            if max_write_vals < total_amount:
                fout.write(f"     ... {total_amount - max_write_vals} more ... \n")
            fout.write("\n")
    
    print("finished writing to unique")
                
            
            