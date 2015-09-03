import win32api, win32con, os, sys, win32pdh, time, random


# def GetProcessID( name ) :
    # object = "Process"
    # items, instances = win32pdh.EnumObjectItems( None, None, object,
                                                 # win32pdh.PERF_DETAIL_WIZARD )
    # val = None
    # if name in instances :
        # hq = win32pdh.OpenQuery()
        # hcs = [ ]
        # item = "ID Process"
        # path = win32pdh.MakeCounterPath( ( None, object, name, None, 0, item ) )
        # hcs.append( win32pdh.AddCounter( hq, path ) )
        # win32pdh.CollectQueryData( hq )
        # time.sleep( 0.01 )
        # win32pdh.CollectQueryData( hq )

       # for hc in hcs:
            # type, val = win32pdh.GetFormattedCounterValue( hc, win32pdh.PDH_FMT_LONG )
            # win32pdh.RemoveCounter( hc )
       # win32pdh.CloseQuery( hq )
       # return val


def killProcessByName(name):
	os.system('pskill.exe %s'%(name))

def killProcessById(pid):
	handle = win32api.OpenProcess( win32con.PROCESS_TERMINATE, 0, pid )
	#If you already have the handle (e.g., if you had started the process in the same bit of code as Rajkumar did in his blog), then you can go straight to terminating the process:
	win32api.TerminateProcess( handle, 0 )
	win32api.CloseHandle( handle )

def runCmd(cmd):
	print cmd
	os.system(cmd)
	
def runOneSuite(learn_dir, playlist_file):
	print 'runOneSuite', playlist_file
	#prepare files
	killProcessByName('visionproc')
	killProcessByName('solarhost')
	
	runCmd('rmdir /s/q c:\\wineagle\\log\\autorpt')
	runCmd('del c:\\wineagle\\*.txt')
	
	runCmd('xcopy /c/q/e/y "%s" c:\\wineagle'%(learn_dir))
	runCmd('copy /y "%s" c:\\wineagle\\playlist.txt'%(playlist_file))
	
	#start exe
	runCmd('c:\\WinEagle.1\\solarhost.exe')
	runCmd('pause')
	
	#wait done & move results
	dest_base_dir = 'c:\\wineagle\\test_result'
	dest_dir='%s\\%s'%(dest_base_dir,learn_dir[-10:].replace('\\','_'))
	runCmd("move /y c:\\wineagle\\log\\autorpt %s"%(dest_dir))
	
	#gen report
	runCmd('repeatibility.py.bat %s'%(dest_dir))
	
# def runAllSuite(dirs):
	# dest_base_dir = 'c:\\wineagle\\test_result'
	
	# for learn_dir in dirs:
		# print learn_dir
		# runOneSuite(learn_dir, learn_dir+'\\plsylist.txt')
	
	# #gen result
	# runCmd('python extractMaxThicknessEx.py %s'%(dest_base_dir))
	
# def runAllSuiteInDir(dir):
	# dirs = [os.path.join(dir,folder) for folder in os.listdir(dir)]
	# print dirs
	# runAllSuite(dirs)
	

runCmd('xcopy /c/q/e/y g:\\system c:\\wineagle\\system')
learn_folder = r'J:\App\User\aeejshe\3dsolar\test\Learn'
plsy_lists=['test_solar\\playlist_mono1.txt', 'test_solar\\playlist_mono2.txt','test_solar\\playlist_poly1.txt','test_solar\\playlist_poly2.txt']

for plsylist in plsy_lists:
	runOneSuite(learn_folder, plsylist)
