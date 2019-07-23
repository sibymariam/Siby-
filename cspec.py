s=input()
a=0
for i in s:
	c=i.isalpha()
	d=i.isdigit()
	if(c==False and d==False):
		a=a+1
print(a)
