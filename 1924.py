x,y = map(int, input().split())
sum = 0
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, x):
    sum += months[i-1]
sum += y
print(days[sum % 7])