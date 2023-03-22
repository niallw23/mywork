# More lab work from Week 8
# Made a new file to start from the beginning

import matplotlib.pyplot as plt
import numpy as np

min_salary = 20000
max_salary = 80000
number_of_entries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)

salaries = np.random.randint(min_salary, max_salary, number_of_entries)

plt.hist(salaries)
plt.show()