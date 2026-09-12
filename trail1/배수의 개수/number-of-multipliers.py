counta = 0
countb = 0
for _ in range(10):
    n = int(input())
    if n % 3 == 0:
        counta += 1 
    if n % 5 == 0:
        countb += 1
print(counta, countb)