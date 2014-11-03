setwd("C:\\Users\\Kyle\\Dropbox\\CS\\CS3654\\R\\Inclass9")

load("fdata.rdata")
attach(final)

# Prepare the model and get a summary for som1-5
model1 <- glm(disorder~som1 + som2 + som3 + som4 + som5, data = final, family = "binomial")
model1$coef
exp(model1$coef)
summary(model1)

# Prepare the model and get a summary for som6-9
model2 <- glm(disorder~som6 + som7 + som8 + som9, data = final, family = "binomial")
model2$coef
exp(model2$coef)
summary(model2)

# Prepare the model and get a summary for som10-14
model3 <- glm(disorder~som10 + som11 + som12 + som13 + som14, data = final, family = "binomial")
model3$coef
exp(model3$coef)
summary(model3)
