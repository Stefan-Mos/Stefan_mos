# Stefan_mos
#Tic Tac Toe programma
#dit is een test voor vlads commit.
from tkinter import *
from tkinter import messagebox
from random import choice
import random
import time

s = Tk()
s.title('hoeveel rondes?')
times = 0

actuele_stand = []
hatsa = 1
def tweeopeenrijchecken(eg):
        for i in range(0,9):
            eg = int(eg)
            a.append(eg["text"])
            eg = int(eg)
            eg = eg + 1
            print(a)
def een_keer():
    global times
    times = 1
    s.destroy()

def drie_keer():
    global times
    times = 3
    s.destroy()
    
def vijf_keer():
    global times
    times = 5
    s.destroy()


bs = Button(s, text = 'een keer', command = een_keer,  width = 10, height = 3)
bd = Button(s,text = 'drie keer', command = drie_keer, width = 10, height = 3)
bf = Button(s,text = 'vijf keer', command = vijf_keer, width = 10, height = 3 )
bs.grid(row = 1, column = 1)
bd.grid(row = 2, column = 1)
bf.grid(row = 3, column = 1)

s.mainloop()

root = Tk()
root.title("tic tac toe")

uitslagen = []

player1 = False
count = 0
x = 0
o = 0

b = Button

def print_uitslagen():
    for i in range(len(uitslagen)):
            print(f'''
            {uitslagen[i][0]}|{uitslagen[i][1]}|{uitslagen[i][2]}
            ---------------------------------------
            {uitslagen[i][3]}|{uitslagen[i][4]}|{uitslagen[i][5]}
            ---------------------------------------
            {uitslagen[i][6]}|{uitslagen[i][7]}|{uitslagen[i][8]}''')
c = 0
def win1():
    global o
    wino = False
    if b1["text"] == 'O' and b2["text"] == "O" and b3["text"] == "O":
        print('O wins')
        o += 1
        wino = True
    elif b4["text"] == 'O' and b5["text"] == "O" and b6["text"] == "O":
        print('O wins')
        o += 1
        wino = True
    elif b7["text"] == 'O' and b8["text"] == "O" and b9["text"] == "O":
        print('O wins')
        o += 1
        wino = True
    elif b1["text"] == 'O' and b4["text"] == "O" and b7["text"] == "O":
        print('O wins')
        o += 1
        wino = True
    elif b2["text"] == 'O' and b5["text"] == "O" and b8["text"] == "O":
        print('O wins')
        o += 1
        wino = True
    elif b3["text"] == 'O' and b6["text"] == "O" and b9["text"] == "O":
        print('O wins')
        o += 1
        wino = True
    elif b1["text"] == 'O' and b5["text"] == "O" and b9["text"] == "O":
        print('O wins')
        o += 1
        wino = True
    elif b3["text"] == 'O' and b5["text"] == "O" and b7["text"] == "O":
        print('O wins')
        o += 1
        wino = True
    if wino:
        uitslagen.append([b1["text"],b2["text"],b3["text"],b4["text"],b5["text"],b6["text"],b7["text"],b8["text"],b9["text"]])
        kom()
        

def win2():
    winx = False
    global x
    if b1["text"] == 'X' and b2["text"] == "X" and b3["text"] == "X":
        print('X wins')
        x += 1
        winx = True
    elif b4["text"] == 'X' and b5["text"] == "X" and b6["text"] == "X":
        print('X wins')
        x += 1
        winx = True
    elif b7["text"] == 'X' and b8["text"] == "X" and b9["text"] == "X":
        print('X wins')
        x += 1
        winx = True
    elif b1["text"] == 'X' and b4["text"] == "X" and b7["text"] == "X":
        print('X wins')
        x += 1
        winx = True
    elif b2["text"] == 'X' and b5["text"] == "X" and b8["text"] == "X":
        print('X wins')
        x += 1
        winx = True
    elif b3["text"] == 'X' and b6["text"] == "X" and b9["text"] == "X":
        print('X wins')
        x += 1
        winx = True
    elif b1["text"] == 'X' and b5["text"] == "X" and b9["text"] == "X":
        print('X wins')
        x += 1
        winx = True
    elif b3["text"] == 'X' and b5["text"] == "X" and b7["text"] == "X":
        print('X wins')
        x += 1
        winx = True
    if winx:
        uitslagen.append([b1["text"],b2["text"],b3["text"],b4["text"],b5["text"],b6["text"],b7["text"],b8["text"],b9["text"]])
        kom()


    
