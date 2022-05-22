from turtle import color
import matplotlib
import numpy as np
import pandas as pd
from copy import deepcopy
from matplotlib import pyplot as plt

dataset = {
    'Points' : ['P1','P2','P3','P4','P5','P6','P7','P8',],
    'x_coordinate' : [0.1,0.15,0.08,0.16,0.2,0.25,0.24,0.3],
    'y_coordinate' : [0.6,0.71,0.9,0.85,0.3,0.5,0.1,0.2]
}

df = pd.DataFrame(dataset,columns=['Points','x_coordinate','y_coordinate'])

def dist(a,b,ax = 1):
    return np.linalg.norm(a - b,axis=ax)

k = 2

f1 = df['x_coordinate'].values
f2 = df['y_coordinate'].values

X = np.array(list(zip(f1,f2)))
print(X)
centroid_m1 = list(X[0])
centroid_m2 = list(X[7])

centroids = np.array([centroid_m1,centroid_m2])

c_old = np.zeros(centroids.shape)

clusters = np.zeros(len(X))
error = dist(centroids,c_old,None)
print(error)

while error != 0:
    for i in range(len(X)):
        distances = dist(X[i],centroids)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    c_old = deepcopy(centroids)
    print(c_old)

    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        centroids[i] = np.mean(points,axis=0)
        print(centroids[i])
    error = dist(centroids,c_old,None)

colors = ['r','g']
fig,ax = plt.subplots()
for i in range(k):
    points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
    print("Centroid",i)
    print(points)
    ax.scatter(points[:,0],points[:,1],s = 7,c=colors[i])

ax.scatter(centroids[:,0],centroids[:,1],marker='*',s = 200,c = '#050505')

print(centroids)