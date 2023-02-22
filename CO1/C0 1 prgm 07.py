"""7. Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums 
to same value (c) whether any value occur in both"""
l1=[10,11,12,13,14,15,16,17,18,19,20]
l2=[11,12,33,44,55,66,77,88,99,100]
if len(l1)==len(l2):
    print("Length equal")
else:
    print("Length is different")
if sum(l1)==sum(l2):
    print("Sum is equal")
else:
    print("Sum is Different")
l3=[]
print("Elements that matched are")
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if l1[i]==l2[j]:
            l3.append(l1[i] and l2[j])
            
        else:
            continue
print(l3)
        

