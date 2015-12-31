# -*- coding: utf-8 -*-

"""
    TITLE:      LearningExcelInPython.py
    AUTHOR:     John Himics
    EMAIL:      john@johnhimics.com
    TIMEZONE:   EST
    VERSION:    0
    
    DESCRIPTION:    Beginning file for learning how to
                    manipulate excel with python
    
    DEPENDANCIES: mmap, xlrd
    
"""
# imports
from mmap import mmap, ACCESS_READ
from xlrd import open_workbook,XL_CELL_TEXT,cellname,XL_CELL_TEXT

#Global Variables


#Methods



#Program starts here
if __name__ == "__main__":
    print 'Hello and Welcome! Program running'
    pass
    print 'Program Complete, Goodbye!'


    #**********************************
    print "**THIS IS JUST OPENING A WORKBOOK**"
    print open_workbook('simple.xlsx')

    with open('simple.xlsx','rb') as f:
        print open_workbook(
                            file_contents=mmap(f.fileno(),0,access=ACCESS_READ)
                            )
    aString = open('simple.xlsx','rb').read()
    print open_workbook(file_contents = aString)

    #**********************************
    print "**THIS IS NAVIGATING A WORKBOOK**"

    wb = open_workbook('simple.xlsx')

    for s in wb.sheets():
        print 'Sheet:', s.name
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                values.append(s.cell(row,col).value)
            print (values)
        print
        
        
    #**********************************
    print "**THIS IS WORKING WITH WORKBOOKS AND WORKSHEETS**"

    book = open_workbook('simple.xlsx')

    print book.nsheets #this attribute returns the number of sheets

    for sheet_index in range(book.nsheets):
        #this method returns sheets by numerical index
        print book.sheet_by_index(sheet_index) 
        

    #this method returns a list of unicodes containing the names of all sheets
    print book.sheet_names() 
    for sheet_name in book.sheet_names():
        #This method returns sheets by thier names
        print book.sheet_by_name(sheet_name)
        
    for sheet in book.sheets(): #this method returns a list of sheets
        print sheet
        
    #Other xlrd.Book object attributes are codepage, countries, user_name


    #**********************************
    print "**THIS IS INTROSPECTING A SHEET**"    
    #from xlrd import open_workbook,cellname

    book = open_workbook('simple.xlsx')
    sheet = book.sheet_by_index(0)

    print sheet.name  #name of the sheet
    print sheet.nrows #number of rows used in the sheet
    print sheet.ncols #number of cols used in the sheet

    for row_index in range(sheet.nrows):
        for col_index in range(sheet.ncols):
            print cellname(row_index,col_index),'-', #returns the "A5" "B16" name of the cell
            print sheet.cell(row_index,col_index).value #returns the cell value
            
    #**********************************
    print "**THIS IS GETTING A PARTICULAR CELL**"        
