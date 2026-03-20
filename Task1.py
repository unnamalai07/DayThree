def findVowels(value):
    try:
        if value in ["a","e","i","o","u"]:
            result=f"{value} is a vowels"
        else:
            result=f"{value} is a consonant"   
    except Exception as e:
        result=str(e)
    finally:
        return result   

if __name__=="__main__":
    try:
        value=input("Enter a value ")
    except Exception as e:
        print(f"{str(e)}")
    print(findVowels(value))    



