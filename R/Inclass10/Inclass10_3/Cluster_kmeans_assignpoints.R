data(iris)
names(iris)

#Always examine data first
names(iris)
head(iris)
summary(iris)

#Scale variables if they are not in the same
#unit of measurement (make them have mean 0 and std =1)

#features we will use to determine distances and clusters
features <- iris[,1:4]

scaled_features <- scale(features)

summary(scaled_features)

#retain the means and std devs for each initial feature
#to be able to unscale later
#they are returned as attributes of the
#result returned by the scale() function
?scale
means <- attr(scaled_features,"scaled:center")
print(means)
stdv <- attr(scaled_features, "scaled:scale")
print(stdv)

#Distance matrix calculation
#Use Euclidean distance
distance <- dist(scaled_features, method = "euclidean")
#this matrix contains the distance between each 2 countries
#using their coordinates in therms of the 10 food groups (features)

#Use kmeans clustering algorithm
#on iris data
#with 5 clusters
  
kmeans_clusters <- kmeans(scaled_features, 3 , nstart=100, iter.max=100)

#Results of the kmeans clustering algo implementation on the scaled_features instead 
#of distance matrix

#retain centers of clusters

kmeans_clusters$centers

#Suppose we need to assign a new observation/row/country
#to one of the three clusters
#assign to cluster that has the nearest center

#Process

#1. Create new point coordinates in terms of the 9 food groups and give it a country name:
species <- 'setosa'
newpt <- cbind(5.1, 2.2, 1.5, 0.8)
newpt <- as.data.frame(newpt)
names(newpt) <- names(features)
newpt

#2. Scale the new point; use the means and standard deviations from the old iris data

newpt_sc <- (newpt - means)/stdv
newpt_sc

#3. Calculate the Euclidian distance from this new point to each of the centers
#of the 5 clusters

centers <- kmeans_clusters$centers

#We would create a function and apply it accross rows but we will
#take each row one at a time here for simplicity and illustration

dist1 <- sqrt(sum((newpt_sc - centers[1,])^2)) #to first cluster centroid
dist1

dist2 <- sqrt(sum((newpt_sc - centers[2,])^2))
dist2

dist3 <- sqrt(sum((newpt_sc - centers[3,])^2))
dist3

#assign point to cluster with smallest dist
