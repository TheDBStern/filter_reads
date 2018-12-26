'''
This script performs bowtie filtering on multiple indexed databases, while bookeeping names.  Databases should be listed with commas and no spaces.  To execute,
cd to the directory where your fastq files are located and execute the script as follows: 
python bowtie_filter_error_corrected_reads2.py <singletons> <out_base_name> <path to databases> <databases>
Note that when specifiying multiple databases, be sure to separate them by commas and no spaces
'''
#!/usr/bin/env python

import sys, os

singletons = sys.argv[1]
out_base_name = sys.argv[2] + '_'
path_to_dbs = sys.argv[3] + '/'
databases = sys.argv[4]

db_list = databases.split(',')

db_complete = ''
updated_sing = ''
for d in db_list:
	if db_complete:#this says that the string is not empty (aka not the first)
		if d.startswith('bacteria'):
			abbrev_db = d.replace('teria_refseq_and_general_all_ti_', '').replace('idx', '')
		elif d.startswith('fungi'):
			abbrev_db = d.replace('_refseq_and_general_all_ti_', '')
		elif d.startswith('viruses'):
			abbrev_db = d.replace('_refseq_and_general_all_ti_', '')
		else:
			abbrev_db = d
		db_complete += abbrev_db
		new_base_name = out_base_name + db_complete
		command = "bwa aln -t 16 %s%s -b %s | bwa samse %s%s - | samtools view -b -f 4 > %s_unmapped.bam" % (path_to_dbs, d, updated_sing, path_to_dbs, d, new_base_name)
		print "executing: " + command
		os.system(command)
		updated_sing = new_base_name + '_unmapped.bam'
#		print command
	else:# this is for empty string (aka first database in the list)
		if d.startswith('bacteria'):
			abbrev_db = d.replace('teria_refseq_and_general_all_ti_', '').replace('idx', '')
		elif d.startswith('fungi'):
			abbrev_db = d.replace('_refseq_and_general_all_ti_', '')
		elif d.startswith('viruses'):
			abbrev_db = d.replace('_refseq_and_general_all_ti_', '')
		else:
			abbrev_db = d
		new_base_name = out_base_name + abbrev_db
		command = "bwa aln -t 16 %s%s -b %s | bwa samse %s%s - | samtools view -b -f 4 > %s_unmapped.bam" % (path_to_dbs, d, singletons, path_to_dbs, d, new_base_name)
		print "executing: " + command
		os.system(command)
		db_complete += abbrev_db
		updated_sing = new_base_name + '_unmapped.bam'
#		print command