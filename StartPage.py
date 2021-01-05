import tkinter as tk
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
