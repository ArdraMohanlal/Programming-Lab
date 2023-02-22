#Count the occurence of each word in a line of text
text="lets lets get lets started"
words={}
text1=text.split(" ")
for i in text1:
    if i in words:
        words[i]+=1
    else:
        words[i]=1
print(words)        