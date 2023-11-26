process	downSample {
	tag " downSampled $filename "
	publishDir "${params.outDir}/downSampled/${filename}", mode: 'copy'

	input:
	tuple val (filename), path (index)
	path (combined)

	output:
	path ('*.fastq.gz')

	script:
	"""
	python3.11 ${baseDir}/src/filter_tsv.py $index $combined $filename
	gzip *_ds_*
	"""
}
