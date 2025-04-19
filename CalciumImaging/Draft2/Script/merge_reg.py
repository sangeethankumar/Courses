import tifffile
import glob
import numpy as np


# Find all registered TIFFs
reg_files = sorted(glob.glob("C:/Sangeetha/Course/Courses/CalciumImaging/Draft2/data/suite2p_output/suite2p/plane0/reg_tif/*.tif"))

# Read and stack all frames
all_frames = []
for file in reg_files:
    frames = tifffile.imread(file)
    all_frames.append(frames)


# Concatenate and save as single TIFF


full_movie = np.concatenate(all_frames, axis=0)
tifffile.imwrite("data_reg.tif", full_movie, bigtiff=True)
