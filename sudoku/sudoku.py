from Tkinter import *
import random
a=random.randint(1,9)
b=random.randint(1,9)
c=random.randint(1,9)
d=random.randint(1,9)
e=random.randint(1,9)
f=random.randint(1,9)
g=random.randint(1,9)
h=random.randint(1,9)
i=random.randint(1,9)
j=random.randint(1,9)
k=random.randint(1,9)
l=random.randint(1,9)
m=random.randint(1,9)
n=random.randint(1,9)
o=random.randint(1,9)
p=random.randint(1,9)
q=random.randint(1,9)
r=random.randint(1,9)
s=random.randint(1,9)
t=random.randint(1,9)
u=random.randint(1,9)
v=random.randint(1,9)
w=random.randint(1,9)
x=random.randint(1,9)
y=random.randint(1,9)
z=random.randint(1,9)
k1=random.randint(1,9)
b0=[]
b1=[]
b2=[]
b3=[]
b4=[]
b5=[]
b6=[]
b7=[]
b8=[]
a0=[]
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
a6=[]
a7=[]
a8=[]
while a in a0 or a in b1:
	a=random.randint(1,9)
a0.append(a)
b1.append(a)
while b in a0 or b in b3:
	b=random.randint(1,9)
a0.append(b)
b3.append(b)
while c in a0 or c in b8:
	c=random.randint(1,9)
a0.append(c)
b8.append(c)
while d in a1 or d in b0:
	d=random.randint(1,9)
a1.append(d)
b0.append(d)
while e in a1 or e in b4:
	e=random.randint(1,9)
a1.append(e)
b4.append(e)
while f in a1 or f in b6:
	f=random.randint(1,9)
a1.append(f)
b6.append(f)
while g in a2 or g in b2:
	g=random.randint(1,9)
a2.append(g)
b2.append(g)
while h in a2 or h in b5:
	h=random.randint(1,9)
a2.append(h)
b5.append(h)
while i in a2 or i in b7:
	i=random.randint(1,9)
a2.append(i)
b7.append(i)
while j in a3 or j in b0:
	j=random.randint(1,9)
a3.append(j)
b0.append(j)
while k in a3 or k in b3:
	k=random.randint(1,9)
a3.append(k)
b3.append(k)
while l in a3 or l in b6:
	l=random.randint(1,9)
a3.append(l)
b6.append(l)
while m in a4 or m in b1:
	m=random.randint(1,9)
a4.append(m)
b1.append(m)
while n in a4 or n in b5:
	n=random.randint(1,9)
a4.append(n)
b5.append(n)
while o in a4 or o in b8:
	o=random.randint(1,9)
a4.append(o)
b8.append(o)
while p in a5 or p in b2:
	p=random.randint(1,9)
a5.append(p)
b2.append(p)
while q in a5 or q in b4:
	q=random.randint(1,9)
a5.append(q)
b4.append(q)
while r in a5 or r in b6:
	r=random.randint(1,9)
a5.append(r)
b6.append(r)
while s in a6 or s in b0:
	s=random.randint(1,9)
a6.append(s)
b0.append(s)
while t in a6 or t in b3:
	t=random.randint(1,9)
a6.append(t)
b3.append(t)
while u in a6 or u in b7:
	u=random.randint(1,9)
a6.append(u)
b7.append(u)
while v in a7 or v in b1:
	v=random.randint(1,9)
a7.append(v)
b1.append(v)
while w in a7 or w in b5:
	w=random.randint(1,9)
a7.append(w)
b5.append(w)
while k1 in a7 or k1 in b7:
	k1=random.randint(1,9)
a7.append(k1)
b7.append(k1)
while x in a8 or x in b2:
	x=random.randint(1,9)
a8.append(x)
b2.append(x)
while y in a8 or y in b4:
	y=random.randint(1,9)
a8.append(y)
b4.append(y)
while z in a8 or z in b8:
	z=random.randint(1,9)
a8.append(z)
b8.append(z)
fnt=("Arial",16,"bold")
root=Tk()
root.title("Sudoku")
root.geometry("410x390")
frame=Frame(root)
frame.grid()
button10 = Button(frame, font =fnt, text = "  ",
                 fg = "black", bg = "white")
