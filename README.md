# mNGSDiversity

This base folder contains bare-bones scripts for mNGS diversity analysis.

1. Download the scripts in this repo to your local working directory.
2. Create a file "background_models.txt" containing one integer ID per line 

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





