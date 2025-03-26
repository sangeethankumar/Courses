# Calcium Imaging Workshop 

## Announcement

### Calcium Imaging Analysis in Python
  - **When**: April 7th-9th, 2025 @ 9:30 - 17:00 CET
  - **Format**: Hands-On Workshop (>50% Small-Group Exercises)
  - **Length**: 18 Hours
  - **Location**: Online (Zoom link will be provided upon registration)
  - **Registration**: TBA


How do I extract calcium traces from images, and how do I analyze them? In this workshop, we cover the essential concepts needed to answer these questions using Python tools like NumPy, SciPy, and Napari. We will explore how to convert continuous calcium traces into neural spikes through deconvolution, extract fluorescence estimates both manually and automatically, and improve these estimates by removing contributions from the surrounding neuropil. Participants will work with real calcium imaging data to apply the above tools and methods.  

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
## Day 1

### Unit: From Calcium Traces to Spikes
  1. Deconvolution: From a 1D Continuous Signal to Another 1D Continuous Signal
     - `scipy.convolve`: General Convolution  
     - `scipy.convolve`: Calcium Spike Transient Kernel  
     - `scipy.deconvolve`: Calcium Spike Transient Kernel  

  2. Thresholding and Events: Continuous, Regularly-Sampled Data to Categorical, Irregularly Sampled Timestamps   
      - `numpy`: Detecting key values  
      - `numpy`: Extracting Timestamps  
      - **OASIS**: Extracting everything!  
      - `np.diff()`: Firing Rate Plot  

### Unit: From Single-Cell Images to Calcium Traces

  1. Multi-Pixel Data Extraction to 1D Calcium Trace
     - `numpy`: Thresholding  
     - `numpy`: Fancy Indexing for Non-Rectangular ROIs  
     - `numpy`: Averaging: Multiple Pixels to Single Value  
     - `numpy` / `scipy.stats`: Weighted Averaging, Non-Parametric Aggregations  

  2. dF/F0 Normalization: Using the Neuropil to Get Better Cell Fluorescence Estimates
     
     - `numpy`: Transforms (`sub`, `div`)  
     - `scikit-image`  
     - Moving Averages  

## Day 2

### Unit: Manual ROI Selection with Napari

  1. Napari GUI from the Notebook: Labeling Images
     - Manual ROI Selection: Napari Labeling in Notebooks  
     - Napari Installation  
     - `napari.Viewer.view_image()`: Napari Image Layer  
     - `napari.Viewer.labels['labels']`: Napari Labels Layer  

  2. Napari in Notebook: Working with Image-Labelled Data for Extraction
     - `rgb2hsv`  
     - Fancy Indexing  
     - Loop-indexing: Getting a 2D Array of Averaged ROI Traces  

### Unit: Automated ROI Selection     
       - `numpy`  
       - `scikit-image`  

## Day 3

1. **(Added now)** Motion Correction
   
   - `skimage.registration`: Rigid  
   - `skimage.registration`: Non-Rigid 

2. **(Added now)** Motion Correction with Suite2p
   
   - `suite2p`: Motion correction metrics

3. Calcium imaging pipeline with suite2p
   
   - `suite2p`: Motion correction 
   - `suite2p`: ROI Detection  
   - `suite2p`: Trace Extraction  