button10.grid(row = 1, column = 0)
button11=Button(frame,font=fnt,text=str(a),fg="black",bg="green")
button11.grid(row=1,column=1)
button12=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button12.grid(row=1,column=2)
button13=Button(frame,font=fnt,text=str(b),fg="black",bg="green")
button13.grid(row=1,column=3)
button14=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button14.grid(row=1,column=4)
button15=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button15.grid(row=1,column=5)
button16=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button16.grid(row=1,column=6)
button17=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button17.grid(row=1,column=7)
button18=Button(frame,font=fnt,text=str(c),fg="black",bg="green")
button18.grid(row=1,column=8)
button20=Button(frame,font=fnt,text=str(d),fg="black",bg="green")
button20.grid(row=2,column=0)
button21=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button21.grid(row=2,column=1)
button22=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button22.grid(row=2,column=2)
button23=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button23.grid(row=2,column=3)
button24=Button(frame,font=fnt,text=str(e),fg="black",bg="green")
button24.grid(row=2,column=4)
button25=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button25.grid(row=2,column=5)
button26=Button(frame,font=fnt,text=str(f),fg="black",bg="green")
button26.grid(row=2,column=6)
button27=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button27.grid(row=2,column=7)
button28=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button28.grid(row=2,column=8)
button30=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button30.grid(row=3,column=0)
button31=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button31.grid(row=3,column=1)
button32=Button(frame,font=fnt,text=str(g),fg="black",bg="green")
button32.grid(row=3,column=2)
button33=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button33.grid(row=3,column=3)
button34=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button34.grid(row=3,column=4)
button35=Button(frame,font=fnt,text=str(h),fg="black",bg="green")
button35.grid(row=3,column=5)
button36=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button36.grid(row=3,column=6)
button37=Button(frame,font=fnt,text=str(i),fg="black",bg="green")
button37.grid(row=3,column=7)
button38=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button38.grid(row=3,column=8)
button40=Button(frame,font=fnt,text=str(j),fg="black",bg="green")
button40.grid(row=4,column=0)
button41=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button41.grid(row=4,column=1)
button42=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button42.grid(row=4,column=2)
button43=Button(frame,font=fnt,text=str(k),fg="black",bg="green")
button43.grid(row=4,column=3)
button44=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button44.grid(row=4,column=4)
button45=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button45.grid(row=4,column=5)
button46=Button(frame,font=fnt,text=str(l),fg="black",bg="green")
button46.grid(row=4,column=6)
button47=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button47.grid(row=4,column=7)
button48=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button48.grid(row=4,column=8)
button50=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button50.grid(row=5,column=0)
button51=Button(frame,font=fnt,text=str(m),fg="black",bg="green")
button51.grid(row=5,column=1)
button52=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button52.grid(row=5,column=2)
button53=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button53.grid(row=5,column=3)
button54=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button54.grid(row=5,column=4)
button55=Button(frame,font=fnt,text=str(n),fg="black",bg="green")
button55.grid(row=5,column=5)
button56=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button56.grid(row=5,column=6)
button57=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button57.grid(row=5,column=7)
button58=Button(frame,font=fnt,text=str(o),fg="black",bg="green")
button58.grid(row=5,column=8)
button60 = Button(frame, font =fnt, text = "  ",
                 fg = "black", bg = "white")
