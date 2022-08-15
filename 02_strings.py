# Exploring strings and methods for string manipulation

a = "Hello World"
#print(type(a))

b = '''this is a 
multiline string with 
name b'''

#print(type(b))
#print(b)

#strings as arrays
#index starts at 0
print(a[0:]) # should print: Hello World
print(a[:-1]) # should print: Hello Worl
print(a[-1:]) # should print: d
print(a[::-1]) #reverse order, should print: dlroW olleH

for x in a : print(x) #looping through string

#concatenating string and int daat types using format()
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#using backslash as escape character
x = "to use double quotes inside a string, I shall use \"backslash\" in this way."
print(x)