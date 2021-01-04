import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import ttk
import time

LargeFont = ("Verdana", 12)

def options():
    print ('''\n**************************************************************
          Welcome to the GUI interface of the python program
**************************************************************''')

class PageContainer(tk.Tk):  

    def __init__(self, *args, **kwargs):  
        options()
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self,default="ico_image.ico")  

        container = tk.Frame(self) 
        print ("Setting frams") 
        tk.Tk.geometry(self,'250x250')  
        container.pack(side='top', fill='both', expand = True )     
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frame = {}

        for F in (StartPage, Project_1,Project_2,Project_3,Project_4, Project_5,Project_6,Project_7):

            frame = F(container, self)

            self.frame[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew") 

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frame[cont]    
        frame.tkraise()    



class StartPage(tk.Frame):    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)   
        label = tk.Label(self, text="MAIN MENU FOR PROJECTS", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Project1",
            command = lambda: controller.show_frame(Project_1), width = 20, height = 1)     
        button2 = tk.Button(self, text = " Project2 ",
            command = lambda: controller.show_frame(Project_2), width = 20, height = 1)
        button3 = tk.Button(self, text = "   Project3   ",
            command = lambda: controller.show_frame(Project_3), width = 20, height = 1)
        button4 = tk.Button(self, text = "Project4",
            command = lambda: controller.show_frame(Project_4), width = 20, height = 1)
        button5 = tk.Button(self, text = "    Project5    ",
            command = lambda: controller.show_frame(Project_5), width = 20, height = 1)
        button6 = tk.Button(self, text = "Projec6    ",
            command = lambda: controller.show_frame(Project_6), width = 20, height = 1)
        button7 = tk.Button(self, text = "Projec7",
            command = lambda: controller.show_frame(Project_7), width = 20, height = 1)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()


