
class Animal:
    def __init__(self,name,):
        self.name=name
    def show1(self):
        return f"Animal name is {self.name}"
        

class Dog(Animal):
    def __init__(self, name,sound):
        self.sound=sound
        super().__init__(name)
    def show(self):
        return f"sound is {self.sound}"

    
    # def bark(self):
    #     return f"{self.name} says Woof!"

# Example usage:
dog1 = Dog("Buddy", "Woof")
print(dog1.show1())  # Output: Buddy
print(dog1.show())  # Output: sound is Woof

#multible inheritance
class Father:
    def gardening(self):
        return "I enjoy gardening."
class Mother:
    def cooking(self):
        return "I love cooking."
    
class Child(Father, Mother):
    @staticmethod
    def chook():
         print("hello")
    def playing(self):
        return "I like playing."
# Example usage:

class math:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
   

class child(math):
     sum=math.x+math.y
     

class xog(child):
    def display(self):
        print("The sum is:",self.sum)
obj=xog()
obj.display()



child1 = Child()
Child.chook()
print(child1.gardening())  # Output: I enjoy gardening.
print(child1.cooking())    # Output: I love cooking.
print(child1.playing())    # Output: I like playing.