button60.grid(row = 6, column = 0 )
button61=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button61.grid(row=6,column=1)
button62=Button(frame,font=fnt,text=str(p),fg="black",bg="green")
button62.grid(row=6,column=2)
button63=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button63.grid(row=6,column=3)
button64=Button(frame,font=fnt,text=str(q),fg="black",bg="green")
button64.grid(row=6,column=4)
button65=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button65.grid(row=6,column=5)
button66=Button(frame,font=fnt,text=str(r),fg="black",bg="green")
button66.grid(row=6,column=6)
button67=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button67.grid(row=6,column=7)
button68=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button68.grid(row=6,column=8)
button70=Button(frame,font=fnt,text=str(s),fg="black",bg="green")
button70.grid(row=7,column=0)
button71=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button71.grid(row=7,column=1)
button72=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button72.grid(row=7,column=2)
button73=Button(frame,font=fnt,text=str(t),fg="black",bg="green")
button73.grid(row=7,column=3)
button74=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button74.grid(row=7,column=4)
button75=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button75.grid(row=7,column=5)
button76=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button76.grid(row=7,column=6)
button77=Button(frame,font=fnt,text=str(u),fg="black",bg="green")
button77.grid(row=7,column=7)
button78=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button78.grid(row=7,column=8)
button80=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button80.grid(row=8,column=0)
button81=Button(frame,font=fnt,text=str(v),fg="black",bg="green")
button81.grid(row=8,column=1)
button82=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button82.grid(row=8,column=2)
button83=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button83.grid(row=8,column=3)
button84=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button84.grid(row=8,column=4)
button85=Button(frame,font=fnt,text=str(w),fg="black",bg="green")
button85.grid(row=8,column=5)
button86=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button86.grid(row=8,column=6)
button87=Button(frame,font=fnt,text=str(k1),fg="black",bg="green")
button87.grid(row=8,column=7)
button88=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button88.grid(row=8,column=8)
button90=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button90.grid(row=9,column=0)
button91=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button91.grid(row=9,column=1)
button92=Button(frame,font=fnt,text=str(x),fg="black",bg="green")
button92.grid(row=9,column=2)
button93=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button93.grid(row=9,column=3)
button94=Button(frame,font=fnt,text=str(y),fg="black",bg="green")
button94.grid(row=9,column=4)
button95=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button95.grid(row=9,column=5)
button96=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button96.grid(row=9,column=6)
button97=Button(frame,font=fnt,text="  ",fg="black",bg="white")
button97.grid(row=9,column=7)
button98=Button(frame,font=fnt,text=str(z),fg="black",bg="green")
button98.grid(row=9,column=8)
count1 ="  "
def handle1() :
	global count1
	if count1<9:
		count1 = count1 + 1
	else:
		count1=1
	button10.configure(text = str(count1));
	if count1 in a0 or count1 in b0:
		button10.configure(text=str(count1),fg="red",bg="blue")
	else:
		button10.configure(text=str(count1),fg="black",bg="white")
		a0.append(count1)
		b0.append(count1)
button10.configure(text = str(count1), command = handle1)
count0 ="  "
def handle2() :
	global count0
	if count0<9:
		count0 = count0 + 1
	else:
		count0=1
	button12.configure(text = str(count0));
	if count0 in a0 or count0 in b2:
		button12.configure(text=str(count0),fg="red",bg="blue")
	else:
		button12.configure(text=str(count0),fg="black",bg="white")
		a0.append(count0)
		b2.append(count0)
button12.configure(text = str(count0), command = handle2)
count2 ="  "
def handle3() :
	global count2
	if count2<9:
		count2 = count2 + 1
	else:
		count2=1
	button14.configure(text = str(count2));
	if count2 in a0 or count2 in b4:
		button14.configure(text=str(count2),fg="red",bg="blue")
	else:
		button14.configure(text=str(count2),fg="black",bg="white")
		a0.append(count2)
		b4.append(count2)
button14.configure(text = str(count2), command = handle3)
count3="  "
def handle4() :
	global count3
	if count3<9:
		count3 = count3 + 1
	else:
		count3=1
	button15.configure(text = str(count3));
	if count3 in a0 or count3 in b5:
		button15.configure(text=str(count3),fg="red",bg="blue")
	else:
		button15.configure(text=str(count3),fg="black",bg="white")
		a0.append(count3)
		b5.append(count3)
button15.configure(text = str(count3), command = handle4)
count4="  "
def handle5() :
	global count4
	if count4<9:
		count4 = count4 + 1
	else:
		count4=1
	button16.configure(text = str(count4));
	if count4 in a0 or count4 in b6:
		button16.configure(text=str(count4),fg="red",bg="blue")
	else:
		button16.configure(text=str(count4),fg="black",bg="white")
		a0.append(count4)
		b6.append(count4)
button16.configure(text = str(count4), command = handle5)
count5="  "
def handle6() :
	global count5
	if count5<9:
		count5 = count5 + 1
	else:
		count5=1
	button17.configure(text = str(count5));
	if count5 in a0 or count5 in b7:
		button17.configure(text=str(count5),fg="red",bg="blue")
	else:
		button17.configure(text=str(count5),fg="black",bg="white")
		a0.append(count5)
		b7.append(count5)
