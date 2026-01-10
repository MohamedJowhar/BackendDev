# class student:
#     def __init__(self,st_id,std_name,st_course):
#         self.st_id=st_id
#         self.std_name=std_name
#         self.st_course=st_course
#     def show_info(self):
#             print(f"Student ID:{self.st_id}, Name: {self.std_name}, Course: {self.st_course}")


# class student_Manager:
#      def __init__(self):
#           self.students=[]
#      def add_students(self,student):
#           self.students.append(student)
#           print("Student added successfully!")

    
#      def show_all(self):
#         if not self.students:
#             print("No students to display.")
#             return
#         for st in self.students:
#             st.show_info()

#      def find_by_id(self,st_id):
#          for st in self.students:
#              if st.st_id==st_id:
#                  st.show_info()
#                  return
        
#                  print("Student not found.")

# # Example usage:
# manager=student_Manager()
# while True:
#     # st_id=input("Enter student ID:")
#     # std_name=input("Enter student name:")
#     # st_course=input("Enter student course:")
#     # student1=student(st_id,std_name,st_course)
#     # manager.add_students(student1)

#     print("\n1. Add Student")
#     print("2. Show All Students")
#     print("3. Search Student")
#     print("4. Exit")
#     choose=input("Choose an option:")
#     if(choose=="1"):
#         st_id=input("Enter student ID:")
#         std_name=input("Enter student name:")
#         st_course=input("Enter student course:")
#         student1=student(st_id,std_name,st_course)
#         manager.add_students(student1)
#         print("Student added successfully!")
#     elif(choose=="2"):
#         manager.show_all()
#     elif(choose=="3"):
#         search_id=input("Enter student ID to search:")
#         manager.find_by_id(search_id)
#     elif (choose == "4"):
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice")



#  



# while True:
#     username=input("Enter username:")
#     password=input("Enter password:")
#     if username=="Admin"  and password=="6666":
#         print("Login successful!")
#         break
#     else:
#         print("Invalid username or password. Please try again.")
             

# class  BankAccount:
#     def __init__(self,balance=100):
#         self.balance=balance
#     def deposit(self,amount):
#          self.balance+=amount
#          print(f"Deposited {amount}. New balance is {self.balance}.")
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("Insufficient balance.")
#         else:
#             self.balance-=amount
#             print(f"Withdrew {amount}. New balance is {self.balance}.")
# # Example usage:
# account=BankAccount()
# while True:
#     print("1. check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")
#     choice=input("Choose an option:")
#     if choice=="1":
#         print(f"Current balance is {account.balance}.")
#     elif choice=="2":
#         amount=int(input("Enter amount to deposit:"))
#         account.deposit(amount)
#     elif choice=="3":
#         amount=int(input("Enter amount to withdraw:"))
#         account.withdraw(amount)
#     elif choice=="4":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")
    


class BankAccount:
    def __init__(self, balance=100):
        self.balance = balance
        self.transactions = []  # List to store all actions

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdraw amount must be positive!")
            return
        if amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("\n=== Transaction History ===")
            for t in self.transactions:
                print("-", t)
            print("===========================")

# -------- Main Program --------
account = BankAccount()

while True:
    print("\n===== BANK MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Transaction History")
    print("5. Exit")
    print("=====================")
    
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Current balance is {account.balance}.")
    elif choice == "2":
        try:
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)
        except ValueError:
            print("❌ Please enter a valid number!")
    elif choice == "3":
        try:
            amount = int(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        except ValueError:
            print("❌ Please enter a valid number!")
    elif choice == "4":
        account.show_transactions()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
