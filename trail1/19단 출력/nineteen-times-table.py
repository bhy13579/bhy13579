for i in range(19):
    for j in range(19):
        print(f"{i+1} * {j+1} = {(i+1) * (j+1)}", end=' ')

        if j % 2== 1:
            print()

        elif j == 18:
            print()
        
        else:
            print('/ ', end='')