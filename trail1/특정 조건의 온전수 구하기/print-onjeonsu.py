n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0: # 2로 나누어 떨어진다
        continue
    if i % 10 == 5: # 10으로 나누면 나머지 5 -> 일의 자리가 5
        continue
    if i % 3 ==0 and i % 9 != 0: # 3으로 나누어 떨어지면서 9로 나누어 떨어지지 않는다.
        continue
    print(i, end=' ')
  