import numpy as np
student_ids = np.arange(1, 11)
print("Student IDs:", student_ids)

#-----------------------------------------------------

import numpy as np
books = np.arange(1, 13)
shelf = books.reshape(3, 4)
print("Books on shelf:\n", shelf)

#------------------------------------------------------

import numpy as np
classroom_seats = np.arange(1, 26).reshape(5, 5)
front_side_seats = classroom_seats[:3, :2]
print("Front side seats:\n", front_side_seats)

#-------------------------------------------------------

import numpy as np
sales_jan = np.array([100, 200, 150, 300, 250])
sales_feb = np.array([120, 190, 160, 310, 240])

monthly_add = sales_jan + sales_feb
monthly_sub = sales_jan - sales_feb
monthly_mul = sales_jan * sales_feb
monthly_div = sales_jan / sales_feb

print("Addition:", monthly_add)
print("Subtraction:", monthly_sub)
print("Multiplication:", monthly_mul)
print("Division:", monthly_div)

#------------------------------------------------------------------

import numpy as np
transformation_matrix = np.array([[1, 2], [3, 4]])
character_position = np.array([[5, 6], [7, 8]])

new_position = np.dot(transformation_matrix, character_position)
print("New character position:\n", new_position)

#----------------------------------------------------------------------

import numpy as np
grid = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

transposed_grid = np.transpose(grid)
print("Transposed grid:\n", transposed_grid)

#----------------------------------------------------------------------

import numpy as np
numbers = np.arange(1, 21)

even_numbers = numbers[numbers % 2 == 0]
print("Even numbers:", even_numbers)

#-----------------------------------------------------------------------

import numpy as np
responses_group1 = np.array([1, 2, 3])
responses_group2 = np.array([4, 5, 6])

all_responses = np.concatenate((responses_group1, responses_group2))
print("All survey responses:", all_responses)
