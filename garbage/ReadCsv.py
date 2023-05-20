import os, sys
import pandas as pd

class ReadCsv:
    def __init__(self, file_path):
        self.path = file_path

    def run(self, verbose=False):
        self.raw_data = pd.read_csv(self.path)
        if verbose:
            print(self.raw_data.info())