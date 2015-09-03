#!/usr/bin/env python

from win32com.client import Dispatch
import pdb

xlApp = Dispatch("Excel.Application") 
xlApp.Visible = 1

# Check if any workbook exists. 
#pdb.set_trace()
if xlApp.Workbooks.Count == 0:
    # If not, create a new one.
    workbook = xlApp.Workbooks.Add()
else:
    # If yes, use the first one.
    workbook = xlApp.Workbooks[0]

# Check if any sheet exists.
if workbook.Sheets.Count == 0:
    # If not, add a sheet to current workbook.
    sheet = workbook.Sheets.Add()
else:
    # If yes, use the first sheet of current workbook.
    sheet = workbook.Sheets[0]
    
# Generate the multiplication table(9x9). 
for i in xrange(2, 10):
    # Cells(<column>, <row>)
    sheet.Cells(1, i).Value = i
    sheet.Cells(1, i).Font.Color = 0xFF0000
    sheet.Cells(i, 1).Value = i
    sheet.Cells(i, 1).Font.Color = 0x00FF00
    
def a2i(ch):
    return ord(ch.upper()) - ord('A') + 1

def i2a(i):
    return chr((i-1) + ord('A'))
    
for i in xrange(2, 10):
    for j in xrange(2, 10): 
        # Generate the Excel formula.       
        sheet.Cells(i, j).Formula = '=%s1*A%s' % (i2a(j), i)
        sheet.Cells(i, j).Font.Color = 0x000000
sheet.Name = "Multiplication Table"
workbook.SaveAs('xxx.xls')
#xlApp.Quit()
