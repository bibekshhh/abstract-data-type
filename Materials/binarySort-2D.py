# import random

# arr = [[random.randint(0,100) for i in range(0,2)] for y in range(0, 10)]

# print(arr)

# for x in range(len(arr)):
#     for y in range(len(arr) -1):
#         for z in range(len(arr) - y-1):
#             if (arr[x][z] > arr[x][z+1]):
#                 arr[x][z], arr[x][z+1] = arr[x][z+1], arr[x][z]

# print(arr)


array = [
  [12, 18], 
  [ 4,  3], 
  [15,  8]
]

# convert 2d array to ascending order using loop 
for i in range(len(array)):
  for j in range(len(array[i])):
    for k in range(len(array[i])):
      if array[i][j] < array[i][k]:
        temp = array[i][j]
        array[i][j] = array[i][k]
        array[i][k] = temp

# print the result
print(array)
print(array.sort())