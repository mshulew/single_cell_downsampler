process	downSample {
	tag " downSampled $filename "
	publishDir "${params.outDir}/downSampled/${filename}", mode: 'copy'

	input:
	tuple val (filename), path (myfiles)

	output:
	path ('*.fastq.gz')

	script:
	"""
	bash ${baseDir}/src/subpop_barcodes.sh $params.barcodes
	python3.11 ${baseDir}/src/map_barcodes.py cell_barcode_subpop.txt cell_barcode.txt
	python3.11 ${baseDir}/src/filter_tsv.py read_index.txt $filename
	gzip *_ds_*
	"""
}
