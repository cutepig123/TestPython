import pywinauto
import pywinauto.application

pwa_app = pywinauto.application.Application()
pwa_app.start_ex('calc.exe','')
w_handle = pywinauto.findwindows.find_windows(title=u'Calculator', class_name='SciCalc')[0]
window = pwa_app.window_(handle=w_handle)
window.SetFocus()
ctrl = window['1']
ctrl.Click()
ctrl = window['+']
ctrl.Click()
ctrl = window['2']
ctrl.Click()
ctrl = window['=']
ctrl.Click()
ctrl = window['Edit']
ctrl.SetFocus()
print ctrl.Texts()
assert(ctrl.Texts()[0]=='3. ')
