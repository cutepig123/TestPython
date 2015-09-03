# -*- coding: utf-8 -*-

import pywinauto,os,time
import pywinauto.application

def FindTreeElem(ctrl, text):
	C=[]
	CC=ctrl.Children()
	
	for c in CC:
		
		if len(text)==0 or c.Text()==text:
			C.append(c)
		
	if( 1 ):
		print '-->cannot find<', text, '>in:'
		for x in CC:
			print x.Text()
	return C
	
def FindTreeElemsID(ctrl, text):
	C=[]
	CC=ctrl.Children()
	
	i=0
	for c in CC:
		
		if len(text)==0 or c.Text()==text:
			C.append(i)
		i=i+1
	if( 1 ):
		print '-->cannot find<', text, '>in:'
		for x in CC:
			print x.Text()
	return C
	
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

	time.sleep(1)
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

	time.sleep(1)
	w_handle = pywinauto.findwindows.find_windows(title=u'Install From Disk', class_name='#32770')[0]
	window = pwa_app.window_(handle=w_handle)
	window.SetFocus()

	time.sleep(1)
	ctrl = window['ComboBox']	#copy files from
	ctrl.Click()
	#print dir(ctrl)
	#ctrl.Select(r'\\Vis_i7_test\latest_kernal_otf\Cam and card\check\03082013')
	ctrl.Select(r'\\vis_i7_test\Latest_Kernal_Otf\Cam and card\check\03112013(2)\drv')
	time.sleep(1)
	ctrl = window['OK']		#OK
	ctrl.Click()

	time.sleep(1)
	w_handle = pywinauto.findwindows.find_windows(title=u'Hardware Update Wizard', class_name='#32770')[0]
	window = pwa_app.window_(handle=w_handle)
	window.SetFocus()
	ctrl = window['Button3']	#Next
	ctrl.Click()

	time.sleep(1)
	ctrl = window['Finish']
	ctrl.Click()
	
pwa_app = pywinauto.application.Application()
window =pwa_app['Computer Management']
ctrl = window['TreeView']
#x=ctrl.GetItem('\VIS_MC_SOLAR\System devices\NecUsb3 Dynamic Bus Enumerator')
#x
c2=FindTreeElem(ctrl.Root(), 'System devices')[0]
cid3=FindTreeElemsID(c2, 'NecUsb3 Dynamic Bus Enumerator')
print cid3
for c in cid3:
	#c2.Children()[c].SetFocus()
	c2.Children()[c].Click()
	c2.Children()[c].Click('right')
	time.sleep(1)
	popup = pwa_app.PopupMenu.WrapperObject()
	popup.SetFocus()
	print '-->right click texts:',popup.Texts()
	time.sleep(1)
	popup.TypeKeys("{HOME}{DOWN 1}{ENTER}")
	#os.system('pause')
	time.sleep(1)
	after_right_click()
	