import numpy as np

print(np.random.randint(1, 7, 2))  # start, end, number of random numbers
print(np.random.rand(2, 2))  # 2x2 matrix of random numbers between 0 and 1


print(np.eye(3))  # 3x3 identity matrix 
print(np.eye(3, k=1))  # 3x3 matrix with 1s on the diagonal starting from the 1st row
print(np.eye(3,4,2))  # 3x4 matrix with 1s on the diagonal starting from the 2nd column

print(np.zeros((2, 3)))  # 2x3 matrix of zeros
print(np.ones((2, 3)))  # 2x3 matrix of ones
print(np.full((2, 3), 5))  # 2x3 matrix of 5s

# Arthimatic & Mathematical Functions
arr = np.array([1, 2, 3, 4, 5])
print(arr + 2)  # add 2 to each element
print(arr - 2)  # subtract 2 from each element
print(arr * 2)  # multiply each element by 2
print(arr / 2)  # divide each element by 2
print(arr ** 2)  # square each element

print(np.add(arr, 2))  # add 2 to each element
print(np.subtract(arr, 2))  # subtract 2 from each element
print(np.multiply(arr, 2))  # multiply each element by 2
print(np.divide(arr, 2))  # divide each element by 2
print(np.power(arr, 2))  # square each element


# add to arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
print(np.add(arr1, arr2))

print(np.max(arr1))  # maximum value in the array

# sortings
arr = np.array([1, 3, 2, 5, 4])
print(np.sort(arr))  # sort the array
print(np.sort(arr)[::-1])  # sort the array in descending order




