#7.Add 'ing' at the end of a string.If already exist add 'ly'.
string=input("Enter the string:")
if string.endswith('ing'):
    string+='ly'
else :
    string+='ing'
print(string)