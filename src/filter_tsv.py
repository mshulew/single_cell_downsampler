#!/usr/bin/env python3
# coding: utf-8

"""

filters single cell fastq files by read index

"""

import sys
import os
import time
import re

def addToLog(entry):
    with open(logfile, 'a') as log_file:
        log_file.write(entry)


if __name__ == "__main__":

    
# handle arugments
    mapfile = sys.argv[1]
    fileprefix = sys.argv[2]
    logfile = 'filter_reads_log.txt'

# output files name/path
    basename = fileprefix.split(re.search('_S[0-9]_L',fileprefix).group())[0] + '_ds' + re.search('_S[0-9]_L',fileprefix).group() + fileprefix.split(re.search('_S[0-9]_L',fileprefix).group())[1] + '.fastq'
    R1_out=basename
    R2_out=basename.replace('_R1','_R2')
    I1_out=basename.replace('_R1','_I1')
    
    with open(logfile, 'w') as log_file:
        log_file.write('Filtering reads started\n')

    start_time = time.time()
              
# import map
    read_index = []
    with open(mapfile, 'r') as reads:
        for line in reads:
            read_index.append(int(line.splitlines()[0]))

    addToLog(' Number of reads to filter: {}\n'.format(len(read_index)))

# get file names
    for filename in os.listdir():
        if 'R1' in filename:
            R1 = filename
        elif 'R2' in filename:
            R2 = filename
        elif 'I1' in filename:
            I1 = filename

# filter reads using map    
    addToLog('Reading fastq files into memory\n')
    iteration = 0
    entry = 0
    total_entries = 0
    total_filtered = 0
    partial_read_index = []
    R1entry = []
    R2entry = []
    I1entry = []
    linenum = 0
    with open(R1, 'r') as R1f, open(R2, 'r') as R2f, open(I1, 'r') as I1f:
# filter 10000000 reads at a time
        for lineR1, lineR2, lineI1 in zip(R1f,R2f,I1f):
            R1entry.append(lineR1.splitlines()[0])
            R2entry.append(lineR2.splitlines()[0])
            I1entry.append(lineI1.splitlines()[0])
            linenum += 1
            if linenum == 4:
                if entry == 0:
                    partial_reads = []
                partial_reads.append(R1entry + R2entry + I1entry)
                R1entry = []
                R2entry = []
                I1entry = []
                entry += 1
                total_entries += 1
                linenum = 0
                if entry == 1000000:

# subdivide read_index
                    for readindx in read_index:
                        if readindx < 1000000*(iteration + 1):
                            if readindx >= 1000000*iteration:
                                partial_read_index.append(readindx - 1000000*iteration)
                
 # filter portion of reads                   
                    partial_filtered = [partial_reads[i] for i in partial_read_index]
                    total_filtered += len(partial_filtered)
                    addToLog('iteration: {} elapsed time: {} sec\n'.format(iteration + 1,round((time.time()-start_time),0)))
                    addToLog('          total reads read: {}M\n'.format(total_entries/1000000))
                    addToLog('      total reads filtered: {}\n'.format(total_filtered))
                    addToLog('\n')

# write filtered reads to file
                    with open(R1_out, 'a') as R1out:
                        for read in partial_filtered:
                            R1out.write('{}\n'.format(read[0]))
                            R1out.write('{}\n'.format(read[1]))
                            R1out.write('{}\n'.format(read[2]))
                            R1out.write('{}\n'.format(read[3]))

                    with open(R2_out, 'a') as R2out:
                        for read in partial_filtered:
                            R2out.write('{}\n'.format(read[4]))
                            R2out.write('{}\n'.format(read[5]))
                            R2out.write('{}\n'.format(read[6]))
                            R2out.write('{}\n'.format(read[7]))

                    with open(I1_out, 'a') as I1out:
                        for read in partial_filtered:
                            I1out.write('{}\n'.format(read[8]))
                            I1out.write('{}\n'.format(read[9]))
                            I1out.write('{}\n'.format(read[10]))
                            I1out.write('{}\n'.format(read[11]))

# reset counters, partial_read_index
                    iteration += 1
                    entry = 0
                    partial_read_index = []
                    partial_reads = []


 # Add final reads
 # subdivide read_index
        for readindx in read_index:
            if readindx < 1000000*(iteration + 1):
                if readindx >= 1000000*iteration:
                    partial_read_index.append(readindx - 1000000*iteration)
        partial_filtered = [partial_reads[i] for i in partial_read_index]
        total_filtered += len(partial_filtered)
        addToLog('iteration: {} elapsed time: {} sec\n'.format(iteration + 1,round((time.time()-start_time),0)))
        addToLog('          total reads read: {}\n'.format(total_entries))
        addToLog('      total reads filtered: {}\n'.format(total_filtered))
        addToLog('Filtering complete, total reads filtered: {} elapsed time: {} sec\n'.format(total_filtered,round((time.time()-start_time),0)))
                

# write final filteredreads to file
        for read in partial_filtered:
            with open(R1_out, 'w') as R1out:
                R1out.write('{}\n'.format(read[0]))
                R1out.write('{}\n'.format(read[1]))
                R1out.write('{}\n'.format(read[2]))
                R1out.write('{}\n'.format(read[3]))

            with open(R2_out, 'w') as R2out:
                R2out.write('{}\n'.format(read[4]))
                R2out.write('{}\n'.format(read[5]))
                R2out.write('{}\n'.format(read[6]))
                R2out.write('{}\n'.format(read[7]))

            with open(I1_out, 'w') as I1out:
                I1out.write('{}\n'.format(read[8]))
                I1out.write('{}\n'.format(read[9]))
                I1out.write('{}\n'.format(read[10]))
                I1out.write('{}\n'.format(read[11]))

