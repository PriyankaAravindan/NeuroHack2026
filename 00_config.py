import os, numpy as np

PROJECT_DIR = '.'
DATA_DIR = os.path.join(PROJECT_DIR, 'eeg_data', 'Oddball')
CHECKPOINT_DIR = os.path.join(PROJECT_DIR, 'checkpoints')
RESULTS_DIR = os.path.join(PROJECT_DIR, 'results')
os.makedirs(CHECKPOINT_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ICA
ICA_HIGHPASS = 1.0
ICA_RESAMPLE = 250
ICA_MAX_ITER = 1000
ICA_RANDOM_STATE = 42
EOG_THRESHOLD = 3.0
TOPO_RATIO = 2.5
MIN_VOTES = 2

# single filter path
ERP_HIGHPASS = 0.1
ERP_LOWPASS = 30.0

# epochs
EPOCH_TMIN = -0.200
EPOCH_TMAX = 0.700
BASELINE = (None, 0)
DROP_CHANNELS = ['HEOG']

# ERP components
ERP_COMPONENTS = {
    'N170': {'tmin': 0.130, 'tmax': 0.200, 'channels': ['P7','P8','PO9','PO10'], 'polarity': 'negative'},
    'VPP':  {'tmin': 0.130, 'tmax': 0.200, 'channels': ['Cz','Fz','FC1','FC2'], 'polarity': 'positive'},
    'P300': {'tmin': 0.250, 'tmax': 0.500, 'channels': ['Pz','CP1','CP2','Cz'], 'polarity': 'positive'},
}
ERP_WINDOWS = [(0.130, 0.200), (0.250, 0.500)]
N_POSITIONS = 6

# classification
CLASS_WEIGHT = {1: 5.0, 0: 1.0}

# checkpoint paths
CKPT = {
    'epochs':      os.path.join(CHECKPOINT_DIR, 'epochs'),
    'ica_summary': os.path.join(CHECKPOINT_DIR, 'ica_summary.npz'),
    'erp_results': os.path.join(CHECKPOINT_DIR, 'erp_results.npz'),
    'clf_data':    os.path.join(CHECKPOINT_DIR, 'classification_data.npz'),
    'subjects':    os.path.join(CHECKPOINT_DIR, 'subjects.npy'),
}

def result_path(key):
    return os.path.join(RESULTS_DIR, f'result_{key}.npz')
