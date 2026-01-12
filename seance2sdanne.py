# import os

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

fileCreateByVs.close()
fileFromTerminal.close()
