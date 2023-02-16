def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")

def get_move(player, board):
    while True:
        move = input(f"{player}' ход (X or O): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
            return int(move) - 1
        else:
            print("Неправильный ход, пробуй еще раз")

def check_win(board):
    winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]
    for position in winning_positions:
        if board[position[0]] == board[position[1]] == board[position[2]] != " ":
            return True
    return False

def play_game():
    board = [" "] * 9
    print("Крестики нолики!")
    print_board(list(range(1, 10)))
    player = "X"
    while True:
        print()
        print_board(board)
        print()
        move = get_move(player, board)
        board[move] = player
        print_board(list(range(1, 10)))
        if check_win(board):
            print(f"{player} Выиграл")
            break
        if " " not in board:
            print("Ничья!")
            break
        player = "O" if player == "X" else "X"

play_game()
