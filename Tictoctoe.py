board = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])

player = "X"

for _ in range(9):
    show()
    pos = int(input(f"{player} position (0-8): "))
    board[pos] = player
    player = "O" if player == "X" else "X"

show()
