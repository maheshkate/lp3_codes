from turtle import color
import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    
    #number of observations/points
    n = np.size(x)

    #mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    #calculate cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    #calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0,b_1)

def plot_regression_line(x,y,b):

    #plotting the actual points as scatter plot
    plt.scatter(x,y,color='m',marker='o',s=30)

    #predicted response vector
    y_pred = b[0] + b[1] * x

    #plotting the regression line
    plt.plot(x,y_pred,color='g')

    #putting labels
    plt.xlabel('X')
    plt.ylabel('Y')

    #function to show plot
    plt.show()

def main():
    x = np.array([10,9,2,15,10,16,11,16])
    y = np.array([95,80,10,50,45,98,38,93])
    
    #estimation coefficients
    b = estimate_coef(x,y)

    print("Estimated corffcients:\nb_0 = {} \nb_1 = {}".format(b[0],b[1]))

    #plotting the regression line
    plot_regression_line(x,y,b)

if __name__ == "__main__":
    main()