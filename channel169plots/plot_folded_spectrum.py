#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
import sys

# Publication-quality plotting
from matplotlib import rc
rc('text', usetex=True)
rc('font',**{'family':'serif','serif':['serif']})

infile = sys.argv[1]
whdu = fits.open(infile)
wcube = whdu[0].data

# frequency info
chans = np.arange(whdu[0].header["CRVAL3"], whdu[0].header["CRVAL3"]+whdu[0].header["NAXIS3"]*whdu[0].header["CDELT3"], whdu[0].header["CDELT3"])
chans = [x * 1.e-6 for x in chans]

# cube takes up approx 1degree x 1degree (see num_beams.py)
wdata = wcube[:,859:1141,859:1141]
nchans = wdata.shape[0]

fig = plt.figure(figsize = (5,3))
ax = fig.add_subplot(111)
alpha_crrls = np.array([203.64,207.52,209.50,211.51,213.54,217.68,219.79,224.09,226.28,230.76])
alpha_crrls -= 200.32 # value of channel 0
alpha_crrls *= 100    # crrls converted from freq. to channel no.

# Need to average flux over square degree to get a single list to plot
avedata = np.zeros(3072)
for i in range(3072):
   avedata[i] = np.mean(wdata[i,:,:])

# we will have one centre channel, with 20 on either side
folded_data = np.zeros(41)

# selects the required section of spectrum around each RRL and adds to the spectrum
for line in alpha_crrls:
   start = int(line)-20
   end = int(line)+21
   segment = avedata[start:end]
   folded_data += segment
   
folded_data /= len(alpha_crrls)
 
ax.plot(np.arange(-200,201,10),1.e3*folded_data,'k')
ax.set_xlim([-200,200])
ax.set_xlabel("Frequency from RRL (kHz)")
ax.set_ylim([-2.5,2.5])
ax.set_ylabel("flux density (mJy/beam)")
fig.savefig(infile.replace(".fits", "_folded_spectrum.pdf"), bbox_inches="tight")
fig.savefig(infile.replace(".fits", "_folded_spectrum.png"), bbox_inches="tight")
