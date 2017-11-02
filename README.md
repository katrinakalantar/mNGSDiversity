# mNGSDiversity

This base folder contains bare-bones scripts for mNGS diversity analysis.

### Basic Analysis of Microbial Diversity

1. Download the scripts in this repo to your local working directory.
2. Create a file "background_models.txt" containing one integer ID per line 

note: you can run with multiple different background models at once by adding multiple lines with integers, but for final analysis BM 4 (all NID + H2O) has been most effective.

```
4

```

3. Create a file "sampleIDs.txt" containing the sample IDs for all samples of interest.

*note these IDs must match those on assembler2.

```
VAP_1
VAP_2
VAP_3
...

```

4. Download all report files for the samples of interest and the given background models.

```
bash generate_reports_by_background_model.sh background_models.txt sampleIDs.txt
```

outputs a folder BM_X (where X is the background model ID) for each background model. The folder contains all report files for the samples of interest.

5. Create a merged genus-level count file

```
python3 create_merged_genus_rpm_v2.py --genus
```

6. Generate basic diversity stats

```
Rscript getSimpsonsDiversityIndex.R
```


### Taxonomy-Walking Plots

1. Generate a taxonomy-level-specific version of the genus counts

On Assembler2 (required for database access) run the following

```
python PhyloWalk.py merged_genusrpm.tsv phylum mysql_password
```

outputs:

**phyloMap.csv** - matrix of taxonomy level x genus ID, showing the associated taxonomy levels for each genus in the merged_genusrpm file

**merged_genusrpm[taxonomylevel].csv** - taxonomy-level ID (corresponding to the input parameter, ie. phylum in example above) x sample ID
   note: some taxonomy IDs in the index will be duplicated, because counts are still specified at genus-level



2. Generate taxonomy-level-specific stacked barchart

```
python PhyloPlot.py merged_genusrpmphylum.csv 
```

outputs:

**TaxonomyPlot.pdf** - PDF file containing the taxonomy-specific (by input file) stacked bar chart

[![Snip20171101_6.png](https://s26.postimg.org/lwe4vqqa1/Snip20171101_6.png)](https://postimg.org/image/u1w6tweit/)

