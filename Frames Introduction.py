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

label = tk.Label(text = 'Main Frame', relief = "solid")
label.grid(row = 0, column = 0, columnspan = 2)

#Frames initializaion

leftFrame = tk.Frame(root, bg = 'blue')
rightFrame = tk.Frame(root)
# Left frame configuration

leftFrame.rowconfigure(0, weight = 1)
leftFrame.rowconfigure(1, weight= 1)
leftFrame.rowconfigure(2, weight = 1)

leftFrame.columnconfigure(0 , weight = 1)

leftFrame.grid_propagate(False)

leftFrame.grid(row = 1, column =0, sticky= 'nsew')

# Right frame configuration

rightFrame.rowconfigure(0, weight = 1 )

rightFrame.rowconfigure(0, weight = 1)
rightFrame.rowconfigure(1, weight= 1)
rightFrame.rowconfigure(2, weight = 1)

rightFrame.columnconfigure(0 , weight = 1)
rightFrame.columnconfigure(1, weight= 1)
rightFrame.columnconfigure(2, weight= 1)
rightFrame.grid_propagate(False)

rightFrame.grid(row = 1, column =0)


# 3 entries in the left row 2-3
entry1 = tk.Entry(leftFrame)
entry1.grid(row = 0, column = 0)

entry2 = tk.Entry(leftFrame)
entry2.grid(row = 1, column = 0)

root.mainloop()