# Stefan_mos
Tic Tac Toe programma
from tkinter import *
from tkinter import messagebox
from random import choice
import random
import time

b = Button
l = Label
s = Tk()
s.title('hoeveel rondes?')
times = 0

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


bs = Button(s, text = 'een keer', command = een_keer,  width = 60, height = 10)
bd = Button(s,text = 'drie keer', command = drie_keer, width = 60, height = 10)
bf = Button(s,text = 'vijf keer', command = vijf_keer, width = 60, height = 10)
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
gelijk = 0
c = 0
count = 0

def win1():
    global o
    if b1["text"] == 'O' and b2["text"] == "O" and b3["text"] == "O":
        print('O wins')
        o += 1
        volgende()
    elif b4["text"] == 'O' and b5["text"] == "O" and b6["text"] == "O":
        print('O wins')
        o += 1
        volgende()
    elif b7["text"] == 'O' and b8["text"] == "O" and b9["text"] == "O":
        print('O wins')
        o += 1
        volgende()
    elif b1["text"] == 'O' and b4["text"] == "O" and b7["text"] == "O":
        print('O wins')
        o += 1
        volgende()
    elif b2["text"] == 'O' and b5["text"] == "O" and b8["text"] == "O":
        print('O wins')
        o += 1
        volgende()
    elif b3["text"] == 'O' and b6["text"] == "O" and b9["text"] == "O":
        print('O wins')
        o += 1
        volgende()
    elif b1["text"] == 'O' and b5["text"] == "O" and b9["text"] == "O":
        print('O wins')
        o += 1
        volgende()
    elif b3["text"] == 'O' and b5["text"] == "O" and b7["text"] == "O":
        print('O wins')
        o += 1
        volgende()

def win2():
    global x
    if b1["text"] == 'X' and b2["text"] == "X" and b3["text"] == "X":
        print('X wins')
        x += 1
        volgende()
    elif b4["text"] == 'X' and b5["text"] == "X" and b6["text"] == "X":
        print('X wins')
        x += 1
        volgende()
    elif b7["text"] == 'X' and b8["text"] == "X" and b9["text"] == "X":
        print('X wins')
        x += 1
        volgende()
    elif b1["text"] == 'X' and b4["text"] == "X" and b7["text"] == "X":
        print('X wins')
        x += 1
        volgende()
    elif b2["text"] == 'X' and b5["text"] == "X" and b8["text"] == "X":
        print('X wins')
        x += 1
        volgende()
    elif b3["text"] == 'X' and b6["text"] == "X" and b9["text"] == "X":
        print('X wins')
        x += 1
        volgende()
    elif b1["text"] == 'X' and b5["text"] == "X" and b9["text"] == "X":
        print('X wins')
        x += 1
        volgende()
    elif b3["text"] == 'X' and b5["text"] == "X" and b7["text"] == "X":
        print('X wins')
        x += 1
        volgende()
    else:
        win1()
        
 
