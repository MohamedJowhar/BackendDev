class person:
    def greet(self):
        return "Hello from the person class."

class student(person):
    def greet(self):
        return "Hello from the student class."
class teacher(person):
    def greet(self):
        return "Hello from the teacher class."
# Example usage:
people = [person(), student(), teacher()]
for p in people:
    print(p.greet())