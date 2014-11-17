setwd('C:/Users/Kyle/Dropbox/CS/CS3654/R/Inclass11')
data(mtcars)

head(mtcars)
names(mtcars)

?mtcars

# [, 1]   mpg   Miles/(US) gallon
# [, 2]   cyl   Number of cylinders
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

names(mtcars)

#create the 0/1 response/class variable
mtcars$response <- mtcars$am > 0

#Package for Naive Bayes implementation
install.packages("e1071")
library(e1071)



########### CART algo

f <- 'response ~ mpg + cyl + disp + hp + drat + wt + qsec + vs + gear + carb'
f
system.time(tmodel <- rpart(f,data=mtcars))
tmodel

#another measure of performance :ROC curve and AUC

mtcars$pred <- predict(tmodel, newdata = mtcars)
eval <- prediction(mtcars$pred, mtcars$response) #from ROCR package

#calculate AUC

auc_calc <- performance(eval,'auc')
auc_calc@y.values

# Time = 0s, AUC = 90.9%



################# KNN

#use all 11 variables as features
knnTrain <- mtcars

#known classes in training set; 
#change levels to 0=False=neg class and 1=TRUE=pos class
response <- mtcars$am > 0

#use system.time function to time the training of the model

system.time(knnDecision <- knn(knnTrain,knnTrain,response,k=10,prob=T))


knnPred <- ifelse(knnDecision==TRUE,
                  attributes(knnDecision)$prob,
                  1-(attributes(knnDecision)$prob))
head(knnPred)

#calculate AUC
eval <- prediction(knnPred, response) #from ROCR package
auc_calc <- performance(eval,'auc')
auc_calc@y.values

# Time = 0s, AUC = 91.9%



################# Logistic algo

#compare to logistic regression AUC and system time
f <- 'response ~ mpg + cyl + disp + hp + drat + wt + qsec + vs + am gear + carb' #create formula
system.time(gmodel <- glm(as.formula(f),
                          data=knnTrain,
                          family=binomial(link='logit'))) #get system time and train the model
log_predict <- predict(gmodel, 
                       newdata=knnTrain, 
                       type = "response") #get p predictions

#get AUC for logistic model

eval <- prediction(log_predict, response) #from ROCR package
auc_calc <- performance(eval,'auc')
auc_calc@y.values #special object; this is how we extract the exact AUC part

# Time = 0.04s, AUC = 100%


################# Naive Bayes

#train model on selected variables from dTrain data set
#use the shortcut to formula as before

#train the model
system.time(fit <- naiveBayes(as.formula(f), data=mtcars))

#make predictions
system.time(naivB_pred <- predict(fit, mtcars, type = 'raw'))
head(naivB_pred) #need just the "probability of TRUE" as prediction

#calculate AUC for Naive Bayes
#notice that second column from predictions denotes "p of pos"
eval <- prediction(naivB_pred[,2], mtcars$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

# Time = 0.02, AUC = 98.4%