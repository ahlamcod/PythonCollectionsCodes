#imprtantcomponents
buttons=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#GUI of the game board
import tkinter
window=tkinter.Tk()
window.title("Tic Tac Toe Game")
window.configure(bg="grey")
label=tkinter.Label(window, text="Player 1 turn", font=("Ariel", 20))
value=0
label.grid(row=0, column=0, columnspan=3, sticky="we")  #sticky="we" is used to stretch label from west to east "we"
for row in range(3):
    for column in range(3):
        value=value+1
        button=tkinter.Button(window, text=value, font=("Ariel", 20), width=3, height=1)
        button.config(command=(lambda b=button, i=value-1: play(b, i))) #value stores the button index so we can use it with buttons array later
        button.grid(row=row+1, column=column)
#Button functions
def endOfGame(buttons):
    if (buttons[0]==buttons[1]==buttons[2]) or (buttons[3]==buttons[4]==buttons[5]) or (buttons[6]==buttons[7]==buttons[8]) or (buttons[0]==buttons[4]==buttons[8]) or (buttons[2]==buttons[4]==buttons[6]) or (buttons[0]==buttons[3]==buttons[6]) or (buttons[1]==buttons[4]==buttons[7]) or (buttons[2]==buttons[5]==buttons[8]):
        result=True
    else: result=False
    return result
def play(button, value):
    global label, buttons
    if label["text"]=="Player 1 turn": #the 1st player/ the X player turn 
        if button["text"]!="X" and button["text"]!="O": #not choose an already chosen button
            buttons[value]="X"
            button["text"]="X"
            if endOfGame(buttons)==True:
                if buttons[0]=="X":
                    label["text"]="Player 1 won!"
                else:
                    label["text"]="Player 2 won!"
            else:
                buttonsSet=set(buttons) #turnning the array to a set to get rid of duplicated elements
                xoSet={"X","O"}
                if buttonsSet==xoSet:
                    label["text"]="Game Over" 
                else:
                    label["text"]="Player 2 turn"  
    elif label["text"]=="Player 2 turn": #the 2nd player/ the O player turn 
        if button["text"]!="X" and button["text"]!="O": #not choose an already chosen button
            buttons[value]="O"
            button["text"]="O"
            if endOfGame(buttons)==True:
                if buttons[0]=="X":
                    label["text"]="Player 1 won!"
                else:
                    label["text"]="Player 2 won!"
            else:
                buttonsSet=set(buttons) #turnning the array to a set to get rid of duplicated elements
                xoSet={"X","O"}
                if buttonsSet==xoSet:
                    label["text"]="Game Over" 
                else:
                    label["text"]="Player 1 turn"
 
window.mainloop()
