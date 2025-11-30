# Write a Python program that accepts a list of integers and returns a new list with the squares of all the values.
num_list=['3','4','2']
result_list=[]
y=0
for x in num_list:
    y=int(x) * int(x)
    result_list.append(y)

print(result_list)