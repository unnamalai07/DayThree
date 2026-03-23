def findevenodd(number):
    try: 
        if num%2==0 :
            result="even number"
        else:
            result="odd number"       
    except Exception as e:
        result=str(e)
    finally:
        return result 
try:
    num=input("Enter the number ")
    try:
        num=int(num)
    except Exception as e:
        num=float(num)
except Exception as e:
    result=str(e)
print(findevenodd(num))
        