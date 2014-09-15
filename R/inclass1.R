setwd("C:\\Users\\Kyle\\Dropbox\\CS\\CS3654\\R")
mydata1<-read.table("cars1.csv",sep=",",header=TRUE)
dim(mydata1)
# The dimensions are 50x2
var1<-0
mydata1[2, 2]<-var1
# The variable names are Speed1-50, Dist1-50
print(mydata1[1,])
print(mydata1[ ,2])
colnames(mydata1)<-c("SPEED", "dist")
print(mydata1[15])