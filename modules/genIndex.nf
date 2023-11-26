process	genIndex {
	tag " gen index $filename "
	publishDir "${params.outDir}/genIndex/${filename}", mode: 'copy'

	input:
	tuple val (filename), path (myfiles)

	output:
	tuple val (filename), path ('read_index.txt'), emit: index
	path ('combined_fastqs.tsv'), emit: combined

	script:
	"""
	bash ${baseDir}/src/subpop_barcodes.sh $params.barcodes
	python3.11 ${baseDir}/src/map_barcodes.py cell_barcode_subpop.txt cell_barcode.txt
	bash ${baseDir}/src/combine_fastqs.sh
	"""
}
