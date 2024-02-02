def calculate_heuristic(board, player):
    player_count = 0
    opponent_count = 0

    # Check rows and columns
    for i in range(3):
        row_player_count = row_opponent_count = col_player_count = col_opponent_count = 0

        for j in range(3):
            # Check rows
            if board[i][j] == player:
                row_player_count += 1
            elif board[i][j] != ' ':
                row_opponent_count += 1

            # Check columns
            if board[j][i] == player:
                col_player_count += 1
            elif board[j][i] != ' ':
                col_opponent_count += 1

        if row_player_count == 3:
            player_count += 1
        if row_opponent_count == 3:
            opponent_count += 1

        if col_player_count == 3:
            player_count += 1
        if col_opponent_count == 3:
            opponent_count += 1

    # Check diagonals
    diag1_player_count = diag2_player_count = diag1_opponent_count = diag2_opponent_count = 0

    for i in range(3):
        # Check diagonals
        if board[i][i] == player:
            diag1_player_count += 1
        elif board[i][i] != ' ':
            diag1_opponent_count += 1

        if board[i][2 - i] == player:
            diag2_player_count += 1
        elif board[i][2 - i] != ' ':
            diag2_opponent_count += 1

    if diag1_player_count == 3 or diag2_player_count == 3:
        player_count += 1
    if diag1_opponent_count == 3 or diag2_opponent_count == 3:
        opponent_count += 1

    return player_count - opponent_count

# Example Tic-Tac-Toe board
example_board = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    ['O', 'X', 'O']
]

# Example player
example_player = 'X'

# Calculate heuristic value
heuristic_value = calculate_heuristic(example_board, example_player)

print("Heuristic value:", heuristic_value)