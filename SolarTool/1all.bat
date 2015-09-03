set casepath=C:\WinEagle\log\AutoRpt
J:\App\User\aeejshe\Python25_2\python J:\App\User\aeejshe\Python25_2\extractGeneratinfoINresult.py %casepath%

J:\App\User\aeejshe\Python25_2\python J:\App\User\aeejshe\Python25_2\repeatibility4.py %casepath% > %casepath%\log.txt
rem 
J:\App\User\aeejshe\Python25_2\python J:\App\User\aeejshe\Python25_2\repeatability_extractMaxThicknessEx.py  %casepath% 

pause
