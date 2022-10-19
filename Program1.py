#Using NumPy to create random vector of size 15 having only Integers in the range 1-20.

import numpy as np

#printing a random array of size 15 with values between 1 and 20
v=np.random.randint(1,20, size=15)
print("Array of size 15 with random numbers from 1 to 20")
print(v)

#reshaping the array to 3 by 5
new_v=np.reshape(v, (3, 5))
print("\n3 by 5 array")
print(new_v)

print("\nArray after replacing max value with 0")
replace = np.where(new_v == [[i] for i in np.amax(new_v, axis = 1)], 0 ,new_v)
print(replace)

