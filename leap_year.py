# Write the condition used to check whether a given year is a leap year or not.
year =int(input("enter the year: "))
if year % 4 == 0:
    print("its leapyear")
elif year % 100 :
    print("its not leap year ")
elif year % 400 :
    print("its leap year")