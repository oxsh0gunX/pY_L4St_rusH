# Write a Python program to read a list of integers.
# For every number greater than 100, store the word "over" instead of the number.
num_list=[1,234,234,23,43]
result=[]

for num in num_list:
    if num < 100 :
        result.append(num)
    elif num > 100:
        result.append("over")
print(num_list)
print(result)