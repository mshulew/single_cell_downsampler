#!/usr/bin/env nextflow
nextflow.enable.dsl = 2

"""
Downsample single cell sequencing data
"""

def helpMessage() {
  log.info Header()
  log.info """
  Usage:

  The typical command for running the pipeline is as follows:

  Required:
    --inDir		    Path to input directory
    --outDir                Path to output directory
    --barcodes		    Number of different barcodes to filter; default = 1000
 
    """.stripIndent()
}

// Show help emssage
if (params.help){
    helpMessage()
    exit 0
}

//include modules containing processes
include { preProcessing }                    	from './modules/preProcessing'
include { unzipFiles }                    	from './modules/unzipFiles'
include { genIndex }                    	from './modules/genIndex'
include { downSample }                    	from './modules/downSample'

// make path to input directory a file
dir = file(params.inDir)

def summary = [:]
summary['Run Name'] = workflow.runName
summary['Config Profile'] = workflow.profile
summary['Input Directory'] = params.inDir
summary['Output directory'] = params.outDir
summary['Number of barcodes'] = params.barcodes
log.info Header()
log.info summary.collect { k,v -> "${k.padRight(18)}: $v" }.join("\n")
log.info "----------------------------------------------------"

// Check for input/output
if (!params.inDir) {
    exit 1,"Input directory not supplied"
}

if (!params.outDir) {
    exit 1,"Output directory not supplied"
}

workflow {
	preProcessing(dir)
	unzipFiles(preProcessing.out.flatten(),dir)
	genIndex(unzipFiles.out)
	downSample(genIndex.out.index,genIndex.out.combined)
}
  
  
def Header() {
    return """
    Downsampler single cell sequencing data
    """.stripIndent()
    }
