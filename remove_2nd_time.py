# Write a Python program to remove duplicate characters from a string
# (but keep the first appearance of each character).
string="programing"
result=""
result_list=[]
for ch in string:
    if ch   not in result:
        result+=ch
print(result)
