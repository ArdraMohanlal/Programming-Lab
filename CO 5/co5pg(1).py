#1. Write a Python program to read a file line by line and store it into a list.
#print([line.strip() for line in open("sample.txt",'r')])
obj=open("sample.txt",'r')
rl=obj.readlines()
print("File line by line in list")
print(rl)
#removing newline character
rl=[x.strip() for x in rl]
print("File line by line post removing newline")
print(rl)
#obj.close()