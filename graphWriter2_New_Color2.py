import os
import csv
import re
import sys
import glob as g
import numpy as np
import traceback
import matplotlib.cm as mplcm
import matplotlib.pyplot as plt
from matplotlib import pylab
from matplotlib import style
import matplotlib.colors as colors

##os.chdir('Y:\\\\PavementAnalysis\\\\Pavemgmt\\\\DATA_COLLECTION\\\\AUTOMATED_VANS\\\\02_COLLECTION_VEHICLES\\\\01_CALIBRATION\\\\calibrationFiles_2017\\\\South')


def listNew():
    listRiri = []
    listLiri = []
    listRrut = []
    listLrut = []
    avgIRIleft = []
    avgIRIright = []
    avgRUTleft = []
    avgRUTright = []
    startList = []
    fileList = []
    baseFiles = []
    for data in os.listdir(os.getcwd()):
        if data.endswith('.TXT') and 'baseline' in data:
            with open(data,'rU') as file:
                R_iri = [[] for i in xrange(0)]
                L_iri = [[] for i in xrange(0)]
                R_rut = [[] for i in xrange(0)]
                L_rut = [[] for i in xrange(0)]
                for row in csv.DictReader(file):
                    R_iri.append(float(row[' IRI RWP']))
                    L_iri.append(float(row['IRI LWP ']))
                    R_rut.append(float(row[' RUT RWP']))
                    L_rut.append(float(row[' RUT LWP']))
            listRiri.append(R_iri)
            listLiri.append(L_iri)
            listRrut.append(R_rut)
            listLrut.append(L_rut)
    transRiri = zip(*listRiri) 
    transLiri = zip(*listLiri)
    transRrut = zip(*listRrut) 
    transLrut = zip(*listLrut)
    for a in range(0,len(transRiri)):
        rAvgIRI = np.average(transRiri[a])
        avgIRIright.append(round(float(rAvgIRI),4))
    for b in range(0,len(transLiri)):
        lAvgIRI = np.average(transLiri[b])
        avgIRIleft.append(round(float(lAvgIRI),4))
    for c in range(0,len(transRrut)):
        rAvgRUT = np.average(transRrut[c])
        avgRUTright.append(round(float(rAvgRUT),4))
    for d in range(0,len(transLrut)):
        lAvgRUT = np.average(transLrut[d])
        avgRUTleft.append(round(float(lAvgRUT),4))

    try:
        for files in fileList:
            if 'baseline' in files:
                baseFiles.append(files)
        with open(baseFiles[0],'rU') as file:
            for row in csv.DictReader(file):
                startList.append(float(row['Start-Mi']))
    except IndexError: pass

    return startList,avgIRIright,avgIRIleft,avgRUTright,avgRUTleft



def baselineCSV():
    IRIavgLeft = []
    IRIavgRight = []
    RUTavgLeft = []
    RUTavgRight = []
    for data in os.listdir(os.getcwd()):
        if data.endswith('.csv') and 'LWP_IRI_baseline_' in data:
            for row in csv.DictReader(open(data,'rU')):
                IRIavgL = float(row['Average'])
                IRIavgLeft.append(IRIavgL)
        elif data.endswith('.csv') and 'RWP_IRI_baseline_' in data:
            for row in csv.DictReader(open(data,'rU')):
                IRIavgR = float(row['Average'])
                IRIavgRight.append(IRIavgR)
        else: pass

        if data.endswith('.csv') and 'LWP_RUT_baseline_' in data:
            for row in csv.DictReader(open(data,'rU')):
                RUTavgL = float(row['Average'])
                RUTavgLeft.append(RUTavgL)
        elif data.endswith('.csv') and 'RWP_RUT_baseline_' in data:
            for row in csv.DictReader(open(data,'rU')):
                RUTavgR = float(row['Average'])
                RUTavgRight.append(RUTavgR)
        else: pass

    return IRIavgRight,IRIavgLeft,RUTavgRight,RUTavgLeft


