# Lab Work week 08
# numpy

import numpy as np 

min_salary = 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1)
salaries = np.random.randint (min_salary, max_salary, number_of_entries) 

salaries_plus = salaries + 5000

salaries_mult = salaries * 1.05

print (salaries)
print (salaries_plus)
#print (salaries_mult)

new_salaries = salaries_mult.astype(int)
print (new_salaries)