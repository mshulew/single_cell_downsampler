#!/usr/bin/env python3
# coding: utf-8

"""

maps barcodes to original sequence file

"""

import sys
import os


if __name__ == "__main__":

    subpopulated_barcode_file = sys.argv[1]
    all_barcodes_file = sys.argv[2]

# create a list of wanted barcodes
# this is the list of barcodes created with Linux bash
    wanted_barcodes = []
    with open(subpopulated_barcode_file, 'r') as file:
        for line in file:
            barcode = line.splitlines()[0]
            wanted_barcodes.append(barcode)
            
# create a list of all barcodes
    all_barcodes = []
    with open(all_barcodes_file,'r') as file:
        for line in file:
            all_barcodes.append(line.splitlines()[0])

# find indices of each wanted barcode in list of all barcodes
    wantedbarcodes = set(wanted_barcodes)
    barcode_map = ([i for i, e in enumerate(all_barcodes) if e in wantedbarcodes])
                
# save to file
    with open('read_index.txt', 'w') as outputfile:
        for index in barcode_map:
            outputfile.write('{}\n'.format(index))




    
    
