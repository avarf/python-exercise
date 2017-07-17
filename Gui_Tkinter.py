# import sys
import tkinter as tk

# tk._test()

LARGE_FONT = ("Verdana", 12)



class Testgui(tk.Tk):
	""""This class is a test for working with Tkinter and buid a gui in python for Tag Filemanager"""

	def __init__(self, *args, **kwargs):
		"*args are the infinite number of argumants"
		"**kwargs is for passing objects such as dictionaries"
		tk.Tk.__init__(self, *args, **kwargs)
		# tk.Tk()

		container = tk.Frame(self) # The edge of a window

		"pack is for small and simple windows"
		container.pack(side="top",fill="both",expand=True)

		container.grid_rowconfigure(0, weigh=1)
		container.grid_columnconfigure(0, weigh=1)

		"The frame that is on top is the one that we contract with"
		self.frames = {}

		for F in (StartPage, PageOne, PageTwo):
					# frame = StartPage(container, self)
					frame = F(container, self)
					self.frames[F] = frame
					"where we put our elements - which row and column"
					"sticky is for the corners like north, west, etc."
					frame.grid(row=0, column=0, sticky="nsew")

		"Which frame we want to show"
		"We used StartPage because we want to initialize"
		self.show_frame(StartPage)

	def show_frame(self, cont):
		"cont is the key"
		frame = self.frames[cont]
		frame.tkraise()



def test_command(string_to_print = "Without reciveing from frame"):
	# print("You did it")
	print(string_to_print)

class StartPage(tk.Frame):
	"""creating a StartPage"""
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Start Page", font = LARGE_FONT)
		"If we just have 1-3 items it is better to just use pack instead of grid"
		label.pack(pady = 10, padx=10)

		# button1 = tk.Button(self, text="Visit Page 1", command = test_command)
		"When we want to send parameters to the command we should use lambda as below"
		button1 = tk.Button(self, text="Visit Page 1", command = lambda: test_command("Hello from frame"))
		button1.pack()

		button2 = tk.Button(self, text="Go ot Page One", command = lambda:controller.show_frame(PageOne))
		button2.pack()


		button3 = tk.Button(self, text="Go ot Page Two", command = lambda:controller.show_frame(PageTwo))
		button3.pack()


class PageOne(tk.Frame):
	"""docstring for PageOne"""
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One", font = LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text="Back to Home", command = lambda:controller.show_frame(StartPage))
		button1.pack()

		button2 = tk.Button(self, text="Go ot Page Two", command = lambda:controller.show_frame(PageTwo))
		button2.pack()


class PageTwo(tk.Frame):
	"""docstring for PageOne"""
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Two !!!", font = LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text="Go to Page One", command = lambda:controller.show_frame(PageOne))
		button1.pack()

		button2 = tk.Button(self, text="Back to Home", command = lambda:controller.show_frame(StartPage))
		button2.pack()

app = Testgui()
app.mainloop()