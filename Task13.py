def findleapyear(year):
    try:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
           result= (f"{year} is a leap year")
        else:
            result=(f"{year} is not a leap year")
    except Exception as e:
        print (str(e))
    finally:
        print(result)
try:
     year = int(input("Enter a year: "))
except Exception as e:
    print(str(e), "--- Please enter a valid integer for the year.")
findleapyear(year)
