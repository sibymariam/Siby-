a,b,c=map(int,input().split())
if (a>b)and(a>c):
	l=a
elif (b>a)and(b>c):
	l=b
else:
	l=c
print(l)
