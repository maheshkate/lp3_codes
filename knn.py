from turtle import distance
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import warnings
import math
warnings.filterwarnings('ignore')
import sys

data = {
    'x' : [2,4,4,4,6,6],
    'y' : [4,2,4,6,2,4],
    'label' : ['orange','orange','blue','orange','blue','orange']
}

df = pd.DataFrame.from_dict(data)
label = "label"

def check_data(df,k,input_val,weight,metric):
    if len(input_val) != df.shape[1] - 1:
        print("Proveded input points are invalid")
        return False
    if k > len(df):
        print("K value cannot be greater than size of dataset")
        return False
    if weight not in ['distance','uniform']:
        print("Param weight takes values distance or uniform")
        return False
    if metric not in ['manhattan','euclidean']:
        print("Param metric takes values manhattan or eculidean")
        return False
    return True

def euclidean_distance(point_a,point_b):

    distance = 0
    for i in range(len(point_a)):
        distance = distance + (point_a[i] - point_b[i]) ** 2
    return distance ** 0.5

def manhattan_distance(point_a,point_b):
    distance = 0
    for i in range(len(point_a)):
        distance = distance + abs(point_a[i] - point_b[i])
    return distance

def weighted_prediction(nearest_neighbors):
    label_frequency = {}
    for distance, label in nearest_neighbors:
        if int(distance) == 0:
            label_frequency[label] = sys.maxsize
            break
        if label in label_frequency:
            label_frequency[label] += 1/distance
        else:
            label_frequency[label] = 1/distance
    return max(label_frequency,key=label_frequency.get)

def chooseK(arr):
    print("Size of array: ",arr.shape[0])
    k = round(math.sqrt(arr.shape[0]))
    if k % 2 == 0:
        k = k + 1
    print("Choosen value of K: ",k)
    return k

def KNearestNeighbours(X,Y,k,input_val,weight,metric):
    distances = []
    if metric == 'manhattan':
        for i in range(len(X)):
            distances.append((manhattan_distance(X[i],input_val),Y[i]))
    else:
        for i in range(len(X)):
            distances.append((euclidean_distance(X[i],input_val),Y[i]))
    
    distances.sort(key=lambda distance: distance[0])
    if weight == 'distance':
        nearest_neighbors = distances[:k].copy()
        prediction = weighted_prediction(nearest_neighbors=nearest_neighbors)
    else:
        nearest_neighbors = distances[:k].copy()
        if int(distances[0][0]) == 0:
            prediction = distances[0][1]
            return prediction
        nearest_classes = [label[1] for label in nearest_neighbors]
        prediction = max(set(nearest_classes),key=nearest_classes.count)
    return prediction

k = 3
metric = 'euclidean'
weight = 'uniform'
input_val = [1,4]
X = None
Y = None

if check_data(df,k,input_val=input_val,weight=weight,metric=metric):
    X = df.drop(columns=[label]).values.tolist()
    Y = df[label].values.tolist()
    print("Predicted value: ",KNearestNeighbours(X,Y,k,input_val,weight,metric))


