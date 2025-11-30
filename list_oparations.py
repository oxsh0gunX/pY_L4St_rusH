# Given two lists of integers, write a Python program to check:

# 1️⃣ Whether both lists have the same length
# 2️⃣ Whether the sum of both lists is the same
# 3️⃣ Whether any common elements exist (print them)

list_1=[3,4,5,6,]
list_2=[3,4,5,6,]

len_list1=len(list_1)
len_list2=len(list_2)
if len_list1 == len_list2:
    print("same lenght")
else:
    print("not same lenght")

sum_list1=sum(list_1)
sum_list2=sum(list_2)
if sum_list1 == sum_list2:
    print("same sum")
else:
    print("difrend sum")

print("Common number ")
for same in list_1:
    if same in list_2:
        print(same)