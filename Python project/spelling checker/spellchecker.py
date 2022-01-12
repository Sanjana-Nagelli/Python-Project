from tkinter import *
from textblob import TextBlob

def check_spelling():
    a=TextBlob(spell_check.get())
    spell=Label(root,text="The correct spelling is:",font=("Arial",30,"bold"),bg="gray")
    spell.pack()
    correct_text=Label(root,text=str(a.correct()),font=("Arial",45,"bold"),bg="light pink")
    correct_text.pack()

root=Tk()
root.title("My Spelling Checker")
root.geometry("800x600")
root.config(background="light green")

text_heading=Label(root,text="Spelling Checker",
        font=("Arial",50,"bold"),bg="black",fg="light pink" )
text_heading.pack()
text_check=Label(root,text="Enter the spelling",
                 font=("Arial",35,"bold"),bg="yellow",fg="red")
text_check.pack()

spell_check=Entry(root,font=("Arial",45,"bold"),width=500,bg="light blue")
spell_check.pack()

Check_button=Button(root,text="Check!",font=("Arial",30,"bold"),fg="white",bg="red",command=check_spelling)
Check_button.pack()

root.mainloop()
