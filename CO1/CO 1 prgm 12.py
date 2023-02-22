# 12.Accept a file name from user and print extension of that.
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is :", (f_extns[-1]))