button17.configure(text = str(count5), command = handle6)
count6="  "
def handle7() :
	global count6
	if count6<9:
		count6 = count6 + 1
	else:
		count6=1
	button21.configure(text = str(count6));
	if count6 in a1 or count6 in b1:
		button21.configure(text=str(count6),fg="red",bg="blue")
	else:
		button21.configure(text=str(count6),fg="black",bg="white")
		a1.append(count6)
		b1.append(count6)
button21.configure(text = str(count6), command = handle7)
count7="  "
def handle8() :
	global count7
	if count7<9:
		count7 = count7 + 1
	else:
		count7=1
	button22.configure(text = str(count7));
	if count7 in a1 or count7 in b2:
		button22.configure(text=str(count7),fg="red",bg="blue")
	else:
		button22.configure(text=str(count7),fg="black",bg="white")
		a1.append(count7)
		b2.append(count7)
button22.configure(text = str(count7), command = handle8)
count8="  "
def handle9() :
	global count8
	if count8<9:
		count8 = count8 + 1
	else:
		count8=1
	button23.configure(text = str(count8));
	if count8 in a1 or count8 in b3:
		button23.configure(text=str(count8),fg="red",bg="blue")
	else:
		button23.configure(text=str(count8),fg="black",bg="white")
		a1.append(count8)
		b3.append(count8)
button23.configure(text = str(count8), command = handle9)
count9="  "
def handle10() :
	global count9
	if count9<9:
		count9 = count9 + 1
	else:
		count9=1
	button25.configure(text = str(count9));
	if count9 in a1 or count9 in b5:
		button25.configure(text=str(count9),fg="red",bg="blue")
	else:
		button25.configure(text=str(count9),fg="black",bg="white")
		a1.append(count9)
		b5.append(count9)
button25.configure(text = str(count9), command = handle10)
count10="  "
def handle11() :
	global count10
	if count10<9:
		count10 = count10 + 1
	else:
		count10=1
	button27.configure(text = str(count10));
	if count10 in a1 or count10 in b7:
		button27.configure(text=str(count10),fg="red",bg="blue")
	else:
		button27.configure(text=str(count10),fg="black",bg="white")
		a1.append(count10)
		b7.append(count10)
button27.configure(text = str(count10), command = handle11)
count11="  "
def handle12() :
	global count11
	if count11<9:
		count11 = count11 + 1
	else:
		count11=1
	button28.configure(text = str(count11));
	if count11 in a1 or count11 in b8:
		button28.configure(text=str(count11),fg="red",bg="blue")
	else:
		button28.configure(text=str(count11),fg="black",bg="white")
		a1.append(count11)
		b8.append(count11)
button28.configure(text = str(count11), command = handle12)
count12="  "
def handle13() :
	global count12
	if count12<9:
		count12 = count12 + 1
	else:
		count12=1
	button30.configure(text = str(count12));
	if count12 in a2 or count12 in b0:
		button30.configure(text=str(count12),fg="red",bg="blue")
	else:
		button30.configure(text=str(count12),fg="black",bg="white")
		a2.append(count12)
		b0.append(count12)
button30.configure(text = str(count12), command = handle13)
count13="  "
def handle14() :
	global count13
	if count13<9:
		count13 = count13 + 1
	else:
		count13=1
	button31.configure(text = str(count13));
	if count13 in a2 or count13 in b1:
		button31.configure(text=str(count13),fg="red",bg="blue")
	else:
		button31.configure(text=str(count13),fg="black",bg="white")
		a2.append(count13)
		b1.append(count13)
button31.configure(text = str(count13), command = handle14)
count14="  "
def handle15() :
	global count14
	if count14<9:
		count14 = count14 + 1
	else:
		count14=1
	button33.configure(text = str(count14));
	if count14 in a2 or count14 in b3:
		button33.configure(text=str(count14),fg="red",bg="blue")
	else:
		button33.configure(text=str(count14),fg="black",bg="white")
		a2.append(count14)
		b3.append(count14)
button33.configure(text = str(count14), command = handle15)
count15="  "
def handle16() :
	global count15
	if count15<9:
		count15 = count15 + 1
	else:
		count15=1
	button34.configure(text = str(count15));
	if count15 in a2 or count15 in b4:
		button34.configure(text=str(count15),fg="red",bg="blue")
	else:
		button34.configure(text=str(count15),fg="black",bg="white")
		a2.append(count15)
		b4.append(count15)
