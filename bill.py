from tkinter import*
class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("700x700")
        self.root.title("Billing Software")
        bg_color="#074363"
        title = Label(self.root,bd = 12, relief=GROOVE,bg=bg_color,fg="white" ,font = ("times new roman",30,"bold"))
        title.pack(fill=BOTH)
        title2 = Label(self.root,text="Billing Software",bd = 12, relief=GROOVE,bg=bg_color,fg="white" ,font = ("times new roman",30,"bold"))
        title2.pack(fill=BOTH)
root=Tk()

obj = Bill_App(root)

root.mainloop()