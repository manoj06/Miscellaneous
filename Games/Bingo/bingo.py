import random
a=[[i for i in range(1,6)],[i for i in range(6,11)],[i for i in range(11,16)],[i for i in range(16,21)],[i for i in range(21,26)]]
b=[[i for i in range(26,31)],[i for i in range(31,36)],[i for i in range(36,41)],[i for i in range(41,46)],[i for i in range(46,51)]]
empty=[]
while True:
	k=random.randint(1,50)
	if k not in empty:
		empty.append(k)
		p=len(a)
		for l in range(p):
			o=a[l]
			h=len(o)
			for g in range(h):
				if o[g]==k:
					del(a[l][g])
					break
		for l in range(len(b)):
			for m in range(len(b[l])):
				if b[l][m]==k:
					del(b[l][m])
					break
	count=0
	for i in a:
		if i==[]:
			count=count+1
	if count==5:
		print "A is winner"
		break
	count=0
	for i in b:
		if i==[]:
			count=count+1
	if count==5:
		print "B is winner"
		break
