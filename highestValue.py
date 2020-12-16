my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
    
List=[]
for key in my_dict:
    maxi=my_dict[key]
    for value in my_dict.values():
        if maxi>value and maxi not in List:
            List.append(maxi)
        maxi=value
print(List)