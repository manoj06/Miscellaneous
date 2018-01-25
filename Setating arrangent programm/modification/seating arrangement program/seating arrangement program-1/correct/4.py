import random
a=open("rgukt.txt","r")
b=list(a)
d=dict()
for i in b:
	k=i.split()
	d[k[0]]=k[1]
key=d.keys()
seat=["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9","B0","B1","B2","B3","B4","B5","B6","B7","B8","B9","C0","C1","C2","C3","C4","C5","C6","C7","C8","C9","D0","D1","D2","D3","D4","D5","D6","D7","D8","D9","E0","E1","E2","E3","E4","E5","E6","E7","E8","E9"]
empty=[]
do=dict()
s=[]
kappa=["k1","k2","k3","k4","k5","k6","k7","k8","k9","k10","k11","k12","l1","l2","l3","l4","l5","l6","l7","l8","l9","l10","l11","l12","p1","p2","p3","p4","p5","p6","p7","p8","m1","m2","m3","m4","m5","m6","m7","m8"]
while True:
	for i in kappa:
		s=[]
		while True:
			tw=random.randint(0,len(key)-1)
			yer=random.randint(0,len(seat)-1)
			yu=seat[yer]
			if tw not in empty:
				if yu not in s:
					empty.append(tw)
					s.append(yu)
					nre=50
					we=open("rgu.odt","a")
					we.write("\n")
					for l in range(nre):
						we.write("-")
					we.write("\n")
					we.write("|")
					we.write(key[tw])
					we.write(" |")
					we.write(d[key[tw]])
					wer=30-len(d[key[tw]])
					mine=" "*wer
					we.write(mine)
					we.write("|")
					we.write(i)
					we.write("   |")
					we.write(yu)
					we.write("|")
			if len(s)==50:
				break
	if i=="m8":
		break
