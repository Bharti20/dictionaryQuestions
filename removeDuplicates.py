dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
dic2=[]
result=dict()
for key, val in dic.items():
     if  key not in dic2:
        dic2.append(key)
        result[key]=val
print(result)


dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
dic2={}
for key in dic:
     if  key not in dic2:
          dic2.update(dic)
print(dic2)
