hour = input()
min = hour.split(":")
h = int(min[0])
m = int(min[1])

print(f"{h+1}:{m}")