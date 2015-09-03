@echo off

:START
rem call :Sleep 200
call :RestartServices
rem goto :START
pause

:RestartServices
tasklist /svc | findstr /i "Workstation"
set sts=%errorlevel%
if %errorlevel% EQU 0 (
	echo services already exists
) else (
	echo Start services
	net start Workstation
	net start Server
) 
goto :EOF

:Sleep
ping 127.0.0.1 -n %1 > nul
goto :EOF
