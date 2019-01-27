from tkinter import *
from random import randint
import time


def clic(event):
    X=event.x
    Y=event.y
    if X<800/w and Y<400/h:
        lose=Label(main,text="C'est perdu")
        lose.pack()
        lose.configure(font=font28)
        clear()
    i=1
    while X>(i*800/w):
        i=i+1
    xa=(i-1)*800/w
    i=1
    while Y>(i*400/h):
        i=i+1
    ya=(i-1)*400/h
    canvas.create_rectangle(xa,ya,800,400,fill='black')
    #time.sleep(3)
    #hasard()

def clear():
    canvas.delete(ALL)
    lose=Label(text='')
    for i in range (1, w):
        canvas.create_rectangle(i*800/(w),0,i*800/(w),400,fill='black')
    for i in range (1,h):
        canvas.create_rectangle(0,i*400/h,800,i*400/h,fill ='black')
    canvas.create_rectangle(0,0,800/w,400/h,fill ='green')

def hasard():
    xp=randint(1,799)
    yp=randint(1,399)
    if xp<800/w and yp<400/h:
        lose=Label(main,text="Vous avez gagné!")
        lose.pack()
        clear()
    i=1
    while xp>(i*800/w):
        i=i+1
    xa=(i-1)*800/w
    i=1
    while yp>(i*400/h):
        i=i+1
    ya=(i-1)*400/h
    canvas.create_rectangle(xa,ya,800,400,fill='white')

    


d=0
while d==0:
    try:
        print ("Entrez la taille de la tablette de chocolat\n(Maximum 10 par 10)\n")
        h=int(input("Entrer la largeur : "))
        w=int(input("Entrer la longueur : "))
        if h>10 or w>10:
            print("Les dimensions sont trop grandes\n")
        else :
            d=1
    except:
        print ("Les donnees ne sont pas correctes\n")


main = Tk()
main.title ("Jeu du chocolat")
main.geometry('1000x800+25+25')
main.config(cursor='hand1')
font28="-size 28"
titre = Label (main, text="Bienvenue dans le jeu du chocolat")
titre.pack()
titre.configure(font=font28)
effacer=Button(main, text="Effacer", command=clear)
effacer.pack()


canvas = Canvas(main, width=800, height=400, background='brown')
canvas.pack(padx=10, pady=100)
for i in range (1, w):
    canvas.create_rectangle(i*800/(w),0,i*800/(w),400,fill='black')
for i in range (1,h):
    canvas.create_rectangle(0,i*400/h,800,i*400/h,fill ='black')
canvas.create_rectangle(0,0,800/w,400/h,fill ='green')


canvas.bind('<Button-1>', clic)

main.mainloop()