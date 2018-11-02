########## Format data (only needed if data is not formatted properly)
# Fix data format
init <- read.csv('./prosst_topology3_prosstt0/prosstt0_simulation.txt', sep='\t', row.names=1)
dim(init)
write.table(t(init), './prosst_topology3_prosstt0/input.txt', quote=FALSE, sep='\t')
