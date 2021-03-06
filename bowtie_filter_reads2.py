'''
This script performs bowtie filtering on multiple indexed databases, while bookeeping names.  Databases should be listed with commas and no spaces.  To execute,
cd to the directory where your fastq files are located and execute the script as follows: 
python bowtie_filter_error_corrected_reads2.py <left_paired> <right_paired> <singletons> <out_base_name> <path to databases> <databases>
Note that when specifiying multiple databases, be sure to separate them by commas and no spaces
'''
#!/usr/bin/env python

import sys, os

left_paired = sys.argv[1]
right_paired = sys.argv[2]
singletons = sys.argv[3]
out_base_name = sys.argv[4] + '_'
path_to_dbs = sys.argv[5] + '/'
databases = sys.argv[6]

db_list = databases.split(',')

db_complete = ''
updated_for = ''
updated_rev = ''
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
		command = "bowtie2 --local -x %s%s -p 16 -t -1 %s -2 %s -U %s --un-conc %s_unmapped_paired.fastq --al-conc %s_mapped_paired.fastq --un %s_unmapped_singles.fastq --al %s_mapped_singles.fastq -S %s.sam" % (path_to_dbs, d, updated_for, updated_rev, updated_sing, new_base_name, new_base_name, new_base_name, new_base_name, new_base_name)
		print "executing: " + command
		os.system(command)
		updated_for = new_base_name + '_unmapped_paired.1.fastq'
		updated_rev = new_base_name + '_unmapped_paired.2.fastq'
		updated_sing = new_base_name + '_unmapped_singles.fastq'
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
		command = "bowtie2 --local -x %s%s -p 16 -t -1 %s -2 %s -U %s --un-conc %s_unmapped_paired.fastq --al-conc %s_mapped_paired.fastq --un %s_unmapped_singles.fastq --al %s_mapped_singles.fastq -S %s.sam" % (path_to_dbs, d, left_paired, right_paired, singletons, new_base_name, new_base_name, new_base_name, new_base_name, new_base_name)
		print "executing: " + command
		os.system(command)
		db_complete += abbrev_db
		updated_for = new_base_name + '_unmapped_paired.1.fastq'
		updated_rev = new_base_name + '_unmapped_paired.2.fastq'
		updated_sing = new_base_name + '_unmapped_singles.fastq'
#		print command