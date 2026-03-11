import scipy.io as spio
import os
import matplotlib.pyplot as plt
import numpy as np

DataPath = 'D:/Hochschule Wismar/Summer 2023/Telecommuincation Project/Final_Project/Task_6/'

Files = os.listdir(DataPath)
currentfile = str(DataPath) + str(Files[0])

# importing MATLAB mat file
mat = spio.loadmat(currentfile, squeeze_me=True)
datenums = mat['datenums']
ranges = mat['ranges']
data = mat['data']

antpos = np.empty([3]).astype(complex)
antpos[0] = 150.88 + 41.56j
antpos[1] = 68.67 - 13.6j
antpos[2] = 206 - 40.79j

f = 3.17e6
c = 3e8
wl = c / f

wl = 94.5718  # in m

t = (datenums - np.floor(np.min(datenums))) * 24

# number of range gates, data points, receivers
noRG = np.size(data, 0)
noDP = np.size(data, 1)
noRx = np.size(data, 2)

RXPhases = [0, 5.1, 0.0, -7.75]  # Phase values for receivers 2 to 5

# Receiver phase adjustment
for rx in range(1, noRx):
    data[:, :, rx] = data[:, :, rx] * np.exp(1j * RXPhases[rx] / 180 * np.pi)

# Plotting echo power for receiver 1
plt.figure(1)
plt.subplot(1,2,1)
plt.pcolor(t, ranges, 20*np.log10(np.abs(data[:, :, 0])), cmap='jet', shading='auto')
plt.colorbar(label='Echo Power')
plt.title('Echo Power for Receiver 1')
plt.xlabel('Time')
plt.ylabel('Range')
plt.subplot(1,2,2)
superposition = np.sum(20*np.log10(np.abs(data[:, :, 1:])), axis=2)
plt.pcolor(t, ranges, superposition, cmap='jet', shading='auto')
plt.colorbar(label='Echo Power')
plt.title('Superposition of Echo Power for Receivers 2 to 4')
plt.xlabel('Time')
plt.ylabel('Range')

plt.tight_layout()
plt.show()


complex_voltage = np.sum(data[:, :, 1:], axis=2)
normalized_voltage = complex_voltage / np.max(np.abs(complex_voltage))

phi = np.angle(normalized_voltage / np.exp(1j * np.angle(antpos[0]))).real
theta = np.angle(normalized_voltage / np.exp(1j * np.angle(antpos[0]))).imag

plt.figure(2)
plt.subplot(1,2,1)
plt.pcolor(t, ranges, phi, cmap='jet', shading='auto')
plt.colorbar(label='Phi (degrees)')
plt.title('Angle-of-Arrival (Phi) for Receivers 2 to 4')
plt.xlabel('Time')
plt.ylabel('Range')
plt.subplot(1,2,2)
plt.pcolor(t, ranges, theta, cmap='jet', shading='auto')
plt.colorbar(label='Theta (degrees)')
plt.title('Angle-of-Arrival (Theta) for Receivers 2 to 4')
plt.xlabel('Time')
plt.ylabel('Range')

plt.tight_layout()
plt.show()
