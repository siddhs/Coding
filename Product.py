# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Asked in UBER

def product(input):
    tmp = 1
    i = 0
    result = []
    while i < len(input):
        tmp = 1
        j = 0
        while j < len(input):
            if i !=j:
                tmp = tmp * input[j]
            j += 1
        result.append(tmp)
        i += 1
    return result

input = [1,2,3,4,5]
input1 = [3, 2, 1]
print(product(input))
print(product(input1))