import pandas as pd
import pyper as py
import matplotlib as mat

iris = pd.read_csv('iris.csv')

iris.head()
iris.shape
iris.describe

r = py.R(RCMD = 'C:\\Program Files\\R\\R-3.1.1\\bin\R', use_pandas = True)

r.assign("rdata", iris)

print r("head(rdata)")
print r("names(rdata)")
print r("summary(rdata)")

r("?princomp")

r("p = princomp(rdata)")

print r("names(p)")

print r("head(p$scores, n=6")

irisPd = pd.DataFrame(r.get("p$scores"),columns=['pc1','pc2','pc3','pc4','pc5'])

irisPd.head()

mat.scatter(irisPY.Comp1,irisPY.Comp2).
title('Iris').
xlabel('Primary Component 1').
ylabel('Primary Component 2')
	
mat.show()
	  
	  
colors = ['red', 'green', 'blue']
labels = ['Setosa', 'Virginica', 'Versicolor']

fig = mat.figure()
ax = mat.add_subplot(1, 1, 1)

ax.set_xlabel('Primary Component 1')
ax.set_ylabel('Primary Component 2')
ax.set_title('Species Data')

for z in xrange (len(colors)):
    px = irisPd.Comp1[:][iris.Species == z]
    py = irisPd.Comp2[:][iris.Species == z]
    plt.scatter(px, py, c = colors[z], label = labels[z])

	
mat.show()

# Overall, the principal components are still good for sumarizing the data