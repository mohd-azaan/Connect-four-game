from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame, CTkImage
from PIL import Image

# Define the Connect Four grid (7x7)
connect_four_grid = [[' ' for _ in range(7)] for _ in range(7)]

# Variable to track current player (Player 1 starts)
current_player = 1


def change_color(row, col):
    global current_player
    if row != 0:
        if current_player == 1:
            color = "#FFE569"  # Player 1 color
            piece = '1'
            current_player = 2  # Switch to Player 2's turn
        else:
            color = "#B70404"  # Player 2 color
            piece = '2'
            current_player = 1  # Switch to Player 1's turn

        # Update the grid and GUI
        connect_four_grid[row][col] = piece
        buttons[row][col].configure(text='', fg_color=color)
        check_win(row, col)  # Check for a win after each move


def column_clicked(col):
    # Find the lowest empty row in the clicked column and place the piece
    for row in range(6, -1, -1):
        if connect_four_grid[row][col] == ' ':
            change_color(row, col)
            break


def check_win(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # Horizontal, vertical, diagonal (\), diagonal (/)

    for dx, dy in directions:
        count = 1
        for dir in (-1, 1):
            x, y = row, col
            while 0 <= x + dx * dir < 7 and 0 <= y + dy * dir < 7 and connect_four_grid[x + dx * dir][y + dy * dir] == \
                    connect_four_grid[row][col]:
                count += 1
                x, y = x + dx * dir, y + dy * dir
            if count >= 4:
                # print(f"Player {connect_four_grid[row][col]} wins!")
                frame.pack_forget()
                window.geometry("600x430")
                congrats = CTkLabel(window,text=f"Congratulations", font=("arial", 40, "bold"), text_color="black")
                congrats.place(relx=0.5, rely=0.35, anchor="center")

                winning_label = CTkLabel(window, text=f"Player {connect_four_grid[row][col]} wins!", font=("arial", 35, "bold"), text_color="black")
                winning_label.place(relx=0.5, rely=0.45, anchor="center")
                # Implement further actions for winning scenario here
                return


buttons = [[0 for _ in range(7)] for _ in range(7)]

window = CTk()
window.configure(fg_color="#F8F0E5")
window.geometry("800x630")
label = CTkLabel(window, text="Connect FOUR", text_color="#0174BE", font=("arial", 50, "bold"))
label.pack(pady=20)

my_image = CTkImage(dark_image=Image.open("mark.png"), size=(30, 30))

frame = CTkFrame(window)
frame.pack(padx=30, pady=0)

for i in range(7):
    for j in range(7):
        if i == 0:
            button = CTkButton(frame, corner_radius=50, text="", width=10, height=50, image=my_image,
                               fg_color="light grey", hover_color="grey", command=lambda col=j: column_clicked(col))
            button.grid(row=i, column=j, padx=10, pady=10)
        else:
            button = CTkButton(frame, corner_radius=50, text="", width=50, height=50, hover=False, fg_color="#F8F0E5")
            button.grid(row=i, column=j, padx=10, pady=10)
        buttons[i][j] = button

window.mainloop()
