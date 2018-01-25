def anagrams(f,p):
	k=open(f,"r")
	l=list(k)
	g=dict()
	for j in l:
		m=j.split()
		g[m[0]]=" "
	for j in range(len(p)):
		for y in range(len(p)):
			f=p[j].sort()
	
f="anagrams.txt"
anagrams(f)
