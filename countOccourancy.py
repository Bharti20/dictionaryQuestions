word="MISSISSIPPI"
index=0
dic={}
while index<len(word):
    j=0
    count=0
    while j<len(word):
        if word[index]==word[j]:
            count=count+1
        j=j+1
    a=word[index]
    dic[a]=count
    index=index+1
print(dic)