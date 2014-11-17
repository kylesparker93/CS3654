setwd('C:/Users/Kyle/Dropbox/CS/CS3654/R/Inclass11')
data(mtcars)

head(mtcars)
names(mtcars)

?mtcars

# [, 1]   mpg   Miles/(US) gallon
# [, 2]	 cyl	 Number of cylinders
# [, 3]	 disp	 Displacement (cu.in.)
# [, 4]	 hp	 Gross horsepower
# [, 5]	 drat	 Rear axle ratio
# [, 6]	 wt	 Weight (lb/1000)
# [, 7]	 qsec	 1/4 mile time
# [, 8]	 vs	 V/S
# [, 9]	 am	 Transmission (0 = automatic, 1 = manual)
# [,10]	 gear	 Number of forward gears
# [,11]	 carb	 Number of carburetors

#use all 11 variables as features
knnTrain <- mtcars
names(knnTrain)

#known classes in training set; 
#change levels to 0=False=neg class and 1=TRUE=pos class
response <- mtcars$am > 0

#examine features and classes to know our data
head(response)
head(knnTrain)
dim(knnTrain)

################kNN algo

#package to implement kNN algo
install.packages('class')
library(class)

#use system.time function to time the training of the model

system.time(knnDecision <- knn(knnTrain,knnTrain,response,k=10,prob=T))
?knn #to learn more about the knn implementation

#notice that response should not be part of the training set(knnTrain)
#for knn training

#the values of knnDecision are classifications
head(knnDecision)

#the "prob" argument returns, for each observation, the proportion of
#votes for the winning class (pos or neg)
#we want the predicted probabilities (which is p = probability(pos))
#so we will use the "prob" attribute values
#to get the p predictions


knnPred <- ifelse(knnDecision==TRUE,
                  attributes(knnDecision)$prob,
                  1-(attributes(knnDecision)$prob))
head(knnPred)

#calculate AUC
library(ROCR)
eval <- prediction(knnPred, response) #from ROCR package
auc_calc <- performance(eval,'auc')
auc_calc@y.values #special object; this is how we extract the exact AUC part

# We see that the knn algorithm leaves us with a slightly better AUC.
# I did not run into any problems with this algorithm