class Project_1(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Project 1", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Data Load",
            command = data_load_all_proj, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Create QR Image",
            command = generate_qr_code, width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Generate Report",
            command = generate_report, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Freeze Data",
            command = freeze_data, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Delete Data",
            command = delete_data, width = 25, height = 1)
        button5.pack()
        button6 = tk.Button(self, text = "Generate Revenue Report",
            command = generate_revenue_report, width = 25, height = 1)
        button6.pack()
        button7 = tk.Button(self, text = "Back to Main Menu",
            command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
        button7.pack()

class Project_2(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Project 2", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Data Load",
            command = data_load_all_proj, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Create QR Image",
            command = generate_qr_code, width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Generate Report",
            command = generate_report, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Freeze Data",
            command = freeze_data, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Delete Data",
            command = delete_data, width = 25, height = 1)
        button5.pack()
        button6 = tk.Button(self, text = "Generate Revenue Report",
            command = generate_revenue_report, width = 25, height = 1)
        button6.pack()
        button7 = tk.Button(self, text = "Back to Main Menu",
            command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
        button7.pack()

class Project_3(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Project 3", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Data Load",
            command = data_load_all_proj, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Create QR Image",
            command = generate_qr_code, width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Generate Report",
            command = generate_report, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Freeze Data",
            command = freeze_data, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Delete Data",
            command = delete_data, width = 25, height = 1)
        button5.pack()
        button6 = tk.Button(self, text = "Generate Revenue Report",
            command = generate_revenue_report, width = 25, height = 1)
        button6.pack()
        button7 = tk.Button(self, text = "Back to Main Menu",
            command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
        button7.pack()

class Project_4(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Project 4", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Data Load",
            command = data_load_all_proj, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Create QR Image",
            command = generate_qr_code, width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Generate Report",
            command = generate_report, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Freeze Data",
            command = freeze_data, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Delete Data",
            command = delete_data, width = 25, height = 1)
        button5.pack()
        button6 = tk.Button(self, text = "Generate Revenue Report",
            command = generate_revenue_report, width = 25, height = 1)
        button6.pack()
        button7 = tk.Button(self, text = "Back to Main Menu",
            command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
        button7.pack()


class Project_5(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Project 5", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Data Load",
            command = data_load_all_proj, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Create QR Image",
            command = generate_qr_code, width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Generate Report",
            command = generate_report, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Freeze Data",
            command = freeze_data, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Delete Data",
            command = delete_data, width = 25, height = 1)
        button5.pack()
        button6 = tk.Button(self, text = "Generate Revenue Report",
            command = generate_revenue_report, width = 25, height = 1)
        button6.pack()
        button7 = tk.Button(self, text = "Back to Main Menu",
            command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
        button7.pack()

class Project_6(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Project 6", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Data Load",
            command = data_load_all_proj, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Create QR Image",
            command = generate_qr_code, width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Generate Report",
            command = generate_report, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Freeze Data",
            command = freeze_data, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Delete Data",
            command = delete_data, width = 25, height = 1)
        button5.pack()
        button6 = tk.Button(self, text = "Generate Revenue Report",
            command = generate_revenue_report, width = 25, height = 1)
        button6.pack()
        button7 = tk.Button(self, text = "Back to Main Menu",
            command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
        button7.pack()

class Project_7(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Project 7", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Data Load",
            command = data_load_all_proj, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Create QR Image",
            command = generate_qr_code, width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Generate Report",
            command = generate_report, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Freeze Data",
            command = freeze_data, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Delete Data",
            command = delete_data, width = 25, height = 1)
        button5.pack()
        button6 = tk.Button(self, text = "Generate Revenue Report",
            command = generate_revenue_report, width = 25, height = 1)
        button6.pack()
        button7 = tk.Button(self, text = "Back to Main Menu",
            command = lambda: controller.show_frame(StartPage), width = 25, height = 1)
        button7.pack()

def data_load_all_proj():
    var0 = tkSimpleDialog.askstring("Data Load","Please enter the month and year(mm-yyyy): ")
    tkMessageBox.showinfo("Message", "Please place the master file in specific folder")
    var1 = tkSimpleDialog.askstring("Data Load","Do you want to start loading master data? ")
    tkMessageBox.showinfo("Message", "Please place the files in specific folder")
    var2 = tkSimpleDialog.askstring("Data Load","Do you want to start loading data? (Y/N): ")
    tkMessageBox.showinfo("Message", "Please wait while the data is loading")
    master_data(var0,var1,var2)

def master_data(var0,var1,var2):
    print(var0, var1, var2)

def generate_qr_code():
    var0 = tkSimpleDialog.askstring("QR IRN Generate","Please enter the Invoice month and year(mm-yyyy): ")
    tkMessageBox.showinfo("Message", "Please wait while the QR IRN is generating")
    create_qr_image(var0)

def create_qr_image(var0):
    print(var0)

def generate_report():
    var0 = tkSimpleDialog.askstring("Generate Invoice","Please enter the Invoice month and year(mm-yyyy): ")
    tkMessageBox.showinfo("Message", "Please wait while the Invoice is gettting generated")
    generate_invoice(var0)

def generate_invoice(var0):
    print(var0)

def freeze_data():
    var0 = tkSimpleDialog.askstring("Freeze data","Please enter the Invoice month and year(mm-yyyy): ")
    tkMessageBox.showinfo("Message", "Please wait while the data is being freezed")
    freeze_data_function_call(var0)

def freeze_data_function_call(var0):
    print(var0)

def delete_data():
    var0 = tkSimpleDialog.askstring("Delete data","Please enter the Invoice month and year(mm-yyyy): ")
    tkMessageBox.showinfo("Message", "Please wait while the data is being deleted")
    delete_data_function_call(var0)

def delete_data_function_call(var0):
    print(var0)

def generate_revenue_report():
    var0 = tkSimpleDialog.askstring("Delete data","Please enter the Invoice month and year(mm-yyyy): ")
    tkMessageBox.showinfo("Message", "Please wait while the MIS Revenue Report is being generated")
    generate_revenue_report_function_call(var0)

def generate_revenue_report_function_call(var0):
    print(var0)



app = PageContainer()
app.mainloop()   