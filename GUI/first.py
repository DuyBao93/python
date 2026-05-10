from tkinter import *

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
      
    def initUI(self):
        self.parent.title("Tăng số")

        name_label = Label(self.parent, text= "0")
        # name_label.grid(row=0, column=5)
        name_label.place(x = 150, y = 90)
        
        def clicked():
            number = int(name_label.cget("text"))
            if number == 20:
                name_label.config(text= "0")
            else:
                name_label.config(text = str(number + 1))

        increment_BT = Button(self.parent, text="Tăng", command=clicked)
        increment_BT.place(x=135, y = 180)

root = Tk()
root.geometry("300x300")
app = Example(root)
root.mainloop()