button34.configure(text = str(count15), command = handle16)
count16="  "
def handle17() :
	global count16
	if count16<9:
		count16 = count16 + 1
	else:
		count16=1
	button36.configure(text = str(count16));
	if count16 in a2 or count16 in b6:
		button36.configure(text=str(count16),fg="red",bg="blue")
	else:
		button36.configure(text=str(count16),fg="black",bg="white")
		a2.append(count16)
		b6.append(count16)
button36.configure(text = str(count16), command = handle17)
count17="  "
def handle18() :
	global count17
	if count17<9:
		count17 = count17 + 1
	else:
		count17=1
	button38.configure(text = str(count17));
	if count17 in a2 or count17 in b8:
		button38.configure(text=str(count17),fg="red",bg="blue")
	else:
		button38.configure(text=str(count17),fg="black",bg="white")
		a2.append(count17)
		b8.append(count17)
button38.configure(text = str(count17), command = handle18)
count18="  "
def handle19() :
	global count18
	if count18<9:
		count18 = count18 + 1
	else:
		count18=1
	button41.configure(text = str(count18));
	if count18 in a3 or count18 in b1:
		button41.configure(text=str(count18),fg="red",bg="blue")
	else:
		button41.configure(text=str(count18),fg="black",bg="white")
		a3.append(count18)
		b1.append(count18)
button41.configure(text = str(count18), command = handle19)
count19="  "
def handle20() :
	global count19
	if count19<9:
		count19 = count19 + 1
	else:
		count19=1
	button42.configure(text = str(count19));
	if count19 in a3 or count19 in b2:
		button42.configure(text=str(count19),fg="red",bg="blue")
	else:
		button42.configure(text=str(count19),fg="black",bg="white")
		a3.append(count19)
		b2.append(count19)
button42.configure(text = str(count19), command = handle20)
count20="  "
def handle21() :
	global count20
	if count20<9:
		count20 = count20 + 1
	else:
		count20=1
	button44.configure(text = str(count20));
	if count20 in a3 or count20 in b4:
		button44.configure(text=str(count20),fg="red",bg="blue")
	else:
		button44.configure(text=str(count20),fg="black",bg="white")
		a3.append(count20)
		b4.append(count20)
button44.configure(text = str(count20), command = handle21)
count21="  "
def handle22() :
	global count21
	if count21<9:
		count21 = count21 + 1
	else:
		count21=1
	button45.configure(text = str(count21));
	if count21 in a3 or count21 in b5:
		button45.configure(text=str(count21),fg="red",bg="blue")
	else:
		button45.configure(text=str(count21),fg="black",bg="white")
		a3.append(count21)
		b5.append(count21)
button45.configure(text = str(count21), command = handle22)
count22="  "
def handle223() :
	global count22
	if count22<9:
		count22 = count22 + 1
	else:
		count22=1
	button47.configure(text = str(count22));
	if count22 in a3 or count22 in b7:
		button47.configure(text=str(count22),fg="red",bg="blue")
	else:
		button47.configure(text=str(count22),fg="black",bg="white")
		a3.append(count22)
		b7.append(count22)
button47.configure(text = str(count22), command = handle223)
count23="  "
def handle24() :
	global count23
	if count23<9:
		count23 = count23 + 1
	else:
		count23=1
	button48.configure(text = str(count23));
	if count23 in a3 or count23 in b8:
		button48.configure(text=str(count23),fg="red",bg="blue")
	else:
		button48.configure(text=str(count23),fg="black",bg="white")
		a3.append(count23)
		b8.append(count23)
button48.configure(text = str(count23), command = handle24)
count24="  "
def handle25() :
	global count24
	if count24<9:
		count24 = count24 + 1
	else:
		count24=1
	button50.configure(text = str(count24));
	if count24 in a4 or count24 in b0:
		button50.configure(text=str(count24),fg="red",bg="blue")
	else:
		button50.configure(text=str(count24),fg="black",bg="white")
		a4.append(count24)
		b0.append(count24)
button50.configure(text = str(count24), command = handle25)
count25="  "
def handle26() :
	global count25
	if count25<9:
		count25 = count25 + 1
	else:
		count25=1
	button52.configure(text = str(count25));
	if count25 in a4 or count25 in b2:
		button52.configure(text=str(count25),fg="red",bg="blue")
	else:
		button52.configure(text=str(count25),fg="black",bg="white")
		a4.append(count25)
		b2.append(count25)
