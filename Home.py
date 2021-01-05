from tkinter import *
run = Tk()
run.geometry("500x500")
run.title("Test Title")
heading = Label(run, text="abcd", relief=FLAT).pack()
heading = Label(run, text="efgh", relief=FLAT).pack()
#heading.pack()
run.mainloop()
