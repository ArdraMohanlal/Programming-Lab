# 5.Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
n=int(input("Enter the number of elements:"))
list=[]
for i in range (0,n):
    number=int(input("Enter the number:"))
    if number>100:
        list.append("over")
    else:
        list.append(number)
print("The output is",list)        
