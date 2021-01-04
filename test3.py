from tkinter import *

class abc (Tk):
    def __init__(self):#,objtk):
        self = Tk()
        self.geometry("1350x700+0+0")
#        Tk.__init__(self)
        frame1_background = "#31C2CE"
        Heading_frame = Frame(self,bg = frame1_background, borderwidth=6, relief = GROOVE)
        Heading_frame.pack(padx = 10, fill = X)
        Heading_frame_label = Label(Heading_frame, text = "Patient Detail ",bg = frame1_background,fg="red", font = ("times new roman",20,"bold"))
        Heading_frame_label.pack(padx=14)
        #==========patient Detail Entry Frame==============
        p_detail_frame =  LabelFrame(self,text = "Mandatory Details" , font = ("times new roman",20,"bold"), bg = frame1_background, borderwidth=10)
        p_detail_frame.pack(fill=X,padx = 10, pady= 20)#lace(x=0, y=0, relwidth=1)

        p_name_label = Label(p_detail_frame, text = "Name", font = ("times new roman",15)).grid(row=0,column=0)


        #f2 = Frame(self, bg = "grey", borderwidth = 60,relief= SUNKEN).pack(fill = Y)
        #Label(f2, text = "Frame 2 ").pack(fill= BOTH,pady = 142)
        self.mainloop()

#obj = Tk()

#abc(obj)
abc()
#obj.mainloop()