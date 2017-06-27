# Birthday Paradox in Python
# Considering that birthday are independant and identiquely distribued
# by a uniform law.
from __future__ import print_function

import numpy as np



def same_birthday(n_people):
    # Generate n birthday dates
    dates = np.random.randint(0, 365, size=n_people)
    
    # If at least 2 people have the same birthday ...
    if len(set(dates)) != len(dates):
        return True
    return False
    


n_people = 23
n_iter = 200000

sum_ = 0.
for _ in range(n_iter):
    sum_ += float(same_birthday(23))
    
print("Probability that in a crowd of", n_people, "people, at least 2 "\
	"have the same birthday:", 100 * sum_ / n_iter, "%")
