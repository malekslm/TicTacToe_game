import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" ".join(row))

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'O'):
        return -1
    elif is_winner(board, 'X'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '
        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val
    return best_move

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'O'

        self.buttons = [[tk.Button(root, text=' ', font=('Arial', 24), width=5, height=2, command=lambda i=i, j=j: self.on_click(i, j)) for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == ' ' and not is_winner(self.board, 'O') and not is_winner(self.board, 'X'):
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)

            if is_winner(self.board, self.current_player):
                messagebox.showinfo("Game Over", "BSAHTAK CHIKH  ")
                self.reset_board()
            elif is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                if self.current_player == 'X':
                    self.ai_move()

    def ai_move(self):
        row, col = best_move(self.board)
        self.board[row][col] = 'X'
        self.buttons[row][col].config(text='X', state=tk.DISABLED)

        if is_winner(self.board, 'X'):
            messagebox.showinfo("Game Over", "RBAHTAK CHIKH")
            self.reset_board()
        elif is_board_full(self.board):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_board()
        else:
            self.current_player = 'O'

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text=' ', state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
