# 가로, 세로, 문자
while True:
    row, column, letter = input().split()
    row, column = int(row), int(column)
    print(row*column)

    # input = (row, column, letter)
    if letter == 'C':
        break