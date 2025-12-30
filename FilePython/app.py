# print("Hello,world!")

#identation test
# if True:
#     print("This is a simple Python application.")

#Single-line comment: starts with #

#Multi-line comment: enclosed in triple quotes
"""
This is a multi-line comment.
It can span multiple lines.
Useful for documentation.
"""

#variables and data types
# #number
# age = 25  # integer
# height = 5.9  # float
# z=3+4j #complex number
# # print(age, height,z)
# print(f"Age :{age}, height :{height}")
# #string
# name = "Alice"
# print(name.upper())
# #boolean
# is_student = True
# print(f"Is student: {is_student}")


#Basic input/output
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")
# user_age = int(input("Enter your age: "))
# print(f"You are {user_age} years old.")

#implicit type conversion
# num_int = 10
# num_float = 2.5
# num_new = num_int + num_float
# print("Data type of num_new:", num_new)

# #Explicit type conversion
# num_str = "100"
# num_converted = int(num_str)
# print("Converted number:", num_converted+6, "Data type:", type(num_converted))

# y=5
# x=0
# m=bool(y)
# print("Converted boolean:", m, "Data type:", type(m))
# n=bool(x)
# print("Converted boolean:", n, "Data type:", type(n))

# #type casting to string
# a=123
# b=str(a)
# print("Converted string:", b, "Data type:", type(b))

# #type casting to float
# c=7 
# d=float(c)
# print("Converted float:", d, "Data type:", type(d))

# m=2.5
# n=int(m)
# print("Converted integer:", n, "Data type:", type(n))


# #arithmetic operations
# a = 15
# b = 4
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Modulus:", a % b)
# print("Exponentiation:", a ** b)
# # operator precedence
# result = a + b * 2
# print("Result of a + b * 2:", result)
# result = (a + b) * 2
# print("Result of (a + b) * 2:", result)
# #modulus operator
# x = 29
# y = 5   
# print("Remainder when", x, "is divided by", y, "is:", x % y)

# #comparison operators
# x = 10
# y = 20
# print("x == y:", x == y)
# print("x != y:", x != y)
# print("x > y:", x > y)
# print("x < y:", x < y)
# print("x >= y:", x >= y)
# print("x <= y:", x <= y)

# #logical operators
# a = True
# b = False
# print("a and b:", a and b)
# print("a or b:", a or b)    
# print("not a:", not a)

# c=10
# d=20
# print (c< d and c!=d)
# print (c< d or c==d)
# print (not(c< d))

# #assignment operators
# x = 5
# print("Initial value of x:", x) 
# x += 3
# print("After x += 3:", x)   
# x -= 2
# print("After x -= 2:", x)


# #membership operators
# my_list = [1, 2, 3, 4, 5]
# print("3 in my_list:", 3 in my_list)
# print("6 not in my_list:", 6 not in my_list)

# #identity operators
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# print("a is b:", a is b)
# print("a is c:", a is c)
# print("a is not c:", a is not c)




# #If statements
# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive.")
# elif num == 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")

# #if nested statements
# age=int(input("Enter your age: "))
# gender=input("Enter your gender (M/F): ")
# if age>=18:
#     if gender.upper()=='M':
#         print("You are an adult male.")
#     elif gender.upper()=='F':
#         print("You are an adult female.")
#     else:
#         print("Invalid gender input.")
# else:
#     print("You are a minor.")


#loops
# #for loop
# print("For loop from 1 to 5:")
# for i in range(8):
#     print(i)

# #while loop
# print("While loop from 1 to 5:")
# count = 1 
# while count<=6:
#     print(count)
#     count += 1

#     #loop with break and continue
# print("Loop with break and continue:")
# for i in range(5, 11):
#     # if i == 5:
#     #     print("Breaking the loop at i =", i)
#     #     break
#     if i % 2 == 0:
#         # print("Skipping even number:", i)
#         continue

#     print("Current number:", i)


#     #do-while loop simulation
# print("Do-while loop simulation:")


# for i in range(1):   # how many stars per row
#     for j in range(i): # repeat star printing i times
#         print("*", end="")
#     print()            # go to next line



#functions
def greet():
    print("Hello! Welcome to the Python application.")

greet()


# def greet_user(name):
#     print(f"Hello, {name}! Welcome to the Python application.")

# user_name = input("Enter your name: ")
# greet_user(user_name)

# def add_numbers(a, b):
#     return a + b    
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = add_numbers(num1, num2)
# print(f"The sum of {num1} and {num2} is: {result}")

# # def factorial(n):
# #     if n == 0 or n == 1:
# #         return 1  
# #     else:
# #         return n * factorial(n - 1) 


# #excrise
# def iseven(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# print(iseven(4))  # True
# print(iseven(7))  # False



# #maxima of three numbers
# def max_of_three(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print(max_of_three(10, 5, 8))  # 10
# print(max_of_three(3, 15, 7))  # 15

# #reverse a string
# def reverse_string(s):
#     return s[::-1]  
# print(reverse_string("hello"))  # "olleh"

# #pow of a number
# def power(base, exponent=2):
#     return base ** exponent
# print(power(3))      # 9
# print(power(2, 3))   # 8
      

#       #sum all numbers
# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(1, 2, 3))        # 6

#list
# my_list = [10, 20, 30, 40, 50]
# print("Original list:", my_list)
# print("First element:", my_list[0])
# print("Last element:", my_list[-1])
# my_list.append(60)
# print("After appending 60:", my_list)
# my_list.remove(30)
# print("After removing 30:", my_list)
# print("Length of the list:", len(my_list))
# print("Slicing the list (index 1 to 3):", my_list[0:2])
# print("Iterating through the list:")
# for item in my_list:
#     print(item)
# # #tuple
# my_tuple = (1, 2, 3, 4, 5)    
# print("Original tuple:", my_tuple)
# print("First element:", my_tuple[0])

# print("Last element:", my_tuple[-1])
# #sets
# my_set = {1, 2, 3, 4, 5}
# print("Original set:", my_set)
# my_set.add(6)
# print("After adding 6:", my_set)
# my_set.remove(3)
# print("After removing 3:", my_set)
# print("Iterating through the set:")
# for item in my_set:
#     print(item)
# #dictionary
# my_dict={"Name":"Alice","Age":25,"City":"New York"}
# print("Original dictionary:", my_dict)
# print("Name:", my_dict["Name"])
# my_dict["Age"]=26
# print("After updating Age:", my_dict)
# my_dict["Country"]="USA"    
# print("After adding Country:", my_dict)
# print("Iterating through the dictionary:")

# for key, value in my_dict.items():
#     print(f"{key}: {value}")


# for key in my_dict:
#     print(f"{key}: {my_dict[key]}")



