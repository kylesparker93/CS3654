# Load libraries, set wd, and load/attach data
library(MASS)
setwd("C:\\Users\\Kyle\\Dropbox\\CS\\CS3654\\R\\Inclass9")
load("fdata.rdata")

# Create/attach training and test subset as demonstrated in text
final$gp <- runif(dim(final)[1])
test <- subset(final, final$gp <= 0.1)
train <- subset(final, final$gp > 0.1)
attach(train)

# Remove columns used for creating subsets
train["gp"] <- NULL
test["gp"] <- NULL

# Fit linear regression with all features
fit <- lm(ssc ~ age + gender + location + ethnicity + coder + som1 + som2 + som3 + som4 
          + som5 + som6 + som7 + som8 + som9 + som10 + som11 + som12 + som13 + som14)

summary(fit)
step <- stepAIC(fit, direction = "both")
step
step$anova

rm(step)
rm(fit)

# Build model with only retained variables
fit1 <- lm( ssc ~ age + location + ethnicity + coder + som1 + som2 + som3 + 
              som4 + som5 + som10 + som11 + som12 + som13 + som14)

summary(fit1)

# Remove training set (no longer needed)
detach(train)
rm(train)

# Now predict using the test set
test$ssc_pred <- predict(fit1, newdata = test)

rm(fit1)

#See how predicted ssc compares to actual ssc values
library(ggplot2)
ggplot(data = test, aes(x = ssc_pred, y = ssc)) +
  geom_point(color = "red") +
  geom_line(aes(x = ssc, y = ssc), color = "blue")
