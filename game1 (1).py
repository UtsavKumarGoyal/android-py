from random import randint
from tkinter import *
from PIL import Image,ImageTk

# main windo 

root=Tk()
root.title("Rock Scissor Paper")
root.configure(background="purple")

#picture
rock_img=ImageTk.PhotoImage(Image.open("rock-user.png"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor-user.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper-user.png"))
rock_img_comp=ImageTk.PhotoImage(Image.open("rock.png"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("scissor.png"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper.png"))

#Insert picture
user_label=Label(root,image=paper_img,bg="purple")
comp_label=Label(root,image=paper_img_comp,bg="purple")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerscore=Label(root,text=0,font=100,bg="purple",fg="white")
computerscore=Label(root,text=0,font=100,bg="purple",fg="white")
playerscore.grid(row=1,column=1)
computerscore.grid(row=1,column=3)

#indicators
user_indicator=Label(root,font=50,text="USER",bg="purple",fg="white").grid(row=0,column=3)
comp_indicator=Label(root,font=50,text="COMPUTER",bg="purple",fg="white").grid(row=0,column=1)

#messages
msg=Label(root,font=50,bg="purple",fg="white").grid(row=3,column=2)

#update message
def updatemessage(x):
    msg ['text'] = x 

#update user score
def updateUserscore ():
    score=int (playerscore["text"])
    score += 1
    playerscore ["text"]=str(score)

#update computer score

def updateCompscore():
    score=int (computerscore["text"])
    score += 1
    computerscore ["text"]=str(score)

# check win

def checkwin(Player,Computer):
    if Player== Computer:
        updatemessage("its tie!!")
    elif Player == "rock":
        if Computer == "paper":
            updatemessage("You loose")
            updateCompscore()
        else:
            updatemessage("You Win")
            updateUserscore()
    elif Player=="paper":
        if Computer == "scissor":
            updatemessage("You loose")
            updateCompscore()
        else:
            updatemessage("You Win")
            updateUserscore()
    elif Player=="scissor":
        if Computer == "rock":
            updatemessage("You loose")
            updateCompscore()
        else:
            updatemessage("You Win")
            updateUserscore() 
    else:
        pass               

#update choice
choice=["rock","paper","scissor"]

def updatechoice(x):

#for computer
    comchoice=choice[randint(0,2)]
    if comchoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif comchoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

#for user
    if x=="rock":
        user_label.configure(image=rock_img)

    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkwin(x,comchoice)



#buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="pink",fg="white",command= lambda:updatechoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="yellow",fg="white",command= lambda:updatechoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSORS",bg="skyblue",fg="white",command= lambda:updatechoice("scissor")).grid(row=2,column=3)

root.mainloop()