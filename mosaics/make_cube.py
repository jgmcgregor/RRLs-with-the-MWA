#!/usr/bin/env python

''' make a cube out of a bunch of fits files '''

import sys
from glob import glob
from astropy.io import fits
import numpy as np

prefix = sys.argv[1]
files = glob(prefix+"-????.fits")
files = sorted(files)

for ind, f in enumerate(files):
    hdu = fits.open(f)
    if ind == 0:
        cube = hdu[0].data.copy()
        cube.resize([len(files),hdu[0].data.shape[0],hdu[0].data.shape[1]])
#        cube.resize([len(files),hdu[0].data.shape[2],hdu[0].data.shape[3]])
    else:
        cube[ind,:,:] = hdu[0].data
#        cube[ind,:,:] = np.squeeze(hdu[0].data)
    hdu.close()

hdu = fits.open(files[0])
try:
    crval3 = hdu[0].header["FREQ"]
except KeyError:
    crval3 = hdu[0].header["CRVAL3"]
hdu[0].data = cube

# Fill in third axis details

hdu[0].header["CTYPE3"] = "FREQ"
hdu[0].header["CRPIX3"] = 1.0
hdu[0].header["CRVAL3"] = crval3
hdu[0].header["CDELT3"] = 10.e3
hdu[0].header["CUNIT3"] = "Hz"

hdu.writeto("cube.fits")
