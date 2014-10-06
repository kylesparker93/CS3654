# 1
import numpy as np

# 2
data1 = ['0.0', '1.0', '2.0' ,'3.0', '4.0']
data2 = [0, 1, 2, 3, 4]

array1 = np.array(d1)
array2 = np.array(d2)

print 'array1-shape: ', array1.shape
print 'array1-type: ', array1.dtype

print 'array2-shape: ', array2.shape
print 'array2-type: ', array2.dtype

# 3
np.add(array1.astype(np.float), array2)

# 4
array1.astype(np.float)*array2

# 5
ident = np.eye(6,6)

# 6
ident[2,] = 5

# 7
ident[ident!=0] = 6

# 8
array3 = np.empty((2,3,4))

# 9
print 'array3 dimensions:', array3.ndim
print 'array3 shape:', array3.shape
print 'array3 data type:', array3.dtype

# 10
array3[0,1,1] = 5

# 11
randoms = rand(20)

# 12
print 'min:', np.min(randoms)
print 'max:', np.max(randoms)
print 'standard deviation: ', np.std(randoms)

# 13
rounded = np.where(randoms > 0.5, 1, 0)

# 14
np.sort(randoms)

# 15
unique(randoms)