def clicked(b):
   # als er geklikt wordt en player1 = false dan volgendet er een X
   # player1 = True dan volgendet een O
    global player1, c, x , o , gelijk, count
    

    if player1 == False and positions is not False:
        
        #vul x in button
            
        if b["text"] == " " and player1 == False:
            
            b["text"] = "X"
            b['foreground'] = 'pink'
            b['background'] = 'red'
            
            print(positions)
            count += 1
            positions.remove(b)
            print(positions)
            
            if not win1() or not win2():
                player1 = True
            if win1() or win2():
                player1 = False
            
            
            
            
            if  not positions:
                count = 0
                messagebox.showinfo('gelijkspel','je hebt gelijkspel gespeeld tegen een randomiser bot                    schaam je diep!!!')
                player1 = False
                gelijk += 1
                volgende()
           
            if player1 == True and len(positions) != 0 or priority():
                
                if b1["text"] == b2["text"] and b3["text"] == " " and b1["text"] != " ":
                    clicked(b3)
                    positions.remove(b3)
                elif b1["text"] == b3["text"] and b2["text"] == " "and b1["text"] != " ":
                    clicked(b2)
                    positions.remove(b2)
                   
                elif b2["text"] == b3["text"] and b1["text"] == " "and b2["text"] != " ":
                    clicked(b1)
                    positions.remove(b1)
                   
                elif b4["text"] == b5["text"] and b6["text"] == " "and b4["text"] != " ":
                    clicked(b6)
                    positions.remove(b6)
                    
                elif b4["text"] == b6["text"] and b5["text"] == " "and b4["text"] != " ":
                    clicked(b5)
                    positions.remove(b5)
                   
                elif b5["text"] == b6["text"] and b4["text"] == " "and b5["text"] != " ":
                    clicked(b4)
                    positions.remove(b4)
                   
                elif b7["text"] == b8["text"] and b9["text"] == " "and b7["text"] != " ":
                    clicked(b9)
                    positions.remove(b9)
                   
                elif b7["text"] == b9["text"] and b8["text"] == " "and b7["text"] != " ":
                    clicked(b8)
                    positions.remove(b8)
                   
                elif b8["text"] == b9["text"] and b7["text"] == " "and b8["text"] != " ":
                    clicked(b7)
                    positions.remove(b7)
                   
                elif b1["text"] == b4["text"] and b7["text"] == " "and b1["text"] != " ":
                    clicked(b7)
                    positions.remove(b7)
                   
                elif b1["text"] == b7["text"] and b4["text"] == " "and b1["text"] != " ":
                    clicked(b4)
                    positions.remove(b4)
                   
                elif b4["text"] == b7["text"] and b1["text"] == " "and b4["text"] != " ":
                    clicked(b1)
                    positions.remove(b1)
                   
                elif b2["text"] == b5["text"] and b8["text"] == " "and b2["text"] != " ":
                    clicked(b8)
                    positions.remove(b8)
                   
                elif b2["text"] == b8["text"] and b5["text"] == " "and b2["text"] != " ":
                    clicked(b5)
                    positions.remove(b5)
                   
                elif b5["text"] == b8["text"] and b2["text"] == " "and b5["text"] != " ":
                    clicked(b2)
                    positions.remove(b2)
                   
                elif b3["text"] == b6["text"] and b9["text"] == " "and b3["text"] != " ":
                    clicked(b9)
                    positions.remove(b9)
                    
                elif b3["text"] == b9["text"] and b6["text"] == " "and b3["text"] != " ":
                    clicked(b6)
                    positions.remove(b6)
                    
                elif b6["text"] == b9["text"] and b3["text"] == " "and b6["text"] != " ":
                    clicked(b3)
                    positions.remove(b3)
                   
                elif b1["text"] == b5["text"] and b9["text"] == " "and b1["text"] != " ":
                    clicked(b9)
                    positions.remove(b9)

                elif b1["text"] == b9["text"] and b5["text"] == " "and b1["text"] != " ":
                    clicked(b5)
                    positions.remove(b5)
                   
                elif b5["text"] == b9["text"] and b1["text"] == " "and b5["text"] != " ":
                    clicked(b1)
                    positions.remove(b1)
                   
                elif b3["text"] == b5["text"] and b7["text"] == " "and b3["text"] != " ":
                    clicked(b7)
                    positions.remove(b7)
                   
                elif b3["text"] == b7["text"] and b5["text"] == " "and b3["text"] != " ":
                    clicked(b5)
                    positions.remove(b5)
                   
                elif b5["text"] == b7["text"] and b3["text"] == " "and b5["text"] != " ":
                    clicked(b3)
                    positions.remove(b3)
                
                elif b8["text"] == b9["text"] and b7["text"] == " " and b8["text"] != " ":
                    clicked(b7)
                    positions.remove(b7)

                else:
                    print('hallo')
                    print(positions)
                    a = random.choice(positions)
                    positions.remove(a)
                    clicked(a)
                    
                player1 = False
                win2()
                win1()
                count += 1
                print(count)
                       
        else:
            messagebox.showerror('tic tac toe', 'why you pressing filled square')
             
    elif player1 == True:    
        if b["text"] == " " and player1 == True:
            b["text"] = "O"
            b['foreground'] = 'cyan'
            b['background'] = 'green'
            player1 = False
       
def print_uitslagen():
    for i in range(len(uitslagen)):
        j = i + 1
        print(f'''
        \033[1mgame {j}\033[0m
         {uitslagen[i][0]}|{uitslagen[i][1]}|{uitslagen[i][2]}
         -----
         {uitslagen[i][3]}|{uitslagen[i][4]}|{uitslagen[i][5]}
         -----
         {uitslagen[i][6]}|{uitslagen[i][7]}|{uitslagen[i][8]}
         ''')
 
def volgende():
    # zet ervoor de code om het venster schoon te maken.
    global c, count
    count = 0
    c += 1
    uitslagen.append([b1["text"],b2["text"],b3["text"],b4["text"],b5["text"],b6["text"],b7["text"],b8["text"],b9["text"]])
    player1 = False
    if c < times:
            positions.clear()
            print(positions)
            root.withdraw()
            positions.extend([b1,b2,b3,b4,b5,b6,b7,b8,b9])
           
            for i in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
                i['background'] = 'black'
                i.configure(text = ' ')
               
            root.deiconify()
            player1 = False
     
    else:
        print_uitslagen()
        print(f"x heeft {x} punten")
        print (f"o heeft {o} punten")
        print(f"{gelijk} keer gelijk gespeeld")
        quit()

