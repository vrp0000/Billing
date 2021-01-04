import tkinter as tk
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