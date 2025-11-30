# Write a Python program to find the sum of all items in a list.
start=int(input("Enter the string point : "))
end=int(input("Enter the ending point : "))
result=[]
for number in range(start,end):
    num_str=str(number)
    if len(num_str) == 4:
        if num_str[0] in "02468" and num_str[1] in "02468" and num_str[2] in "02468" and num_str[3] in "02468":
            r= int(number ** 0.5)
            if r*r ==number:
                result.append(number)
print(result)