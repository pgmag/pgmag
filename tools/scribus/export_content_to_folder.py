#!/usr/bin/env python
#
# File: extract_content_to_folder
# Desc: Extracts the texts from a document, saving them 
#       to multiple text file and put them in one folder per page
#
# Author : Damien Clochard <damien@dalibo.info>
# Version : 20110602-1
# Licence : BSD 
#
# Note : this script is based on the original extract_text.py script
# Check out the Scribus wiki for more information :
# http://wiki.scribus.net/canvas/Export_all_text
#

import scribus 
import os # to create folder

def exportText(root_folder):
    page = 1
    pagenum = scribus.pageCount()
    T = []
    content = []
    while (page <= pagenum):
        scribus.gotoPage(page)
        d = scribus.getPageItems()
        
        page_folder = root_folder+"/p"+str(page)
        if not os.path.isdir(page_folder):
			os.mkdir(page_folder)
        
        for item in d:
            if (item[1] == 4): # the item is a text
				textfile = folder+"/p"+str(page)+"/"+item[0]+".txt"
				output_file = open(textfile,'w')
				output_file.writelines(scribus.getAllText(item[0]))
				output_file.close()
				

        page += 1
        

    endmessage = "Text files successfully saved in "+root_folder
    scribus.messageBox("Finished", endmessage,icon=0,button1=1)


if scribus.haveDoc():
    folder = scribus.fileDialog(\
		'Select the folder', \
         filter='All Files (*)', \
         isdir=True)
    try:
        if folder == '':
            raise Exception
        exportText(folder)
    except Exception, e:
        print e

else:
    scribus.messageBox('Export Error', 'You need a Document open, and a frame selected.', \
                       icon=0, button1=1)

