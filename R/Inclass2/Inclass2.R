setwd("C:\\Users\\Kyle\\Dropbox\\CS\\CS3654\\R\\Inclass2")

load('exampleData.rData')
summary(custdata)
# The range for "custid" is very large, and the column name is not clear
# is.employed has missing data
# Income has a very wide range, as well as possibly some invalid values
# Housing.type and recent.move both have missing data
# num.vehicles is missing data
# age has some invalid values (at the high end and low end)
# is.employed.fix1 is not a clear column name
# age.normalized is not clear what it represents, nor is income.norm
# gp is not a clear column name, nor is income.lt.30k
# income is missing data

uciCar = read.csv('car.data.csv')
summary(uciCar)
# The data seems to be in a strange format (though I know it's CSV)
# The distribution seems very wide and very little data can be gleaned from it
# Clearly data that needs to be fixed up to be usable

load('credit.rData')
summary(d$Personal.status.and.sex)
# Without looking up the key values there is no way for us to know how sex compares with personal status
summary(d$Other.debtors)
# We also get no information from this column
# We can conclude the german credit data will not be easy to work with and the values are arbitrary and not clear


install.packages("hexbin")
library("hexbin")
help(package=hexbin)
hexbinplot(custdata$age, custdata$income)