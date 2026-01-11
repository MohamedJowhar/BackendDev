# import os

# #file
# file=open("example.txt","r")
# content=file.readline()
# print(content)

# file.close()

# #while creating a file use "w" mode
# file2=open("newfile.txt","w")
# file2.write("This is a new file created using Python.")
# file2.close()
# #to append data to existing file use "a" mode
# file3=open("newfile.txt","a")
# file3.write("\nThis line is appended to the file.")
# file3.close()
# #to read file line by line
# file4=open("newfile.txt","r")
# for line in file4:
#     print(line.strip())





# #directory
# # current_directory=os.getcwd()
# # print("Current Directory:",current_directory)



#lambda function
# square=lambda x:x*x
# print(square(5))  # Output: 25

addition=lambda a,b:a+b 
print(addition(3,7))  # Output: 10

#map function
numbers=[1,2,3,4,5]
squared_numbers=map(lambda x:x*x,numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
print(list(squared_numbers))