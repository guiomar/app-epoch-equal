# Copyright (c) 2021 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# set up environment
import os
import json
import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

# == LOAD DATA ==
# FIF
fname = config['fif']
raw = mne.io.read_raw_fif(fname)

# CTF
# fname = config['ctf']
# raw = mne.io.read_raw_ctf(fname)

# == GET CONFIG VALUES ==
duration = config['duration']

# == EPOCH DATA ==
# Make epohs of equal length
epochs = mne.make_fixed_length_epochs(raw, duration=duration, preload=True)

# == SAVE FILE ==
epochs.save(os.path.join('out_dir','meg-epo.fif'))


# == FIGURES ==
plt.figure(1)
fig_ep = epochs.plot_image()
#for i in range(1,len(fig_ep)):
#    plt.figure(1)
fig_ep[0].savefig(os.path.join('out_figs','epochs_image0.png'))
fig_ep[1].savefig(os.path.join('out_figs','epochs_image1.png'))

img0 = matplotlib.image.imread(os.path.join('out_figs','epochs_image0.png'))
img1 = matplotlib.image.imread(os.path.join('out_figs','epochs_image1.png'))
new_image = np.hstack((img0, img1))
matplotlib.image.imsave('epochs_image.png', new_image)


plt.figure(2)
epochs.plot_drop_log()
plt.savefig(os.path.join('out_figs','epochs_drop.png'))

plt.figure(3)
epochs.plot()
plt.savefig(os.path.join('out_figs','epochs_plot.png'))

plt.figure(4)
epochs.plot_psd()
plt.savefig(os.path.join('out_figs','epochs_psd.png'))






