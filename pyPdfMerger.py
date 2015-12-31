# -*- coding: utf-8 -*-

"""
	TITLE:		pyPdfMerger.py
	AUTHOR: 	John Himics
	EMAIL: 		john@johnhimics.com
	TIMEZONE: 	EST
	VERSION: 	0
	
	DESCRIPTION: 	Merges pdf files together
	
	DEPENDANCIES: 	PyPDF2
	
"""
from PyPDF2 import PdfFileMerger

#Global Variables
merger = PdfFileMerger()

#Methods


#Program starts here
if __name__ == "__main__":

	input1 = open("C:\PFile\@ActiveProjects\1050LF Yeild Issues\Emails\All emails 11-18-13 2.pdf", "rb")
	input2 = open("C:\PFile\@ActiveProjects\1050LF Yeild Issues\Emails\Wade 343005 [compatibility mode].pdf", "rb")
	input3 = open("C:\PFile\@ActiveProjects\1050LF Yeild Issues\Emails\1050LF Mill Mix MDR.pdf", "rb")

	# add the first 3 pages of input1 document to output
	#merger.append(fileobj = input1, pages = (0,3))

	# insert the first page of input2 into the output beginning after the second page
	#merger.merge(position = 2, fileobj = input2, pages = (0,1))

	# append entire input3 document to the end of the output document
	merger.append(input1)
	merger.append(input2)
	merger.append(input3)

	# Write to an output PDF document
	output = open("C:\PFile\@ActiveProjects\1050LF Yeild Issues\Emails\document-output.pdf", "wb")
	merger.write(output)
