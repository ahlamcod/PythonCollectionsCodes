#important components-------------------------------------------------------
buttons_values=[
    ["AC", "⬅️", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="]
    ]
top_symbols=["AC", "⬅️", "%", ]
right_symbols=["=", "+", "-", "*", "/"]
#defining color palette variables-------------------------------
blackColor="#000000"
darkgreyColor="#494949"
lightgreyColor="#AAAAAA"
orangeColor="#FF8226"
whiteColor="#FFFFFF"
#window creation------------------------------------------------------------
import tkinter

calcWindow=tkinter.Tk()
calcWindow.title("Calculator")
calcWindow.resizable(False,False)#the window size will be adjusted to the content size
#frame creation------------------------------------------------------------
frame=tkinter.Frame(calcWindow)
label=tkinter.Label(frame, text="0", font=("Ariel", 35), anchor="e", background=blackColor, foreground=whiteColor, width=4) #place the text in the east
label.grid(row=0, column=0, columnspan=4 , sticky="we") #sticky="we" is used to stretch label from west to east -- we --
#grid creation----------------------------------------------------------
for row in range(5):
    for column in range(4):
        value=buttons_values[row][column]
        button=tkinter.Button(frame, text=value, font=("Ariel", 20), width=3, height=1, command=(lambda v=value: button_clicked(v)))#make each value a button
        button.grid(row=row+1, column=column)#each button position
        if value in top_symbols:
            button.config(background=lightgreyColor, foreground=darkgreyColor)
        elif value in right_symbols:
            button.config(background=orangeColor, foreground=whiteColor)
        else:
            button.config(background=darkgreyColor, foreground=whiteColor)

frame.pack()#so the frame will be shown

#defining the button functions-------------------------------------------------------------
A="0"
B=None
operator=None
def clear(): #function used in AC tool
    global A,B, operator
    A="0"
    B=None
    operator=None
def floatToInt(num):
    if num%1==0:
        num=int(num)
    return num
def button_clicked(value):
    global A, B, operator, top_symbols, right_symbols, label
    if value in top_symbols: #test if it is a tool 
            if value=="AC":
                clear()
                label["text"]="0"
            elif value=="⬅️":
                # take the current text, remove the last character, and update it
                label["text"] = label["text"][:-1]
            else: #if its % percentage
                result=float(label["text"])/100
                label["text"]=str(floatToInt(result)) #in case it's not a float desplay it as an integer
    elif value in right_symbols: #test if it is an operator
            if value=="=":
                if operator is not None and A is not None:
                    numA=float(A)
                    numB=float(label["text"])
                    if operator=="+":
                        operationResult=numA+numB
                    elif operator=="-":
                        operationResult=numA-numB
                    elif operator=="*":
                        operationResult=numA*numB
                    else:
                        operationResult=numA/numB
                    label["text"]=str(floatToInt(operationResult))
                    clear() #se we can do multiple operations at once
            elif value in "-*/+":
                if operator==None:
                    A=label["text"]
                    label["text"]="0"
                    B="0"
                    operator=value
    else:
            if value==".": #decimal number
                if value not in label["text"]: #it an integer we can make it decimal
                    label["text"]+=value
            elif value in "0123456789":
                if label["text"]=="0":
                    label["text"]= value #we replace the 0 with the value
                else:
                    label["text"]+= value #we concatinate the new value to the old one
            else: #its ±
                result=float(label["text"])*-1
                label["text"]=str(floatToInt(result)) #in case it's not a float desplay it as an integer
calcWindow.mainloop()#so the window will be shown
