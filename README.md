# RRLs-with-the-MWA
A repository containing all the code I have created or significantly modified for my ICRAR summer project searching for radio recombination lines with the MWA

These scripts were all run after the Murchison Widefield Array (MWA) data had been processed with the GLEAM-X pipeline (https://github.com/tjgalvin/GLEAM-X-pipeline) and the MWA spectral line pipeline (https://github.com/nhurleywalker/MWA-spectral-line-pipeline), with minor modifications made to suit my project. 
This repository includes scripts used to mosaic the processed observations into one cube, and scripts used to create plots used in my final report.

The file 'mosaics' contains scripts used to create the final .fits cubes used in the project. Note that both combine_sgrA.sh and 1chan_combine.sh require the SWarp template to be located in the same directory to work correctly.

The file 'calculations' contains the script used to estimate the brightness of the RRLs investigated in the project, and the script used to determine the number of beams ina square degree for each channel

The file 'channel169plots' contains the python scripts used to create plots for the band centred on channel 169 - plot_spectrum.py, plot_folded_spectrum.py, and plot_expected_decrease.py require the final cubes, black_spot_finderer.py requires all the frequency snapshots from a single observation, and plot_noise.py requires the different-length observations made with 1chan_combine.sh.
The plotting scripts for channels 121 and 69 are just the 169 plotting code with minor modifications, and so aren't included in this repository.
