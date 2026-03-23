vowels=["a","e","i","o","u"]
def findvowels(value):
    try:
        if value in vowels:
            result=(f"{value} is a vowel") 
        else:
            result=(f"{value} is a consonant")
    except Exception as e:
        result=str(e) 
    finally:
        print(result)
try:
    value=input("enter then value ")
except Exception as e:
    result=str(e)
findvowels(value)