dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for val in dict.values():
    for item in val:
        count=count+1
print(count)
    
  