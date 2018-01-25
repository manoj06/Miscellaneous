a=raw_input("E:")
b=int(raw_input("E:"))
v=""
for i in range(len(a)):
	n=ord(a[i])
	m=n+b
	if m>ord("z"):
		k=m-ord("z")
		k=97+k
		m=k
	elif n<ord("Z") and m>ord("Z"):
		k=m-ord("Z")
		k=65+k
		m=k
	v=v+chr(m)
print v

