n = int(input())

for i in range(n):
    l = list(map(int, input().split()))
    a = l.pop(0)
    b = len(list(filter(lambda x: x > sum(l)/a, l)))
    print('{0:0.3f}%'.format(b / a * 100))
    