button52.configure(text = str(count25), command = handle26)
count26="  "
def handle27() :
	global count26
	if count26<9:
		count26 = count26 + 1
	else:
		count26=1
	button53.configure(text = str(count26));
	if count26 in a4 or count26 in b3:
		button53.configure(text=str(count26),fg="red",bg="blue")
	else:
		button53.configure(text=str(count26),fg="black",bg="white")
		a4.append(count26)
		b3.append(count26)
button53.configure(text = str(count26), command = handle27)
count27="  "
def handle28() :
	global count27
	if count27<9:
		count27 = count27 + 1
	else:
		count27=1
	button54.configure(text = str(count27));
	if count27 in a4 or count27 in b4:
		button54.configure(text=str(count27),fg="red",bg="blue")
	else:
		button54.configure(text=str(count27),fg="black",bg="white")
		a4.append(count27)
		b4.append(count27)
button54.configure(text = str(count27), command = handle28)
count28="  "
def handle29() :
	global count28
	if count28<9:
		count28 = count28 + 1
	else:
		count28=1
	button56.configure(text = str(count28));
	if count28 in a4 or count28 in b6:
		button56.configure(text=str(count28),fg="red",bg="blue")
	else:
		button56.configure(text=str(count28),fg="black",bg="white")
		a4.append(count28)
		b6.append(count28)
button56.configure(text = str(count28), command = handle29)
count29="  "
def handle30() :
	global count29
	if count29<9:
		count29 = count29 + 1
	else:
		count29=1
	button57.configure(text = str(count29));
	if count29 in a4 or count29 in b7:
		button57.configure(text=str(count29),fg="red",bg="blue")
	else:
		button57.configure(text=str(count29),fg="black",bg="white")
		a4.append(count29)
		b7.append(count29)
button57.configure(text = str(count29), command = handle30)
count30="  "
def handle31() :
	global count30
	if count30<9:
		count30 = count30 + 1
	else:
		count30=1
	button60.configure(text = str(count30));
	if count30 in a5 or count30 in b0:
		button60.configure(text=str(count30),fg="red",bg="blue")
	else:
		button60.configure(text=str(count30),fg="black",bg="white")
		a5.append(count30)
		b0.append(count30)
button60.configure(text = str(count30), command = handle31)
count31="  "
def handle32() :
	global count31
	if count31<9:
		count31 = count31 + 1
	else:
		count31=1
	button61.configure(text = str(count31));
	if count31 in a5 or count31 in b1:
		button61.configure(text=str(count31),fg="red",bg="blue")
	else:
		button61.configure(text=str(count31),fg="black",bg="white")
		a5.append(count31)
		b1.append(count31)
button61.configure(text = str(count31), command = handle32)
count32="  "
def handle33() :
	global count32
	if count32<9:
		count32 = count32 + 1
	else:
		count32=1
	button63.configure(text = str(count32));
	if count32 in a5 or count32 in b3:
		button63.configure(text=str(count32),fg="red",bg="blue")
	else:
		button63.configure(text=str(count32),fg="black",bg="white")
		a5.append(count32)
		b3.append(count32)
button63.configure(text = str(count32), command = handle33)
count33="  "
def handle34() :
	global count33
	if count33<9:
		count33 = count33 + 1
	else:
		count33=1
	button65.configure(text = str(count33));
	if count33 in a5 or count33 in b5:
		button65.configure(text=str(count33),fg="red",bg="blue")
	else:
		button65.configure(text=str(count33),fg="black",bg="white")
		a5.append(count33)
		b5.append(count33)
button65.configure(text = str(count33), command = handle34)
count34="  "
def handle35() :
	global count34
	if count34<9:
		count34 = count34 + 1
	else:
		count34=1
	button67.configure(text = str(count34));
	if count34 in a5 or count34 in b7:
		button67.configure(text=str(count34),fg="red",bg="blue")
	else:
		button67.configure(text=str(count34),fg="black",bg="white")
		a5.append(count34)
		b7.append(count34)
button67.configure(text = str(count34), command = handle35)
count35="  "
def handle36() :
	global count35
	if count35<9:
		count35 = count35 + 1
	else:
		count35=1
	button68.configure(text = str(count35));
	if count35 in a5 or count35 in b8:
		button68.configure(text=str(count35),fg="red",bg="blue")
	else:
		button68.configure(text=str(count35),fg="black",bg="white")
		a5.append(count35)
		b8.append(count35)
