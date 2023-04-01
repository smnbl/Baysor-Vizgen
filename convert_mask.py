#!/usr/bin/env python3

import numpy as np
import skimage
import sys

# USAGE: ./convert.py masks.npy masks.tiff

mask = np.load(sys.argv[1])
skimage.io.imsave(sys.argv[2], mask.astype(np.uint16))

