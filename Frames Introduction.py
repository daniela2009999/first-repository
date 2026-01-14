import tkinter as tk

root = tk.Tk()

root.geometry("400x400")
root.title("Frames Intro")

# configuration of rows and columns

root.rowconfigure(0, weight = 2)
root.rowconfigure(1, weight = 4)

root.columnconfigure(0, weight= 4)
root.columnconfigure(1, weight= 4)

#label

label = tk.Label(text = 'title')
label.grid(row = 0, column = 0, columnspan = 2)

#Frames initializaion

leftFrame = tk.Frame(root)
rightFrame = tk.Frame(root)
# Left frame configuration

leftFrame.rowconfigure(0, weight = 1)
leftFrame.rowconfigure(1, weight= 1)
leftFrame.rowconfigure(2, weight = 1)

leftFrame.columnconfigure(0 , weight = 1)
leftFrame.columnconfigure(1, weight= 1)
leftFrame.columnconfigure(2, weight= 1)

leftFrame.grid(row = 1, column =0)

# Right frame configuration

rightFrame.rowconfigure(0, weight = )

rightFrame.rowconfigure(0, weight = 1)
rightFrame.rowconfigure(1, weight= 1)
rightFrame.rowconfigure(2, weight = 1)

rightFrame.columnconfigure(0 , weight = 1)
rightFrame.columnconfigure(1, weight= 1)
rightFrame.columnconfigure(2, weight= 1)

rightFrame.grid(row = 1, column =0)


root.mainloop()