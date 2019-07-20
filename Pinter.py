low,upp=map(int,input().split())
for n in range(low+1,upp):
  if(n>0):
  	for i in range(2,n):
  		if(n%i==0):
  			break
  	else:
  			print(n, end=' ')
