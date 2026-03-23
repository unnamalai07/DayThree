def findbetween_1_and_100():
    num1=101
    try:
        try:
            num1=int(num1)
        except:
            num1=float(num1)      
        if num1>=1 and num1<=100:
            result=f"{num1} is between 1 and 100"  
        else:
            result=f"{num1} is not between 1 and 100"
    except Exception as e:
        print=str(e)
    finally:
        return result
print(findbetween_1_and_100())

    



