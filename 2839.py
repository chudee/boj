n = int(input())
B = 0

while True:
    if n % 5 == 0:
        print((n // 5) + B)
        break
    elif n < 0: 
        print(-1) 
        break
    n-=3
    B+=1
