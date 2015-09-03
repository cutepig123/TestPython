import Tkinter
#from Tkinter import *

def HowTo():
	print 'HT'
	pass

def About():
	pass
	
def help_menu():
	help_btn = Tkinter.Menubutton(menu_frame, text='Help', underline=0)
	help_btn.pack(side=Tkinter.LEFT, padx="2m")
	
	help_btn_menu = Tkinter.Menu(help_btn)
	help_btn_menu.add_command(label="How To", underline=0, command=HowTo)
	help_btn_menu.add_command(label="About", underline=0, command=About)
	help_btn['menu'] = help_btn_menu
	return help_btn
	
	
top = Tkinter.Tk()
#top.resizable(False, False)
#top.wm_maxsize(500,500)
#top.wm_minsize(100,100)
top.title('title')

menu_frame = Tkinter.Frame(top)
menu_frame.pack(fill=Tkinter.X, side=Tkinter.TOP)
menu_frame.tk_menuBar(help_menu())

label = Tkinter.Label(top, text='a Label')
label.pack()

btn = Tkinter.Button(top, text='Quit',fg="red",  command=top.quit)
btn.pack()

Tkinter.mainloop()