def priority():
    if b1["text"] == b2["text"] and b3["text"] == " " and b1["text"] == "O":
        clicked(b3)
        positions.remove(b3)
        
    elif b1["text"] == b3["text"] and b2["text"] == " "and b1["text"] == "O":
        clicked(b2)
        positions.remove(b2)
        
    elif b2["text"] == b3["text"] and b1["text"] == " "and b2["text"] == "O":
        clicked(b1)
        positions.remove(b1)
        
    elif b4["text"] == b5["text"] and b6["text"] == " "and b4["text"] == "O":
        clicked(b6)
        positions.remove(b6)
        
    elif b4["text"] == b6["text"] and b5["text"] == " "and b4["text"] == "O":
        clicked(b5)
        positions.remove(b5)           
    elif b5["text"] == b6["text"] and b4["text"] == " "and b5["text"] == "O":
        clicked(b4)
        positions.remove(b4)
                   
    elif b7["text"] == b8["text"] and b9["text"] == " "and b7["text"] == "O":
        clicked(b9)
        positions.remove(b9)
                   
    elif b7["text"] == b9["text"] and b8["text"] == " "and b7["text"] == "O":
        clicked(b8)
        positions.remove(b8)
                   
    elif b8["text"] == b9["text"] and b7["text"] == " "and b8["text"] == "O":
        clicked(b7)
        positions.remove(b7)
                   
    elif b1["text"] == b4["text"] and b7["text"] == " "and b1["text"] == "O":
        clicked(b7)
        positions.remove(b7)
                   
    elif b1["text"] == b7["text"] and b4["text"] == " "and b1["text"] == "O":
        clicked(b4)
        positions.remove(b4)
                   
    elif b4["text"] == b7["text"] and b1["text"] == " "and b4["text"] == "O":
        clicked(b1)
        positions.remove(b1)
                   
    elif b2["text"] == b5["text"] and b8["text"] == " "and b2["text"] == "O":
        clicked(b8)
        positions.remove(b8)
                   
    elif b2["text"] == b8["text"] and b5["text"] == " "and b2["text"] == "O":
        clicked(b5)
        positions.remove(b5)
                   
    elif b5["text"] == b8["text"] and b2["text"] == " "and b5["text"] == "O":
        clicked(b2)
        positions.remove(b2)
                   
    elif b3["text"] == b6["text"] and b9["text"] == " "and b3["text"] == "O":
        clicked(b9)
        positions.remove(b9)

    elif b3["text"] == b9["text"] and b6["text"] == " "and b3["text"] == "O":
        clicked(b6)
        positions.remove(b6)
                   
    elif b6["text"] == b9["text"] and b3["text"] == " "and b6["text"] == "O":
        clicked(b3)
        positions.remove(b3)
                   
    elif b1["text"] == b5["text"] and b9["text"] == " "and b1["text"] == "O":
        clicked(b9)
        positions.remove(b9)

    elif b1["text"] == b9["text"] and b5["text"] == " "and b1["text"] == "O":
        clicked(b5)
        positions.remove(b5)
                   
    elif b5["text"] == b9["text"] and b1["text"] == " "and b5["text"] == "O":
        clicked(b1)
        positions.remove(b1)
                   
    elif b3["text"] == b5["text"] and b7["text"] == " "and b3["text"] == "O":
        clicked(b7)
        positions.remove(b7)
                   
    elif b3["text"] == b7["text"] and b5["text"] == " "and b3["text"] == "O":
        clicked(b5)
        positions.remove(b5)
                   
    elif b5["text"] == b7["text"] and b3["text"] == " "and b5["text"] == "O":
        clicked(b3)
        positions.remove(b3)
        
    elif b8["text"] == b9["text"] and b7["text"] == " " and b8["text"] == "O":
        clicked(b7)
        positions.remove(b7)
    
    win1()


b1 = Button(root,text=" ", font = ("Helvetica","16"), command = lambda:clicked(b1), width = 12, height = 6, bg="black")
b2 = Button(root,text=" ", font = ("Helvetica","16"), command = lambda:clicked(b2), width = 12, height = 6, bg= 'black',)
b3 = Button(root,text=" ", font = ("Helvetica","16"), command = lambda:clicked(b3), width = 12, height = 6, bg="black",)

b4 = Button(root,text=" ", font = ("Helvetica","16"), command = lambda:clicked(b4), width = 12, height = 6, bg= 'black')
b5 = Button(root,text=" ", font = ("Helvetica","16"), command = lambda:clicked(b5), width = 12, height = 6, bg="black")
b6 = Button(root,text=" ", font = ("Helvetica","16"), command = lambda:clicked(b6), width = 12, height = 6, bg= 'black')

b7 = Button(root,text=" ", font = ("Helvetica","16"), command = lambda:clicked(b7), width = 12, height = 6, bg="black")
b8 = Button(root,text=" ", font = ("Helvetica","16"), command = lambda:clicked(b8), width = 12, height = 6, bg= 'black')
b9 = Button(root,text=" ", font = ("Helvetica","16"), command = lambda:clicked(b9), width = 12, height = 6, bg="black",)

b10 = Button(root, text= "volgende", font = ("Helvetica", '11'), command = volgende, width = 8, height = 2)

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)

b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)

b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)

b10.grid(row = 3, column = 1)


positions= [b1,b2,b3,b4,b5,b6,b7,b8,b9]

root.mainloop()
