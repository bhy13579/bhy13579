date = input()
piece = date.split("-")
year = int(piece[2])
month = int(piece[0])
day = int(piece[1])
print(f"{year}.{month}.{day}")


