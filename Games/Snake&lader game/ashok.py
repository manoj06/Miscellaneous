from turtle import *
import random
bgcolor("black")
#=======================================close=======================
clos=Turtle()
clos.pu(),clos.ht()
def close(x,y):
	bye()
clos.goto(340,-200)
clos.color("red")
clos.st()
clos.write("To exit click here",font=("URW Chancery L",30,"italic"))
clos.shape("square")
clos.onclick(close)
#=================================snakes=================================
snake1=Turtle()
snake1.pu()
register_shape("13.gif")
snake1.shape("13.gif")
snake1.goto(100,-140)
snake1.stamp()
register_shape("11.gif")
snake1.shape("11.gif")
snake1.goto(-120,-20)
snake1.stamp()
register_shape("12.gif")
snake1.goto(230,-40)
snake1.shape("12.gif")
snake1.stamp()
register_shape("14.gif")
snake1.shape("14.gif")
snake1.goto(-180,-280)
snake1.stamp()
#==========================================heading============================
pd()
goto(-200,300)
color("yellow")
write("SNAKE & LADER",True,font=("URW Chancery L",50,"italic"));
ht(),pu()
color("green")
pensize(3)
goto(-300,-350)
pd(),st()
speed(0)
def border():
	for i in range(4):
		fd(600)
		lt(90)
def stright():
	for  i in range(9):
		if i==0:
			fd(70)
			lt(90)
		if i%2==0 and i!=0:
			lt(90)
			fd(60)
			lt(90)
		elif i!=0:
			lt(270)
			fd(60)
			rt(90)
		fd(600)
def cros():
	c=90
	rt(90)
	for i in range(11):
	 if i%2==0:
		fd(600)
		lt(90)
		fd(60)
		lt(90)
	 else:
		fd(600)
		rt(90)
		fd(60)
		rt(90)
k=-280
c=0
aa,ab,ac,ad,ae,af,ag,ah=[],[],[],[],[],[],[],[]
posi,posi1=[],[]
def numbers():
	color("red")
	global k,c,aa,ab,ac
	global ad,ae,af,ag,ah
	global posi,posi1
	lt(180)
	for i in range(1,101):
		pu()
		if i==100:
			lt(60)
			write("Finish",font=("URW Chancery L",20,"italic"))
		if i%10!=0:
			write(i,font="50,italic")
			posi.append(i)
			posi1.append(pos())
			fd(60)
		elif i%10==0:
			if c%2==1:
				write(i,font="50,italic")
				posi.append(i)
				posi1.append(pos())
				rt(90)
				fd(60)
				rt(90)
			elif c%2==0:
				write(i,font="50,italic")
				posi.append(i)
				posi1.append(pos())
				lt(90)
				fd(60)
				lt(90)
			c=c+1
		if i==23 or i==54 or i==70 or i==98:
			aa.append(xcor())
			ab.append(ycor())
		if i==1 or i==12 or i==15 or i==28:
			ac.append(xcor())
			ad.append(ycor())
		if i==7 or i==14 or i==41 or i==65:
			ae.append(xcor())
			af.append(ycor())
		if i==30 or i==80 or i==86 or i==96:
			ag.append(xcor())
			ah.append(ycor())
border()
stright()
pu()
ht()
goto(-300,-350)
st()
pd()
cros()
pu()
goto(-280,-330)
speed(0)
numbers()
#=========================laders==============================
dy=Turtle()
ll=Turtle()
dcd=0
def laders(a,b,c,d,k):
	global dcd
	dy.pu()
	dy.ht()
	ll.ht()
	dy.speed(0)
	ll.speed(0)
	dy.color("yellow")
	ll.color("yellow")
	dy.goto(a,b)
	ll.pu()
	ll.goto(a,b)
	dy.pd()
	dy.pensize(3)
	ll.pensize(3)
	if k==8:
		dy.color("blue")
		ll.color("blue")
		dy.lt(60)
		ll.lt(60)
		df=9
	elif k==15:
		dy.color("yellow")
		ll.color("yellow")
		dy.lt(45)
		ll.lt(45)
		df=17
	elif k==42:
		dy.color("blue")
		ll.color("blue")
		dy.lt(0)
		ll.lt(0)
		df=9
	elif k==66:
		dy.color("yellow")
		ll.color("yellow")
		dy.rt(42)
		ll.ht()
		ll.rt(42)
		df=5
	for i in range(df):
		dy.pd()
		dy.fd(30)
		if (i==7 or i==8) and k==8:
			if i==8:
				dy.undo()
			dy.pu()
		if i==(df-1):
			dy.pu()
		if i%2==0:
			dy.rt(90)
			dy.fd(40)
			dy.lt(90)
		else:
			dy.lt(90)
			dy.fd(40)
			dy.rt(90)
	for i in range(df):
		if k!=8:
			dy.pd()
			ll.pd()
			dy.bk(30)
			ll.fd(30)
		elif i==0 and k==8:
			dy.bk(30)
			ll.pu()
			k=9
dy.pu()
		
