
from abc  import ABC, abstractmethod
#abc ''' Abstract Base Class'''
 
class Animal(ABC):
       @abstractmethod
       def sound(self):
              pass
       

class Dog(Animal):
       def sound(self):
              return "Woof!"
       
class Cat(Animal):
       def sound(self):
              return "Meow!"
       
# Example usage:
dog = Dog()
print(dog.sound())  # Output: Woof!
cat = Cat()
print(cat.sound())  # Output: Meow!
