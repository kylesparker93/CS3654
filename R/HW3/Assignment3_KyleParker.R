setwd("C:\\Users\\Kyle\\Dropbox\\CS\\CS3654\\R\\HW3")

# 1
cfb <- read.csv("cfb2013stats.csv")

# 2
summary(cfb)
saveRDS(cfb, "cfb2013.rData")
# All are numeric except for the team names and the site

# 3
# The only issues in this data set is the fact that not all games are bet on, meaning not all
# games have lines.

# 4
install.packages("ggplot2")
library("ggplot2")
ggplot(cfb, aes(x=RushYdsOff+PassYdsOff,y=ScoreOff)) +
  geom_point() +
  ylim(0,100) +
  theme_bw() +
  ggtitle("Scatterplot of Points versus Total Offense")

ggplot(cfb) + 
  geom_bar(aes(x=(RushYdsOff+PassYdsOff)>400)) + 
  xlab("Over 400 yards") + ylab("Number of occurences")

pie <- ggplot(mtcars, aes(x = factor(1), fill = factor(cyl))) +
  geom_bar(width = 1)
pie + coord_polar(theta = "y")

qplot(PassYdsOff, ScoreOff, data=cfb, geom=c("point", "smooth"), 
      method="lm", formula=y~x, 
      main="Regression of Points on Passing Yards", 
      xlab="Points", ylab="Passing Yards")

# 5
# There is no treatment needed for missing values

# 6
# However, there are transformations that can be done to make the data more comprehensive
cfb$TotalOffOff = cfb$PassYdsOff + cfb$RushYdsOff
cfb$TotalOffDef = cfb$PassYdsDef + cfb$RushYdsDef

# 7
saveRDS(cfb, "TransformedData.rData")