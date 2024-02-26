from logic import initial_state, player, actions, result, terminal, utility, minimax 

def print_board(board):
    for row in board:
        print(' | '.join(cell if cell is not None else ' ' for cell in row))
        print('-'*10)

def main():
    board = initial_state()
    while not terminal(board):
        print_board(board)
        current_player = player(board)
        print(f"It's {current_player}\'s turn")   
        
        if player(board) == "X":
            while True:
                try:
                    row = int(input("Enter row number (1, 2 or 3): "))
                    col = int(input("Enter column number (1, 2 or 3): "))
                    row, col = row-1 , col-1
                    if (row, col) in actions(board):
                        break
                    else:
                        print("Invalid move try again")
                except ValueError:
                    print('Invalid Input. Try again')
            board = result(board, (row, col))

        else:
            action = minimax(board)
            board = result(board, action)

    print_board(board)
    game_res = utility(board)
    if game_res == 1:
        print("X wins!")
    elif game_res == -1:
        print("O wins!")
    else:
        print("It's a Tie!")

if __name__ == "__main__":
    main()
