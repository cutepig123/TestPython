set d=F:\Renesola\20130420\test
for /f %%f in ('dir /a /b %d%') do python sendEmail3.py -r jshe@asmpt.com -s "%d%\%%f" -f "%d%\%%f" -m "%d%\%%f"