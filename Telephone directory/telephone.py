def dictionary(v):
	g=open(v,"r")
	k=list(g)
	g=dict()
	for j in k:
		f=j.split()
		for h in range(1):
			g[f[0]]=f[1],f[2]
	print g
def fi(a):
	f=open(a,"a")
	k=int(raw_input("How many numbers do u want to enter:"))
	for i in range(k):
		l=raw_input("Name:")
		j=raw_input("Telephone no:")
		o=raw_input("Adress:")
		f.write(l)
		f.write(" ")
		f.write(j)
		f.write(" ")
		f.write(o)
		f.write("\n")
dictionary("directory.txt")
fi("directory.txt")
		
