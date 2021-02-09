#!/usr/bin/env python

# this script allows you to look through one fine channel (in this case, 0279) for bad observations

from glob import glob
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
from astropy.io import fits
import sys

type = 'centre_pix'

if type == 'centre_pix':
   filenames = sorted(glob("128???????_fine-0279-dirty.fits"))
   val = []
   for f in filenames:
      whdu = fits.open(f)
      wcube = whdu[0].data
      wdata = wcube[:,:,1000,1000]
      val.append(wdata[0][0])

   obsids = [float(x[0:10]) for x in filenames]
   
   fig = plt.figure(figsize=(12,3))
   ax = fig.add_subplot(111)
   ax.set_ylabel("Centre pixel value (Jy/beam)")
   xr = range(0, len(obsids))
   ax.scatter(xr, val, color="red", alpha=0.5)
   ax.plot([0,62],[0,0], 'b--')
   ax.xaxis.set_major_formatter(FormatStrFormatter("%10.0f"))
   
   #ax.text(xr[59], val[59], "{0:10.0f}".format(obsids[59]))
   
   fig.savefig("centre_pix.pdf", bbox_inches="tight")
   fig.savefig("centre_pix.png", bbox_inches="tight")
   
if type == 'centre_sqr':
   filenames = sorted(glob("128???????_fine-0279-dirty.fits"))
   val = []
   for f in filenames:
      whdu = fits.open(f)
      wcube = whdu[0].data
      wdata = wcube[:,:,995,1005]
      val.append(np.mean(wdata[0][0]))

   obsids = [float(x[0:10]) for x in filenames]
   
   fig = plt.figure(figsize=(12,3))
   ax = fig.add_subplot(111)
   ax.set_ylabel("Centre pixels value (Jy/beam)")
   xr = range(0, len(obsids))
   ax.scatter(xr, val, color="red", alpha=0.5)
   ax.xaxis.set_major_formatter(FormatStrFormatter("%10.0f"))
   
   fig.savefig("centre_sqr.pdf", bbox_inches="tight")
   fig.savefig("centre_sqr.png", bbox_inches="tight")
   
if type == 'rms_noise':
   filenames = sorted(glob("128???????_fine-0279-dirty_rms.fits"))
   val = []
   for f in filenames:
      whdu = fits.open(f)
      wcube = whdu[0].data
      wdata = wcube[:,:,1000,1000]
      val.append(wdata[0][0])

   obsids = [float(x[0:10]) for x in filenames]
   
   fig = plt.figure(figsize=(12,3))
   ax = fig.add_subplot(111)
   ax.set_ylabel("RMS noise (Jy/beam)")
   xr = range(0, len(obsids))
   ax.scatter(xr, val, color="red", alpha=0.5)
   ax.xaxis.set_major_formatter(FormatStrFormatter("%10.0f"))
   
   #ax.text(xr[40], val[40], "{0:10.0f}".format(obsids[40]))
   
   fig.savefig("rms_noise.pdf", bbox_inches="tight")
   fig.savefig("rms_noise.png", bbox_inches="tight")
   
if type == 'weight':
   filenames = sorted(glob("128???????_fine-0279-dirty_rms2.fits"))
   val = []
   for f in filenames:
      whdu = fits.open(f)
      wcube = whdu[0].data
      wdata = wcube[:,:,1000,1000]
      val.append(wdata[0][0])

   obsids = [float(x[0:10]) for x in filenames]
   
   fig = plt.figure(figsize=(12,3))
   ax = fig.add_subplot(111)
   ax.set_ylabel("RMS noise (Jy/beam)")
   xr = range(0, len(obsids))
   ax.scatter(xr, val, color="red", alpha=0.5)
   ax.plot([0,42],[0,0], 'b--')
   ax.xaxis.set_major_formatter(FormatStrFormatter("%10.0f"))
   
   #ax.text(xr[38], val[38], "{0:10.0f}".format(obsids[38]))
   
   fig.savefig("weight.pdf", bbox_inches="tight")
   fig.savefig("weight.png", bbox_inches="tight")
