import os
import re
import sys

'''This program manages the entry of information from the user. It begins by changing the
directory of the program to the sharedrive path shown below:
'PavementAnalysis\Pavemgmt\DATA_COLLECTION\AUTOMATED_VANS\02_COLLECTION_VEHICLES\01_CALIBRATION'
it then asks the user to enter the year for of data the want to see. From that point
information is entered about the van number finally show the desired data visualization.
This code is run from the graphing_final_consol.py program'''

from graphWriter2_New_Color2 import *


def driveFind():
    return os.path.abspath(os.getcwd())

  
def directory():
    years = []
    calSpot = os.getcwd()+'\\calibrationFiles_'
    while True: # stays in the loop asking for input
        for line in os.listdir(driveFind()): # get list of files in current directory
            if re.search('calibrationFiles_',line): # look for folders named 'calibrationFiles'
                years.append(line[-4:])
        os.system('mode con: cols=80 lines=60')
        for n in range(0,len(years)):
            print 'Data available for:',years[n]
        print'----------------------------------------------------------'
        year = raw_input('Enter a year or "done" to leave: ') # user input is entered
        print''
        dir_year = calSpot+str(year) # directory path is created
        if os.path.isdir(dir_year) == True: # if dir_year is a directory
            os.chdir(dir_year) # change directory to dir_year
            while True: # stays in the loop asking for input
                os.chdir(dir_year) # keeps the directory in dir_year
                print''
                print'---------------------------------------------'
                ''' this code prints the years for which viewable data is available
                    for visualization by looking one folder up and checking if
                    data exists. If data is available the that year is shown as
                    a possible entry'''
                print''
                print'Data available for: '+str(os.walk('.').next()[1])+' for year '+str(year)
                print''
                van = raw_input('Enter a van name, or enter "done" to leave: ') # enter van name north,south,east or west
                print''
                try:
                    if van.lower() == 'north': # if input = north
                        dir_van = dir_year+'\\\\North' # append 'north' to original directory path
                        os.chdir(dir_van) # change directory to dir_van
                        yield dir_van  # sends new directory to graphWriter2_New_Color2.py
                                
                    elif van.lower() == 'south': # or other directions entered
                        dir_van = dir_year+'\\\\South'
                        os.chdir(dir_van)
                        yield dir_van
                
                    elif van.lower() == 'east':
                        dir_van = dir_year+'\\\\East'
                        os.chdir(dir_van)
                        yield dir_van
                    
                    elif van.lower() == 'west':
                        dir_van = dir_year+'\\\\West'
                        os.chdir(dir_van)
                        yield dir_van
                        
                    elif van.lower() == 'done': # if user enters 'year'
                        break # break from loop and go back one step
                    else:continue # else continue within current loop
                except ValueError: # handles bad user input
                    continue # nevermind/ignore bad user input and ask question again
                except WindowsError:
                    continue
        elif year == 'done':
            print'Have a nice day' # Have a nice day!!
            print''
            print''
            try:
                input("press enter to exit")
                break
            except SyntaxError:
                break
        else: print 'Not a directory'
