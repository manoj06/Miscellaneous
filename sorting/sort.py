a=[1,5,7,8,9,2]
empty=[]
m=1
while True:
	for i in range(len(a)):
		count=0
		for k in range(len(a)):
			if a[i]<a[k]:
				count=count+1
		if count==len(a)-m:
			if a[i] not in empty:
				empty.append(a[i])
				m=m+1
	if len(empty)==len(a):
		print empty
		break
