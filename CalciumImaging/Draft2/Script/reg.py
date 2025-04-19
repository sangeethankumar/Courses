from suite2p.run_s2p import run_s2p

ops = {
    'data_path': ['C:/Sangeetha/Course/Courses/CalciumImaging/Draft2/data/'],
    'tiff_list': ['C:/Sangeetha/Course/Courses/CalciumImaging/Draft2/data/data.tif'],
    'save_path0': 'C:/Sangeetha/Course/Courses/CalciumImaging/Draft2/data/suite2p_output/',
    'nplanes': 1,
    'nchannels': 1,
    'functional_chan': 1,
    'nonrigid': True,
    'block_size': [64, 64],
    'do_registration': True,
    'keep_movie_raw': False,
    'delete_bin': False,
    'save_mat': False,
    'reg_tif': True  # Save registered movie as TIFF
}

run_s2p(ops=ops)
