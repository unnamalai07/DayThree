def findpositivenumber(number):
    try:    
        if number>=0 :
            result="Positive number"
        else:
            result="Negative number"
    except Exception as e:
        result=str(e)
    finally:
         return result
if  __name__=="__main__":
    try:
        num=int(input("Enter the number "))
    except Exception as e:
         result=str(e)
    print(findpositivenumber(num))     
    

