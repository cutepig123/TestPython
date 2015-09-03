import pywinauto,os,time
import pywinauto.application

def after_right_click():
	pwa_app = pywinauto.application.Application()

	#welcome
	w_handle = pywinauto.findwindows.find_windows(title=u'Hardware Update Wizard', class_name='#32770')[0]
	window = pwa_app.window_(handle=w_handle)
	window.SetFocus()
	ctrl = window['RadioButton3']	#No not this time
	ctrl.Click()
	ctrl = window['&Next >']
	ctrl.Click()

	time.sleep(0.3)
	ctrl = window['RadioButton2']	#install fron spec loca
	ctrl.Click()
	ctrl = window['&Next >']
	ctrl.Click()

	time.sleep(1)
	ctrl = window['RadioButton2']	#donot srch
	ctrl.Click()
	ctrl = window['&Next >']
	ctrl.Click()

	time.sleep(1)
	ctrl = window['Button']	#have disk
	ctrl.Click()

	time.sleep(0.3)
	w_handle = pywinauto.findwindows.find_windows(title=u'Install From Disk', class_name='#32770')[0]
	window = pwa_app.window_(handle=w_handle)
	window.SetFocus()

	time.sleep(0.3)
	ctrl = window['ComboBox']	#copy files from
	ctrl.Click()
	#print dir(ctrl)
	#ctrl.Select(r'\\vis_i7_test\Latest_Kernal_Otf\Cam and card\check\03112013(2)\drv')
	ctrl.Select(r'\\vis_i7_test\Latest_Kernal_Otf\Cam and card\check\2013.03.13_crash_whenresetdev\drv'.upper())
	time.sleep(1)
	ctrl = window['OK']		#OK
	ctrl.Click()

	time.sleep(0.3)
	w_handle = pywinauto.findwindows.find_windows(title=u'Hardware Update Wizard', class_name='#32770')[0]
	window = pwa_app.window_(handle=w_handle)
	window.SetFocus()
	ctrl = window['Button3']	#Next
	ctrl.Click()

	time.sleep(0.3)
	ctrl = window['Finish']
	ctrl.Click()

after_right_click()
