import pywikibot
import logging
from mwviews.api import PageviewsClient
import wikipedia
import time
import os
import texttable as tt
from pageimage import *
from images_updatedtime import*

def not_updated_images(edit_Time,endTime):
    edit_Time = str(edit_Time)
    year_edit = edit_Time[0:4]
    year_end = endTime[0:4]
    month_edit = edit_Time[5:7]
    month_end = endTime[5:7]
    day_edit = edit_Time[8:10]
    day_end = endTime[8:10]

    if int(year_edit) < int(year_end):
        return False
    elif int(year_edit) >= int(year_end):
        if int(month_edit) < int(month_end):
            return False
        elif int(month_edit) >= int(month_end):
            if int(day_edit) < int(day_end):
                return False
            elif int(day_edit) >= int(day_end):
                return True

print("----------------------------------------------------------------------------------------")
print("--------------------------------- Starting Milestone:2 ---------------------------------")
print("----------------------------------------------------------------------------------------")
pagename=input("From what page do you want to get all images: ")
print("----------------------------------------------------------------------------------------")
print("------------------------------------ The result is: ------------------------------------")
print("----------------------------------------------------------------------------------------")
pagelist= show_image(pagename)
timelist= image_timelist(pagelist)
tab1 = tt.Texttable()
x1 = [[]]
in11 = 0
for i in pagelist:
    numbering = in11 + 1
    x1.append([numbering,i,timelist[in11]])
    in11 = in11 + 1
tab1.add_rows(x1)
tab1.set_cols_align(['r', 'r', 'r'])
tab1.header(["No","Image name","Uploaded time"])
print(tab1.draw())

Final_notlist = [ ]
Finaldate_notlist = [ ]

Final_list = []
Finaldate_list = []
x12=[[]]
Date_in =input("Insert a date to check image is updated or not: ")
in_11 = 0
for i in pagelist:
    if not_updated_images(timelist[in_11],Date_in) == False:
        Final_notlist.insert(in_11,i)
        Finaldate_notlist.insert(in_11,timelist[in_11])
    if not_updated_images(timelist[in_11],Date_in) == True:
        Final_list.insert(in_11,i)
        Finaldate_list.insert(in_11,timelist[in_11])
    in_11 = in_11 + 1

tab11 = tt.Texttable()
x12 = [[]]
in111 = 0
for i in Final_notlist:
    numbering = in111 + 1
    x12.append([numbering,i,Finaldate_notlist[in111]])
    in111 = in111 + 1
tab11.add_rows(x12)
tab11.set_cols_align(['r', 'r', 'r'])
tab11.header(["No","Image name","Not Uploaded images"])
print(tab11.draw())

Want_to_delete =input("Do you want to delete any image from above list[Yes/No]: ")
if Want_to_delete == 'Yes':
    #select_no = input("select the index[1/2/3..]: ")
    imagename = input("Enter a image name: ")
    os.system('python3 pwb.py image '+imagename)

print("----------------------------------------------------------------------------------------")
print("------------------------------------ Ending Wikibot ------------------------------------")
print("----------------------------------------------------------------------------------------")