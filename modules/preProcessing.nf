process preProcessing {

	input:
	path mydir

	output:
	path '*.txt'

	script:
	"""
	bash ${baseDir}/src/group_files.sh $mydir
	"""
}
