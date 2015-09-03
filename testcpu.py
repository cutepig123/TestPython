import pywinauto
import pywinauto.application

pwa_app = pywinauto.application.Application()
w_handle = pywinauto.findwindows.find_windows(title=u'CPU Stress', class_name='#32770')[0]
window = pwa_app.window_(handle=w_handle)
window.SetFocus()

for i in [2,3,4]:
	ctrl = window['Active%d'%i]
	ctrl.Click()

for i in [2,4,6,8]:
	ctrl = window['ComboBox%d'%i]
	ctrl.Click()
	ctrl.Select('Maximum')
