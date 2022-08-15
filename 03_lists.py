# lists and methods to manipulate lists
# list comprehension

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

list1 = ["abc", 34, True, 40, "male"]
print(type(list1))
print(list1[-1])

thislist[1] = "blackcurrant"
print(thislist)

thislist.append("orange")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

for x in thislist:
  print(x)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

