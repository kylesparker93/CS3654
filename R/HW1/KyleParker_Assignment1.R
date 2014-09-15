# Problem 1
setwd("C:\\Users\\Kyle\\Dropbox\\CS\\CS3654\\R")
mydata1<-read.table('prices.txt', sep='\t', header=FALSE, col.names=c('PRICE', 'SFQT', 'AGE', 'NE'))
print(mydata1)
# row.names can be used to assign names to a row, as opposed to automatically generating them.
# It functions similarly to col.names as used above.
mydata2<-read.table('test.txt', header=TRUE)


# Problem 2
mymatrix<-cbind(c(2,3,1,5), c(1,0,3,1), c(0,2,-3,2), c(0,2,3,1))
mymatrix[4, 4]
t(mymatrix)
solve(mymatrix)


# Problem 3
fpe <- read.table("http://data.princeton.edu/wws509/datasets/effort.dat")
for(i in 1:nrow(fpe)){
  if(fpe[i, 2] == 0)
    print(fpe[i, ])
}
colnames(fpe)
rownames(fpe)
head(fpe)
write.table(fpe, "fpe.txt", sep="\t")
write.csv(fpe, "fpe.csv")
