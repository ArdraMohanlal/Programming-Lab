#6.count the number of characters(count frequency) in a string.
text=str(input("Enter a string"))
c=0
for i in text:
    if i =="":
        continue
    else:
        c=c+1
print(c)