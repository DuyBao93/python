import array as arr
import matplotlib.pyplot as plt
import numpy as np 
import linear


if __name__ == "__main__":
    arrX = arr.array('d',[6, 7, 8, 9, 10])
    arrY = arr.array('d',[80, 100, 120, 130, 140])
    b = linear.linear_regression(arrX, arrY)
    b0 = b[1][0]
    b1 = b[1][1]
    print(b[1])
    x0 = np.linspace(5, 10.5, 2)
    y0 = b0 + (b1*x0)
    print(x0)
    print(y0)
    x = (9)
    print(b0 + (b1 * x))
    plt.plot(arrX, arrY, 'ro')
    plt.plot(x0, y0 , 'y')
    plt.axis([3, 11, 60, 160])
    plt.xlabel('year (y)')
    plt.ylabel('height (cm)')
    plt.show()