def display_pieces(board, turn, posible_movements):
    for i in range(8):
        for j in range(8):
            board[i][j].draw()

    for i in range(8):
        for j in range(8):
            if board[i][j].selected: board[i][j].draw_movements(turn, board, posible_movements)
def initial_position(board):
    for i in range(8):
        board[i][6].set_type('white', 'p')

    for i in range(8):
        board[i][1].set_type('black', 'p')

    for i in range(2):
        board[0 + 7 * i][0].set_type('black', 'T')
        board[1 + 5 * i][0].set_type('black', 'H')
        board[2 + 3 * i][0].set_type('black', 'B')
        board[3][0].set_type('black', 'Q')
        board[4][0].set_type('black', 'K')

    for i in range(2):
        board[0 + 7 * i][7].set_type('white', 'T')
        board[1 + 5 * i][7].set_type('white', 'H')
        board[2 + 3 * i][7].set_type('white', 'B')
        board[3][7].set_type('white', 'Q')
        board[4][7].set_type('white', 'K')