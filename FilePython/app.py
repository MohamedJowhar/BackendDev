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
num_int = 10
num_float = 2.5
num_new = num_int + num_float
print("Data type of num_new:", num_new)

#Explicit type conversion
num_str = "100"
num_converted = int(num_str)
print("Converted number:", num_converted+6, "Data type:", type(num_converted))

y=5
x=0
m=bool(y)
print("Converted boolean:", m, "Data type:", type(m))
n=bool(x)
print("Converted boolean:", n, "Data type:", type(n))

#type casting to string
a=123
b=str(a)
print("Converted string:", b, "Data type:", type(b))

#type casting to float
c=7 
d=float(c)
print("Converted float:", d, "Data type:", type(d))

m=2.5
n=int(m)
print("Converted integer:", n, "Data type:", type(n))





