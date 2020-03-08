import func as F

import matplotlib.pyplot as plt

a = F.getData('datasets/iris.csv')

print(a)


for sepalL,sepalW,petalL,petalW,label in a:

	if(label=='Iris-virginica'):
		plt.plot(sepalL,sepalW,'ro')

	elif(label=="Iris-versicolor"):
	    plt.plot(sepalL,sepalW,'bo')
	

	elif(label=="Iris-setosa"):
		plt.plot(sepalL,sepalW,'go')

plt.ylabel('some numbers')
plt.show()