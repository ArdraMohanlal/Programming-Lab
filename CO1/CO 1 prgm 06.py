#6. Store a list of first names. Count the occurrences of ‘a’ within the list
names=['Ashik','Lishan','Abdullah','Liyona','Aaaardhra']
count=0
for i in names:
    count+=i.count('a')
print("Occurence of 'a' in list:",count)  