'''
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
		command = "/home/dbstern/Programs/bbmap/mapPacBio.sh ref=%s%s in=%s outm=%s_mapped.fastq outu=%s_unmapped.fastq" % (path_to_dbs, d, updated_sing, new_base_name, new_base_name)
		print "executing: " + command
		os.system(command)
		updated_sing = new_base_name + '_unmapped.fastq'
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
		command = "/home/dbstern/Programs/bbmap/mapPacBio.sh ref=%s%s in=%s outm=%s_mapped.fastq outu=%s_unmapped.fastq" % (path_to_dbs, d, singletons, new_base_name, new_base_name)
		print "executing: " + command
		os.system(command)
		db_complete += abbrev_db
		updated_sing = new_base_name + '_unmapped.fastq'
#		print command