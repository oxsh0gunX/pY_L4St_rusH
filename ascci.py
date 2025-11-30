# Write a Python program to create a list of ASCII (ordinal) values of each character in a given string using list comprehension.
strings="RaidenShgun"
op_list=[]

for ch in strings:
    ascii=ord(ch)
    op_list.append(ascii)

print(op_list)