co=0
cou=0
goto(-280,-330)
for i in range(1,101):
	if i%10!=0:
		fd(60)
	elif i%10==0:
		if co%2==1:
			rt(90)
			fd(60)
			rt(90)	
		if co%2==1:
			lt(90)
			fd(60)
			lt(90)
	c=c+1
	if i==8:
		laders(ae[0],af[0],ag[0],ah[0],i)
	elif i==15:
		laders(ae[1],af[1],ag[3],ah[3],i)
	elif i==42:
		laders(ae[2],af[2],ag[1],ah[1],i)
	elif i==66:
		laders(ae[3],af[3],ag[2],ah[2],i)
#==========================================
dd=Turtle()
dd.stamp()
dd.pu()
dd.goto(370,200)
dd.color("yellow")
dd.write("Roll Dice",font=("URW Chancery L",30,"italic"))
dd.rt(90)
dd.fd(50)
dd.rt(90)
dd.write("Click here",font=("URW Chancery L",30,"italic"))
dd.color("blue")
dd.lt(90)
dd.fd(50)
dd.lt(90)
dd.write("first ",font=("URW Chancery L",30,"italic"))
dd.fd(100)
dd.write("second ",font=("URW Chancery L",30,"italic"))
dd.color("green")
dd.goto(340,190)
dd.shape("square")
ccc=0
dy.stamp()
clos.onclick(close)
steps=0
steps=0
def click(x,y):
	dy.undo()
	global c,ccc
	global d,e
	global steps,steps1
	dy.pu()
	dy.goto(340,190)
	dy.ht()
	dy.color("red")
	if ccc%2==0:
		dy.goto(390,80)
		aaa=random.randrange(1,7)
		dy.write(aaa,font=("URW Chancery L",20,"italic"))
		c=c+aaa
		if c>100:
			c=c-aaa
		for i in range(len(posi)):
			if posi[i]==c:
				if c==100:
					a.goto(posi1[i])
					a.write("WOW first person won the game",font=("URW Chancery L",30,"italic"))
					dy.undo()
					dd.ht()
					dd.goto(0,0)
					b.goto(100,-30)
					b.write("seond person complete the game in",steps,"steps",font=("URW Chancery L",30,"italic"))
					break
					dy.color("black")
				if d==100:
					break
					dy.color("black")
				a.goto(posi1[i])
				if posi[i]==8:
					a.goto(posi1[i])
					a.goto(ag[0],ah[0])
					c=31
				elif posi[i]==15:
					a.goto(posi1[i])
					a.goto(ag[3],ah[3])
					c=97
				elif posi[i]==42:
					a.goto(posi1[i])
					a.goto(ag[1],ah[1])
					c=81
				elif posi[i]==66:
					a.goto(posi1[i])
					a.goto(ag[2],ah[2])
					c=87
				if posi[i]==24:
					a.goto(posi1[i])
					a.goto((ac[0]-60),ad[0])
					c=1
				elif posi[i]==55:
					a.goto(posi1[i])
					a.goto(ac[1],ad[1])
					c=13
				elif posi[i]==71:
					a.goto(posi1[i])
					a.goto(ac[3],ad[3])
					c=29
				elif posi[i]==99:
					a.goto(posi1[i])
					a.goto(ac[2],ad[2])
					c=16
	else:
		aab=random.randrange(1,7)
		dy.goto(490,80)
		dy.write(aab,font=("URW Chancery L",20,"italic"))
		d=d+aab
		if d>100:
			d=d-aab
		for i in range(len(posi)):
			if posi[i]==d:
				if d==100:
					b.goto(posi1[i])
					b.color("green")
					b.write("WOW second person won the game",font=("URW Chancery L",30,"italic"))
					b.goto(100,-30)
					b.write("seond person complete the game in",steps,"steps",font=("URW Chancery L",30,"italic"))
					dd.goto(0,0)
					break
					dy.color("black")
				elif c==100:
					break
					dy.color("black")
				b.goto(posi1[i])
				if posi[i]==8:
					b.goto(posi1[i])
					b.goto(ag[0],ah[0])
					d=31
				elif posi[i]==15:
					b.goto(posi1[i])
					b.goto(ag[3],ah[3])
					d=97
				elif posi[i]==42:
					b.goto(posi1[i])
					b.goto(ag[1],ah[1])
					d=81
				elif posi[i]==66:
					b.goto(posi1[i])
					b.goto(ag[2],ah[2])
					d=87
				if posi[i]==24:
					b.goto(posi1[i])
					b.goto((ac[0]-60),ad[0])
					d=1
				elif posi[i]==55:
					b.goto(posi1[i])
					b.goto(ac[1],ad[1])
					d=13
				elif posi[i]==71:
					b.goto(posi1[i])
					b.goto(ac[3],ad[3])
					d=29
				elif posi[i]==99:
					b.goto(posi1[i])
					b.goto(ac[2],ad[2])
					b.clearstamps()
					d=16
	ccc=ccc+1
	



#==========================================
b=Turtle()
a=Turtle()
a.pu(),b.pu()
a.shape("circle")
b.shape("circle")
a.color("green")
b.color("red")
a.goto(-320,-345)
b.goto(-320,-330)
d=0
c=0
e=0
while True:
	dd.onclick(click)
done()
