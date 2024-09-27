import os

# Root Route
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# File Route
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DIR = os.path.join(DATA_DIR, 'raw')
NORMALIZE_DIR = os.path.join(DATA_DIR, 'normalized')
CONVERTED_DIR = os.path.join(DATA_DIR, 'converted')