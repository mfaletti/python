#!/usr/bin/python

f = open("hello.py", "r")
data = f.read()
f.close()
words = data.split(" ")
print("The words in the text are: ")
print(words)
num_words = len(words)
print("The number of words is: ", num_words)
print("The number of lines is: ", len(data.split("\n")))