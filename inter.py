low,upp=map(int,input().split())
for i in range(low+1,upp):
	if(i%2!=0):
		print(i, end=' ')
