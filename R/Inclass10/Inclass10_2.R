data(iris)
names(iris)

features <- iris[,1:4]

scaled_features <- scale(features)

means <- attr(scaled_features,"scaled:center")
stdv <- attr(scaled_features, "scaled:scale")

distance <- dist(scaled_features, method = "euclidean")

hier_cl <- hclust(distance, method="ward.D")
k_cl <- kmeans(distance, 3, nstart=100, iter.max=100)

compare <- cbind(groups,k_cl$cluster)
compare <- as.data.frame(compare)
names(compare) <- c("Hierarchical", "kmeans")
compare <- cbind(iris$Species,compare)
compare

# It seems as if both clustering algorithms faired about equally well,
# though hierarchical seemed to perform slightly better.
#
# Both algorithms have gotten versicolor and setosa categorized almost perfectly.
# Likewise, both seemed to struggle with virginica frequently, placing it generally
# in one of two categories.
#
# As mentioned, the hierarchical and k-means clusters for setosa and versicolor are almost
# perfectly seperated, but not quite.