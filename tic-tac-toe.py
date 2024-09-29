# TIC-TAC-TOE Game Program
from tkinter import *

turn = True

def button_click(row,column):
    global turn

    if turn:
        buttons[row][column].config(text="X", bg="lightblue", state=DISABLED)
        turn_info_label.set("Turn Player_2")
    else:
        buttons[row][column].config(text="O", bg="pink", state=DISABLED)
        turn_info_label.set("Turn Player_1")
    turn = not turn
    
    winner = check_winner()
    if winner is not None:
        if winner == "X":
                turn_info_label.set("Player_1 wins")
                
        elif winner == "O":
                turn_info_label.set("Player_2 wins")
        disable_all_buttons()
    else:
        tie_situation = check_tie()
        if tie_situation == "Tie!":
            turn_info_label.set("Tie!")

def check_winner():
    #check rows
    for row in range(3):
            if buttons[row][0].cget('text') == buttons[row][1].cget('text') == buttons[row][2].cget('text') != "":
                 return buttons[row][0].cget('text')
    
    #check cols
    for col in range(3):
         if buttons[0][col].cget('text') == buttons[1][col].cget('text') == buttons[2][col].cget('text') != "":
              return buttons[0][col].cget('text')
         
    #check cross
    if buttons[0][0].cget('text') == buttons[1][1].cget('text') == buttons[2][2].cget('text') != "":
        return buttons[0][0].cget('text')
    
    elif buttons[0][2].cget('text') == buttons[1][1].cget('text') == buttons[2][0].cget('text') != "":
        return buttons[0][0].cget('text')
    
    return None

def check_tie():
    for i in range(3):
        for j in range(3):
            if buttons[i][j].cget('text') == "":
                return None
    return "Tie!"
            
def disable_all_buttons():
    for i in range(3):
         for j in range(3):
            buttons[i][j].config(state=DISABLED)

def play_again():
    global turn
    turn = True

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=ACTIVE, bg="SystemButtonFace")
            turn_info_label.set("New game!\n Turn Player_1")


window = Tk()
window.title("Tic-Tac-Toe")
icon = PhotoImage(file='my_logo.png')
window.iconphoto(True,icon)
window.geometry("500x780+360+30")

frame = Frame(window)
frame.pack(padx=10, pady=2)

buttons= [[None for i in range(3)] for j in range(3)]

turn_info_label = StringVar()
turn_info_label.set("Turn Player_1")
turn_info = Label(textvariable= turn_info_label, font=('Calibri',15), fg='red')
turn_info.pack() 

for i in  range(3):
    for j in range(3):
        buttons[i][j] = Button(frame, text = "", width=10, height=4, font=('Calibri', 20, 'bold'),
                               command= lambda row=i, col=j: button_click(row,col))
        buttons[i][j].grid(row=i, column=j)

again_button = Button(frame,text = "Play Again", width=63, height=8,
                      font=('Calibri', 10, 'bold'), fg="black", command= play_again)
again_button.grid(row=3, column=0, columnspan=3)

window.mainloop()