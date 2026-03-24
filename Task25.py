def findsmallertnumber():
    num1=4
    num2=1
    num3=2
    try:
        if num1 < num2 and num1 < num3:
            result = num1
        elif num2 < num1 and num2 < num3:
            result = num2
        else:
            result = num3

        print(f"The smallest number is: {result}")
    except Exception as e:
        result=str(e)
    finally:
        print(result)
findsmallertnumber()