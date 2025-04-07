
import numpy as np
import tifffile as tiff
from scipy.ndimage import binary_dilation, generate_binary_structure
from skimage.draw import disk
import matplotlib.pyplot as plt

# Load TIFF stack and compute average image
tif_path = "cropped_bottom_neuron_2000frames.tif"  # Update if path differs
img_stack = tiff.imread(tif_path)
avg_img = img_stack.mean(axis=0)

# Define cell center manually (e.g., center of image) and small radius
center_y, center_x = avg_img.shape[0] // 2, avg_img.shape[1] // 2
soma_radius = 3

# Create cell mask
cell_mask = np.zeros(avg_img.shape, dtype=bool)
rr, cc = disk((center_y, center_x), soma_radius, shape=avg_img.shape)
cell_mask[rr, cc] = True

# Create neuropil mask as a thin annulus around the cell
gap_pixels = 1
thickness_pixels = 3

inner_dilated = binary_dilation(cell_mask, structure=generate_binary_structure(2, 1), iterations=gap_pixels + 1)
outer_dilated = binary_dilation(inner_dilated, structure=generate_binary_structure(2, 1), iterations=thickness_pixels)
neuropil_mask = outer_dilated & ~inner_dilated

# Save masks
np.save("cell_mask_small.npy", cell_mask)
np.save("neuropil_mask_thin_annulus.npy", neuropil_mask)

# Optional visualization
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(avg_img, cmap='gray')
axs[0].set_title("Original Avg Image")
axs[1].imshow(avg_img, cmap='gray')
axs[1].imshow(cell_mask, alpha=0.5, cmap='Reds')
axs[1].set_title("Cell Mask")
axs[2].imshow(avg_img, cmap='gray')
axs[2].imshow(neuropil_mask, alpha=0.5, cmap='Blues')
axs[2].imshow(cell_mask, alpha=0.5, cmap='Reds')
axs[2].set_title("Neuropil Mask (Annular)")
for ax in axs:
    ax.axis('off')
plt.tight_layout()
plt.show()
