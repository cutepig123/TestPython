# -*- coding: utf-8 -*-

import pywinauto,sys,os
import pywinauto.application

is2d=1
camid=0
if len(sys.argv)>1:
	camid=int(sys.argv[1])
	
pwa_app = pywinauto.application.Application()
w_handle = pywinauto.findwindows.find_windows(title='LabEyeII')[0]
window = pwa_app.window_(handle=w_handle)
window.MenuSelect("File->New")

w_handle = pywinauto.findwindows.find_windows(title=u'Camera Select', class_name='#32770')[0]
window2 = pwa_app.window_(handle=w_handle)
ctrl = window2['CameraComboBox']
ctrl.Select('IO_camA%d'%camid)
ctrl = window2['OK']
ctrl.Click()

window.MenuSelect("File->Grab->Continuous")

ctrl = window['Camera:ComboBox']
ctrl.Select('CAMERA A%d'%camid)

if is2d:
	ctrl = window['Light Group:ComboBox']
	ctrl.Select('13.LC_SIDE')
ctrl = window['Light Region:ComboBox']
ctrl.Select('All')
ctrl = window['Light Value:Edit3']
ctrl.SetText('40')
ctrl.TypeKeys('{ENTER}')

#win1 = window['#327704']
#ctrl = win1['Exp Time:Edit4']
#ctrl.SetText('1')

os.system('pause')

ctrl = window['Light Value:Edit3']
ctrl.SetText('0')
ctrl.TypeKeys('{ENTER}')

ctrl = window['IO_camA0']
ctrl.Close()

