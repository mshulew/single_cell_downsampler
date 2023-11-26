#!/usr/bin/env python3
# coding: utf-8

"""

maps barcodes to original sequence file
improve speed
original speed: 408 seconds
update: 11 seconds

"""

import sys
import os
import time


if __name__ == "__main__":

    subpopulated_barcode_file = r'C:\Users\Mark\Documents\bioinformatics\downsample\cell_barcode_subpop.txt'
    all_barcode_file = r'C:\Users\Mark\Documents\bioinformatics\downsample\cell_barcode.txt'

    start_time = time.time()

# create a list of wanted barcodes
# this is the list of barcodes created with Linux commands
    wanted_barcodes = []
    with open(subpopulated_barcode_file, 'r') as file:
        for line in file:
            barcode = line.splitlines()[0]
            wanted_barcodes.append(barcode)

# create a list of all barcodes
    all_barcodes = []
    with open(all_barcode_file,'r') as file:
        for line in file:
            all_barcodes.append(line.splitlines()[0])

# find indices of each wanted barcode in list of all barcodes
    wantedbarcodes = set(wanted_barcodes)
    barcode_map = ([i for i, e in enumerate(all_barcodes) if e in wantedbarcodes])
                
# save to file
    with open(r'C:\Users\Mark\Documents\bioinformatics\downsample\new_read_index.txt', 'w') as outputfile:
        for index in barcode_map:
            outputfile.write('{}\n'.format(index))

    print('elapsed time: {} sec'.format(time.time()-start_time))




    
    
