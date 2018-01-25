def board(l):
	for i in range(len(l)):
		print " +----++----++----++----++----+"
		for k in range(len(l)):
			print " |",l[i][k],
			if k==len(l)-1:
				print "|",
		print ""

def condition(a,z):
	if a=="b":
		if z!="b2" or "b3" or "b4" or "c2" or "c3" or "c4" or "d2" or "d3" or "d4":
			print "Conditon satisfied"
		else:
			print "\t\t\t\tConditions unsatisfied"
			user=raw_input("Enter the letter(b/i/n/g/o)")
			pos=raw_input("Enter the position")
			return condition(user,pos)
	elif a=="i":
		if z=="a2" or "b1" or "b2" or "b3" or "b4" or "b5" or "c2" or "d2" or "e2" or "d3" or "d4" or "d5" or "d1":
			print "Condition satisfied "
		else:
			print "\t\t\t\tConditions unsatisfied"
			user=raw_input("Enter the letter(b/i/n/g/o)")
			pos=raw_input("Enter the position")
			return condition(user,pos)
	elif a=="n":
		if z=="a3" or "c1" or "b3" or "c3" or "d3" or "e3":
			print "Condition satisfied"
		else:
			print "\t\t\t\tConditions unsatisfied"
			user=raw_input("Enter the letter(b/i/n/g/o)")
			pos=raw_input("Enter the position")
			return condition(user,pos)
	elif a=="g":
		if z=="a4" or "d1" or "b1" or "b4" or "b2" or "d2" or "d3" or "d4" or "d5" or "e4":
			print "Condition satisfied"
		else:
			print "\t\t\t\tConditions unsatisfied"
			user=raw_input("Enter the letter(b/i/n/g/o)")
			pos=raw_input("Enter the position")
			return condition(user,pos)
	else:
		if z=="a5" or "b5" or "c5" or "d5" or "e5" or "e1" or "e2" or "e3" or "e4" or "e5":
			print "Condition satisfied"
		else:
			print "\t\t\t\tConditions unsatisfied"
			user=raw_input("Enter the letter(b/i/n/g/o)")
			pos=raw_input("Enter the position")
			return condition(user,pos)
def instruction():
	l=[["a1","b1","c1","d1","e1"],["a2","b2","c2","d2","e2"],["a3","b3","c3","d3","e3"],["a4","b4","c4","d4","e4"],["a5","b5","c5","d5","e5"]]
	board(l)
	print "The above is the Bingo board "
	print "I think you know  the rules"
	print "Every time u have to enter the correct letter other wise you will repeat the sequence"
	print "With letter u have to enter the board number ie row and column number"
	print "R u ready:"
	print "***********************************************************"
	print "\t\t\t\tStart"
	print "***********************************************************"
instruction()
a=[]
a1=[]
b=[]
b1=[]
c=[]
c1=[]
d=[]
d1=[]
e=[]
e1=[]
l=[["a1","b1","c1","d1","e1"],["a2","b2","c2","d2","e2"],["a3","b3","c3","d3","e3"],["a4","b4","c4","d4","e4"],["a5","b5","c5","d5","e5"]]
name1=raw_input("Enter 1st player name:")
name2=raw_input("Enter 2nd player name:")
while True:
	user1=raw_input("Enter the letter(b/i/n/g/o)")
	pos1=raw_input("Enter the position by seeing the board")
	condition(user1,pos1)
	board()
