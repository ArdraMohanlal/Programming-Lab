"""8. Get a string from an input string where all occurrences of first character replaced with 
‘$’, except first character."""
str=input("Enter the string")
char=str[0]
str=str.replace(char,'$')
print(char+str[1:])