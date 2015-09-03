import os,sys

lastkey=None
allRes=[]
allP=[]
allT=[]
for line in open(r'\\vis_3ds_vision\C\WinEagle\log\MapSawMarkValueByPT.txt', 'r').readlines():
	a =line.split(' ')
	assert( len(a)==7 )
	Res =float(a[-1])
	T =float(a[-3])
	P =float(a[-5])
	
	key ='\\'.join(a[0].split('\\')[:-1])
	if lastkey is None:
		lastkey=key
	
	if lastkey==key:
		allRes.append(Res)
		allP.append(P)
		allT.append(T)
	else:	#end of this cases, calc repeatability
		print lastkey, 'rangeP', max(allP)-min(allP),'rangeT', max(allT)-min(allT),'rangeRes', max(allRes)-min(allRes)
		print 'allP',allP
		print 'allT',allT
		print 'allRes',allRes
		#os.system('pause')
		lastkey=key
		allRes=[Res]
		allP=[P]
		allT=[T]
		
		