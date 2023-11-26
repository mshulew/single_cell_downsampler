#!/bin/bash
set -e

# combine R1, R2 and I1 fastq files into a single file, one read per line

for file in *; do
    if [[ $file == *"R1"* ]]; then
    	R1=$file 
    elif [[ $file == *"R2"* ]]; then
	R2=$file
    elif [[ $file == *"I1"* ]]; then
	I1=$file
    fi
done

paste <(cat $R1 | paste - - - -) <(cat $R2 | paste - - - -) <(cat $I1 | paste - - - -) > combined_fastqs.tsv