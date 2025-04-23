# Calcium Imaging Workshop 


### Meeting notes

8 Notebooks as Demos + 2 Demos:
D1:
Spike Inference
Discrete Spike Trace Extraction
Raw Calcium Trace Extraction (Single Cell)
Neuropil Subtracted value *rolling averages
D2:
Napari Intro
Multi-Cell ROI Selection
Cell Segmentation with scikit-image
cell segmaentation with scikit-image (local peaks, binary_opening/binary_closing, bounding boxes, ROI QC metrics)
splitting/merging rois


Notebook 2: Spike times in Neo format and some plots
----------------
Scientific Questions
What camera parameters can be changed to affect sampling timing /spatial resolutions
https://www.nature.com/articles/s41467-017-01031-3
What innvovations/techniques are there for calicum sensors, how do they influence quality of the recordings?
What can't you do with calcium-inferred spikes?  What can you do? 
How slow is calcium decay time? And how does it affect inferred spikes? (latest)
Effect of camera (pixel recordings from top to bottom and left to right) on spike timings of different neurons. (calcium imaging uses global shutter)
One-photon vs two-photon vs gCAMP: what can be seen/not-seen with each of them? How does the data processing differ from one method to another and why? 
What type of cell are we seeing? Based on morpological features like size, shape (structural roi vs signal roi)
What needs to be done to make statements about a cell's morphological features (structure)? Taking images at multi-plane? How thin should the slicing be?
How does calcium imaging setup look like? What are the main parameters/considerations while making recordings? How does it vary 2p, 1p, and gCAMP?
What processes in the cell are we actually detecting in calcium imaging, and what does/doesn't it tell us about the cell's behavior?
Raster plot or PSTHs of all the neurons to have some analysis component.


Calcium Imaging technique
https://www.youtube.com/watch?v=ABeO79_BxwQ
https://www.youtube.com/watch?v=kay3hlHzaLA

Voltage Imaging video
https://www.youtube.com/watch?v=_KIhQZ2-p_o

Softare
Cascade Spike Inference: https://github.com/HelmchenLabSoftware/Cascade
OASIS Spike Deconvolution Paper: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005423 https://github.com/j-friedrich/OASIS
Simulators
Calcium trace simulator: https://github.com/j-friedrich/OASIS/blob/master/examples/Demo.ipynb
2-photon Microscopy Simulator (NAOMi): https://pillowlab.princeton.edu/pubs/Song2021naomi_JNmethods.pdf
https://bitbucket.org/adamshch/naomi_sim/src/master/

## Announcement

### Calcium Imaging Analysis in Python
  - **When**: April 7th-9th, 2025 @ 9:30 - 17:00 CET
  - **Format**: Hands-On Workshop (>50% Small-Group Exercises)
  - **Length**: 18 Hours
  - **Location**: Online (Zoom link will be provided upon registration)
  - **Registration**: TBA


How do I extract calcium traces from images, and how do I analyze them? In this workshop, we cover the essential concepts needed to answer these questions using Python tools like NumPy, SciPy, and Napari. We will explore how to convert continuous calcium traces into neural spikes through deconvolution, extract fluorescence estimates from Region(s) of Interest selected manually and automatically, and improve these estimates by removing contributions from the surrounding neuropil. Participants will work with real calcium imaging data to apply the above tools and methods.  

#### Topics
  - Calcium Traces to Spikes: Extracting flourescence estimates from images and converting them to spikes through `numpy` and `scipy`. 
  - Region(s) of Interest: Manual and automated method for selecting ROIs. 
  - Motion Correction: Correcting movement artifacts in recorded imaging data with `scikit-image` and `suite2p`.   

#### Prerequisites
- **Affiliation**: Researchers and Students from all universities are welcome.  
- **Background**: 
    - Familiar with Topics Covered in: [Essential Computer Tools for Researchers](TBA) 
    - Familiar with Topics Covered in: [Intro to Python for Scientists](TBA)
    - Completely New to Python?  Just take all three courses together as a five-day mega workshop! 
- **Software**: 
  - Windows, Mac, or Linux Computer
  - Zoom Desktop Client
  - Visual Studio Code: https://code.visualstudio.com/download
  - Conda (recommended through installing Miniforge): https://conda-forge.org/download
  - Git: https://git-scm.com/downloads
- **Accounts**:
  - GitHub: https://github.com/
  - (Optional) Sciebo: https://hochschulcloud.nrw/

#### Certification
  - Students who attend at least 75% of the course will receive a participation certificate by email at the end of the course.

---

## Internal Details

### Science Demo
1. Assuming you have calcium traces, what processing is still required to extract spike times? Why is it required? 
2. How do I obtain calcium imaging data? What exactly am I looking at when I see the raw images? 
3. What do I need to do to extract calcium traces from these raw images? Why do I need to do them?  

### Important Code Demos 
1. Manual and automated ROI extraction (Napari and scikit-image/numpy)
2. Motion correction with scikit-image
3. Convolution and Deconvolution 
4. OASIS algorithm (`oasis`) 

---
## Day 1: Flourescence Traces -> Calcium-Inferred Spikes -> Spike Analysis (Raster Plots, PSTH)

  # Working with Flourescence time series and Spike discrtete timestamps
  1. 1 Pixel over time -> Fluorescence Signal: plot, indexing/slicing, (2 Pixels over Time), dF, baseline estimation,  dF/F0 Normalization, 
  2. How to store/load timestamped event data, how to do various basic spike analyses (rasterplot, psth, spike rate, etc)
  # Spike Extraction Analysis Techniques
  1. Spike detection through deconvolution (what is convolution, what is OASIS, thrresholding oasis outputs, saving timestamped data)
  2. Spike detection through machine learning (what is CASCADE, thrresholding oasis outputs, saving timestamped data)
  
  

## Day 2 : Image Data -> Flourescence Traces
### Unit: From Single-Cell Images to Calcium Traces

  1. Working with Image Data / 3D Arrays: Multi-Pixel Data Extraction to 1D Calcium Trace
     - `numpy`: Thresholding & Fancy Indexing for Non-Rectangular ROIs  
     - `numpy`: Averaging: Multiple Pixels to Single Value  
     - `numpy` / `scipy.stats`: Weighted Averaging, Non-Parametric Aggregations  
  2. Napari GUI from the Notebook: Selecting Data and Labeling Images,  Working with Image-Labelled Data for Extraction
     - Napari Installation  
     - Manual ROI Selection: Napari Labeling in Notebooks  
     - `napari.Viewer.view_image()`: Napari Image Layer  
     - `napari.Viewer.labels['labels']`: Napari Labels Laye
     - - `rgb2hsv`  
     - Fancy Indexing  
     - Loop-indexing: Getting a 2D Array of Averaged ROI Traces
     - Save selections
     - 

### Automated ROI selection
   3. Numpy + Sikit-image 
   4. Pipeline review: Suite2p GUI


## Day 3: Image Stacks -> Images / Convenient Pipelines

1. **(Added now)** Motion Correction
   
   - `skimage.registration`: Rigid  
   - `skimage.registration`: Non-Rigid 
   - - `suite2p`: Motion correction metrics

2. **(Added now)** The Suite2P Python API
3. Extracting / Working with Suite2P Outputs
   
    