button68.configure(text = str(count35), command = handle36)
count36="  "
def handle37() :
	global count36
	if count36<9:
		count36 = count36 + 1
	else:
		count36=1
	button71.configure(text = str(count36));
	if count36 in a6 or count36 in b1:
		button71.configure(text=str(count36),fg="red",bg="blue")
	else:
		button71.configure(text=str(count36),fg="black",bg="white")
		a6.append(count36)
		b1.append(count36)
button71.configure(text = str(count36), command = handle37)
count37="  "
def handle38() :
	global count37
	if count37<9:
		count37 = count37 + 1
	else:
		count37=1
	button72.configure(text = str(count37));
	if count37 in a6 or count37 in b2:
		button72.configure(text=str(count37),fg="red",bg="blue")
	else:
		button72.configure(text=str(count37),fg="black",bg="white")
		a6.append(count37)
		b2.append(count37)
button72.configure(text = str(count37), command = handle38)
count38="  "
def handle39() :
	global count38
	if count38<9:
		count38 = count38 + 1
	else:
		count38=1
	button74.configure(text = str(count38));
	if count38 in a6 or count38 in b4:
		button74.configure(text=str(count38),fg="red",bg="blue")
	else:
		button74.configure(text=str(count38),fg="black",bg="white")
		a6.append(count38)
		b4.append(count38)
button74.configure(text = str(count38), command = handle39)
count39="  "
def handle40() :
	global count39
	if count39<9:
		count39 = count39 + 1
	else:
		count39=1
	button75.configure(text = str(count39));
	if count39 in a6 or count39 in b5:
		button75.configure(text=str(count39),fg="red",bg="blue")
	else:
		button75.configure(text=str(count39),fg="black",bg="white")
		a6.append(count39)
		b5.append(count39)
button75.configure(text = str(count39), command = handle40)
count40="  "
def handle41() :
	global count40
	if count40<9:
		count40 = count40 + 1
	else:
		count40=1
	button76.configure(text = str(count40));
	if count40 in a6 or count40 in b6:
		button76.configure(text=str(count40),fg="red",bg="blue")
	else:
		button76.configure(text=str(count40),fg="black",bg="white")
		a6.append(count40)
		b6.append(count40)
button76.configure(text = str(count40), command = handle41)
count41="  "
def handle42() :
	global count41
	if count41<9:
		count41 = count41 + 1
	else:
		count41=1
	button78.configure(text = str(count41));
	if count41 in a6 or count41 in b8:
		button78.configure(text=str(count41),fg="red",bg="blue")
	else:
		button78.configure(text=str(count41),fg="black",bg="white")
		a6.append(count41)
		b8.append(count41)
button78.configure(text = str(count41), command = handle42)
count42="  "
def handle43() :
	global count42
	if count42<9:
		count42 = count42 + 1
	else:
		count42=1
	button80.configure(text = str(count42));
	if count42 in a7 or count42 in b0:
		button80.configure(text=str(count42),fg="red",bg="blue")
	else:
		button80.configure(text=str(count42),fg="black",bg="white")
		a7.append(count42)
		b0.append(count42)
button80.configure(text = str(count42), command = handle43)
count43="  "
def handle44() :
	global count43
	if count43<9:
		count43 = count43 + 1
	else:
		count43=1
	button82.configure(text = str(count43));
	if count43 in a7 or count43 in b2:
		button82.configure(text=str(count43),fg="red",bg="blue")
	else:
		button82.configure(text=str(count43),fg="black",bg="white")
		a7.append(count43)
		b2.append(count43)
button82.configure(text = str(count43), command = handle44)
count44="  "
def handle45() :
	global count44
	if count44<9:
		count44 = count44 + 1
	else:
		count44=1
	button84.configure(text = str(count44));
	if count44 in a7 or count44 in b4:
		button84.configure(text=str(count44),fg="red",bg="blue")
	else:
		button84.configure(text=str(count44),fg="black",bg="white")
		a7.append(count44)
		b4.append(count44)
