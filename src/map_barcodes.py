#!/usr/bin/env python3
# coding: utf-8

"""

maps barcodes to original sequence file

"""

import sys
import os
import time

def addToLog(entry):
    with open(logfile, 'a') as log_file:
        log_file.write(entry)


if __name__ == "__main__":

    subpopulated_barcode_file = sys.argv[1]
    all_barcodes_file = sys.argv[2]
    logfile = 'map_barcodes_log.txt'

    start_time = time.time()

# create a list of wanted barcodes
# this is the list of barcodes created with Linux bash
    wanted_barcodes = []
    with open(subpopulated_barcode_file, 'r') as file:
        for line in file:
            barcode = line.splitlines()[0]
            wanted_barcodes.append(barcode)
    wantedbarcodes = set(wanted_barcodes)
            
# find indices of each wanted barcode in 10,000,000 read subsets of all barcodes
    barcode_map = []
    with open(logfile, 'w') as log_file:
        log_file.write('Reading all barcodes into memory by subset\n')
    iteration = 0
    entry = 0
    total_entries = 0
    with open(all_barcodes_file,'r') as file:
        for line in file:
            if entry == 0:
                barcode_subset = []
            barcode_subset.append(line.splitlines()[0])
            total_entries += 1
            entry += 1
            if entry == 10000000:
                partial_map = ([i + 10000000*iteration for i, e in enumerate(barcode_subset) if e in wantedbarcodes])
                barcode_map.extend(partial_map)
                addToLog('Iteration {}, reads processed: {}, total indices {}, elapsed time {} sec\n'.format(
                          iteration, total_entries, len(barcode_map),round((time.time()-start_time),0)))
                entry = 0
                iteration += 1
# get remaining indices
    partial_map = ([i + 10000000*iteration for i, e in enumerate(barcode_subset) if e in wantedbarcodes])
    barcode_map.extend(partial_map)
    addToLog('Iteration {}, reads processed: {}, total indices {}, elapsed time {} sec\n'.format(
              iteration, total_entries, len(barcode_map),round((time.time()-start_time),0)))
       
# save to file
    with open('read_index.txt', 'w') as outputfile:
        for index in barcode_map:
            outputfile.write('{}\n'.format(index))




    
    
