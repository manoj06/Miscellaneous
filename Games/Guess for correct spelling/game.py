import sys
def f(x,count):
	print x
	d=dict()
	p=open("Game.txt","r")
	c=list(p)
	ne=dict()
	for i in c:
		k=i.split()
		for j in range(1):
			d[k[1]]=k[0]
			ne[k[1]]=k[2]
	user=raw_input("Enter your guess:")
	if user=="H":
		print ne[x]
		return f(x,0)
	elif d[x]==user:
		print "Its correct"
		key=d.keys()
		for i in range(len(key)):
			return f(key[i],count+1)
	else:
		print d[x]
		user=raw_input("Do u want to continue(y/n):")
		if user=="Y":
			key=d.keys()
			for i in range(len(key)):
				return f(key[i],0)
		else:
			print "Your score:",count
			sys.exit()
f("idoswnw",0)