button84.configure(text = str(count44), command = handle45)
count45="  "
def handle46() :
	global count45
	if count45<9:
		count45 = count45 + 1
	else:
		count45=1
	button87.configure(text = str(count45));
	if count45 in a7 or count45 in b7:
		button87.configure(text=str(count45),fg="red",bg="blue")
	else:
		button87.configure(text=str(count45),fg="black",bg="white")
		a7.append(count45)
		b7.append(count45)
button87.configure(text = str(count45), command = handle46)
count46="  "
def handle47() :
	global count46
	if count46<9:
		count46 = count46 + 1
	else:
		count46=1
	button83.configure(text = str(count46));
	if count46 in a7 or count46 in b3:
		button83.configure(text=str(count46),fg="red",bg="blue")
	else:
		button83.configure(text=str(count46),fg="black",bg="white")
		a7.append(count46)
		b3.append(count46)
button83.configure(text = str(count46), command = handle47)
count47="  "
def handle48() :
	global count47
	if count47<9:
		count47 = count47 + 1
	else:
		count47=1
	button88.configure(text = str(count47));
	if count47 in a7 or count47 in b8:
		button88.configure(text=str(count47),fg="red",bg="blue")
	else:
		button88.configure(text=str(count47),fg="black",bg="white")
		a7.append(count47)
		b8.append(count47)
button88.configure(text = str(count47), command = handle48)
count48="  "
def handle49() :
	global count48
	if count48<9:
		count48 = count48 + 1
	else:
		count48=1
	button90.configure(text = str(count48));
	if count48 in a8 or count48 in b0:
		button90.configure(text=str(count48),fg="red",bg="blue")
	else:
		button90.configure(text=str(count48),fg="black",bg="white")
		a8.append(count48)
		b0.append(count48)
button90.configure(text = str(count48), command = handle49)
count49="  "
def handle50() :
	global count49
	if count49<9:
		count49 = count49 + 1
	else:
		count49=1
	button91.configure(text = str(count49));
	if count49 in a8 or count49 in b1:
		button91.configure(text=str(count49),fg="red",bg="blue")
	else:
		button91.configure(text=str(count49),fg="black",bg="white")
		a8.append(count49)
		b1.append(count49)
button91.configure(text = str(count49), command = handle50)
count50="  "
def handle51() :
	global count50
	if count50<9:
		count50 = count50 + 1
	else:
		count50=1
	button93.configure(text = str(count50));
	if count50 in a8 or count50 in b3:
		button93.configure(text=str(count50),fg="red",bg="blue")
	else:
		button93.configure(text=str(count50),fg="black",bg="white")
		a8.append(count50)
		b3.append(count50)
button93.configure(text = str(count50), command = handle51)
count51="  "
def handle52() :
	global count51
	if count51<9:
		count51 = count51 + 1
	else:
		count51=1
	button95.configure(text = str(count51));
	if count51 in a8 or count51 in b5:
		button95.configure(text=str(count51),fg="red",bg="blue")
	else:
		button95.configure(text=str(count51),fg="black",bg="white")
		a8.append(count51)
		b5.append(count51)
button95.configure(text = str(count51), command = handle52)
count52="  "
def handle53() :
	global count52
	if count52<9:
		count52 = count52 + 1
	else:
		count52=1
	button96.configure(text = str(count52));
	if count52 in a8 or count52 in b6:
		button96.configure(text=str(count52),fg="red",bg="blue")
	else:
		button96.configure(text=str(count52),fg="black",bg="white")
		a8.append(count52)
		b6.append(count52)
button96.configure(text = str(count52), command = handle53)
count53="  "
count54="  "
def handle55() :
	global count54
	if count54<9:
		count54 = count54 + 1
	else:
		count54=1
	button86.configure(text = str(count54));
	if count54 in a7 or count54 in b6:
		button86.configure(text=str(count54),fg="red",bg="blue")
	else:
		button86.configure(text=str(count54),fg="black",bg="white")
		a7.append(count54)
		b6.append(count54)
button86.configure(text = str(count54), command = handle55)

def handle54() :
	global count53
	if count53<9:
		count53 = count53 + 1
	else:
		count53=1
	button97.configure(text = str(count53));
	if count53 in a8 or count53 in b7:
		button97.configure(text=str(count53),fg="red",bg="blue")
	else:
		button97.configure(text=str(count53),fg="black",bg="white")
		a8.append(count53)
		b7.append(count53)
button97.configure(text = str(count53), command = handle54)
root.mainloop()
