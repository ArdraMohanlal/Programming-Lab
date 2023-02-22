#Write a python program to read each row from a given csv file and print a list of strings.
import csv as c
fn=open("studentdetails.csv")
rl=c.reader(fn)
for line in rl:
    print(line)