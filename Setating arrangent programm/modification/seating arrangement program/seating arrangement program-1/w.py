a=open("rgukt.txt")
b=list(a)
c=dict()
for i in b:
	k=i.split()
	c[k[0]]=k[1]
key=c.keys()
no=open("1.txt","a")
for l in key:
	count=0
	if l[0]=="R":
		count=count+1
		if l[1]=="0":
			count=count+1
			if l[2]=="9":
				count=count+1
	if count==3:
		no.write(l)
		no.write(" ")
		no.write(c[l])
		no.write("\n")
	
