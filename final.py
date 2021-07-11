from tkinter import Tk,ttk,Button
from tkinter import messagebox

ActivePlayer = 1
newplayer = 2
count = 0
new_count = 0
prev_count = 0
undol=[]
undo_c=0
p1 = []
p2 = []
mov = 0
pp1 = 0
pp2 = 0
dr = 0
u=0
y=-1
    
def SetLayout(id,player_symbol):
    if id==1:
        b1.config(text= player_symbol)
        b1.state(['disabled'])
    elif id==2:
        b2.config(text= player_symbol)
        b2.state(['disabled'])
    elif id==3:
        b3.config(text= player_symbol)
        b3.state(['disabled'])
    elif id==4:
        b4.config(text= player_symbol)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text= player_symbol)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text= player_symbol)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text= player_symbol)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text= player_symbol)
        b8.state(['disabled'])
    elif id==9:
        b9.config(text= player_symbol)
        b9.state(['disabled'])

def CheckWinner():
    k=open("hello1.txt","a+")
    global mov
    global pp1
    global pp2
    global dr
    winner = -1
    if(1 in p1) and (2 in p1) and (3 in p1):
        winner = 1
    if(1 in p2) and (2 in p2) and (3 in p2):
        winner = 2

    if(4 in p1) and (5 in p1) and (6 in p1):
        winner = 1
    if(4 in p2) and (5 in p2) and (6 in p2):
        winner = 2

    if(7 in p1) and (8 in p1) and (9 in p1):
        winner = 1
    if(7 in p2) and (8 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (4 in p1) and (7 in p1):
        winner = 1
    if(1 in p2) and (4 in p2) and (7 in p2):
        winner = 2

    if(2 in p1) and (5 in p1) and (8 in p1):
        winner = 1
    if(2 in p2) and (5 in p2) and (8 in p2):
        winner = 2

    if(3 in p1) and (6 in p1) and ( 9 in p1):
        winner = 1
    if(3 in p2) and (6 in p2) and (9 in p2):
        winner = 2

    if(1 in p1) and (5 in p1) and ( 9 in p1):
        winner = 1
    if(1 in p2) and (5 in p2) and (9 in p2):
        winner = 2

    if(3 in p1) and (5 in p1) and ( 7 in p1):
        winner = 1
    if(3 in p2) and (5 in p2) and (7 in p2):
        winner = 2

    if winner ==1:
        messagebox.showinfo(title="Congratulations.", 
            message="Player 1 is the winner")
        pp1 += 1        
    elif winner ==2:
        messagebox.showinfo(title="Congratulations.", 
            message="Player 2 is the winner")
        pp2 += 1
    elif mov ==9:
        messagebox.showinfo(title="Draw", 
            message="It's a Draw!!")
        dr += 1

def Exit():
    global pp1,pp2,dr
    k = open("hello1.txt","a+")
    spp1=str(pp1)
    spp2=str(pp2)
    sdr=str(dr)
    k.writelines("player one has won ")
    k.writelines(spp1)
    k.writelines(" times\n")
    k.writelines("player two has won ")
    k.writelines(spp2)
    k.writelines(" times\n")
    k.writelines("number of draw matches= ")
    k.writelines(sdr)
    k.writelines("\n")
    k = open("hello1.txt","r")
    data=k.read()    
    messagebox.showinfo(title="Exit", 
            message=data)
    root.destroy()
    k.truncate(0)
    k.close()
        
def Undo(p1,p2):
    global latestmove
    global u
    global count,prev_count,new_count
    global ActivePlayer,newplayer
    global mov
    global undo_c   
    mov = mov-1
    prev_count +=1
    new_count = count
    count = prev_count
    Undo.has_been_called = count
    
    if u == 1:
         b1.config(text= " ")
         b1.state(['!disabled'])
    elif u == 2:
        b2.config(text= " ")
        b2.state(['!disabled'])
    elif u == 3:
        b3.config(text= " ")
        b3.state(['!disabled'])
    elif u == 4:
        b4.config(text= " ")
        b4.state(['!disabled'])
    elif u == 5:
        b5.config(text= " ")
        b5.state(['!disabled'])
    elif u == 6:
        b6.config(text= " ")
        b6.state(['!disabled'])
    elif u == 7:
        b7.config(text= " ")
        b7.state(['!disabled'])
    elif u == 8:
        b8.config(text= " ")
        b8.state(['!disabled'])
    elif u == 9:
        b9.config(text= " ")
        b9.state(['!disabled'])
    else:
        messagebox.showinfo(title="undo", 
            message="no moves made")
    
    if(ActivePlayer == 1):
        print("before pop",p2)

        a=p2.pop()
        print("after pop",p2)

        newplayer = 2
    elif ActivePlayer == 2:
        print("before pop",p1)
        a=p1.pop()
        print("after pop",p1)

        newplayer = 1
    hv=hash(u)
    undol.append(hv)
    undo_c += 1
    if undo_c >1:
        messagebox.showinfo(title="undo", 
            message="no more undo moves")
        undo_c = 0
    print("hash is=",undol)
    Undo.has_been_called = False   

def ButtonClick(id):
    global ActivePlayer
    global p1,p2
    global mov
    global latestmove
    global u
    global count, prev_count,new_count
    u = id
    if prev_count == count and count>0:
        print("undo called")
        ActivePlayer = newplayer
        count = new_count
        print("player number:",ActivePlayer)
    elif count == new_count:
        print("normal button click")
        print("player number:",ActivePlayer)
    if(ActivePlayer ==1):
        SetLayout(id,"X")
        p1.append(id)
        mov +=1
        root.title("Tic Tac Toe : Player 2")
        ActivePlayer =2
    elif(ActivePlayer==2):
        SetLayout(id,"O")
        p2.append(id)
        mov +=1
        root.title("Tic Tac Toe : Player 1")
        ActivePlayer =1
    count+=1
    new_count = count
    CheckWinner()

def EnableAll():
    b1.config(text= " ")
    b1.state(['!disabled'])
    b2.config(text= " ")
    b2.state(['!disabled'])
    b3.config(text= " ")
    b3.state(['!disabled'])
    b4.config(text= " ")
    b4.state(['!disabled'])
    b5.config(text= " ")
    b5.state(['!disabled'])
    b6.config(text= " ")
    b6.state(['!disabled'])
    b7.config(text= " ")
    b7.state(['!disabled'])
    b8.config(text= " ")
    b8.state(['!disabled'])
    b9.config(text= " ")
    b9.state(['!disabled'])

def Restart():
    global p1,p2,mov,ActivePlayer
    p1.clear(); p2.clear()
    mov,ActivePlayer = 0,1
    root.title("Tic Tac Toe : Player 1")
    EnableAll()

root = Tk()
root.title("Tic Tac toe : Player 1")
st = ttk.Style()
st.configure("my.TButton", font=('Chiller',24,'bold'))

b1 = ttk.Button(root, text=" ", style="my.TButton")
b1.grid(row=1, column=0, sticky="nwse", ipadx=50,ipady=50)
b1.config(command = lambda : ButtonClick(1))


b2 = ttk.Button(root, text=" ",style ="my.TButton")
b2.grid(row=1, column=1, sticky="snew", ipadx=50, ipady=50)
b2.config(command = lambda : ButtonClick(2))

b3= ttk.Button(root, text=" ",style="my.TButton")
b3.grid(row=1, column=2, sticky="snew", ipadx=50,
        ipady=50)
b3.config(command = lambda : ButtonClick(3))

b4 = ttk.Button(root, text=" ",style="my.TButton")
b4.grid(row=2, column=0, sticky="snew", ipadx=50,
        ipady=50)
b4.config(command = lambda : ButtonClick(4))

b5 = ttk.Button(root, text=" ",style="my.TButton")
b5.grid(row=2, column=1, sticky="snew", ipadx=50,
        ipady=50)
b5.config(command = lambda : ButtonClick(5))

b6 = ttk.Button(root, text=" ",style="my.TButton")
b6.grid(row=2, column=2, sticky="snew", ipadx=50,
        ipady=50)
b6.config(command = lambda : ButtonClick(6))

b7 = ttk.Button(root, text=" ",style="my.TButton")
b7.grid(row=3, column=0, sticky="snew", ipadx=50,
        ipady=50)
b7.config(command = lambda : ButtonClick(7))

b8 = ttk.Button(root, text=" ",style="my.TButton")
b8.grid(row=3, column=1, sticky="snew", ipadx=50,
        ipady=50)
b8.config(command = lambda : ButtonClick(8))

b9 = ttk.Button(root, text=" ",style="my.TButton")
b9.grid(row=3, column=2, sticky="snew", ipadx=50,
        ipady=50)
b9.config(command = lambda : ButtonClick(9))

Button(text="New Game", font=('Papyrus', 22, 'bold'), bg='Purple', fg='white',
            border=5, width=4,command = lambda :Restart()).grid(row=0, column=0, sticky="we")
Button(text="Exit", font=('Papyrus', 22, 'bold'), bg='Purple', fg='white',
            border=5, width=4,command = lambda :Exit()).grid(row=0, column=1, sticky="we")
Button(text="Undo", font=('Papyrus', 22, 'bold'), bg='Purple', fg='white',
            border=5, width=4,command = lambda :Undo(p1,p2)).grid(row=0, column=2, sticky="we")
root.resizable(100,100)
root.mainloop()