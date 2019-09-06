import numpy as np

#create random vector of size 15
num = np.random.randint(1, high=20, size=15, dtype='int');
print('Random array generated',num)

#reshape the array to 3 by 5
num = np.reshape(num, (3,5));
print('reshape the array to 3 by 5',num)

# maxInRows = np.max(num, axis=1)
# num[np.where(np.amax(num, axis=1))] = 0
#print(np.where(num == np.max(num, axis=1), num, 0))

# print('Max value of every Row: ', maxInRows)

#replace the max in each row by 0
print('Replacing Max No. by 0',np.where(num == np.max(num, axis=1).reshape(-1,1), 0, num))
