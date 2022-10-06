
from tkinter import *
from tkinter import messagebox
import pygame
import time


root = Tk()
root.title("tic tac toe")


player1 = False
count = 0



b = Button

def win1():
    if b1["text"] == 'O' and b2["text"] == "O" and b3["text"] == "O":
        messagebox.showinfo('tic tac ho','O wins')
        quit()
    elif b4["text"] == 'O' and b5["text"] == "O" and b6["text"] == "O":
        messagebox.showinfo('tic tac ho','O wins')
        quit()
    elif b7["text"] == 'O' and b8["text"] == "O" and b9["text"] == "O":
        messagebox.showinfo('tic tac ho','O wins')
        quit()
    elif b1["text"] == 'O' and b4["text"] == "O" and b7["text"] == "O":
        messagebox.showinfo('tic tac ho','O wins')
        quit()
    elif b2["text"] == 'O' and b5["text"] == "O" and b8["text"] == "O":
        messagebox.showinfo('tic tac ho','O wins')
        quit()
    elif b3["text"] == 'O' and b6["text"] == "O" and b9["text"] == "O":
        print('O wins')
        quit()
    elif b1["text"] == 'O' and b5["text"] == "O" and b9["text"] == "O":
        messagebox.showinfo('tic tac ho','O wins')
        quit()
    elif b3["text"] == 'O' and b5["text"] == "O" and b7["text"] == "O":
        messagebox.showinfo('tic tac ho','O wins')
        quit()
      

def win2():
    if b1["text"] == 'X' and b2["text"] == "X" and b3["text"] == "X":
        messagebox.showinfo('tic tac ho','X wins')
        quit()
    elif b4["text"] == 'X' and b5["text"] == "X" and b6["text"] == "X":
        messagebox.showinfo('tic tac ho','X wins')
        quit()
    elif b7["text"] == 'X' and b8["text"] == "X" and b9["text"] == "X":
        messagebox.showinfo('tic tac ho','X wins')
        quit()
    elif b1["text"] == 'X' and b4["text"] == "X" and b7["text"] == "X":
        messagebox.showinfo('tic tac ho','X wins')
        quit()
    elif b2["text"] == 'X' and b5["text"] == "X" and b8["text"] == "X":
        messagebox.showinfo('tic tac ho','X wins')
        quit()
    elif b3["text"] == 'X' and b6["text"] == "X" and b9["text"] == "X":
        messagebox.showinfo('tic tac ho','X wins')
        quit()
    elif b1["text"] == 'X' and b5["text"] == "X" and b9["text"] == "X":
        messagebox.showinfo('tic tac ho','X wins')
        quit()
    elif b3["text"] == 'X' and b5["text"] == "X" and b7["text"] == "X":
        print('X wins')
        messagebox.showinfo('tic tac ho','X wins')
        quit()
    
def clicked(b):
   # als er geklikt wordt en player1 = false dan komt er een X
   # player1 = True dan komt een O
    global player1, count

    if player1 == False:
        #vul x in button
        
        if b["text"] == " " and player1 == False:
            b["text"] = "X"
            count += 1
            player1 = True
        else:
            messagebox.showerror('tic tac toe', 'why you pressing filled square')
        
    elif player1 == True:    
        if b["text"] == " " and player1 == True:
            b["text"] = "O"
            player1 = False
            count += 1
        else:
            messagebox.showerror('tic tac toe', 'why you pressing filled square')
    win1()
    win2()
    if b["text"] != " " and count == 9:
        messagebox.showinfo('tic tac toe', 'Its a draw')
        quit()
        
   
    


b1 = Button(root,text=" ", font = ("Helvetica","16"),command = lambda:clicked(b1)  , width = 12, height = 6)
b2 = Button(root,text=" ", font = ("Helvetica","16"),command = lambda:clicked(b2)  , width = 12, height = 6)
b3 = Button(root,text=" ", font = ("Helvetica","16"),command = lambda:clicked(b3)  , width = 12, height = 6)

b4 = Button(root,text=" ", font = ("Helvetica","16"),command = lambda:clicked(b4)  ,  width = 12, height = 6 )
b5 = Button(root,text=" ", font = ("Helvetica","16"),command = lambda:clicked(b5)  ,  width = 12, height = 6 )
b6 = Button(root,text=" ", font = ("Helvetica","16"),command = lambda:clicked(b6)  ,  width = 12, height = 6 )

b7 = Button(root,text=" ", font = ("Helvetica","16"),command = lambda:clicked(b7)  ,  width = 12, height = 6 )
b8 = Button(root,text=" ", font = ("Helvetica","16"),command = lambda:clicked(b8)  ,  width = 12, height = 6 )
b9 = Button(root,text=" ", font = ("Helvetica","16"),command = lambda:clicked(b9)  ,  width = 12, height = 6 )

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)

b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)

b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)



labels = []
root.mainloop()
