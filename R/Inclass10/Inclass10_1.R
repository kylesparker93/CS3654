data(iris)
names(iris)

head(iris$Sepal.Length, 6)
summary(iris$Sepal.Length)

head(iris$Sepal.Width, 6)
summary(iris$Sepal.Length)

head(iris$Petal.Length, 6)
summary(iris$Sepal.Length)

head(iris$Petal.Width, 6)
summary(iris$Sepal.Length)

features <- iris[,1:4]

scaled_features <- scale(features)

means <- attr(scaled_features,"scaled:center")
print(means)
stdv <- attr(scaled_features, "scaled:scale")
print(stdv)

distance <- dist(scaled_features, method = "euclidean")
print(distance)

hier_cl <- hclust(distance, method="ward.D")

plot(hier_cl, labels = iris$Species)

rect.hclust(hier_cl, k = 3)
groups <- cutree(hier_cl, k = 3)
print(groups) #each country to what group

# It seems as if the first cluster is primarily Setosa,
# the second is primarily Versicolor, and the third
# is primarily Virginica