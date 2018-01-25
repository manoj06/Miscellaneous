import Image
import random
def opposite(opponent):
	if opponent==1:
		print "Choosed opponent:India"
		im=Image.open("India.jpeg")
		im.show()
	elif opponent==2:
		print "Choosed opponent:Pakistan"
		im=Image.open("Pakistan.jpeg")
		im.show()
	elif opponent==3:
		print "Choosed opponent:Australia"
		im=Image.open("Australia.jpeg")
		im.show()
	elif opponent==4:
		print "Chossed opponent:Newzeland"
		im=Image.open("Newzewland.jpeg")
		im.show()
	elif opponent==5:
		print "Choosed opponent:South Africa"
		im=Image.open("SouthAfrica.jpeg")
		im.show()
	elif opponent==6:
		print "Choosed opponent:England"
		im=Image.open("England.jpeg")
		im.show()
	elif opponent==7:
		print "Choosed opponent:Srilanka"
		im=Image.open("Srilanka.jpeg")
		im.show()
	elif opponent==8:
		print "Choosed opponent:Bangladesh"
		im=Image.open("Bangladesh.jpeg")
		im.show()
def single():
	print "**********************************************************************"
	print "\t\t\t\tSingle Run"
	print "**********************************************************************"
def two():
	print "************************************************************************"
	print "\t\t\t\tTwo Runs"
	print "***********************************************************************"
def three():
	print "**********************************************************************"
	print "\t\t\t\tThree Runs"
	print "**********************************************************************"
def four():
	print "**********************************************************************"
	print "\t\t\t\tFour"
	print "*********************************************************************"
def sixer():
	print "*********************************************************************"
	print "\t\t\t\t\tSixer"
	print "********************************************************************"
def out():
	print "********************************************************************"
	print "\t\t\t\t\tOut"
	print "********************************************************************"
def no():
	print "*********************************************************************"
	print "\t\t\t\t\tNo Run"
	print "*********************************************************************"
def match(a,b,c):
	score=0
	wicket=0
	overs=0
	print "Current situation:"
	print "Score:",score
	print "Wickets",wicket
	print "Overs",overs
	m=0
	n=1
	b1=b[m]
	b2=b[n]
	i=0
	l=0
	z=0
	print "***********************************************************************"
	print "\t\t\t\t\tTime to start match"
	print "***********************************************************************"
	while overs!=c or wicket!=10:
		print "Current situation:"
		print "Score:",score
		print "Wickets",wicket
		print "Overs",overs/6,".",overs%6
		print "Batsmens:*",b1,":",i,",",b2,":",l
		
		a=int(raw_input("Enter any number:"))
		run=a%random.randint(2,6)
		if run==0:
			if run%6==0:
				x=0
				im=Image.open("out.jpeg")
				im.show()
				out()
				print b1,":",i
				z=1
				wicket=wicket+z
				if wicket==10:
					break
				b1=b[m+2]
				i=0
				m=m+1
			else:
				x=1
				im.Image.open("1.jpeg")
				im.show()
				single()
				q=b1
				j=b2
				b1=j
				b2=q
				i=i+x
				o=i
				p=l
				i=p
				l=o
				z=0
		elif run==1:
			if run%3==0:
				x=2
				im=Image.open("2.jpeg")
				im.show()
				two()
				i=i+x
				z=0
			else:
				x=4
				im=Image.open("4.jpeg")
				im.show()
				four()
				i=i+x
				z=0
		elif run==3:
			x=6
			im=Image.open("6.jpeg")
			im.show()
			sixer()
			i=i+x
			z=0
		elif run==2:
			x=0
			im=Image.open("pend.jpeg")
			im.show()
			i=i+x
			if run%4==0:
				print b1,":",i
				im.Image.open("catch.jpg")
				im.show()
				z=1
				wicket=wicket+z
				if wicket==10:
					break
				i=0
				b1=b[m+2]
				m=m+1
		else:
			x=0
			i=i+x
			z=0
			im=Image.open("stop.jpeg")
			im.show()
			no()
		score=score+x
		overs=overs+1
		if overs%6==0:
			q=b1
			j=b2
			b1=j
			b2=q
			o=i
			p=l
			i=p
			l=o
		elif overs==c:
			break
	print score
