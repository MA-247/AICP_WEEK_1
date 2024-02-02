# -*- coding: utf-8 -*-
"""AICP_Week_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dha3DnkKuaX8D9GmFHVc63vdN26zicDy
"""

#Task 1
import numpy as np

array = np.arange(30, 71, 2)

print(array)

#Task 2
random_array = np.random.normal(size=15)
print(random_array)

#Task 3

matrix1 = np.matrix([[1,2],
                [3,4]])
matrix2 = np.matrix([[5,6],
                [7,8]])

result = np.cross(matrix1, matrix2)
print(result)

#Task 4

matrix = np.matrix([[1,2],
                   [3,4]])

determinant = np.linalg.det(matrix)
print(int(determinant))

#Task 5

matrix3 = np.array(

                    [
                        [
                            [11,12,13],
                            [14,15,16],
                            [17,18,19],

                        ],
                        [
                            [21,22,23],
                            [24,25,26],
                            [27,28,29],

                        ],
                        [
                            [31,32,33],
                            [34,35,36],
                            [37,38,39],

                        ]
                    ]

)


print("3x3x3 Matrix: \n" , matrix3)

#Task 6

matrix5 = np.random.randint(low=100, size=(5,5,5))

print(matrix5)
print("Minimum Value: ", np.min(matrix5))
print("Maximum Value: ", np.max(matrix5))

matrix = np.matrix([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

#mean along the second axis
mean = np.mean(matrix, axis=1)
print("Mean along the second axis: \n", mean)

#standard deviation along the second axis
std = np.std(matrix, axis=1)
print("Standard deviation along the second axis: \n", std)

#variance deviation along the second axis
std = np.var(matrix, axis=1)
print("Variance along the second axis: \n", std)