def find_child_tennage_adult():
    num=25
    try:
        try:
            num=int(num)       
        except:
            num=float(num)  
        if num<13:
            result="unna is a child"
        elif  num>=13 and num<=18:
            result="unna is a  teenage"
        else:
            result="unna is a  adult"
    except Exception as e:
        print=str(e)
    finally:
        return result
print(find_child_tennage_adult())
    

