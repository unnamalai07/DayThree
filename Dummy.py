def findsmallestnumber(number1,number2):
    try:
        
        if number1!=number2:
            if number1<number2:
                result=f"{number1} is a samllest number"
            else:
                result=f"{number2} is a samllest number"
        else:
            result="Number is same"

    except Exception as e:
            result=str(e) 

    finally:
        return result   

if __name__=="__main__":
    try:
        num1=int(input("Enter the number1 "))
        num2=int(input("Enter the number2 "))

    except Exception as e:
            result=str(e) 

    print(findsmallestnumber(num1,num2))         



# With argument and with return type -  1 to 7
# With argument and without return type 8 to 14
# Without argument and with return type 15 to 21
# Without argument and without return type 22 to 30