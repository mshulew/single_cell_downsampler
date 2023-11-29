process unzipFiles {
	tag " unzipping $filename "
	
	input:
	path myfile
	path mydir

	output:
	tuple val (filename), path ('*.fastq')

	script:
	filename = myfile.toString().split ( ".txt" )[ 0 ]
	"""
	bash ${baseDir}/src/unzip_files.sh $mydir $filename
	"""
}
