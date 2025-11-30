# Write a Python program to find the length of the longest word in a list.
list_item=["python", "java", "machinelearning", "AI"]
big=""
for item in  list_item:
    if len(item) > len(big):
        big=item

print(f"The largest word is :{big}")
print(f"The length of the largest word is :",len(big))