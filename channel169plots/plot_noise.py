#!/usr/bin/env python

# Plots the noise decrease for greater observing time

import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
import sys

xlist = np.array([5.,10.,20.,40.,80.,160.,320.])
xlist /= 60
ylist = []

#calculate average rms for 1obs samples
infile = "1a_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_1a = np.nanstd(wsqr[1000:1100,1000:1100])

infile = "1b_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_1b = np.nanstd(wsqr[1000:1100,1000:1100])

infile = "1c_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_1c = np.nanstd(wsqr[1000:1100,1000:1100])

infile = "1d_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_1d = np.nanstd(wsqr[1000:1100,1000:1100])

rms_1 = np.mean([rms_1a,rms_1b,rms_1c,rms_1d])
ylist.append(rms_1*1000)

#calculate average rms for 2obs samples
infile = "2a_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_2a = np.nanstd(wsqr[1000:1100,1000:1100])

infile = "2b_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_2b = np.nanstd(wsqr[1000:1100,1000:1100])

infile = "2c_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_2c = np.nanstd(wsqr[1000:1100,1000:1100])

infile = "2d_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_2d = np.nanstd(wsqr[1000:1100,1000:1100])

rms_2 = np.mean([rms_2a,rms_2b,rms_2c,rms_2d])
ylist.append(rms_2*1000)

#calculate average rms for 4obs samples
infile = "4a_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_4a = np.nanstd(wsqr[1000:1100,1000:1100])

infile = "4b_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_4b = np.nanstd(wsqr[1000:1100,1000:1100])

rms_4 = np.mean([rms_4a,rms_4b])
ylist.append(rms_4*1000)

#calculate average rms for 8obs samples
infile = "8a_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_8a = np.nanstd(wsqr[1000:1100,1000:1100])

infile = "8b_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_8b = np.nanstd(wsqr[1000:1100,1000:1100])

rms_8 = np.mean([rms_8a,rms_8b])
ylist.append(rms_8*1000)

#calculate rms for 16obs sample
infile = "16_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_16 = np.nanstd(wsqr[1000:1100,1000:1100])
ylist.append(rms_16*1000)

#calculate rms for 32obs sample
infile = "32_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_32 = np.nanstd(wsqr[1000:1100,1000:1100])
ylist.append(rms_32*1000)

#calculate rms for 64obs (complete) sample
infile = "64_weighted_stack-1500.fits"
whdu = fits.open(infile)
wsqr = whdu[0].data
rms_64 = np.nanstd(wsqr[1000:1100,1000:1100])
ylist.append(rms_64*1000)

ylist = np.array(ylist)

m,c = np.polyfit(np.log(xlist),np.log(ylist),1)
yfit = np.e**(m*np.log(xlist) + c)

area_correc = 1 / np.sqrt(2015)   # see num_beams.py
fold_correc = 1 / np.sqrt(20150)  # 10 usable alpha-CRRLs
phase3_correc = 0.375 / np.sqrt(20150) # decrease due to MWA Phase III and better observation date

m1,c1 = np.polyfit(np.log(xlist),np.log(ylist*area_correc),1)
areafit = np.e**(m*np.log(xlist) + c1)

m2,c2 = np.polyfit(np.log(xlist),np.log(ylist*fold_correc),1)
foldfit = np.e**(m*np.log(xlist) + c2)

m3,c3 = np.polyfit(np.log(xlist),np.log(ylist*phase3_correc),1)
phase3fit = np.e**(m3*np.log(xlist) + c3)

pt1 = (np.log(xlist[-1]),np.log(foldfit[-1]))
xdist = (np.log(0.07)-pt1[1]) / m
pt2 = (pt1[0]+xdist,np.log(0.07))
print("Detection expected after",np.e**pt2[0],"hours")

pt3 = (np.log(xlist[-1]),np.log(phase3fit[-1]))
xdist2 = (np.log(0.07)-pt3[1]) / m
pt4 = (pt3[0]+xdist2,np.log(0.07))
print("Detection expected after",np.e**pt4[0],"hours with MWA Phase III")

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.plot(xlist,ylist,'C0o')
ax.plot(xlist,yfit,'C0',label = 'Noise - All freqencies, 1 pixel')
ax.plot(xlist,areafit,'C1', label = 'Noise - All freqencies, 1 square degree')
ax.plot(xlist,foldfit,'C2', label = 'Noise - All frequencies, 1 square degree, RRLs stacked')
ax.plot(xlist,phase3fit, 'C5', label = 'Noise - MWA Phase III')
ax.plot([np.e**(pt1[0]),np.e**(pt2[0])],[np.e**(pt1[1]),np.e**(pt2[1])],'C2--')
ax.plot([np.e**(pt3[0]),np.e**(pt4[0])],[np.e**(pt3[1]),np.e**(pt4[1])],'C5--')
ax.plot([0.05,1000],[0.35,0.35],'C3--',label='Expected RRL brightness')
ax.plot([0.05,1000],[0.07,0.07],'C4--',label='Expected 5 sigma detection')
ax.plot([xlist[-1],xlist[-1]],[0.01,2000],'k')
ax.set_xscale('log')
ax.set_xlabel("Integration time (hours)")
ax.set_xlim([0.05,1000])
ax.set_yscale('log')
ax.set_ylabel("Flux density (mJy/beam)")
ax.set_ylim([0.03,1000])
ax.legend()

fig.savefig("noiseplot.pdf", bbox_inches="tight")
fig.savefig("noiseplot.png", bbox_inches="tight")
