def findgreatestnumber(number1,number2):
    try:    
        if num1!=num2:
            if num1>num2:
              result=f"{num1} is a greatest number"
            else:
               result=f"{num2} is a greatest number"
        else:
            result="Number is same"
    except Exception as e:
        result=str(e)
    finally:
        return result
try:
    num1=input("Enter the number1 ")
    num2=input("Enter the number2 ")
    try:
          num1=int(num1)
          num2=int(num2)
    except:
          num1=float(num1)
          num2=float(num2)   
except Exception as e:
        result=str(e)
print(findgreatestnumber(num1,num2))
