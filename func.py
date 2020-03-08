from math import sqrt
import csv

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)


def getData(filename):
    # Baca File CSV (comma separated values) kemudian returnkan list (array)
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = list(csv_reader)
    return data


# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
    	dist = euclidean_distance(test_row, train_row)
    	distances.append((train_row, dist))

    # https://www.programiz.com/python-programming/methods/list/sort
    # https://www.w3schools.com/python/python_lambda.asp
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
    	neighbors.append(distances[i][0])
    return neighbors

# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[2] for row in neighbors]
    # print(set(output_values))
    prediction = max(set(output_values), key=output_values.count)
    return prediction