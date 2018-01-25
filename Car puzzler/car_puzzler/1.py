a=open("words.txt","r")
b=list(a)
d=dict()
for i in b:
	k=i.split()
	for l in range(len(k)-1):
		d[k[l]]=k[l+1]
key=d.keys()
maxi=0
for p in key:
	temp=[]
	for i in range(len(p)):
		temp.append(p[i:])

	count=0
	if len(temp)>maxi:
		for l in temp:
			if l in d:
				count=count+1
			else:
				break
		if count==len(temp):
			print temp,":",count
			maxi=count
