#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
import sys

beams_per_pix = 1/39.4703

# used to set up second axis later
def pix2beam(x):
   return x * beams_per_pix
   
def beam2pix(x):
   return x / beams_per_pix

box_lengths = np.array([1.,3.,10.,32.,100.,282.,400.])
box_areas = box_lengths**2
observed_noise = np.zeros_like(box_areas)

infile = sys.argv[1]     # .fits cube to be analysed
whdu = fits.open(infile)
wcube = whdu[0].data

#1x1 cube
wdata = wcube[:,1000:1001,1000:1001]
#wdata = wcube[:,1600:1601,1600:1601]
avedata = np.zeros(3072)
for i in range(3072):
   avedata[i] = np.mean(wdata[i,:,:])

init_noise = 1000*np.nanstd(avedata)
observed_noise[0] = init_noise

#3x3 cube
wdata = wcube[:,999:1002,999:1002]
#wdata = wcube[:,1599:1602,1599:1602]
avedata = np.zeros(3072)
for i in range(3072):
   avedata[i] = np.mean(wdata[i,:,:])

aprxrms = 1000*np.nanstd(avedata)
observed_noise[1] = aprxrms

#10x10 cube
wdata = wcube[:,995:1005,995:1005]
#wdata = wcube[:,1595:1605,1595:1605]
avedata = np.zeros(3072)
for i in range(3072):
   avedata[i] = np.mean(wdata[i,:,:])

aprxrms = 1000*np.nanstd(avedata)
observed_noise[2] = aprxrms

#32x32 cube
wdata = wcube[:,984:1016,984:1016]
#wdata = wcube[:,1584:1616,1584:1616]
avedata = np.zeros(3072)
for i in range(3072):
   avedata[i] = np.mean(wdata[i,:,:])

aprxrms = 1000*np.nanstd(avedata)
observed_noise[3] = aprxrms

#100x100 cube
wdata = wcube[:,950:1050,950:1050]
#wdata = wcube[:,1550:1650,1550:1650]
avedata = np.zeros(3072)
for i in range(3072):
   avedata[i] = np.mean(wdata[i,:,:])

aprxrms = 1000*np.nanstd(avedata)
observed_noise[4] = aprxrms

#282x282 cube (approx. 1 square degree)
wdata = wcube[:,859:1141,859:1141]
#wdata = wcube[:,1459:1741,1459:1741]
avedata = np.zeros(3072)
for i in range(3072):
   avedata[i] = np.mean(wdata[i,:,:])

aprxrms = 1000*np.nanstd(avedata)
observed_noise[5] = aprxrms

#400x400 cube
wdata = wcube[:,800:1200,800:1200]
#wdata = wcube[:,1400:1800,1400:1800]
avedata = np.zeros(3072)
for i in range(3072):
   avedata[i] = np.mean(wdata[i,:,:])

aprxrms = 1000*np.nanstd(avedata)
observed_noise[6] = aprxrms

# noise, if noise went down like 1/sqrt(no. pix)
sqrt_pix_noise = np.zeros_like(box_areas)
for i in range(len(box_areas)):
   sqrt_pix_noise[i] = init_noise / np.sqrt(box_areas[i])

# noise, if noise went down like 1/sqrt(no. beams)
sqrt_beams_noise = np.zeros_like(box_areas)
for i in range(len(box_areas)):
   sqrt_beams_noise[i] = init_noise / np.sqrt(box_areas[i]*beams_per_pix)
print(sqrt_beams_noise)   

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.plot(box_areas,observed_noise,'C0o',label='Observed noise levels')
ax.plot(box_areas,sqrt_pix_noise,'C1',label='Predicted noise using 1/sqrt(no. pixels)')
ax.plot(box_areas,sqrt_beams_noise,'C2',label='Predicted noise using 1/sqrt(no. beams)')
ax.set_xscale('log')
ax.set_xlabel("Area observed (pixels)")
ax.set_xlim([0.5,200000])
ax.set_yscale('log')
ax.set_ylabel("RMS noise (mJy/beam)")
ax.set_ylim([0.2,200])
ax.legend()
secax = ax.secondary_xaxis('top', functions=(pix2beam, beam2pix))
secax.set_xlabel('Area observed (beams)')

fig.savefig("expected_decrease.pdf",bbox_inches="tight")
fig.savefig("expected_decrease.png",bbox_inches="tight")
