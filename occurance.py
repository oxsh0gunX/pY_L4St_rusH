# Write a Python program to count the occurrences of each word in a given line of text
strings=" hy python i love you python"
string_slpit=strings.split()
op={}
# len_str=len(string_slpit)
for string in string_slpit:
    if string in op:
        op[string]+=1
    else:
        op[string]=1
print(op)