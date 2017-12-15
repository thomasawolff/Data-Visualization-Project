import os
import csv
import re
import glob as g
import numpy as np
import matplotlib.cm as mplcm
import matplotlib.pyplot as plt
from matplotlib import pylab
from matplotlib import style
import matplotlib.colors as colors

#os.chdir('Y:\\\\PavementAnalysis\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\02_COLLECTION_VEHICLES\\\\01_CALIBRATION\\\\calibrationFiles_2016\\\\North')

def graphWriterIRI():
    i = 0
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.TXT') and 'baseline' not in filename:
            i = i + 1

    NUM_COLORS_RIGHT = i
    NUM_COLORS_LEFT = i
    
    fig = plt.figure(figsize=(18,10))

    ax1 = fig.add_subplot(2,1,1)
    cm = plt.get_cmap('gist_rainbow')
    ax1.set_color_cycle([cm(1.*i/NUM_COLORS_RIGHT) for i in range(NUM_COLORS_RIGHT)])
    ax1.grid(True)
    plt.title('Right IRI data per mile for verification runs:')
    ax1.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)

    ax2 = fig.add_subplot(2,1,2)
    cm = plt.get_cmap('gist_rainbow')
    ax2.set_color_cycle([cm(1.*i/NUM_COLORS_LEFT) for i in range(NUM_COLORS_LEFT)])
    ax2.grid(True)
    plt.title('Left IRI data per mile for verification runs:')
    ax2.tick_params(axis='both', which='major', labelsize=8)
    plt.hold(True)

    # Iterate over the files in the current directory
    for filename in os.listdir(os.getcwd()):
        # Initialize a new set of lists for each file
        startList = []
        endList = []
        iriRList = []
        iriLList = []
        # Load the file
        if filename.endswith('.TXT') and 'baseline' not in filename:
            with open(filename, 'rU') as file:
                for row in csv.DictReader(file):
                    try:
                        startList.append(float(row['Start-Mi']))
                        endList.append(float(row['  End-Mi']))
                    except:
                        startList.append(float(row['Start-MP']))
                        endList.append(float(row['  End-MP']))
                    try:
                        iriRList.append(float(row[' IRI R e']))
                        iriLList.append(float(row['IRI LWP ']))
                    except:
                        iriRList.append(float(row[' IRI RWP']))
                        iriLList.append(float(row['IRI LWP ']))
        else:continue
        # Add new data to the plots
        try:
            ax1.plot(startList,iriRList,label=filename,linewidth=2)

            ax2.plot(startList,iriLList,label=filename,linewidth=2)
            ax2.legend(loc='lower right',borderaxespad=-4,bbox_to_anchor=(1.062, 0.2),ncol=1)
        except ValueError:pass

    plt.show()
    plt.close('all')
    
#graphWriterIRI()

def graphWriterRut():
    i = 0
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.TXT') and 'baseline' not in filename:
            i = i + 1

    NUM_COLORS_RIGHT_RUT = i
    NUM_COLORS_LEFT_RUT = i
    
    fig = plt.figure(figsize=(18,10))
    
    ax3 = fig.add_subplot(2,1,1)
    cm = plt.get_cmap('gist_rainbow')
    ax3.set_color_cycle([cm(1.*i/NUM_COLORS_RIGHT_RUT) for i in range(NUM_COLORS_RIGHT_RUT)])
    ax3.grid(True)
    plt.title('Right RUT data per mile for verification runs:')
    ax3.tick_params(axis='both', which='major', labelsize=8)
    pylab.ylim([0,.4])
    plt.hold(True)

    ax4 = fig.add_subplot(2,1,2)
    cm = plt.get_cmap('gist_rainbow')
    ax4.set_color_cycle([cm(1.*i/NUM_COLORS_LEFT_RUT) for i in range(NUM_COLORS_LEFT_RUT)])
    ax4.grid(True)
    plt.title('Left RUT data per mile for verification runs:')
    ax4.tick_params(axis='both', which='major', labelsize=8)
    pylab.ylim([0,.4])
    plt.hold(True)
    
    # Iterate over the files in the current directory
    for filename in os.listdir(os.getcwd()):
        # Initialize a new set of lists for each file
        startList = []
        endList = []
        RutRList = []
        RutLList = []
        # Load the file
        if filename.endswith('.TXT') and 'baseline' not in filename:
            with open(filename, 'rU') as file:
                for row in csv.DictReader(file):
                    try:
                        startList.append(float(row['Start-Mi']))
                    except:
                        startList.append(float(row['Start-MP']))
                    try:
                        endList.append(float(row['  End-Mi']))
                    except:
                        endList.append(float(row['  End-MP']))
                    try:    
                        RutRList.append(float(row[' RUT R e']))
                    except:pass
                    try:
                        RutRList.append(float(row[' RUT RWP']))
                    except:pass
                    try:
                        RutLList.append(float(row[' RUT L e']))
                    except:pass
                    try:
                        RutLList.append(float(row[' RUT LWP']))
                    except:pass
        else:continue
        # Add new data to the plots
        try:      
            ax3.plot(startList,RutRList,label=filename,linewidth=2)
            
            ax4.plot(startList,RutLList,label=filename,linewidth=2)
            ax4.legend(loc='lower right',borderaxespad=-4,bbox_to_anchor=(1.062, 0.2),ncol=1)
        except ValueError:pass
        
    plt.show()
    plt.close('all')

#graphWriterRut()
