# Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.
num_1=22
num_2=44
result=[]
if num_1>num_2:
    temp=num_1
else:
    temp=num_2

for num in range(2,temp):
    if num_1 % num ==0 and num_2 % num ==0:
        result.append(num)
print(result[-1])