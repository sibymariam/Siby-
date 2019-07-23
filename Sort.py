i=int(input())
while(i>=0 and i<=10000):
	x = [int(i) for i in input().split()]
	x.sort()
	print (*x, sep =' ')
