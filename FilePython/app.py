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
#for loop
print("For loop from 1 to 5:")
for i in range(8):
    print(i)

#while loop
print("While loop from 1 to 5:")
count = 1 
while count<=6:
    print(count)
    count += 1

    #loop with break and continue
print("Loop with break and continue:")
for i in range(5, 11):
    # if i == 5:
    #     print("Breaking the loop at i =", i)
    #     break
    if i % 2 == 0:
        # print("Skipping even number:", i)
        continue
    print("Current number:", i)


