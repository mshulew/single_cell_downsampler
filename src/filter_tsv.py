#!/usr/bin/env python3
# coding: utf-8

"""

filters a .tsv file with a list of lines to keep
outputs fastq files

"""

import sys
import os
import time
import re

def addToLog(entry):
    with open(logfile, 'a') as log_file:
        log_file.write(entry)


if __name__ == "__main__":

    mapfile = sys.argv[1]
    tsvfile = sys.argv[2]
    fileprefix = sys.argv[3]
    logfile = 'log.txt'
    
    with open(logfile, 'w') as log_file:
        log_file.write('Filtering .tsv file started\n')

    start_time = time.time()
              
# import map
    read_index = []
    with open(mapfile, 'r') as reads:
        for line in reads:
            read_index.append(int(line.splitlines()[0]))

    addToLog(' Number of reads to filter: {}\n'.format(len(read_index)))

# filter reads using map    
    filtered = []
    addToLog('Reading .tsv file into memory, low memory mode\n')
    iteration = 0
    entry = 0
    total_entries = 0
    partial_read_index = []
    with open(tsvfile, 'r') as tsv_file:
# filter 10000000 reads at a time
        for line in tsv_file:
            total_entries += 1
            if entry == 0:
                tsv = []
            tsv.append(line.splitlines()[0].split('\t'))
            entry += 1
            if entry == 1000000:

# subdivide read_index
                for readindx in read_index:
                    if readindx < 1000000*(iteration + 1):
                        if readindx >= 1000000*iteration:
                            partial_read_index.append(readindx - 1000000*iteration)
                
 # filter portion of reads                   
                partial_filtered = [tsv[i] for i in partial_read_index]
                filtered.extend(partial_filtered)
                addToLog('iteration: {} relapsed time: {} sec\n'.format(iteration + 1,round((time.time()-start_time),0)))
                addToLog('          total reads read: {}M\n'.format(total_entries/1000000))
                addToLog('  number of reads filtered: {} \n'.format(len(partial_read_index)))
                addToLog('      total reads filtered: {}\n'.format(len(filtered)))
                addToLog('\n'.format(len(filtered)))

# reset counters, partial_read_index
                iteration += 1
                entry = 0
                partial_read_index = []

 # Add final reads
 # subdivide read_index
        for readindx in read_index:
            if readindx < 1000000*(iteration + 1):
                if readindx >= 1000000*iteration:
                    partial_read_index.append(readindx - 1000000*iteration)
        partial_filtered = [tsv[i] for i in partial_read_index]
        filtered.extend(partial_filtered)
        addToLog('iteration: {} relapsed time: {} sec\n'.format(iteration + 1,round((time.time()-start_time),0)))
        addToLog('          total reads read: {}M\n'.format(total_entries/1000000))
        addToLog(' number of reads to filter: {} entries\n'.format(len(partial_read_index)))
        addToLog('      total reads filtered: {}\n'.format(len(filtered)))
        addToLog('Filtering complete, total reads filtered: {} elapsed time: {} sec\n'.format(len(filtered),round((time.time()-start_time),0)))
                
# write fastq files
    basename = fileprefix.split(re.search('_S[0-9]_L',fileprefix).group())[0] + '_ds' + re.search('_S[0-9]_L',fileprefix).group() + fileprefix.split(re.search('_S[0-9]_L',fileprefix).group())[1] + '.fastq'
    R1_out=basename
    R2_out=basename.replace('_R1','_R2')
    I1_out=basename.replace('_R1','_I1')

    for read in filtered:
        with open(R1_out, 'a') as R1out:
            R1out.write('{}\n'.format(read[0]))
            R1out.write('{}\n'.format(read[1]))
            R1out.write('{}\n'.format(read[2]))
            R1out.write('{}\n'.format(read[3]))

        with open(R2_out, 'a') as R2out:
            R2out.write('{}\n'.format(read[4]))
            R2out.write('{}\n'.format(read[5]))
            R2out.write('{}\n'.format(read[6]))
            R2out.write('{}\n'.format(read[7]))

        with open(I1_out, 'a') as I1out:
            I1out.write('{}\n'.format(read[8]))
            I1out.write('{}\n'.format(read[9]))
            I1out.write('{}\n'.format(read[10]))
            I1out.write('{}\n'.format(read[11]))
            
                                       
        




    
    
