import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from extract import extract
from load import load

extract()
load()