# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# Required libraries
# pip install mne-bids coloredlogs tqdm pandas scikit-learn json_tricks fire

# set up environment
#import mne-study-template
import os
import json
import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
#Make epohs of equal length
epochs = mne.make_fixed_length_epochs(raw, duration=duration, preload=True)

# == SAVE FILE ==
epochs.save(os.path.join('out_dir','meg-epo.fif'))


# == FIGURES ==
plt.figure(1)
fig_ep = epochs.plot_image()
plt.savefig(os.path.join('out_figs','epochs_image.png'))

plt.figure(2)
epochs.plot_drop_log()
plt.savefig(os.path.join('out_figs','epochs_drop.png'))

plt.figure(3)
epochs.plot()
plt.savefig(os.path.join('out_figs','epochs_plot.png'))

plt.figure(4)
epochs.plot_psd()
plt.savefig(os.path.join('out_figs','epochs_psd.png'))






