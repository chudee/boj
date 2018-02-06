n = int(input())
l = list(map(int, input().split()))
m = max(l)
sum = 0
for i in range(n):
    sum += l[i]/m*100

print(sum/len(l))
