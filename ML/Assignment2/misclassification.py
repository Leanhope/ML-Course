import numpy as np 
import random

def misclassification_rate(truth, predictions):
	"""Given two one-dimensional arrays ‘truth‘ and ‘predictions‘
	of the same length, compute the misclassification rate.
	"""
	print(truth)
	print(predictions)
	if len(truth) == len(predictions):
		equal=0
		unequal=0
		size=len(truth)
		for i in range(size):
			if truth[i] == predictions[i]:
				equal += 1
			else:
				unequal += 1
		mis_class_rate = unequal / size
		print("misclassification rate is: ",mis_class_rate )
	else:
		print("Arrays are of length: ",len(truth)," and ",len(predictions),". They have to be the same size!")

def feature_scaling(feature1, feature2):
	"""Given two one-dimensional arrays 'feature1' and ‘feature2‘
	of the same length, this function scales the feature domain to 0<=x<=1
	"""
	max_1 = np.amax(feature1)
	max_2 = np.amax(feature2)
	for i in range(len(feature1)):
		feature1[i] = feature1[i] / max_1
	for i in range(len(feature2)):
		feature2[i] = feature2[i] / max_2

	return feature1, feature2

def feature_scale(feature):
	"""Given an one-dimensional arrays 'feature', this function scales the feature domain to 0<=x<=1
	"""
	max_1 = np.amax(feature)
	for i in range(len(feature)):
		feature[i] = feature[i] / max_1

	return feature

def LMS(x, c_x, learning_rate):
	"""least mean square method"""
	w = np.random.rand(len(x))
	w_0 = 1
	y = w
	ctr = 0
	while ctr < 100:
		ctr += 1
		rand_idx = random.randint(0,len(y)-1)
		for i in range(0,len(y)-1):
			y[i] = w[i]*x[i]

		delta = c_x[rand_idx] - y[rand_idx]
		#not sure
		delta_w = learning_rate * delta * x[rand_idx]
		w[rand_idx] = w[rand_idx] + delta_w

		for i in range(0,len(y)-1):
			summe = pow((c_x[i]-y[i]),2)
			print(summe)	
	print(summe)		
	return w


truth_set = np.array([1,-1,1,-1,1,1,-1])
predi_set = np.array([1,1,-1,-1,1,1,-1])
misclassification_rate(truth_set, predi_set)
feature_one = np.array([500,200,100,300], dtype = float)
feature_two = np.array([1,2,3,4], dtype = float)
print("Before scaling: ", feature_one, " & ", feature_two)
feature_one, feature_two = feature_scaling(feature_one,feature_two)
print("After scaling: ", feature_one, " & ", feature_two)
learn_rate = 1
LMS(predi_set, truth_set, learn_rate)