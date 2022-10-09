from tkinter import *
import os
from PIL import Image, ImageTk

#--INITIALIZE--
dir = os.path.dirname(__file__)
win = Tk()

#-----------------GLOBALVAR
playerOneName = ''
playerTwoName = ''
#-----------------GLOBALVAR

#-----------------MENU
def menu(e):
    # canvas reset
    for i in win.winfo_children():
        i.destroy()

    #-----------------FUNCTIONS
    def togglePlay(e):
        if((str)(e)[1:6] == 'Enter'):
            canvas.itemconfig(play, image=playHoverImage)
            canvas.config(cursor='hand2')
        else:
            canvas.itemconfig(play, image=playImage)
            canvas.config(cursor='')
    #-----------------FUNCTIONS

    #-----------------CANVAS OBJECT
    canvas = Canvas(
        master=win,
        bg='black',
        borderwidth=0,
        highlightthickness=0
    )
    canvas.pack(fill='both', expand=True)
    canvas.create_image(
        0, 0,
        image=bgImage,
        anchor='nw'
    )

    play = canvas.create_image(
        (int)((screenWidth/2)-(screenWidth*0.279/2)), (int)(screenHeight*0.6),
        image=playImage,
        anchor='nw'
    )
    #-----------------CANVAS OBJECT

    # binding
    canvas.tag_bind(play, '<Enter>', togglePlay)
    canvas.tag_bind(play, '<Leave>', togglePlay)
    canvas.tag_bind(play, '<Button>', playerOne)
#-----------------MENU

#-----------------PLAYER ONE
def playerOne(e):
    # canvas reset
    for i in win.winfo_children():
        i.destroy()

    #-----------------FUNCTIONS
    def togglePlay(e):
        if((str)(e)[1:6] == 'Enter'):
            canvas.itemconfig(play, image=enterHoverImage)
            canvas.config(cursor='hand2')
        else:
            canvas.itemconfig(play, image=enterImage)
            canvas.config(cursor='')

    def getName(e):
        if(entry.get() == ''):
            return
        global playerOneName
        playerOneName = entry.get()
        print(playerOneName)
        playerTwo('')
    #-----------------FUNCTIONS
    
    #-----------------CANVAS OBJECT
    canvas = Canvas(
        master=win,
        bg='black',
        borderwidth=0,
        highlightthickness=0
    )
    canvas.pack(fill='both', expand=True)
    canvas.create_image(
        0, 0,
        image=playeroneImage,
        anchor='nw'
    )

    entry = Entry(
        master=canvas, 
        background='black', fg='white', selectbackground='white', selectforeground='black', 
        borderwidth=0, highlightthickness=0, 
        font='SegoeUIBlack ' + (str)((int)(screenHeight*0.05)) + ' bold',
        justify=CENTER
    )
    entryBox = canvas.create_window(
        (int)((screenWidth/2)-(screenWidth*0.303/2)), (int)(screenHeight*0.503),
        anchor='nw',
        window=entry,
        width=(int)(screenWidth*0.303),
        height=(int)(screenHeight*0.09),
    )

    play = canvas.create_image(
        (int)((screenWidth/2)-(screenWidth*0.279/2)), (int)(screenHeight*0.7),
        image=enterImage,
        anchor='nw'
    )
    #-----------------CANVAS OBJECT

    # binding
    canvas.tag_bind(play, '<Enter>', togglePlay)
    canvas.tag_bind(play, '<Leave>', togglePlay)
    canvas.tag_bind(play, '<Button>', getName)
#-----------------PLAYER ONE

#-----------------PLAYER TWO
def playerTwo(e):
    # canvas reset
    for i in win.winfo_children():
        i.destroy()

    #-----------------FUNCTIONS
    def togglePlay(e):
        if((str)(e)[1:6] == 'Enter'):
            canvas.itemconfig(play, image=enterHoverImage)
            canvas.config(cursor='hand2')
        else:
            canvas.itemconfig(play, image=enterImage)
            canvas.config(cursor='')

    def getName(e):
        if(entry.get() == ''):
            return
        global playerTwoName
        playerTwoName = entry.get()
        print(playerTwoName)
    #-----------------FUNCTIONS
    
    #-----------------CANVAS OBJECT
    canvas = Canvas(
        master=win,
        bg='black',
        borderwidth=0,
        highlightthickness=0
    )
    canvas.pack(fill='both', expand=True)
    canvas.create_image(
        0, 0,
        image=playertwoImage,
        anchor='nw'
    )

    entry = Entry(
        master=canvas, 
        background='black', fg='white', selectbackground='white', selectforeground='black', 
        borderwidth=0, highlightthickness=0, 
        font='SegoeUIBlack ' + (str)((int)(screenHeight*0.05)) + ' bold',
        justify=CENTER
    )
    entryBox = canvas.create_window(
        (int)((screenWidth/2)-(screenWidth*0.303/2)), (int)(screenHeight*0.503),
        anchor='nw',
        window=entry,
        width=(int)(screenWidth*0.303),
        height=(int)(screenHeight*0.09),
    )

    play = canvas.create_image(
        (int)((screenWidth/2)-(screenWidth*0.279/2)), (int)(screenHeight*0.7),
        image=enterImage,
        anchor='nw'
    )
    #-----------------CANVAS OBJECT

    # binding
    canvas.tag_bind(play, '<Enter>', togglePlay)
    canvas.tag_bind(play, '<Leave>', togglePlay)
    canvas.tag_bind(play, '<Button>', getName)
#-----------------PLAYER TWO

#-----------------WINDOW
screenWidth = (int)(win.winfo_screenwidth()/2.2)
screenHeight = (int)(screenWidth*0.71)

win.geometry((str)(screenWidth) + 'x' + (str)(screenHeight))
win.resizable(False,False)
win.title('Smacked!')
#-----------------WINDOW

#-----------------RESOURCES
#--MENU RESOURCES--
bgImage = ImageTk.PhotoImage(Image.open(os.path.join(dir, 'Resources/bg.png')).resize((screenWidth, screenHeight)))
playImage = ImageTk.PhotoImage(Image.open(os.path.join(dir, 'Resources/play.png')).resize(((int)(screenWidth*0.279), (int)(screenHeight*0.109))))
playHoverImage = ImageTk.PhotoImage(Image.open(os.path.join(dir, 'Resources/playHover.png')).resize(((int)(screenWidth*0.279), (int)(screenHeight*0.109))))

#--PLAYER RESOURCES--
playeroneImage = ImageTk.PhotoImage(Image.open(os.path.join(dir, 'Resources/playerone.png')).resize((screenWidth, screenHeight)))
playertwoImage = ImageTk.PhotoImage(Image.open(os.path.join(dir, 'Resources/playertwo.png')).resize((screenWidth, screenHeight)))
enterImage = ImageTk.PhotoImage(Image.open(os.path.join(dir, 'Resources/enter.png')).resize(((int)(screenWidth*0.279), (int)(screenHeight*0.109))))
enterHoverImage = ImageTk.PhotoImage(Image.open(os.path.join(dir, 'Resources/enterHover.png')).resize(((int)(screenWidth*0.279), (int)(screenHeight*0.109))))
#-----------------RESOURCES

# start
menu('')

win.mainloop()