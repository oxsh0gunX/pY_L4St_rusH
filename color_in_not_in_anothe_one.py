
# Write a Python program to print all colors from list1 that are NOT present in list2.
color_list1=["green","blue","red"]
color_list2=["green","white"]
result=[]
for color in color_list1:
    if color  in color_list2:
        result.append(color)
print(result)