def clicked(b):
   # als er geklikt wordt en player1 = false dan komt er een X
   # player1 = True dan komt een O
    global player1, c, x , o

    if player1 == False and positions != None:
        #vul x in button
        win1()
        win2()
        
        if b["text"] == " " and player1 == False:
            b["text"] = "X"    
            positions.remove(b)
            win1()
            win2()
            
            
            player1 = True       
            
            if player1 == True and len(positions) != 0:
                win1()
                win2()
                b = 0
                if b == 0:
                    if b5["text"] == " ":
                        clicked(b5)
                        b = b + 1
                if b1["text"] == b2["text"] and b3["text"] == " " and b1["text"] != " ":
                    clicked(b3)
    
                elif b1["text"] == b3["text"] and b2["text"] == " "and b1["text"] != " ":
                    clicked(b2)
                    
                elif b2["text"] == b3["text"] and b1["text"] == " "and b2["text"] != " ":
                    clicked(b1)
                    
                elif b4["text"] == b5["text"] and b6["text"] == " "and b4["text"] != " ":
                    clicked(b6)
                    
                elif b4["text"] == b6["text"] and b5["text"] == " "and b4["text"] != " ":
                    clicked(b5)
                    
                elif b5["text"] == b6["text"] and b4["text"] == " "and b5["text"] != " ":
                    clicked(b4)
                    
                elif b7["text"] == b8["text"] and b9["text"] == " "and b7["text"] != " ":
                    clicked(b9)
                    
                elif b7["text"] == b9["text"] and b8["text"] == " "and b7["text"] != " ":
                    clicked(b8)
                    
                elif b8["text"] == b9["text"] and b7["text"] == " "and b8["text"] != " ":
                    clicked(b7)
                    
                elif b1["text"] == b4["text"] and b7["text"] == " "and b1["text"] != " ":
                    clicked(b7)
                    
                elif b1["text"] == b7["text"] and b4["text"] == " "and b1["text"] != " ":
                    clicked(b4)
                    
                elif b4["text"] == b7["text"] and b1["text"] == " "and b4["text"] != " ":
                    clicked(b1)
                    
                elif b2["text"] == b5["text"] and b8["text"] == " "and b2["text"] != " ":
                    clicked(b8)
                    
                elif b2["text"] == b8["text"] and b5["text"] == " "and b2["text"] != " ":
                    clicked(b5)
                    
                elif b5["text"] == b8["text"] and b2["text"] == " "and b5["text"] != " ":
                    clicked(b2)
                    
                elif b3["text"] == b6["text"] and b9["text"] == " "and b3["text"] != " ":
                    clicked(b9)
                    
                elif b3["text"] == b9["text"] and b6["text"] == " "and b3["text"] != " ":
                    clicked(b6)
                    
                elif b6["text"] == b9["text"] and b3["text"] == " "and b6["text"] != " ":
                    clicked(b3)
                    
                elif b1["text"] == b5["text"] and b9["text"] == " "and b1["text"] != " ":
                    clicked(b9)
                    
                elif b1["text"] == b9["text"] and b5["text"] == " "and b1["text"] != " ":
                    clicked(b5)
                    
                elif b5["text"] == b9["text"] and b1["text"] == " "and b5["text"] != " ":
                    clicked(b1)
                    
                elif b3["text"] == b5["text"] and b7["text"] == " "and b3["text"] != " ":
                    clicked(b7)
                    
                elif b3["text"] == b7["text"] and b5["text"] == " "and b3["text"] != " ":
                    clicked(b5)
                    
                elif b5["text"] == b7["text"] and b3["text"] == " "and b5["text"] != " ":
                    clicked(b3)
    
                else:
                    a = random.choice(positions)
                    positions.remove(a)
                    clicked(a)
                
                win1()
                win2()
                
                player1 = False
                
                
        else:
            messagebox.showerror('tic tac toe', 'why you pressing filled square')
        
        
    
        
    elif player1 == True:    
        if b["text"] == " " and player1 == True:
            b["text"] = "O"
            player1 = False
    
    win1()
    win2()
            
    if not positions:
        messagebox.showinfo('gelijkspel','je hebt gelijkspel gespeeld tegen een randomiser bot      Schaam je diep!!!')
        player1 = False
        kom()
    
    
    tweeopeenrijchecken(hatsa)
  
def kom():
    # zet ervoor de code om het venster schoon te maken.
    
    global c
    c += 1
    player1 = False
    if c < times:
            positions.clear()
            root.withdraw()
            positions.extend([b1,b2,b3,b4,b5,b6,b7,b8,b9])
            
            
            for i in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
                i.configure(text = ' ')
                
            
            root.deiconify()
            player1 = False
            print(c)
            
            
    else:
        print_uitslagen()
        print(f"x heeft {x} punten")
        print (f"o heeft {o} punten")
        
        
        quit()
    
    return count



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

positions = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

root.mainloop()



