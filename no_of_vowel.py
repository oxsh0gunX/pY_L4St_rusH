# Write a Python program to count how many times each vowel (a, e, i, o, u) appears in a given string.
name="safvan"
count=0
for x in name:
    if x in "aeiouAEIOU":
        count+=1
print(count)