def allDataBaseline():
    n = 0
    miles = []
    start = []
    iriL = []
    iriR = []
    rutL = []
    rutR = []
    rightr = []
    rightRUT = []
    leftr = []
    leftRUT = []
    righti = []
    rightIRI = []
    lefti = []
    leftIRI = []
    avgIRIleft = []
    avgIRIright = []
    avgRUTleft = []
    avgRUTright = []
    for data in os.listdir(os.getcwd()):
        if data.endswith('.TXT') and 'baseline' in data\
           or 'Baseline' in data or 'All' in data:
            for row in csv.DictReader(open(data,'rU')):
                try:
                    start.append(float(row['Start-Mi']))
                except:
                    try:
                        start.append(float(row['Start-MP']))
                    except KeyError:
                        print 'Column Name Error: Start MP'
                        break
                try:
                    iriR.append(float(row[' IRI R e']))
                    iriL.append(float(row['IRI LWP ']))
                except:
                    try:
                        iriR.append(float(row[' IRI RWP']))
                        iriL.append(float(row['IRI LWP ']))
                    except KeyError:
                        print 'Column Name Error: IRI'
                        break
                try:    
                    rutR.append(float(row[' RUT R e']))
                except:pass
                try:
                    rutR.append(float(row[' RUT RWP']))
                except:pass
                try:
                    rutL.append(float(row[' RUT L e']))
                except:pass
                try:
                    rutL.append(float(row[' RUT LWP']))
                except:pass
    for row in start:
        miles.append(row)
        if row == max(start):
            break
    for row1 in iriL:
        lefti.append(row1)
        n = n + 1
        if n/len(miles) == 1:
            if len(lefti) != len(miles):
                pass
            else:
                n = 0
                leftIRI.append(lefti)
                lefti = []
                continue
    for row2 in iriR:
        righti.append(row2)
        n = n + 1
        if n/len(miles) == 1:
            if len(righti) != len(miles):
                pass
            else:
                n = 0
                rightIRI.append(righti)
                righti = []
                continue
    for row3 in rutL:
        leftr.append(row3)
        n = n + 1
        if n/len(miles) == 1:
            if len(leftr) != len(miles):
                pass
            else:
                n = 0
                leftRUT.append(leftr)
                leftr = []
                continue
    for row4 in rutR:
        rightr.append(row4)
        n = n + 1
        if n/len(miles) == 1:
            if len(rightr) != len(miles):
                pass
            else:
                n = 0
                rightRUT.append(rightr)
                rightr = []
                continue
    transRiri = zip(*rightIRI) 
    transLiri = zip(*leftIRI)
    transRrut = zip(*rightRUT) 
    transLrut = zip(*leftRUT)
    for a in range(0,len(transRiri)):
        rAvgIRI = np.average(transRiri[a])
        avgIRIright.append(round(float(rAvgIRI),4))
    for b in range(0,len(transLiri)):
        lAvgIRI = np.average(transLiri[b])
        avgIRIleft.append(round(float(lAvgIRI),4))
    for c in range(0,len(transRrut)):
        rAvgRUT = np.average(transRrut[c])
        avgRUTright.append(round(float(rAvgRUT),4))
    for d in range(0,len(transLrut)):
        lAvgRUT = np.average(transLrut[d])
        avgRUTleft.append(round(float(lAvgRUT),4))

##    print len(avgIRIright)
##    print len(avgIRIleft)
##    print len(avgRUTright)
##    print len(avgRUTleft)

    return avgIRIright,avgIRIleft,avgRUTright,avgRUTleft



