#polymorphsm in python
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Cat(Animal):
    def speak(self):
        return "Cat meows"
# Example usage:
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())
# Output:
# Dog barks
# Cat meows