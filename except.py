try:
	a=10
	b=0
	a=a/b
except Exception,ex:
	print Exception,":",ex
	
import traceback
try:
	a=b
	b=c
except:
	traceback.print_exc()
	
try:
	a=b
	b=c
except:
	f=open("log.txt",'a')
	traceback.print_exc(file=f)
	f.flush()
	f.close()