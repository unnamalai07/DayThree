def findsmallestnumber(num1,num2):
    try:
        if num1!=num2:
            if num1<num2:
                result=f"{num1} is a samllest number"
            else:
                result=f"{num2} is a samllest number"
        else:
            result="Number is same"
    except Exception as e:
        result=str(e)
    finally:
      return result
if __name__=="__main__":
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
        print(f"{str(e)}")
    print(findsmallestnumber(num1,num2))


