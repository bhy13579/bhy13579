a, b, c = map(int, input().split())

print(int(a == min(a, b, c)), int(a == b == c))