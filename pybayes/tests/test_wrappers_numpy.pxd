# wrappers.numpy test needs this file, because in cython wrappers.numpy, there are only
# cdefs, not cpdefs

cimport pybayes.wrappers._numpy as nw
