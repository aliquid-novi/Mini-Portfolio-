year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    #  Write the if-elif-elif-else block here.
    if year % 4 != 0:
        print("Tis a common year")
    elif year % 100 != 0:
        print("Tis a leapity leap")
    elif year % 400 != 400:
        print("Tis a commony com")
    else:
        print("Leap year babyyy")
