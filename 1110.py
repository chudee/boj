def cycle(n):
    a, b = n[-2], n[-1]
    c = str(int(a)+int(b))[-1]
    return b+c

n = input()
if(len(n) < 2):
    n = '0' + n
m = n
cnt = 0
while True:
    if cnt != 0 and m == n:
        print(cnt)
        break
    else: 
        n = cycle(n)
        cnt += 1
