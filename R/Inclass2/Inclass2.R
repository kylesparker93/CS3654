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

install.packages("ggplot2", dependencies=TRUE)
library("ggplot2")
custdata2 <- subset(custdata,
                    (custdata$age > 0 & custdata$age < 100
                     & custdata$income > 0))
cor(custdata2$age, custdata2$income)

ggplot(custdata2, aes(x=age,y=income)) +
  geom_point() +
  ylim(0,200000) +
  theme_bw() +
  ggtitle("Scatterplot of Income vs Age")

install.packages("hexbin")
library("hexbin")
ggplot(custdata2, aes(x=age, y=income)) +
  geom_hex(binwidth=c(5,10000)) +
  theme_bw() +
  ylim(0, 200000)
# The hexbin looks relatively similar to the scatterplot in shape and density

ggplot(custdata2, aes(x=num.vehicles,y=income)) +
  geom_point() +
  ylim(0,200000) +
  geom_smooth() + 
  theme_bw() +
  ggtitle("Scatterplot of Income vs Age")
# I opted to use a scatterplot with a smoothed curve to show the correlation, which is loose

ggplot(custdata2) + 
  geom_bar(aes(x=income.lt.30K, fill=recent.move))
# I opted to use a bar chart. It seems as if there is a small correlation between income
# below 30k and recent moves, however the data is not complete.