library("vegan")

# Read in input data
merged_microbes <- read.csv('./BM_4/merged_genusrpm.tsv',header=TRUE,sep='\t',row.names=1)

# Calculate Simpson's Diversity Index for all individuals
simpsons_div <- diversity(t(merged_microbes),index = "simpson", MARGIN = 1)
print(simpsons_div)  # write to consol
write.csv(simpsons_div,"SDI.csv", quote=FALSE)  # output to file

# Calculate Bray-Curtis distance between all pairs of samples
bray_curtis <- vegdist(t(merged_microbes),method="bray",binary=FALSE,diag=FALSE,upper=TRUE,na.rm=FALSE)
write.csv(as.matrix(bray_curtis), "BrayCurtis.csv", quote=FALSE)  # output to file

