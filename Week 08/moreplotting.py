# More lab work from Week 8
# Made a new file to start from the beginning

import matplotlib.pyplot as plt
import numpy as np
low = 21
high = 65

min_salary = 20000
max_salary = 80000
number_of_entries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)

salaries = np.random.randint(min_salary, max_salary, number_of_entries)
ages = np.random.randint (low, high, size = number_of_entries)

plt.scatter(ages, salaries, color = 'green', label = 'Salaries')

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = 'purple', label = 'X Squared')

plt.title('Random Plot')
plt.xlabel('Salaries')
plt.ylabel('Age')
plt.legend()
# plt.show()

plt.savefig('Prettier-Plot.png')