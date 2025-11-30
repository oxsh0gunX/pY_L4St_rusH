# colors="blue,green,yellow,red"
# color_split=colors.split(',')
# first_color=color_split[0]
# last_color=color_split[-1]
# result=['The first color is :']
num=int(input("Enter the number of the colors: "))
colors=[]
for x in range (num):
    color=input(f"enter the {x }th color: ")
    colors.append(color)


print("the first color is : ",colors[0])
print("the last color is : ",colors[-1])
