# Write a Python program to display all future leap years between a starting year and an ending year entered by the user.
start=int(input("Enter the starting year: "))
end=int(input("Enter the edning year: "))
for year in range(start,end):
    if year % 4==0:
        print(year)
    elif year % 100 == 0:
        continue
    elif year % 400 == 0:
        print(year) 
        