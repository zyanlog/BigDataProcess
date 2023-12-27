#!/usr/bin/python3
import os
import sys
import numpy as np
import operator

def createDataSet(folder_name):
	file_list = os.listdir(folder_name)

	group = []; labels = [];
	for file_name in file_list:
		file = os.path.join(folder_name, file_name)

		nm = file_name.split('_')
		label = nm[0]
		labels.append(label)

		with open(file, 'rt') as f:
			element = []
			for line in f:
				row = [int(c) for c in line.strip()]
				element.append(row)
			group.append(element)
	
	group_np = np.array(group, float)
	
	return group_np, labels

def classify(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 2)
	sqDistances = sqDistances.sum(axis = 1)

	sortedDistIndicies = sqDistances.argsort()

	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(),
			key = operator.itemgetter(1), reverse = True)
	
	return sortedClassCount[0][0]

training = sys.argv[1]
test = sys.argv[2]

group, labels = createDataSet(training)
test_group, test_labels = createDataSet(test)

for k in range(1, 21):
	error_count = 0
	for t in range(0, test_group.shape[0]):
		result = classify(test_group[t], group, labels, k)
		if result != test_labels[t]:
			error_count += 1
	error_rate = error_count / test_group.shape[0] * 100
	print(int(error_rate))
