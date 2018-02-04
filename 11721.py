str = input(); n = len(str)

for i in range(n):
    if (i+1) % 10 == 0: print(str[i])
    else: print(str[i], end='')
    