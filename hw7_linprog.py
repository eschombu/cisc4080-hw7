''' HW7 Problem 5(d)

Modify the code below to have SciPy's linear program solver, which uses the
simplex algorithm, solve the advertising campaign problem posed in the homework
question. See the documentation here:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

If you do not have python installed on your machine, you can run this
online at https://www.tutorialspoint.com/execute_python_online.php.

'''

import numpy as np
from scipy.optimize import linprog as LP

## Demographic population sizes
n1 = 75000   # 16-20 year olds
n2 = 200000  # 21-35 year olds
n3 = 350000  # 36+ year olds

## Changes in probability for commercials A, B, C within each demographic
dp_a1 =  0.05
dp_a2 = -0.025
dp_a3 = -0.025
dp_b1 = -0.05
dp_b2 =  0.025
dp_b3 = -0.1
dp_c1 = -0.07
dp_c2 = -0.05
dp_c3 =  0.03
dp = np.array([[dp_a1, dp_a2, dp_a3],
               [dp_b1, dp_b2, dp_b3],
               [dp_c1, dp_c2, dp_c3]])

## Probabilities that someone in each age group will drink and drive in a month
p1 = 0.1
p2 = 0.15
p3 = 0.12

## Define objective and constraint parameters for scipy.optimize.linprog


## Optimize/solve linear program with scipy linprog
#result = LP(objective and constraint args...)
#print(result)

'''
While not necessarily true for different settings of the problem parameters,
using the ones given in the problem should result in your full budget being
spent, and tens of thousands fewer (predicted) drunk driving incidents per
month. Please provide your code, the output of `print(result)`, and any other
analysis or output you would like to show that may help to illustrate the
result is correct.
'''
