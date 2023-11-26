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


if __name__ == "__main__":

    #mapfile = sys.argv[1]
    #tsvfile = sys.argv[2]
    #fileprefix = sys.argv[3]
    #logfile = 'log.txt'

    mapfile=r'C:\Users\Mark\Documents\bioinformatics\downsample\new_read_index.txt'
    tsvfile=r'C:\Users\Mark\Documents\bioinformatics\downsample\combined_fastqs.tsv'
    logfile=r'C:\Users\Mark\Documents\bioinformatics\downsample\log.txt'
    fileprefix='pbmc_1k_v3_S1_L001_R1_001'
    
    with open(logfile, 'w') as log_file:
        log_file.write('Filtering .tsv file started\n')

    start_time = time.time()
              
# import map
    read_index = []
    with open(mapfile, 'r') as reads:
        for line in reads:
            read_index.append(int(line.splitlines()[0]))

    with open(logfile, 'a') as log_file:
        log_file.write('Number of reads to filter: {}\n'.format(len(read_index)))

# read tsv file into memory
    with open(logfile, 'a') as log_file:
        log_file.write('Reading .tsv file into memory\n')
    tsv = []
    with open(tsvfile, 'r') as tsv_file:
        for line in tsv_file:
            tsv.append(line.splitlines()[0])
            if len(tsv)%10000000 == 0:
                with open(logfile, 'a') as log_file:
                    log_file.write('{} million reads read, elapsed time: {} sec\n'.format(len(tsv)/1000000,round((time.time()-start_time),0)))

    with open(logfile, 'a') as log_file:
        log_file.write('Total number of input reads: {} elapsed time: {} sec\n'.format(len(tsv),round((time.time()-start_time))))

# filter tsv file
    #filtered = []
    filtered = [tsv[i] for i in read_index]
    #for index in read_index:
    #    filtered.append(tsv[index].split('\t'))
    with open(logfile, 'a') as log_file:
        log_file.write('total filtered reads: {} elapsed time: {} sec\n'.format(len(filtered),round((time.time()-start_time),0)))

# write fastq files
    basename = fileprefix.split(re.search('_S[0-9]_L',fileprefix).group())[0] + '_ds' + re.search('_S[0-9]_L',fileprefix).group() + fileprefix.split(re.search('_S[0-9]_L',fileprefix).group())[1] + '.fastq'
    R1_out= 'C:/Users/Mark/Documents/bioinformatics/downsample/' + basename
    R2_out='C:/Users/Mark/Documents/bioinformatics/downsample/' + basename.replace('_R1','_R2')
    I1_out='C:/Users/Mark/Documents/bioinformatics/downsample/' + basename.replace('_R1','_I1')

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
            
                                       
        




    
    
