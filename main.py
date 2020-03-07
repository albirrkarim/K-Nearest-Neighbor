import func as F

a = F.getData('datasets/iris.csv')

# print(a)

# Step 1: Calculate Euclidean Distance.
# Test distance function
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]

# row0 = dataset[0]
# for row in dataset:
#     distance = F.euclidean_distance(row0, row)
#     # print(distance)
#     print(f' {row0} | {row} | {distance}')


# neighbors = F.get_neighbors(dataset, dataset[0], 3)
# for neighbor in neighbors:
# 	print(neighbor)


prediction = F.predict_classification(dataset, dataset[0], 3)
print('Expected %d, Got %d.' % (dataset[0][-1], prediction))

# Step 2: Get Nearest Neighbors.
# Step 3: Make Predictions.