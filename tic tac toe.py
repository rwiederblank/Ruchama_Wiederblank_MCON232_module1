import random
def make_gameboard():
    gameboard = []
    for i in range(3):
        row = []
        for i in range(3):
            row.append("_")
        gameboard.append(row)
    return gameboard

def print_gameboard(board):
    for row in board:
        for elem in row:
            print(elem, end=" ")
        print()

def row_guess():
    while True:
        try:
            row_guess = int(input("Enter a row: "))
        except ValueError:
            print("Input must be an integer between 0 and 2")
            continue
        if row_guess < 0 or row_guess > 2:
            print("Input must be an integer between 0 and 2")
            continue
        return row_guess

def col_guess():
    while True:
        try:
            col_guess = int(input("Enter a col: "))
        except ValueError:
            print("Input must be an integer between 0 and 2")
            continue
        if col_guess < 0 or col_guess > 2:
            print("Input must be an integer between 0 and 2")
            continue
        return col_guess

def check_guess(board, row, col):
    if board[row][col] == "_":
        return True
    else:
        return False

def computer_guess(board):
    while True:
        if board[0][0] == "_":
            board[0][0] = "O"
            return board
        if board[0][2] == "_":
            board[0][2] = "O"
            return board
        if board[2][0] == "_":
            board[2][0] = "O"
            return board
        if board[2][2] == "_":
            board[2][2] = "O"
            return board
        if board[1][1] == "_":
            board[1][1] == "O"
            return board
        rand_row = random.randint(0,2)
        rand_col = random.randint(0,2)
        if board[rand_row][rand_col] == "_":
            board[rand_row][rand_col] = "O"
            return board
        continue

def check_for_x_winner(board):
    for row in board:
        if row[0] == "X" and row[1] == "X" and row[2] == "X":
            return True
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return True
    if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return True
    if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return True
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return True
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return True
    return False

def check_for_o_winner(board):
    for row in board:
        if row[0] == "O" and row[1] == "O" and row[2] == "O":
            return True
    if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return True
    if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return True
    if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return True
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return True
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return True
    return False

def check_for_tie(board):
    count = 0
    for row in board:
        for elem in row:
            if elem != "_":
                count += 1
    if count == 9:
        return True
def game_loop(board):
    while True:
        row = row_guess()
        col = col_guess()
        if check_guess(board, row, col):
            board[row][col] = "X"
            print("Current Board:")
            print_gameboard(board)
            if check_for_x_winner(board):
                print("X wins! ")
                return "X"
            if check_for_tie(board):
                print("No winner! It is a tie!")
                return None
            print("Computers Turn:")
            board = computer_guess(board)
            print_gameboard(board)
            if check_for_o_winner(board):
                print("O wins! ")
                return "O"
            if check_for_tie(board):
                print("No winner! It is a tie!")
                return None
        else:
            print("Spot taken. Choose again")
            continue

def play_game():
    board = make_gameboard()
    print_gameboard(board)
    score = game_loop(board)
    x = 0
    o = 0
    ties = 0
    if score == "X":
        x+=1
    if score == "O":
        o+=1
    if score == None:
        ties+=1
    while True:
        ask = input("Would you like to play again? (yes/no) ")
        if ask != "yes" and ask != "no":
            print("Please answer only y or n ")
            continue
        if ask == "no":
            print(f"Final Score X: {x}, O: {o}, Ties: {ties}")
            break
        if ask == "yes":
            print(f"Current Score X: {x}, O: {o}, Ties: {ties}")
            print("Have fun!")
            board = make_gameboard()
            score = game_loop(board)
            if score == "X":
                x += 1
            if score == "O":
                o += 1
            if score == None:
                ties += 1

play_game()





