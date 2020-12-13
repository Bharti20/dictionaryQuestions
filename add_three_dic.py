dic1= {1:10,2:20}
dic2= {1:30, 2:40}
dic3={1:50, 3:60} 
length= len(dic1)+len(dic2)+len(dic3)
sum=0
sum2=0
sum3=0
index=0
dic4={}
while index<=length:
    if index in dic1.keys() and index in dic2.keys() and index in dic3.keys():
        sum=dic1[index]+ dic2[index]+dic3[index]
    elif index in dic1.keys() and index in dic2.keys():
        sum2=dic1[index]+ dic2[index]
        dic4[index]=sum2
    elif index in dic2.keys() and index in dic3.keys(): 
        sum3=dic2[index]+ dic3[index]
        dic4[index]=sum3
    index=index+1
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
dic4[1]=sum2
dic4[2]=sum
print(dic4)