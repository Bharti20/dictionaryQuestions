my_list=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
    ]
List=[]
for dic in my_list:
    for key in dic:
        if (dic[key])not in List:
            List.append(dic[key])
print(List)
        