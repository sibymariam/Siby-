low,upp = map(int,input().split())
for num in range(low+1,upp):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num, end=' ')
