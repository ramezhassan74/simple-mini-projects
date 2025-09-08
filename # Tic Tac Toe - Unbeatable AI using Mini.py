

def init_board():
    return [None] * 9  # 9 cells (0..8)

def print_board(b):
    def cell(i):
        return b[i] if b[i] is not None else str(i+1)
    row = lambda r: f" {cell(3*r)} | {cell(3*r+1)} | {cell(3*r+2)} "
    sep = "---+---+---"
    print("\n" + row(0) + f"\n{sep}\n" + row(1) + f"\n{sep}\n" + row(2) + "\n")

WIN_LINES = [
    (0,1,2), (3,4,5), (6,7,8),   # rows
    (0,3,6), (1,4,7), (2,5,8),   # columns
    (0,4,8), (2,4,6)             # diagonals
]

def check_winner(b):
    for a, c, d in WIN_LINES:
        if b[a] is not None and b[a] == b[c] and b[a] == b[d]:
            return b[a]
    return None

def available_moves(b):
    return [i for i, v in enumerate(b) if v is None]

def is_draw(b):
    return check_winner(b) is None and len(available_moves(b)) == 0

def evaluate_terminal(b, ai, human, depth):
    winner = check_winner(b)
    if winner == ai:
        return 10 - depth
    if winner == human:
        return -10 + depth
    if is_draw(b):
        return 0
    return None

def minimax(b, depth, is_maximizing, ai, human):
    terminal = evaluate_terminal(b, ai, human, depth)
    if terminal is not None:
        return terminal, None

    if is_maximizing:  # AI's turn
        best_score = float('-inf')
        best_move = None
        for m in available_moves(b):
            b[m] = ai
            score, _ = minimax(b, depth + 1, False, ai, human)
            b[m] = None
            if score > best_score:
                best_score, best_move = score, m
        return best_score, best_move
    else:  # Human's turn
        best_score = float('inf')
        best_move = None
        for m in available_moves(b):
            b[m] = human
            score, _ = minimax(b, depth + 1, True, ai, human)
            b[m] = None
            if score < best_score:
                best_score, best_move = score, m
        return best_score, best_move

def get_ai_move(b, ai='O', human='X'):
    _, move = minimax(b, depth=0, is_maximizing=True, ai=ai, human=human)
    return move

def get_user_move(b):
    while True:
        raw = input("Choose a cell (1-9): ").strip()
        if not raw.isdigit():
            print("⚠️ Enter a number 1-9.")
            continue
        idx = int(raw) - 1
        if idx < 0 or idx > 8:
            print("⚠️ Invalid cell. Use 1-9.")
            continue
        if b[idx] is not None:
            print("⚠️ Cell already taken.")
            continue
        return idx

def play():
    board = init_board()
    human, ai = 'X', 'O'
    print("Welcome! You are 'X'. The computer is 'O'.")
    print_board(board)

    while True:
        # Human move
        u = get_user_move(board)
        board[u] = human
        print_board(board)
        if check_winner(board) == human:
            print("🎉 You win!")
            break
        if is_draw(board):
            print("🤝 It's a draw.")
            break

        ai_move = get_ai_move(board, ai=ai, human=human)
        board[ai_move] = ai
        print("🤖 AI plays...")
        print_board(board)
        if check_winner(board) == ai:
            print("💻 AI wins!")
            break
        if is_draw(board):
            print("🤝 It's a draw.")
            break

if __name__ == "__main__":
    play()
