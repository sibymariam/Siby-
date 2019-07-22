N = int(input())
l = len(str(N))
sum = 0
t = N
while(t != 0 and t <=1000):
	sum = sum + ((t % 10) ** l)
	t = t // 10
if sum == N:
	print("yes")
else:
	print("no")
