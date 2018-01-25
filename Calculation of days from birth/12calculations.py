from time import *
li=list(localtime())
m=[31,28,31,30,31,30,31,31,30,31,30,31]
year=li[0]
month=li[1]
day=li[2]
y=int(raw_input("Enter the year:"))
k=int(raw_input("Enter month:"))
z=int(raw_input("Enter Day:"))
if k>month:
	if z>day:
		de=z-day
		prs=year-y
		prs=prs*365
		pr=k-month
		sum=0
		for i in range(month,k):
			sum=sum+m[i]
	else:
		de=m[month-1]-day+z
		prs=year-y
		prs=prs*365
		pr=k-month
		sum=0
		for i in range(month,k-1):
			sum=sum+m[i]
else:
	if z>day:
		prs=year-y
		prs=prs-1
		prs=prs*365
		pr=month-k
		n=m[month:]+m[:k+1]
		sum=0
		for i in range(len(n)):
			sum=sum+n[i]
	else:
		prs=year-y
		prs=prs-1
		de=m[month-1]-day+z
		prs=prs*365
		pr=
		n=m[month:]+m[:k]
		sum=0
		for i in range(len(n)):
			sum=sum+n[i]
total=sum+prs+de
newer=total%7;
print newer;

