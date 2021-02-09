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

fig = plt.figure(figsize = (15,3))
ax = fig.add_subplot(111)
ax2 = ax.twiny()
ax2.set_xlim((np.min(chans), np.max(chans)))

# alpha_crrls from splatalogue
alpha_crrls = np.array([203.64,207.52,209.50,211.51,213.54,217.68,219.79,224.09,226.28,230.76])
for line in alpha_crrls:
   ax.plot([(line-200.32)*100,(line-200.32)*100],[-1000.,1000.],'C3--')
# next plot is not visible, just sets up the legend
ax.plot([0,1],[0,1],'C3--',label=r'$C\alpha$ lines')

# Need to average flux over desired pixels to get a single list to plot
avedata = np.zeros(3072)
for i in range(3072):
   avedata[i] = np.mean(wdata[i,:,:])

# noise levels determined using the 3072 frequencies plotted - could be more accurate if flagged frequencies were excluded
aprxrms = 1000*np.nanstd(avedata)

ax.fill_between(np.arange(0,nchans), -3*aprxrms, 3*aprxrms, color='blue',alpha=0.3, lw=0)
ax.plot(1.e3*avedata, label="SgrA* spectrum", color="black")
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 100))
ax2.set_xlabel("Frequency / MHz")
ax.set_ylabel("peak flux density (mJy/beam)")
ax.set_xlabel("10-kHz channel number")
ax.set_xlim([0, 3072])
# y-axis limits set to a suitable level
ax.set_ylim([-10.,10.]) 

ax.legend()
fig.savefig(infile.replace(".fits", "_spectrum.pdf"), bbox_inches="tight")
fig.savefig(infile.replace(".fits", "_spectrum.png"), bbox_inches="tight")
