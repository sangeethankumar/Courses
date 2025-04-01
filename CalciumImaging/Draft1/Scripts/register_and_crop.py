import numpy as np
import tifffile
from skimage.registration import phase_cross_correlation
from scipy.ndimage import fourier_shift, center_of_mass
import matplotlib.pyplot as plt
import os

# ---- Load Data ----
input_path = "demoMovie.tif"  # path to your file
stack = tifffile.imread(input_path)

# ---- Image Registration ----
reference_image = stack[0].astype(np.float32)
registered_stack = np.zeros_like(stack)

for i in range(stack.shape[0]):
    shift, _, _ = phase_cross_correlation(reference_image, stack[i], upsample_factor=10)
    shifted_fft = np.fft.fftn(stack[i])
    shifted_image = np.fft.ifftn(fourier_shift(shifted_fft, shift)).real
    registered_stack[i] = shifted_image.astype(stack.dtype)

# ---- Detect Cell in Bottom Quarter ----
mean_proj = np.mean(registered_stack[:100], axis=0)  # optional: use first 100 frames
height, width = mean_proj.shape
bottom_quarter = mean_proj[height * 3 // 4:, :]
local_max_idx = np.unravel_index(np.argmax(bottom_quarter), bottom_quarter.shape)
local_y = local_max_idx[0] + height * 3 // 4
local_x = local_max_idx[1]

# ---- Manual Region (override based on visual inspection) ----
y_start, y_end = 45, height         # Y range (adjust as needed)
x_start, x_end = 40, 60             # X range

# ---- Crop and Save ----
cropped_200 = registered_stack[:200, y_start:y_end, x_start:x_end]
cropped_500 = registered_stack[:500, y_start:y_end, x_start:x_end]
cropped_all = registered_stack[:, y_start:y_end, x_start:x_end]

# ---- Output Paths ----
os.makedirs("output", exist_ok=True)
tifffile.imwrite("output/cropped_bottom_neuron_200frames.tif", cropped_200)
tifffile.imwrite("output/cropped_bottom_neuron_500frames.tif", cropped_500)
tifffile.imwrite("output/cropped_bottom_neuron_allframes.tif", cropped_all)

print("Saved all cropped stacks successfully!")
