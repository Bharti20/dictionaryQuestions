# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]  
# List3=dict(zip(list1, list2))
# print(List3)

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]  
dictionary = {}
for n in range(len(list1)):
    dictionary[list1[n]]=list2[n]
print(dictionary)


list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]  
itretor=zip(list1, list2)
pair_of_list=list(itretor)
dictionary=dict(pair_of_list)
print(dictionary)