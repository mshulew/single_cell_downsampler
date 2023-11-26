# Downsampling Single Cell RNA-Seq (scRNA-Seq) sequencing data

Downsamples scRNA-Seq data

3 FASTQ files must be supplied:

1. R1
2. R2
3. I1

## Naming convention
1. Must be: [sample name]_S[0-99]_L[0-9][0-9][0-9]_[R,I][0-9]_[0-9][0-9][0-9].fastq.gz
2. All 3 files (R1, R2 & I1) from a sample sample must have the same name except for the R1/R2/I1 portion of the name

## Installation
1. Install latest version of Nextflow (version 23.10.0+)
2. Install Python3.11 (must be able to execute python with command python3.11) - if you have a different version of Python, just edit the Python steps in main.nf

Note: This pipeline does not use a Docker container

## Pre-flight
Place all FASTQ files into a single directory. The pipeline will identify the 3 files for each sample based on the name

## Run

```bash

nextflow run single_cell_downsampler/main.nf --inDir [path to directory with FASTQ files] --outDir [output directory] 

example:
nextflow run single_cell_downsampler/main.nf --inDir pbmc_1k_v3_fastqs/ --outDir downsampled

```

## Run options

--indir		[path to input directory]  
--outDir		[path to output directory]  
--barcodes	[number of different barcodes to filter; default in 1000]  

## Output files

Subdirectories in parent output directory defined by --outDir

### samples
Each filename is the same of each samples + .txt
File contents is name of sample

### unzip
Unzipped FASTQ files

### genIndex
combined_fastqs.tsv - R1, R2 & I1 FASTQs combined into a single file. Each read is a single line
read_index.txt - Index of reads that are selected

### downSampled
Downsampled FASTQ files zipped (end in .gz)



