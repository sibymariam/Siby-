num = int(input())
if (num>0 and num<=1000):
    for i in range(2, num):
        if (num % i) == 0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
