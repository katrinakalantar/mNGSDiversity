
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sys

# read in the output from assembler2 script: 
# python PhyloWalk.py merged_genusrpm.tsv order
DF = pd.read_csv(sys.argv[1],index_col=0) 
print(DF.shape)
combined_DF = DF.groupby(DF.index).sum()  # merged the dataframe on duplicate indices
print(combined_DF.shape)

normalized_combined_DF = combined_DF/combined_DF.sum(axis=0)  # normalize the counts for a stacked bar chart
new_order = normalized_combined_DF.sum(axis=1).sort_values(ascending=False).index  # re-order so that maximal taxonomy is on bottom
plot_DF = normalized_combined_DF.loc[new_order] 

# create the taxonomy plot (grouped at whatever level the input taxonomy file was generated)
c = sns.color_palette("Paired",20)  # set color scheme
plot_DF.transpose().plot(kind='bar',legend=True,stacked=True,figsize=(24,14),color = c, width=.8)
plt.legend(bbox_to_anchor=(1.02,1), loc="upper left")
plt.savefig('TaxonomyPlot.pdf')  # save to .pdf


