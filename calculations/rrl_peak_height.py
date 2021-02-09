import numpy as np
import astropy.units as u

# Centre Channel 169
opt_depth = 0.0002
haslam_brightness = 1433.
haslam_freq = 408.               # in MHz
bmaj = 0.02317 * 3600.           # in arcsec
bmin = 0.01895 * 3600.
freq = 215.                      # in MHz

T_cont = (freq/haslam_freq)**-2.7 * haslam_brightness
T_line = T_cont * opt_depth

peak = (T_line * (freq/1000)**2 * bmaj * bmin) / 1222

print("Expected RRL brightness for centre channel 169 is:",peak,"mJy/beam")

# Centre Channel 121
opt_depth = 0.0001
haslam_brightness = 1433.
haslam_freq = 408.               # in MHz
bmaj = 0.03302 * 3600.           # in arcsec
bmin = 0.02650 * 3600.
freq = 154.                      # in MHz

T_cont = (freq/haslam_freq)**-2.7 * haslam_brightness
T_line = T_cont * opt_depth

peak = (T_line * (freq/1000)**2 * bmaj * bmin) / 1222

print("Expected RRL brightness for centre channel 121 is:",peak,"mJy/beam")


# Centre Channel 69
opt_depth = 0.00075
haslam_brightness = 1433.
haslam_freq = 408.               # in MHz
bmaj = 0.05705 * 3600.           # in arcsec
bmin = 0.04734 * 3600.
freq = 87.                       # in MHz

T_cont = (freq/haslam_freq)**-2.7 * haslam_brightness
T_line = T_cont * opt_depth

peak = (T_line * (freq/1000)**2 * bmaj * bmin) / 1222

print("Expected RRL brightness for centre channel 69 is:",peak,"mJy/beam")

