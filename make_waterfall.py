import sys
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(sys.argv[1],skiprows=2,delimiter=',',usecols=np.arange(1,101))
#data = np.loadtxt(sys.argv[1],skiprows=2,delimiter=',')
#data = data[1:,:]

scanFreqs = np.arange(879,1080,2)

# Setup figure and axes
fig = plt.figure(figsize=(12,9))
ax1 = plt.subplot(111)

# Set labels and tick sizes
ax1.set_ylabel(r'Data Row',fontsize=18)
ax1.set_xlabel(r'Frequency',fontsize=18)
ax1.tick_params(axis='both', which='major', labelsize=16)

# Plotting
ax1.imshow(data,cmap=plt.get_cmap('afmhot'),aspect=sys.argv[2])
#ax1.set_xticks(scanFreqs)

plt.show()
