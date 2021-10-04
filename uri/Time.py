n = int(input())

a = n // 365
n = n - a*365

m = n // 30
n = n - m*30

d = n

print(a,'ano(s)')
print(m,'mes(es)')
print(d,'dia(s)')