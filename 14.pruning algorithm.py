import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = alpha_beta_pruning(board, depth + 1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = alpha_beta_pruning(board, depth + 1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = alpha_beta_pruning(board, 0, -math.inf, math.inf, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        if current_player == "X":
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                if check_winner(board) == "X":
                    print_board(board)
                    print("Player X wins!")
                    break
                current_player = "O"
            else:
                print("This spot is already taken. Try again.")
        else:
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = "O"
                if check_winner(board) == "O":
                    print_board(board)
                    print("Player O wins!")
                    break
                current_player = "X"

        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()
