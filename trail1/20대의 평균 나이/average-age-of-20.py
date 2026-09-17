total = 0 # 입력된 나이
count = 0 # 입력된 수


# 나오기 전까지
while True:
    n = int(input()) 
    if n < 20 or n > 29: 
        break
    total += n
    count += 1

print(f"{total / count:.2f}")    
