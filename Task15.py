def check_Number_divisible_Two_not_Fiv():
    Number=2
    try:
            if (Number % 2 == 0) and (Number % 5 != 0):
                result="Given number is divisible by 2 but not divisible by 5"
            else:
                result="Given number is not divisible by 2 or is divisible by 5"               
    except Exception as e:
        print=str(e)
    finally:
        return result
print(check_Number_divisible_Two_not_Fiv())

