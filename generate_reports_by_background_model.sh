#!/bin/bash

# Script written by kkalantar 06/12/17
# run as follows: 
# bash generate_reports_by_background_model.sh [filename for list of background model IDs] [filename for list of sample names]
# background and sample name files should contain one value per line

models_file=$1
samples_file=$2

echo Background Models File: $models_file
echo Samples File: $samples_file

# loop over all background models, generating new director for each "BM_#"
for bm in `cat $models_file`;
do 
echo $bm;
mkdir "BM_"$bm;

# loop over all samples, generating reports for each and writing output to appropriate "BM_#" directory
for s in `cat $samples_file`;
do
echo $s;
curl -o "BM_"$bm/$s.report.csv --data "csv_only=1&sampleID=$s&model_pulldown=$bm&preset_pulldown=1&submit=Run%20Report&score_cutoff=-9999999&sp_nt_z=-9999999&genus_nt_z=-9999999&sp_nt_rm=-9999999&genus_nt_rm=-9999999&sp_nr_z=-9999999&genus_nr_z=-9999999&sp_nr_rm=-9999999&genus_nr_rm=-9999999" http://assembler2.ucsf.edu/page_generator-v2.php

done;

done;

