n=[]
f=open("anagram.txt","r")
k=list(f)
for j in k:
	d=j.split()
	for l in d:
		n.append(l)
f={}
q=[]
for k in range(len(n)):
	z=n[k]
	y=list(z)
	y.sort()
	empty=[]
	if y not in q:
		q.append(y)
		for l in range(len(n)):
			r=n[l]
			s=list(r)		
			s.sort()
			if y==s and r!=z:
				empty.append(r)
		f[z]=empty
print f
for y,m in f.items():
	print y,":",m
	print "" 	
