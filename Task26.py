def isuppercase_IsLowercase():
    char="I"
    try:
        if char.isupper():
            result=(f"{char} is an uppercase character.")
        elif char.islower():
            result=(f"{char} is a lowercase character.")
        else:
            result=(f"{char} is not an alphabetic character.")
    except Exception as e:
        result=str(e)
    finally:
        print(result)
isuppercase_IsLowercase()


