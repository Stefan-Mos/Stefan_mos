# Stefan_mos
Tic Tac Toe programma
#tic tac toe random ai x side
# code werkt alleen het is oneindig
# je kan alleen gelijkspelen


from tkinter import *
from tkinter import messagebox
from random import choice
import random
import time

root = Tk()
root.title("tic tac toe")


player1 = False
count = 0

b = Button

x = 2
def win1():
    if b1["text"] == 'O' and b2["text"] == "O" and b3["text"] == "O":
        print('O wins')
        kom()
    elif b4["text"] == 'O' and b5["text"] == "O" and b6["text"] == "O":
        print('O wins')
        kom()
    elif b7["text"] == 'O' and b8["text"] == "O" and b9["text"] == "O":
        print('O wins')
        kom()
    elif b1["text"] == 'O' and b4["text"] == "O" and b7["text"] == "O":
        print('O wins')
        kom()
    elif b2["text"] == 'O' and b5["text"] == "O" and b8["text"] == "O":
        print('O wins')
        kom()
    elif b3["text"] == 'O' and b6["text"] == "O" and b9["text"] == "O":
        print('O wins')
        kom()
    elif b1["text"] == 'O' and b5["text"] == "O" and b9["text"] == "O":
        print('O wins')
        kom()
    elif b3["text"] == 'O' and b5["text"] == "O" and b7["text"] == "O":
        print('O wins')
        kom()
      

def win2():
    if b1["text"] == 'X' and b2["text"] == "X" and b3["text"] == "X":
        print('X wins')
        kom()
    elif b4["text"] == 'X' and b5["text"] == "X" and b6["text"] == "X":
        print('X wins')
        kom()
    elif b7["text"] == 'X' and b8["text"] == "X" and b9["text"] == "X":
        print('X wins')
        kom()
    elif b1["text"] == 'X' and b4["text"] == "X" and b7["text"] == "X":
        print('X wins')
        kom()
    elif b2["text"] == 'X' and b5["text"] == "X" and b8["text"] == "X":
        print('X wins')
        kom()
    elif b3["text"] == 'X' and b6["text"] == "X" and b9["text"] == "X":
        print('X wins')
        kom()
    elif b1["text"] == 'X' and b5["text"] == "X" and b9["text"] == "X":
        print('X wins')
        kom()
    elif b3["text"] == 'X' and b5["text"] == "X" and b7["text"] == "X":
        print('X wins')
        kom()



    
def clicked(b):
   # als er geklikt wordt en player1 = false dan komt er een X
   # player1 = True dan komt een O
    global player1, count, x

    if player1 == False and count < 9:
        #vul x in button
        
        if b["text"] == " " and player1 == False:
            b["text"] = "X"
            
            positions.remove(b)
            
            count += 1
            player1 = True
            
            while player1 == True and len(positions) != 0:
                a = random.choice(positions)
                positions.remove(a)
                clicked(a)
                count +=1
                
                player1 = False
                
        else:
            messagebox.showerror('tic tac toe', 'why you pressing filled square')
        
        
    
    elif player1 == True:    
        if b["text"] == " " and player1 == True:
            b["text"] = "O"
            player1 = False
            
        
    if positions == 0 or count >= 9 :
        messagebox.showinfo('gelijkspel','je hebt gelijkspel gespeeld tegen een randomiser bot      Schaam je diep!!!')

        count = 0
        positions.extend([b1,b2,b3,b4,b5,b6,b7,b8,b9])
        if x == 2:
            kom()
            player1 = False
            
            return x
        else:
            quit()
        
    
  
def kom():
    # zet ervoor de code om het venster schoon te maken.
    
    root.withdraw()
    
    for i in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
        i.configure(text = ' ')
    
    
    root.deiconify()
    

bs = Button(root, text = 1, width = 3, height = 1)

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
bs.grid(row = 3, column = 1)

positions= [b1,b2,b3,b4,b5,b6,b7,b8,b9]


root.mainloop()
