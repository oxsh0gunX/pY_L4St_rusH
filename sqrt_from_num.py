# Write a Python program using list comprehension to read N numbers from the user and print a list of their squares.
input_list=[2,4,6,7,3,12]
output_list=[]
result=0
for number in input_list:
    result=number * number
    output_list.append(result)

print(output_list)