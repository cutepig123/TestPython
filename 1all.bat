path J:\app\User\aeejshe\tools\Python27_2;%path%
set casepath=c:\wineagle\log
python extractGeneratinfoINresult.py "%casepath%"

python repeatibility4.py "%casepath%"
rem 
python repeatability_extractMaxThicknessEx.py  "%casepath%"

pause
