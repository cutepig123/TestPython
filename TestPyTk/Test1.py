#http://stackoverflow.com/questions/18729147/python-2-7-no-module-named-tkinter
# keywords
# tkMessageBox, Button, callback of button

import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
