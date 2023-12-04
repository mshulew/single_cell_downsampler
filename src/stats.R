#!/usr/bin/env Rscript

# creates stats for single cell downsampler
# process R1.fastq file: awk 'NR%4==2' R1 file | cut -b 1-16 | sort | uniq -c | sort -rnk1 | awk 'BEGIN{FS=" "; OFS="\t"} {print $2,$1}' > cell_barcode_frq.txt
# made for R studio

library(readr)
library(ggplot2)
library(inflection)

input_file <- 'C:/Users/Mark/Documents/bioinformatics/dev/cell_barcode_frq.txt'

fltr_stats <- read_tsv(input_file, col_names=c("barcode","counts"))

fltr_stats$row <- seq.int(nrow(fltr_stats))
fltr_stats$cumsum <- cumsum(fltr_stats$counts)

#plot1 <- barplot(height= fltr_stats$counts, names.arg = fltr_stats$row, xlim=c(0,300), ylim = c(0,max(fltr_stats$counts)), 
                main='Stats', xlab='barcode #', ylab='counts')

#plot2 <- barplot(height= fltr_stats$cumsum, names.arg = fltr_stats$row, xlab='barcode #', ylab='cumulative counts')

plot3 <- plot(fltr_stats$row, fltr_stats$cumsum, xlab='barcode', ylab='cumulative sum',main='barcode cumulative sum')

x=fltr_stats$row
y=fltr_stats$cumsum
cc = check_curve(x,y)
ede = ede(x,y,cc$index)[1]
