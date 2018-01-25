l=[["a1","b1","c1","d1","e1"],["a2","b2","c2","d2","e2"],["a3","b3","c3","d3","e3"],["a4","b4","c4","d4","e4"],["a5","b5","c5","d5","e5"]]
k=[]
m=[]
n=[]
p=[]
r=[]
s=[]
for i in range(len(l)):
	if i==0:
		for o in range(len(l[i])):
			if l[i][o]=="a5":
				s.append("1")
			else:
				s.append(l[i][o])
	if i==1:
		for o in range(len(l[i])):
			if l[i][o]=="a5":
				k.append("1")
			else:
				k.append(l[i][o])
	if i==2:
		for o in range(len(l[i])):
			if l[i][o]=="a5":
				m.append("1")
			else:
				m.append(l[i][o])
	if i==3:
		for o in range(len(l[i])):
			if l[i][o]=="a5":
				n.append("1")
			else:
				n.append(l[i][o])
	if i==4:
		for o in range(len(l[i])):
			if l[i][o]=="a5":
				p.append("1")
			else:
				p.append(l[i][o])
	if i==5:
		for o in range(len(l[i])):
			if l[i][o]=="a5":
				s.append("1")
			else:
				s.append(l[i][o])
print k
print m
print n
print p
print s
y.append(s)
y.append(k)
y.append(m)

 