print "********************************************************************************"
print "This is the sample cricket game"
print "********************************************************************************"
print "Instructions:"
print "At first you have to choose the team we will automatically send the players into the ground after their expiry"
print "And next u have to choose the game format"
print "And next u have to choose the concerned overs format"
im=Image.open("cricket-logo.jpg")
im.show()
print "********************************************************************************"
print "Teams\t\t\t\ttheir concerned no."
print "India\t\t\t\t\t",1
print "Pakistan\t\t\t\t",2
print "Australia\t\t\t\t",3
print "Newzeland\t\t\t\t",4
print "SouthAfrica\t\t\t\t",5
print "England\t\t\t\t\t",6
print "Srilanka\t\t\t\t",7
print "Bangladesh\t\t\t\t",8
team=int(raw_input("Enter option(1/2/3/4/5/6/7/8):"))
India=["Sehwag","Sachin","Gambir","Raina","Rohith","Yuvaraj","Dhoni","Harbajan","Zaheer","Nehra","Oja"]
Pakistan=["Inzamum","Youniskhan","Butt","Akmal","Afridi","Younis","Malik","Razak","Akthar","Kanaria","Asif"]
Australia=["Gilcrist","Haden","Clark","Warner","Pointing","White","Hopes","Hussy","Bretlee","Jhonson","Tait"]
Newzeland=["Mcintosh","Mccullum","Ryder","Hopkins","vettori","Mortin","ShaneBond","Astil","Styris","Mill","Oram"]
SouthAfrica=["Smith","Gibbs","Devellieris","Kallis","Amla","Pollock","Nells","Morckel","Botha","Styen","Boucher"]
England=["Strauss","Bell","Peterson","Pain","Collingwood","Flintoff","Broad","Hauris","Waghun"]
Srilanka=["Jayasurya","Dilshan","Sangarkara","Jayawardene","Samaravera","Malinga","Mathews","Murali","Mendis","Kulasekara","Maharoof"]
Bangladesh=["Bashar","Raquble","Shaqible","Rahim","Iqbal","Khadar","Mohinddun"]
if team==1:
	print "Choosed team:India"
	im=Image.open("India.jpeg")
	im.show()
	opponent=int(raw_input("Enter option(1/2/3/4/5/6/7/8):"))
	opposite(opponent)
	d=dict()
	k=dict()
	for i in range(len(India)):
		d[India[i]]=0
	for j in range(len(India)):
		k[j]=India[j]
	overs=int(raw_input("How many overs:"))
	overs=overs*6
	print "*************************************************************************"
	print "\t\t\t\t\tIts time for toss"
	toss=int(raw_input("Enter any number:"))
	if toss%(random.randint(2,10))==0:
		print "You had won the toss"
		choice=raw_input("Batting or fielding(b/f):")
		match(d,k,overs)
	else:
		print "You loss the toss"
		match(d,k,overs)
elif team==2:
	print "Choosed team:Pakistan"
	im=Image.open("Pakistan.jpeg")
	im.show()
	opponent=int(raw_input("Enter option(1/2/3/4/5/6/7/8):"))
	opposite(opponent)
	overs=int(raw_input("How many overs:"))
	print "*************************************************************************"
	print "\t\t\t\t\tIts time for toss"
	toss=int(raw_input("Enter any number:"))
	if toss%(random.randint(2,10))==0:
		print "You had won the toss"
		choice=raw_input("Batting or fielding(b/f):")

	else:
		print "You loss the toss"

elif team==3:
	print "Choosed team:Australia"
	im=Image.open("Australia.jpeg")
	im.show()
	opponent=int(raw_input("Enter option(1/2/3/4/5/6/7/8):"))
	opposite(opponent)
	overs=int(raw_input("How many overs:"))
	print "*************************************************************************"
	print "\t\t\t\t\tIts time for toss"
	toss=int(raw_input("Enter any number:"))
	if toss%(random.randint(2,10))==0:
		print "You had won the toss"
		choice=raw_input("Batting or fielding(b/f):")
		match()
	else:
		print "You loss the toss"
		field()
elif team==4:
	print "Chossed team:Newzeland"
	im=Image.open("Newzewland.jpeg")
	im.show()	
	opponent=int(raw_input("Enter option(1/2/3/4/5/6/7/8):"))
	opposite(opponent)
	overs=int(raw_input("How many overs:"))
	print "*************************************************************************"
	print "\t\t\t\t\tIts time for toss"
	toss=int(raw_input("Enter any number:"))
	if toss%(random.randint(2,10))==0:
		print "You had won the toss"
		choice=raw_input("Batting or fielding(b/f):")
		match()
	else:
		print "You loss the toss"
		field()
elif team==5:
	print "Choosed team:South Africa"
	im=Image.open("SouthAfrica.jpeg")
	im.show()
	opponent=int(raw_input("Enter option(1/2/3/4/5/6/7/8):"))
	opposite(opponent)
	overs=int(raw_input("How many overs:"))
	print "*************************************************************************"
	print "\t\t\t\t\tIts time for toss"
	toss=int(raw_input("Enter any number:"))
	if toss%(random.randint(2,10))==0:
		print "You had won the toss"
		choice=raw_input("Batting or fielding(b/f):")
		match()
	else:
		print "You loss the toss"
		field()
elif team==6:
	print "Choosed team:England"
	im=Image.open("England.jpeg")
	im.show()
	opponent=int(raw_input("Enter option(1/2/3/4/5/6/7/8):"))
	opposite(opponent)
	overs=int(raw_input("How many overs:"))
	print "*************************************************************************"
	print "\t\t\t\t\tIts time for toss"
	toss=int(raw_input("Enter any number:"))
	if toss%(random.randint(2,10))==0:
		print "You had won the toss"
		choice=raw_input("Batting or fielding(b/f):")
		match()
	else:
		print "You loss the toss"
		field()
elif team==7:
	print "Choosed team:Srilanka"
	im=Image.open("Srilanka.jpeg")
	im.show()
	opponent=int(raw_input("Enter option(1/2/3/4/5/6/7/8):"))
	opposite(opponent)
	overs=int(raw_input("How many overs:"))
	print "*************************************************************************"
	print "\t\t\t\t\tIts time for toss"
	toss=int(raw_input("Enter any number:"))
	if toss%(random.randint(2,10))==0:
		print "You had won the toss"
		choice=raw_input("Batting or fielding(b/f):")
		match()
	else:
		print "You loss the toss"
		field()
elif team==8:
	print "Choosed team:Bangladesh"
	im=Image.open("Bangladesh.jpeg")
	im.show()
	opponent=int(raw_input("Enter option(1/2/3/4/5/6/7/8):"))
	opposite(opponent)
	overs=int(raw_input("How many overs:"))
	print "*************************************************************************"
	print "\t\t\t\t\tIts time for toss"
	toss=int(raw_input("Enter any number:"))
	if toss%(random.randint(2,10))==0:
		print "You had won the toss"
		choice=raw_input("Batting or fielding(b/f):")
		match()
	else:
		print "You loss the toss"
		field()
