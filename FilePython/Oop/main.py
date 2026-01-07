from person import person
from person import MathOperations

p1=person("Alice",30,"Female","123 Main St")
p1.age2=31
p1.display()
print("District:",person.district)
# print(p1.name2)
# print(p1.age2)
# print(p1.gender2)
# print(p1.address2)
result_add = MathOperations.add(10, 5)
print("Addition:", result_add)  # Output: 15
result_subtract = MathOperations.subtract(10, 5)
print("Subtraction:", result_subtract)  # Output: 5