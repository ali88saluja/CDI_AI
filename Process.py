import sys 
import pandas as pd

from Config import Config
from Procedure.DataPreprocessing import DataPreprocessing

class Process:
    def __init__(self, config_path):
        self.config_path = config_path

    def run_procedures(self, verbose=False):
        config = Config(self.config_path)
        self.setting = config.set_config()

        # read starcom & current raw data
        try:
            self.starcom_data = pd.read_excel(f"./Raw/{self.setting.starcom_path}", sheet_name="Preprocessing")
        except:
            print(f"Incorrect starcom path: ./Raw/{self.setting.starcom_path}")  
        try:  
            self.current_data = pd.read_excel(f"./Raw/{self.setting.current_path}", sheet_name="Preprocessing")
        except:
            print(f"Incorrect current path: ./Raw/{self.setting.current_path}")

        # generate the input data
        data_preprocessing = DataPreprocessing(
            self.starcom_data, 
            self.current_data, 
            self.setting
        )
        data_preprocessing.run(verbose=True)

if __name__ == "__main__":
    config_path = "./Config.yaml"
    data_analysis = Process(config_path)
    data_analysis.run_procedures(verbose=True)