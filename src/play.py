import board
b = board.Board()
i = 0
col = 'B'
while(i != 10):
    print(b.toString())
    i+=1
    if(col == 'W'):
        col = 'B'
    else:
        col = 'W'
    while(True):
        start = str(input("Choose your starting piece: "))
        end = str(input("Choose your end place: "))
        if(b.play(start,end,col)):
            break
        else:
            print("Your move was invalid, try again")

