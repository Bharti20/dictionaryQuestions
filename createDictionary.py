def my_function():
    dic={}
    i=0
    while i<2:
        student=input("enter the name")
        marks=int(input("enter the marks"))
        dic[student]=marks
        i=i+1
    return dic
print(my_function())
    