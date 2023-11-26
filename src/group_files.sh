#!/bin/bash
set -e

# get files in directory

for file in $1/*; do
    if [[ $file == *"R1"* ]]; then
    	echo "$(basename "${file%.fastq.*}")" > "$(basename "${file%.fastq.*}")".txt 
    fi
done


