def findless_greater_100():
    num1=89.5
    try:
        try:
            num1=int(num1)
        except:
            num1=float(num1)
        if num1<100:
            result=f"{num1} is less than 100" 
        else:
            result=f"{num1} is greater than 100"
    except Exception as e:
            print=str(e)
    finally:
         return result
print(findless_greater_100())

    

