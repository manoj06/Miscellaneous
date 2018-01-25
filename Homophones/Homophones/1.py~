a=open("words.txt","r")
s=list(a)
g=dict()
for j in s:
	f=j.split()
	for k in range(len(f)-2):
		l=f[k]
		o=f[k+1]
		g[l]=o
r=g.keys()
for l in r:
	print l
	if len(l)>=3:
		p=l[1:]
		d=l[0]+l[2:]
		if p and d in g:
			print l
