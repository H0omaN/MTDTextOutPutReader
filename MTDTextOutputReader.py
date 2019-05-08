import pandas as pd 
import matplotlib.pyplot as plt
import glob
import numpy as np
MRMSCentroidX=list()
IMERGCentroidX=list()
MRMSCentroidY=list()
IMERGCentroidY=list()
IMERGArea=list()
MRMSArea=list()
IMERGVelocity=list()
MRMSVelocity=list()
IMERG90=list()
MRMS90=list()
# Netcdf file mode outputs for PC:
outputfolder="/home/ho0man/Temp/modeoutputs/ModeOutPut-Modified/"
# Netcdf file mode outputs for Storms:
#outputfolder="/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/ModeOutPut-Modified/"

## TXT mode outputs
txtoutputfiles=glob.glob(outputfolder+"*_obj.txt")
txtoutputfiles.sort()
i=0
for file in txtoutputfiles:
    
    # extracting centorid of each cluster       
    table = pd.read_table(file, delim_whitespace=True)  
    
    IMERGID = 'CF001'
    MRMSID = 'CO001'
    MRMSmatchIndex = table['OBJECT_ID'] == MRMSID
    IMERGmatchIndex = table['OBJECT_ID'] == IMERGID
    
    
    
    ICX = table["CENTROID_X"].values[IMERGmatchIndex]
    MCX = table["CENTROID_X"].values[MRMSmatchIndex]    
    MRMSCentroidX.append(MCX)
    IMERGCentroidX.append(ICX)
    ICY = table["CENTROID_Y"].values[IMERGmatchIndex]
    MCY = table["CENTROID_Y"].values[MRMSmatchIndex]
    MRMSCentroidY.append(MCY)
    IMERGCentroidY.append(ICY)

#    print(MRMSCentroidX[-1])
#    print(MRMSCentroidX[-2])
    if i>0:
        ### MRMS Velocity km/h therefore it should be multiplied by 10 divided by 0.5
        MV=(((MRMSCentroidX[-2]-MRMSCentroidX[-1])**2+(MRMSCentroidY[-2]-MRMSCentroidY[-1])**2)**0.5)*10/0.5
        IV=(((IMERGCentroidX[-2]-IMERGCentroidX[-1])**2+(IMERGCentroidY[-2]-IMERGCentroidY[-1])**2)**0.5)*10/0.5
        IMERGVelocity.append(IV)
        MRMSVelocity.append(MV)
    IA = table["AREA"].values[IMERGmatchIndex]
    MA = table["AREA"].values[MRMSmatchIndex]
    IMERGArea.append(IA)
    MRMSArea.append(MA)
    I90 = table["INTENSITY_90"].values[IMERGmatchIndex]
    M90 = table["INTENSITY_90"].values[MRMSmatchIndex]
    IMERG90.append(I90)
    MRMS90.append(M90)
    i=i+1
Timestep=np.arange(len(IMERGArea))

#
##### plotting track 
#plt.plot(MRMSCentroidX,MRMSCentroidY,label='MRMS-Track')
#plt.plot(IMERGCentroidX,IMERGCentroidY,label='IMERG-Track')
#plt.title('MRMS-IMERG Track')
#plt.legend(loc='lower right') 
#plt.ylabel("10 km")   
#plt.xlabel("10 km")   
##plt.yticks(np.arange(-60, 100, step=20))  
##plt.xticks(np.arange(0, 74, step=1))  
##plt.grid()
#plt.tight_layout()  

##### plotting track 
#plt.plot(Timestep,IMERGArea,label='IMERG')
#plt.plot(Timestep,MRMSArea,label='MRMS')
#plt.title('MRMS-IMERG Area')
#plt.legend(loc='lower left') 
#plt.ylabel("100 km^2")   
#plt.xlabel("30 min")   
##plt.yticks(np.arange(-60, 100, step=20))  
##plt.xticks(np.arange(0, 74, step=1))  
##plt.grid()
#plt.tight_layout()  


##### plotting Velocity 
#Timestep=np.arange(len(IMERGVelocity))
#plt.plot(Timestep,IMERGVelocity,label='IMERG')
#plt.plot(Timestep,MRMSVelocity,label='MRMS')
#plt.title('MRMS-IMERG Velosity')
#plt.legend(loc='upper left') 
#plt.ylabel("Km/hr")   
#plt.xlabel("30 min")   
##plt.yticks(np.arange(-60, 100, step=20))  
##plt.xticks(np.arange(0, 74, step=1))  
##plt.grid()
#plt.tight_layout()  

#### plotting Intensity

plt.plot(Timestep,IMERG90,label='IMERG')
plt.plot(Timestep,MRMS90,label='MRMS')
plt.title('MRMS-IMERG Intensity 90')
plt.legend(loc='upper left') 
plt.ylabel("mm/hr")   
plt.xlabel("30 min")   
#plt.yticks(np.arange(-60, 100, step=20))  
#plt.xticks(np.arange(0, 74, step=1))  
#plt.grid()
plt.tight_layout()  