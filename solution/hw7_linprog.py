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

# Demographic population sizes
n1 = 75000   # 16-20 year olds
n2 = 200000  # 21-35 year olds
n3 = 350000  # 36+ year olds

# Changes in probability for commercials A, B, C within each demographic
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

# Probabilities that someone in each age group will drink and drive in a month
p1 = 0.1
p2 = 0.15
p3 = 0.12


### Define objective and constraint parameters for scipy.optimize.linprog ###

# x_a, x_b, x_c coefficients in objective
c_a = -1 * (dp_a1*n1 + dp_a2*n2 + dp_a3*n3)
c_b = -1 * (dp_b1*n1 + dp_b2*n2 + dp_b3*n3)
c_c = -1 * (dp_c1*n1 + dp_c2*n2 + dp_c3*n3)
c = np.array([c_a, c_b, c_c])

# Flip sign of objective coefficients to turn maximization into minimization
# (scipy.optimize.linprog minimizes objective)
c_LP = -1 * c

# Budget constraint: Probabilities above per $10k spent, so in these units,
# (x_a + x_b + x_c) less than or equal to 3
x = [1, 1, 1]
x_ub = 3

# Upper bound constraint coefficients
A_ub = np.array([-dp[:,0], dp[:,0], -dp[:,1], dp[:,1], -dp[:,2], dp[:,2], x])

# Upper bound constraint constants
b_ub = np.array([p1, 1-p1, p2, 1-p2, p3, 1-p3, x_ub])


### Optimize/solve linear program with scipy linprog ###
result = LP(c_LP, A_ub, b_ub)
print(result)
