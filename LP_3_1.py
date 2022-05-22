import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
# input data
 
x=np.array ( [10, 9, 2, 15, 10, 16, 11, 16] ) 
y=np.array ( [95, 80, 10, 50, 45, 98, 38, 93] ) 
plt. scatter(x, y)

def estimate_coefficient (x, y): 
    #Number of oberservations
    N =np.size (x)
    #calculate mean of x and y 
    x_mean,y_mean=np.mean(x),np.mean(y)
    # calculating cross—deviation and deviation about axsis 
    ss_xy=np.sum (y*x) - N*x_mean*y_mean 
    ss_xx=np.sum (x*x) - N*x_mean*x_mean
    #calculating regression coefficients 
    b1=ss_xy/ss_xx; 
    b0=y_mean-b1*x_mean;
    return ( b0,b1) ;



def plot_regression_line (x, y, b):
    #plotting actual points as scatter points 
    plt.scatter (x, y,color="m", marker="o" , s=30)
    #predicted response vector 
    y_pred=b[0]+b[1]*x
    plt.plot(x,y_pred,color='g') 
    #putting labels 
    plt.xlabel ( "X" ) 
    plt.ylabel ( "Y" )
    # function to show plot 
    plt.show( ) 
	

b=estimate_coefficient(x, y) 
print ("Estimated coefficients: \n b0={} \n bl={}".format(b[0],b[1])) 
# plotting regression line 
plot_regression_line (x, y, b)