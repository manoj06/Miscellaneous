d=dict()
l=[]
def store_anagrams():
    f=open("anagram.txt",'r')
    for line in f:
        word=line.strip()
        l.append(word)

    return l

store_anagrams()

empty_list=[]

for i in range(len(l)):
    temp = sorted(l[i])
    temp = ''.join(temp)
    #print temp
    value=[]
    if l[i] not in empty_list:
        for j in range(i+1,len(l)):
            newtemp=sorted(l[j])
            newtemp=''.join(newtemp)
            if temp==newtemp:
                empty_list.append(l[j])
                value.append(l[j])

        #print value

        d[l[i]]=value

#print d
for key,value in d.items():
    print key,":",value
            
    
