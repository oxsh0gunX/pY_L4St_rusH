# Using list comprehension, extract all positive numbers from the list:
input_list=[-5, 10, 30, -45, -3, 33, -12, 24]
output_list=[]
for x in input_list:
    if x >= 1:
        output_list.append(x)

print(output_list)
        