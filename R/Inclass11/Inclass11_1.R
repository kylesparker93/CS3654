setwd('C:/Users/Kyle/Dropbox/CS/CS3654/R/Inclass11')
data(mtcars)

head(mtcars)
names(mtcars)

mtcars$response <- mtcars$am > 0

?mtcars

# [, 1]   mpg	 Miles/(US) gallon
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

?rpart
tmodel <- rpart(response ~ am, data=mtcars)
tmodel

#to visualize tree
install.packages("rpart.plot")
library(rpart.plot)
prp(tmodel)

#another measure of performance :ROC curve and AUC

install.packages('ROCR') #only need to do this once
library(ROCR)

mtcars$pred <- predict(tmodel, newdata = mtcars)
eval <- prediction(mtcars$pred, mtcars$response) #from ROCR package

#calculate AUC

auc_calc <- performance(eval,'auc')
auc_calc@y.values

plot(performance(eval, "tpr", "fpr"))
# I see a 100% true positive rate, which is what we would expect