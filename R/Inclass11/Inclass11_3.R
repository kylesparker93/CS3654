setwd('C:/Users/Kyle/Dropbox/CS/CS3654/R/Inclass11')
data(mtcars)

head(mtcars)
names(mtcars)

?mtcars

# [, 1]   mpg   Miles/(US) gallon
# [, 2]   cyl	 Number of cylinders
# [, 3]	 disp	 Displacement (cu.in.)
# [, 4]	 hp	 Gross horsepower
# [, 5]	 drat	 Rear axle ratio
# [, 6]	 wt	 Weight (lb/1000)
# [, 7]	 qsec	 1/4 mile time
# [, 8]	 vs	 V/S
# [, 9]	 am	 Transmission (0 = automatic, 1 = manual)
# [,10]	 gear	 Number of forward gears
# [,11]	 carb	 Number of carburetors

library(ROCR)
library(rpart)
library(class)

#Use dTrain data for KDD Cup
#use pre-selected 27 variables as features
#previous data wrangling and variable selection 

names(mtcars)

#create the 0/1 response/class variable
mtcars$response <- mtcars$am > 0

#Package for Naive Bayes implementation
install.packages("e1071")
library(e1071)

#train model on selected variables from dTrain data set
#use the shortcut to formula as before

#train the model
system.time(fit <- naiveBayes(as.formula(f), data=mtcars))

#make predictions
system.time(naivB_pred <- predict(fit, mtcars, type = 'raw'))
head(naivB_pred) #need just the "probability of TRUE" as prediction

?naiveBayes

#calculate AUC for Naive Bayes
#notice that second column from predictions denotes "p of pos"
eval <- prediction(naivB_pred[,2], mtcars$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values