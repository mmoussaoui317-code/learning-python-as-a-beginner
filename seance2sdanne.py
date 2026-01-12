import os

# # create a function that calculate the multiplication 
# def calculate(num1, num2):
#     return num1 * num2

# print(calculate(5, 1)) # this line call the function calculate and send to it the argument

# # this give you the working directory
# print(os.getcwd())

# # to access to the all folders and content of the folder use the following will return an list of the names files and folders in your's directory
# print(os.listdir())

# # create the new folder by use the following
# # print(os.mkdir("nameFolder"))

# #verify the exist of the folder by
# print(os.path.exists("hello.js"))
# print(os.path.exists("nameFolder"))

# # adding the files by the following
# open("fileCreated.py", "w")
# open("fileCreatedToDeleted.py", "w")


# # remove a file from you directory
# os.remove("fileCreatedToDeleted.py")


# we're creating a file text and the directory 
# so now will open it and read there content
fileCreateByVs = open("filetextUTF-8.txt", "r")
fileFromTerminal = open("filetextUTF-8.txt", "r")


print(fileCreateByVs.read()) # use the method read to read the content of the file
print(fileFromTerminal.read())

print(fileCreateByVs.readline()) # Read the first line from your file
print(fileCreateByVs.readlines()) # Read the Content Of the File Like as A list

fileCreateByVs.close()
fileFromTerminal.close()


# # re-open the file and write instead of it

# t = open("filetextUTF-8.txt", 'w') # w key word remove the content of file and replace it by the changes doing

# t.write("hello this change is made by Python code\n") # write in side of the file and go to the new line by '\n'
# t.write("i'm also made by the python Code\n") # this also new line on the file and return to the new line

# print("this is just an overview The Write Completed") # feed back to tell's the operation completed

# t.close()

# # use the 'a' key word to let's the exist content and add the changes

# t = open("filetextUTF-8.txt", 'a')

# t.write("\nhello this change is made by Python code\n") # write in side of the file and go to the new line by '\n'
# t.write("i'm also made by the python Code\n") # this also new line on the file and return to the new line

# print("this is just an overview The Write Completed") # feed back to tell's the operation completed

# t.close()


# three method to add multiples lines in the file by this ->
# listContent = ["\nhello\t", "i'm from the list content\b", "just the file of the content."] #create the list must be added to the file

# fileAdr = open("filetext.txt", "a") # open the file with the mode creation

# fileAdr.writelines(listContent) # use the method writelines to add multiple lines

# fileAdr.close() # close the file

# creation of file from the code python exercise
f = open("menage.txt", "w") # create a file by write mode

f.write("Write what you want\n\t\tYES")

f.close()
 
# os.remove("menage.txt") #-------use the method remove to delete the file created by open method
