i=int(input())
x = [int(i) for i in input().split()]
x.sort()
print (*x, sep =' ')
