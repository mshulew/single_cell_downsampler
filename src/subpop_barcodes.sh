#!/bin/bash
set -e

# subpopulate cell barcodes
# identify R1, R2 & I1 files

for file in *; do
    if [[ $file == *"R1"* ]]; then
    	R1=$file 
    elif [[ $file == *"R2"* ]]; then
	R2=$file
    elif [[ $file == *"I1"* ]]; then
	I1=$file
    fi
done

# extract cell barcodes from R1 file
    awk 'NR%4==2' $R1 | cut -b 1-16 > cell_barcode.txt

# sort cell barcodes by frequency
    sort cell_barcode.txt | uniq -c | sort -rnk1 > cell_barcode_freq.txt

# randomly select specific number of barcodes ($1) out of the top 40,000 cell barcodes
    head -40000 cell_barcode_freq.txt | shuf -n $1 | sort -rnk1 > cell_barcode_subpop_freq.txt

# remove frequency column
    awk 'BEGIN{FS=" "; OFS=" "} {print $2}' cell_barcode_subpop_freq.txt > cell_barcode_subpop.txt
