## Wanyee Stephen 100565 ICS4A

import numpy as np


# Calculates the area under curve using trapezoidal rule
def trapezoidal_rule(x, y):
    subintervals = x.size - 1
    y_right = y[1:]  # right endpoints
    y_left = y[:-1]  # left endpoints
    a = x[0]
    b = x[-1]
    dx = (b - a)/subintervals
    area = (dx/2) * np.sum(y_right + y_left)
    return area

# Define the coordinates
x = np.array([0, 2, 4, 6, 8, 10])
y = np.array([4, 6, 6, 4, 4, 5])

print("Area under the curve: ", trapezoidal_rule(x,y))
