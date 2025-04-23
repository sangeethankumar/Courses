### Formula to choose window size for baseline estimation from moving median window:

$\text{Window size} = \text{frame rate} \times \text{event length in seconds} \times \text{safety factor}$

- **Frame rate**: how many frames your recording has per second (like 30 fps)
- **Event length**: how long a typical calcium spike lasts (like 2 seconds)
- **Safety factor**: how much bigger the window should be to fully cover the event (usually between **1.5 and 3**)
