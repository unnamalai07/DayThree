def find_largest():
    num1=2
    num2=3
    num3=4
    try:
        if num1 >= num2 and num1 >= num3:
            largest = num1        
        elif num2 >= num1 and num2 >= num3:
            largest = num2        
        else:
            largest = num3
    except Exception as e:
        print(str(e), "--- An error occurred while finding the largest number.")
    finally:
        return largest
print(find_largest())
       