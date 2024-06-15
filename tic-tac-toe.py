import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []

        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.window, text=" ", font='normal 20 bold', height=3, width=6,
                               command=lambda i=i: self.click_button(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def click_button(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif " " not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True
        return False

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
