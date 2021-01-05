from tkinter import *
from tkinter import Entry, Frame, Label, LabelFrame, Tk, ttk

import tkinter

class abc (Tk):
    def __init__(self):#,objtk):
        self = Tk()
        self.geometry("500x350+0+0")
        self.title("Patient Info Entry")
#        Tk.__init__(self)
        frame1_background = "#31C2CE"
        Heading_frame = Frame(self,bg = frame1_background, borderwidth=6, relief = GROOVE)
        Heading_frame.pack(padx = 10, fill = X)
        Heading_frame_label = Label(Heading_frame, text = "Patient Detail ",bg = frame1_background,fg="red", font = ("times new roman",20,"bold"))
        Heading_frame_label.pack(padx=14)
        #==========patient Detail Entry Frame==============
        p_detail_frame =  LabelFrame(self,text = "Mandatory Details" , font = ("times new roman",15), bg = "grey", fg = "black" , borderwidth=2, relief = SOLID)
        p_detail_frame.pack(fill=X,padx = 10, pady= 20)#lace(x=0, y=0, relwidth=1)

        font_value= ("times new roman",12)

        #=============Input Labels==========================

        p_name_label = Label(p_detail_frame, 
                            text = "Name :",
                            font = font_value,
                            justify = CENTER,
                            bg = "grey").grid(row=0,column=0, padx = 10, pady = 5 )
        p_age_label = Label(p_detail_frame, 
                            text = "Age : ",
                            font = font_value,
                            justify = CENTER,
                            bg = "grey").grid(row=1,column=0, padx = 10, pady = 5)
        p_dob_label = Label(p_detail_frame,
                            text = "DoB : ",
                            font = font_value,
                            justify = CENTER,
                            bg = "grey").grid(row=2,column=0, padx =10, pady = 5)
        p_sex_label = Label(p_detail_frame,
                            text = "Sex : ",
                            font = font_value,
                            justify = CENTER,
                            bg= "grey").grid(row=3,column=0, padx =10, pady = 5)
        p_address_label = Label(p_detail_frame,
                            text = "Address : ",
                            font = font_value,
                            justify = CENTER,
                            bg= "grey").grid(row=4,column=0, padx =10, pady = 5)
        p_contact_label = Label(p_detail_frame,
                            text = "Contact : ",
                            font = font_value,
                            justify = CENTER,
                            bg= "grey").grid(row=5,column=0, padx =10, pady = 5)

        #=============Input Text Box===============================
        p_name_entry = Entry(p_detail_frame,
                            width = 30,
                            font = font_value,
                            ).grid(row = 0, column =1 , padx = 20, pady = 5)
        p_age_entry = Entry(p_detail_frame,
                            width = 30,
                            font = font_value,
                            ).grid(row = 1, column =1 , padx = 20, pady = 5)
        p_dob_entry = Entry(p_detail_frame,
                            width = 30,
                            font = font_value,
                            ).grid(row = 2, column =1 , padx = 20, pady = 5)
        
        sex = tkinter.StringVar()
        p_sex_entry = ttk.Combobox(p_detail_frame,
                                        width = 30,
                                        textvariable = sex)
        p_sex_entry['values']= ('MALE','FEMALE','OTHER')
        p_sex_entry.grid(row = 3, column =1 , padx = 20, pady = 5)
        '''Entry(p_detail_frame,
                            width = 30,
                            font = font_value,
                            ).grid(row = 3, column =1 , padx = 20, pady = 5)'''
        p_address_entry = Entry(p_detail_frame,
                            width = 30,
                            text = "50",
                            font = font_value,
                            ).grid(row = 4, column =1 , padx = 20, pady = 5)
        p_contact_entry = Entry(p_detail_frame,
                            width = 30,
                            font = font_value,
                            ).grid(row = 5, column =1 , padx = 20, pady = 5)



        '''n = tkinter.StringVar() 
        monthchoosen = tkinter.Combobox(p_detail_frame,
                                     width = 27, 
                                    textvariable = n) 
        monthchoosen['values'] = (' January',' February',' March',' April',' May',
                                    ' June', ' July',' August',' September',' October',' November',' December') 
'''
        self.mainloop()

#obj = Tk()

#abc(obj)
abc()
#obj.mainloop()