def graphWriterIRI():
    i = 0
    start = []
    
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.TXT') and 'baseline' not in filename\
           and 'Baseline' not in filename:
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
        if filename.endswith('.TXT') and 'baseline' not in filename\
           and 'Baseline' not in filename:
            with open(filename, 'rU') as file:
                for row in csv.DictReader(file):
                    try:
                        startList.append(float(row['Start-Mi']))
                        endList.append(float(row['  End-Mi']))
                    except:
                        try:
                            startList.append(float(row['Start-MP']))
                            endList.append(float(row['  End-MP']))
                        except KeyError:
                            print 'Column Name Error: Start MP'
                            break
                    try:
                        iriRList.append(float(row[' IRI R e']))
                        iriLList.append(float(row['IRI LWP ']))
                    except:
                        try:
                            iriRList.append(float(row[' IRI RWP']))
                            iriLList.append(float(row['IRI LWP ']))
                        except KeyError:
                            print 'Column Name Error: IRI'
                            break
        else:continue
        start.append(startList)        
    
        # Add new data to the plots
        try:
            ax1.plot(startList,iriRList,label=filename,linewidth=2)
            ax2.plot(startList,iriLList,label=filename,linewidth=2)
            #ax2.legend(loc='lower right',borderaxespad=-4,bbox_to_anchor=(1.062, 0.2),ncol=1)
        except ValueError:pass
        
    try:
        base1 = ax1.plot(start[0][0:50],listNew()[1][0:50])
        plt.setp(base1, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties

        base2 = ax2.plot(start[0][0:50],listNew()[2][0:50],label='Baseline')
        plt.setp(base2, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties
        ax2.legend(loc='lower right',borderaxespad=-4,bbox_to_anchor=(1.062, 0.2),ncol=1)
    except KeyError: pass
    except TypeError: pass
    except ValueError: pass

    try:
        base11 = ax1.plot(start[0],baselineCSV()[0][0:50])
        plt.setp(base11, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties

        base21 = ax2.plot(start[0],baselineCSV()[1][0:50],label='Baseline')
        plt.setp(base21, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties
        ax2.legend(loc='lower right',borderaxespad=-4,bbox_to_anchor=(1.062, 0.2),ncol=1)
    except KeyError: pass
    except TypeError: pass
    except ValueError: pass

    #print start[0][0:50],allDataBaseline()[0][0:50]
##    try:
##        base12 = ax1.plot(start[0][0:50],allDataBaseline()[0][0:50])
##        plt.setp(base12, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties
##
##        base22 = ax2.plot(start[0][0:50],allDataBaseline()[1][0:50])
##        plt.setp(base22, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties
##    except KeyError: print'KeyError: allDataBaseline(),','Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
##    except TypeError: print'TypeError: allDataBaseline(),','Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
##    except ValueError: print'ValueError: allDataBaseline(),','Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
    
    plt.show()
    plt.close('all')
    


def graphWriterRut():
    i = 0
    start = []
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.TXT') and 'baseline' not in filename\
           and 'Baseline' not in filename:
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
    pylab.ylim([-0.05,.45])
    plt.hold(True)

    ax4 = fig.add_subplot(2,1,2)
    cm = plt.get_cmap('gist_rainbow')
    ax4.set_color_cycle([cm(1.*i/NUM_COLORS_LEFT_RUT) for i in range(NUM_COLORS_LEFT_RUT)])
    ax4.grid(True)
    plt.title('Left RUT data per mile for verification runs:')
    ax4.tick_params(axis='both', which='major', labelsize=8)
    pylab.ylim([-0.05,.45])
    plt.hold(True)
    
    # Iterate over the files in the current directory
    for filename in os.listdir(os.getcwd()):
        # Initialize a new set of lists for each file
        startList = []
        RutRList = []
        RutLList = []
        # Load the file
        if filename.endswith('.TXT') and 'baseline' not in filename\
           and 'Baseline' not in filename:
            with open(filename, 'rU') as file:
                for row in csv.DictReader(file):
                    try:
                        startList.append(float(row['Start-Mi']))
                    except:
                        try:
                            startList.append(float(row['Start-MP']))
                        except KeyError:
                            print 'Column Name Error: Start Mi'
                            break
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
        start.append(startList)  

        # Add new data to the plots
        try:      
            ax3.plot(startList,RutRList,label=filename,linewidth=2)
            
            ax4.plot(startList,RutLList,label=filename,linewidth=2)
            ##ax4.legend(loc='lower right',borderaxespad=-4,bbox_to_anchor=(1.062, 0.2),ncol=1)
        except ValueError:pass


    try:
        base1 = ax3.plot(start[0][0:50],listNew()[3][0:50])
        plt.setp(base1, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties

        base2 = ax4.plot(start[0][0:50],listNew()[4][0:50],label='Baseline')
        plt.setp(base2, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties
        ax4.legend(loc='lower right',borderaxespad=-4,bbox_to_anchor=(1.062, 0.2),ncol=1)
    except KeyError: pass
    except TypeError: pass
    except ValueError: pass

    try:
        base31 = ax3.plot(start[0][0:50],baselineCSV()[2][0:50])
        plt.setp(base31, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties

        base41 = ax4.plot(start[0][0:50],baselineCSV()[3][0:50],label='Baseline')
        plt.setp(base41, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties
        ax4.legend(loc='lower right',borderaxespad=-4,bbox_to_anchor=(1.062, 0.2),ncol=1)
    except KeyError: pass
    except TypeError: pass
    except ValueError: pass

##    try:
##        base32 = ax3.plot(start[0],allDataBaseline()[2][0:50])
##        plt.setp(base32, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties
##
##        base42 = ax4.plot(start[0],allDataBaseline()[3][0:50])
##        plt.setp(base42, color='y', linewidth=8.0, alpha=0.7) # adjusting the plot lines properties
##    except KeyError: pass
##    except TypeError: pass
##    except ValueError: pass

    
    plt.show()
    plt.close('all')


##graphWriterIRI()
##graphWriterRut()
