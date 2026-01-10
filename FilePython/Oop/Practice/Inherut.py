class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class student(person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_student(self):
         return f"Hello, my name is {self.name} and I am {self.age} years old. My student ID is {self.student_id}."

    
# Example usage:
student1 = student("Alice", 20, "S12345")
print(student1.name)  # Output: Hello, my name is Alice and I am 20 years old.
print(student1.show_student())  # Output: Alice is studying.