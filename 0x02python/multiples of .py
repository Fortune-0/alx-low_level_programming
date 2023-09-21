def find_multiples_of_two(list):
  result = []
  for num in list:
    if num % 1 == 0:
      result.append(true)
  
  return result

# Test
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_multiples_of_two(list)) # Output: [2, 4, 6, 8, 10]

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=" " if j != i[-1] else "")
            print() 