l=[]
f=open("anagram.txt","r")
for line in f:
    word = line.strip().lower()
    l.append(word)
f.close()

empty_list=[]
d={}
for i in range(len(l)):
    temp=sorted(l[i])
    temp=''.join(temp)
    print temp
    t=[]
    if l[i] not in empty_list:
        for j in range(i+1,len(l)):
            key=''.join(sorted(l[j]))
            if temp==key:
                empty_list.append(l[j])
                t.append(l[j])        
        d[l[i]]=t



for k,v in d.items():
    print k,":",v
