import pywinauto,os,time
import pywinauto.application

app = pywinauto.application.Application()
win =app['Computer Management']
#win.TreeView1.Select('Computer')
#win.print_control_identifiers()
win.TreeView2.print_control_identifiers()
def TestNotepad():
	win =app.Notepad
	win.MenuSelect("Format->Font")
	app.Font['Font:ComboBox'].Select('Mangal')
	#app.Font.OK.Click()
	#win.TypeKeys("%FX")
	#win.TypeKeys("Helo")
