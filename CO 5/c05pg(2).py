#Write a python program to copy odd lines of one file to another.
fn=open("sample.txt",'r')
fn1=open("new.txt",'w')
rl=fn.readlines()
for i in range(0,len(rl)):
    if (i % 2!=0):
        fn1.write(rl[i])
    else:
        pass
fn1.close()
fn1=open("new.txt",'r')
rlnew=fn1.read()
print(rlnew)
fn.close()
fn1.close()