i=int(input())
x = [int(i) for i in input().split()]
x.sort()
if(i%2!=0):
	y=i//2
	print(x[y])
else:
	z=(i//2)
	l=z-1
	print(x[l],x[z])
