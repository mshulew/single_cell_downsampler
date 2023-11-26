#!/bin/bash
set -e

# get files in directory

for file in $1/*; do
    if [[ $file == *"$2"* ]] || [[ $file == *"${2//R1/R2}"* ]] || [[ $file == *"${2//R1/I1}"* ]]; then
    	zcat $file > "$(basename "${file%.fastq.*}")".fastq
    fi
done


