import panda as pd
import glob
MRMSCentroidX=list()
IMERGCentroidX=list()
MRMSCentroidY=list()
IMERGCentroidY=list()
IMERGArea=list()
MRMSArea=list()
IMERGVelocity=list()
MRMSVelocity=list()
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
#    print(table["OBJECT_ID"].values[-2])
    ICX = table["CENTROID_X"].values[-3]
    MCX = table["CENTROID_X"].values[-2]    
    MRMSCentroidX.append(MCX)
    IMERGCentroidX.append(ICX)
    ICY = table["CENTROID_Y"].values[-3]
    MCY = table["CENTROID_Y"].values[-2]
    MRMSCentroidY.append(MCY)
    IMERGCentroidY.append(ICY)
    print(MRMSCentroidX[-1])
    print(MRMSCentroidX[-2])
    if i>0:
        ### MRMS Velocity km/h therefore it should be multiplied by 10 divided by 0.5
        MV=(((MRMSCentroidX[-2]-MRMSCentroidX[-1])**2+(MRMSCentroidY[-2]-MRMSCentroidY[-1])**2)**0.5)*10/0.5
        IV=(((IMERGCentroidX[-2]-IMERGCentroidX[-1])**2+(IMERGCentroidY[-2]-IMERGCentroidY[-1])**2)**0.5)*10/0.5
        IMERGVelocity.append(IV)
        MRMSVelocity.append(MV)
    IA = table["AREA"].values[-3]
    MA = table["AREA"].values[-2]
    IMERGArea.append(IA)
    MRMSArea.append(MA)
    i=i+1
Timestep=np.arange(len(IMERGArea))


#### plotting track 
plt.plot(MRMSCentroidX,MRMSCentroidY,label='MRMS-Track')
plt.plot(IMERGCentroidX,IMERGCentroidY,label='IMERG-Track')
plt.title('MRMS-IMERG Track')
plt.legend(loc='lower right') 
plt.ylabel("10 km")   
plt.xlabel("10 km")   
#plt.yticks(np.arange(-60, 100, step=20))  
#plt.xticks(np.arange(0, 74, step=1))  
#plt.grid()
plt.tight_layout()  