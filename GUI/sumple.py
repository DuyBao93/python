from tkinter import *

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        # self.parent.title("Simple")
        # self.pack(fill=BOTH, expand=1)
        name_label = Label(self.parent, text="Name")
        name_label.grid(row=0, column=0)
        e1 = Entry(self.parent)
        e1.grid(row=0, column=1)
        name_label_2 = Label(self.parent, text="Text")
        name_label_2.grid(row=0, column=3)

        password_label = Label(self.parent, text="Password")
        password_label.grid(row=1, column=0)
        # Tạo một ô nhập liệu và đặt nó tại hàng 1, cột 1
        e2 = Entry(self.parent)
        e2.grid(row=1, column=1)
        # Tạo nút với văn bản "Submit" và đặt nó tại hàng 4, cột 0
        submit_button = Button(self.parent, text="Submit")
        submit_button.grid(row=4, column=0)

root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()