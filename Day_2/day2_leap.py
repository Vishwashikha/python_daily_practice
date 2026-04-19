year = int(input("Enter a year:"))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("No Leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print(" NO leap year")


    #shorter version of code
    year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not leap year")