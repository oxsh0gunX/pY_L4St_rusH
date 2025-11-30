# Write a Python program to remove all even numbers from a list and keep only the odd numbers.
number_list=[12, 13, 20, 45, 43, 23, 36]
result=[]
for x in number_list:
    if x % 2 == 1:
        result.append(x)
print(result)