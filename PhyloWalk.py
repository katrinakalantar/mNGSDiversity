


import MySQLdb
import pandas as pd
import numpy as np
import sys

# inputs:
# filename - genus-level merged counts file

# read input file to pandas dataframe
DF = pd.read_csv(sys.argv[1],sep='\t',index_col=0) 

# Make database connections
tsdb = MySQLdb.connect(host='localhost',user='mysql_user',passwd='balamuthia',db='taxa_scoring')
ncbi_db = MySQLdb.connect(host='localhost',user='mysql_user',passwd='balamuthia',db='NCBI_Taxonomy')


full_map = {}
return_names = []
for i in DF.index:
	#print(i) 
	genus = i.split('(')[1].split(')')[0].strip()

	# get path levels to root - specify genus/family/phylum levels
	path2root = 'call path_to_root_node(' + genus + ')'
	p2r = pd.read_sql(path2root,ncbi_db)['@path_to_root'][0].split(';')
	#print(p2r)

	# get path taxonomy IDs to root - specify integer phylogeny IDs
	Vpath2root = 'call vedas_path_to_root_node(' + genus + ')'
	Vp2r = pd.read_sql(Vpath2root,ncbi_db)['@path_to_root'][0].split(';')
	#print(Vp2r)

	names2root = []
	for j in Vp2r:
		hr_tax_name = 'select * from ncbi_names where tax_id=' + j + ' and name_class = "scientific name"'
		hr = pd.read_sql(hr_tax_name, ncbi_db)['name_txt'][0]
		names2root.append(hr)

	#print(names2root)
	# zip the levels with the taxonomy IDs 
	dictionary = dict(zip(p2r,names2root))#Vp2r))
	print(dictionary)

	try:
		return_names.append(dictionary[sys.argv[2]])
	except:
		return_names.append('other')


	full_map[genus] = dictionary

output_df = pd.DataFrame(full_map)
output_df.dropna(axis=0, how='all')
print(output_df.index)
output_df = output_df.loc[['genus','family','order','class','phylum','kingdom','domain']]
output_df.to_csv("phyloMap.csv")

DFout = DF
DFout.index = return_names
DFout.to_csv(sys.argv[1].split('.')[0] + sys.argv[2] + '.csv')


