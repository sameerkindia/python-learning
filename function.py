from functools import reduce

# What is function

def hello(name):
    return f'hello {name}'


# print(hello('sameer'))


# What is pure function
# Pure function doesn't change outside world (scoop)

myArr = [1, 2, 3]

newList = []


def multiplyArr(arr):

    # If we use print we cause a side effect becouse it print someting on outside
    # |||
    # print(arr , "this is arr")

    newArr = []
    for item in arr:
        # This also cause side effect
        # |||
        # newList.append(item ** 3)

        newArr.append(item ** 2)

    return newList
    # return newArr


newArr = multiplyArr(myArr)

# print(myArr)
# print(newArr)


x = 10

def add_impure(a, b):
    return a + b + x


# print(add_impure(10,220))


arr = [1, 2, 3, 4]

def add_to_array(a):
    arr.append(a)
    return arr

# print(add_to_array(10))
# print(add_to_array(10))
# print(add_to_array(10))
# print(add_to_array(10))
# print(add_to_array(10))



# numArr = [1,2,3,4]

# Isme ye error hai ki array ki length badhti hi jaa rahi hai

# def impure_function():
#     for item in numArr:
#         numArr.append(item ** 2)
    

# impure_function()
# print(numArr)



# map(), filter(), zip() or reduce() functions

numbers = [1,2,3,4,5]

def multiply_by2(num):
    return num * 2

def power_of2(num):
    return num ** 2

def filter_odd(num):
    if(num % 2 != 0):
        return num

# print(list(map(multiply_by2 , numbers)))
# print(list(map(power_of2 , numbers)))

# print(list(filter(filter_odd, numbers)))


names = ['sahil', 'sameer', 'haasem']
ages = [27, 35, 3]
cites = ['pali', 'pali', 'pali']

# Combine names and ages using zip()
# zipped = zip(names, ages, cites)

# Convert zip object to list
# print(list(zipped))



def add(acc, num):
    return acc + num

def multiply(acc, num):
    # print(f'acc is {acc} , num is {num}')
    return acc * num

numbers = [1, 2, 3, 4, 5]

# Use reduce with the 'add' function
result = reduce(add, numbers, 10)
result2 = reduce(multiply, numbers, 10)

# print(result) 
# print(result2) 


# Lambda


lambda_multiply = lambda x, y, z: x * y * z

result = lambda_multiply(2, 3, 4)
# print(result)


squared_numbers = map(lambda x: x ** 2, numbers)

# print(list(squared_numbers))


even_numbers = filter(lambda x: x % 2 == 0, numbers)

# print(list(even_numbers))


product = reduce(lambda x, y: x * y, numbers)
product2 = reduce(lambda x, y: x * y, numbers, 2)

# print(product)
# print(product2)


# comprehension
# List comprehension

squares = [x ** 2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]

print(squares)
print(even_numbers)

# Set comprehension

squares_set = {x ** 2 for x in numbers}
print(squares_set)

numbers2 = [1, 2, 3, 4, 5, 6, 2, 4]
even_numbers_set = {x for x in numbers2 if x % 2 == 0}
print(even_numbers_set)

# Dictionary comprehension

squares_dict = {x: x ** 2 for x in numbers}
even_numbers_dict = {x: x ** 2 for x in numbers if x % 2 == 0}

print(squares_dict)
print(even_numbers_dict)