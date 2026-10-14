n = int(input())
arr = list(map(int,input().split()))

new_arr = []
for element in arr:
    new_arr.append(element ** 2)

print(*new_arr)