def findeligiblevote(age):
    try:
        if age>=18:
            result=f"{age} eligible for vote"
        else:
            result=f"{age} not eligible for vote"       
    except Exception as e:
        result=str(e)
    finally:
        return result
try:
    age=(input("Enter the age "))
    try:
        age=int(age)
    except:
        age=float(age)
except Exception as e:
    result=str(e)
print(findeligiblevote(age))

    
