#List Comprehension
#(c)From list of vowels selected from a given word
v=['A','E','I','O','U','a','e','i','o','u']
w=str(input("Enter the word:"))
s=[i for i in w if i in v]
print(s)