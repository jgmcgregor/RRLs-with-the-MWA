import numpy as np
import astropy.units as u


# centre channel 169
deg_per_pixel_side = 0.6/169.*u.degree
deg2_per_pixel = deg_per_pixel_side**2
pix_required = np.sqrt((1*u.degree**2)/deg2_per_pixel)
# pix_required shows that we need a 282x282 pixel box to cover 1 square degree

area = deg2_per_pixel * 282**2
# this area should be approx 1 square degree

bmaj = 0.02317*u.degree
bmin = 0.01895*u.degree

solid_angle = (np.pi*bmaj*bmin) / (4*np.log(2))

nbeams = area/solid_angle

nbeams = nbeams.decompose()
print("There will be",nbeams,"beams in 1 square degree for centre channel 169")

pix_per_beam = solid_angle / deg2_per_pixel


# centre channel 121
deg_per_pixel_side = 0.6/121.*u.degree
deg2_per_pixel = deg_per_pixel_side**2
pix_required = np.sqrt((1*u.degree**2)/deg2_per_pixel)
# pix_required shows that we need a 202x202 pixel box to cover 1 square degree

area = deg2_per_pixel * 202**2
# this area should be approx 1 square degree

bmaj = 0.03302*u.degree
bmin = 0.02650*u.degree

solid_angle = (np.pi*bmaj*bmin) / (4*np.log(2))

nbeams = area/solid_angle

nbeams = nbeams.decompose()
print("There will be",nbeams,"beams in 1 square degree for centre channel 121")

pix_per_beam = solid_angle / deg2_per_pixel


# centre channel 69
deg_per_pixel_side = 0.6/69.*u.degree
deg2_per_pixel = deg_per_pixel_side**2
pix_required = np.sqrt((1*u.degree**2)/deg2_per_pixel)
# pix_required shows that we need a 115x115 pixel box to cover 1 square degree

area = deg2_per_pixel * 115**2
# this area should be approx 1 square degree

bmaj = 0.05705*u.degree
bmin = 0.04734*u.degree

solid_angle = (np.pi*bmaj*bmin) / (4*np.log(2))

nbeams = area/solid_angle

nbeams = nbeams.decompose()
print("There will be",nbeams,"beams in 1 square degree for centre channel 121")

pix_per_beam = solid_angle / deg2_per_pixel

