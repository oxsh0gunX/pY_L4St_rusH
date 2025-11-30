# Write a Python program that reads n numbers into a list, and creates two separate lists:
input_list=[5, 12, 7, 20, 13]
odd_list=[]
even_list=[]
for x in input_list:
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)
    
print(odd_list)
print(even_list)