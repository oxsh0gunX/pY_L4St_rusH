# Write a Python program to create a list of unique elements from a list (remove duplicates).
num_list=[2,4,5,6,3,6,2,33,5,4,22,55,33]
result=[]
for num in num_list:
    if num not in result:
        result.append(num)
print(result)