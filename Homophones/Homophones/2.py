a=open("words.txt","r")
s=list(a)
g=dict()
for j in s:
	f=j.split()
	for k in range(len(f)-2):
		l=f[k]
		o=f[k+1]
		g[l]=o
d="wrack"
l=d[1:]
h=d[0]+d[2:]
if l in g:
	if h in g:
		print "True"
	else:
		print "False"
else:
	print "False" 
