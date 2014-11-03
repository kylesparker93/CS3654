setwd("C:\\Users\\Kyle\\Dropbox\\CS\\CS3654\\R\\Inclass9")
load("NatalRiskData.rData")
train <- sdata[sdata$ORIGRANDGROUP<=5,]
test <- sdata[sdata$ORIGRANDGROUP>5,]

complications <- c("ULD_MECO","ULD_PRECIP","ULD_BREECH")
riskfactors <- c("URF_DIAB", "URF_CHYPER", "URF_PHYPER",
                 "URF_ECLAM")
y <- "atRisk"
x <- c("PWGT",
       "UPREVIS",
       "CIG_REC",
       "GESTREC3",
       "DPLURAL",
       complications,
       riskfactors)
fmla <- paste(y, paste(x, collapse="+"), sep="~")

print(fmla)

model <- glm(fmla, data=train, family=binomial(link="logit"))

train$pred <- predict(model, newdata=train, type="response")
test$pred <- predict(model, newdata=test, type="response")

library(ggplot2)
ggplot(train, aes(x=pred, color=atRisk, linetype=atRisk)) +
  geom_density()

#Use threshold for test set prediction and get confusion matrix

confusion.test <- table(pred=test$pred>0.02, target = test$atRisk)
confusion.test
#rows contain predicted negative and positives
#columns contain actual negatives and positives

#Then calculate, accuracy, precision and recall
accuracy <- (confusion.test[2,2] + confusion.test[1,1])/sum(confusion.test[,])
accuracy 
precision <- confusion.test[2,2] / sum(confusion.test[2,])
precision
recall <- confusion.test[2,2] / sum(confusion.test[,2])
recall