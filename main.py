from pl.form import SearchWord
from tkinter import *
from be.db import dbContext


if __name__=="__main__":
    db=dbContext()
    screen=Tk()
    screen.geometry("%dx%d+%d+%d" % (600, 400, 520, 200))
    screen.title("واژه یاب")
    screen.iconbitmap("icon.ico")
    screen.resizable(False, False)
    PageMe=SearchWord.App(screen)
    screen.mainloop()

