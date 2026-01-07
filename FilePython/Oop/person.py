class person:
   district="Hodan"  #class variable
   def __init__(self,name,age,gender,address):
       self.name2=name  #instance variable
       self.age2=age
       self.gender2=gender
       self.address2=address
       person.district="Waberi"  #modifying class variable inside constructor

   def display(self):
      print("Name:",self.name2)
      print("Age:",self.age2)
      print("Gender:",self.gender2)
      print("Address:",self.address2)   



#static method

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b
# Example usage:







    