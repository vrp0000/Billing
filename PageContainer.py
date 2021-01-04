import tkinter as tk
class PageContainer(tk.Tk):  

	def __init__(self, *args, **kwargs):  
		options()
		tk.Tk.__init__(self, *args, **kwargs)
		#tk.Tk.iconbitmap(self,default="ico_image.ico")  

		container = tk.Frame(self)  
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
app = PageContainer()
app.mainloop()   