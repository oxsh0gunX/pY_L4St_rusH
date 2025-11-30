list_item=["python", "java", "machinelearning", "AI"]
longest=""
result=[]
for item in list_item:
    if len(item) > len(longest):
        longest=item
    
print(longest)

    
