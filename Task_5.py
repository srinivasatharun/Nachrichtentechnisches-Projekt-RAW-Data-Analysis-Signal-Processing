import scipy.io as spio
import os
import matplotlib.pyplot as plt
import numpy as np

DataPath='D:/Hochschule Wismar/Summer 2023/Telecommuincation Project/Final_Project/Task_5/'
Files=os.listdir(DataPath)
currentfile=str(DataPath)+str(Files[0])

# importing MATLAB mat file
mat = spio.loadmat(currentfile, squeeze_me=True)

datenums=mat['datenums']
ranges=mat['ranges']
data=mat['data']

t=(datenums-np.floor(np.min(datenums)))*24

# number of range gates , data points, receivers

noRG=np.size(data,0)
noDP=np.size(data,1)
noRx=np.size(data,2)

# Function to calculate FFT
def make_fft(t, y):
    dt = t[1] - t[0]  # dt -> temporal resolution ~ sample rate
    f = np.fft.fftfreq(t.size, dt)  # frequency axis
    Y = np.fft.fft(y)  # FFT
    f = np.fft.fftshift(f)
    Y = np.fft.fftshift(Y) / (len(y))
    return f, Y

tsec = t * 60 * 60

# Phase-correction - Receiver / antenna phases
RXPhases=[0, 5.1, 0.0, -7.75]
RXPhases=np.mat(RXPhases)*-1/180*np.pi

# receiver phase adjustment 
for rx in range (noRx):
    data[rx,:,:]=data[rx,:,:]*np.exp(1j*RXPhases[0,rx])   

#--------------------------------------------------------- TASK 5A ---------------------------------------------------------------

nci=8;
noDPn=int(np.floor(noDP/nci))

# perform incoherent integrations
def make_nci(t, y, ci):
    nptsn = int(np.floor(len(y) / ci))
    yn = np.empty(nptsn) + 1j * np.empty(nptsn)
    tn = np.empty(nptsn)
    for i in range(0, nptsn):
        yn[i] = np.sum(np.abs(y[i * ci:i * ci + ci - 1]))
        tn[i] = np.mean(t[i * ci:(i + 1) * ci])
    return tn, yn

# predefine matrix for integrated raw data
datan_nci     = np.zeros([noRG,noDPn,noRx])+1j*np.zeros([noRG,noDPn,noRx])
spectrumn_nci = np.zeros([noRG,noDPn,noRx])+1j*np.zeros([noRG,noDPn,noRx])

for rx in range(noRx):
    for rg in range(noRG):
        tn_nci,datan_nci[rg,:,rx] = make_nci(t,data[rg,:,rx],nci)
        spectrumn_nci[rg,:,rx]    = np.fft.fftshift( np.fft.fft( datan_nci[rg,:,rx] ) )/ len(tn_nci) 

dt_nci  = (np.max(tn_nci)-np.min(tn_nci))/(len(tn_nci)-1)
fs_nci      = 1/dt_nci                               
freq_nci    = np.linspace(-fs_nci/2, fs_nci/2, len(tn_nci))

RG_nci, FG_nci = np.meshgrid(ranges, freq_nci, indexing='ij')

# Plot for Magnitude and Phase of Incoherent Integrations Receiver - 1

plt.figure(1)
plt.subplot(1, 2, 1)
ampln=10*np.log10(np.abs(spectrumn_nci[:,:,0]))
SNRsel=ampln<-5   
ampln[SNRsel]="nan"
plt.pcolor(FG_nci/1000, RG_nci, ampln, cmap='jet', shading='auto')
plt.xlabel('Frequency')
plt.ylabel('Range')
plt.title('Magnitude - Incoherent Integrations (Receiver - 1)')
plt.colorbar()
plt.subplot(1, 2, 2)
phases1=np.angle(spectrumn_nci[:,:,0])/np.pi*180
SNRsel1=10*np.log10(abs(spectrumn_nci[:,:,0])/2)<-5   
phases1[SNRsel1]="nan"
plt.pcolor(FG_nci/1000, RG_nci, phases1, cmap='jet', shading='auto')
plt.xlabel('Frequency')
plt.ylabel('Range')
plt.title('Phase - Incoherent Integrations (Receiver - 1)')
plt.colorbar()

plt.tight_layout()
plt.show()

# Plot for Magnitude and Phase of Incoherent Integrations Receiver - 3

plt.figure(2)
plt.subplot(1, 2, 1)
ampln=10*np.log10(np.abs(spectrumn_nci[:,:,2]))
SNRsel=ampln<-5   
ampln[SNRsel]="nan"
plt.pcolor(FG_nci/1000, RG_nci, ampln, cmap='jet', shading='auto')
plt.xlabel('Frequency')
plt.ylabel('Range')
plt.title('Magnitude - Incoherent Integrations (Receiver - 3)')
plt.colorbar()
plt.subplot(1, 2, 2)
phases1=np.angle(spectrumn_nci[:,:,2])/np.pi*180
SNRsel1=10*np.log10(abs(spectrumn_nci[:,:,2])/2)<-5   
phases1[SNRsel1]="nan"
plt.pcolor(FG_nci/1000, RG_nci, phases1, cmap='jet', shading='auto')
plt.xlabel('Frequency')
plt.ylabel('Range')
plt.title('Phase - Incoherent Integrations (Receiver - 3)')
plt.colorbar()

plt.tight_layout()
plt.show()

#--------------------------------------------------------- TASK 5B ---------------------------------------------------------------

# Cross-Spectra for all ranges and all receivers

Spectrn=np.zeros([noRG,noDPn,noRx])+1j*np.zeros([noRG,noDPn,noRx])

for rx in range(noRx):
    for rg in range(noRG):
        fn,Spectrn[rg,:,rx]=make_fft(tn_nci,datan_nci[rg,:,rx])

XSpectrn=np.zeros([noRG,noDPn,noRx])+1j*np.zeros([noRG,noDPn,noRx])

XSpectrn[:,:,0] = Spectrn[:,:,1] * np.conj(Spectrn[:,:,3]) #2-4

# Plot for Magnitude and Phase of Cross_Spectrum (Incoherent Integrations)  Receiver - 2-4

plt.figure(3)
plt.subplot(1,2,1)
plt.pcolor(FG_nci/1000, RG_nci, 10*np.log10(abs(XSpectrn[:,:,0]))/2,cmap='jet')
plt.xlabel('frequency')
plt.ylabel('ranges')
plt.title('Magnitude - Cross-Spectra NCI')
plt.colorbar()
plt.subplot(1,2,2)
plt.pcolor(FG_nci/1000, RG_nci, np.angle(XSpectrn[:,:,0])/np.pi*180,cmap='jet')
plt.xlabel('frequency')
plt.ylabel('ranges')
plt.title('Phase - Cross-Spectra NCI')
plt.colorbar()

plt.tight_layout()
plt.show()