set root=\\aeejshe\share\Solar3DSpec\LogCaseSample
for /f %%f in ('dir /b /ad %root%') do (
 python cfgToXml.py %root%\%%f\cmdrpy.log >%root%\%%f\cmdrpy.log.xml
 pause
)
