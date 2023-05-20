import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from Config import Config

class DataPreprocessing:
    def __init__(self, starcom_data=None, current_data=None, setting=None):
        self.starcom_data = starcom_data
        self.current_data = current_data
        if setting:
            self.cycle = setting.cycle
            self.starcom_data_interval = setting.starcom_data_interval
            self.current_data_interval = setting.current_data_interval
            self.voltage = setting.voltage
            self.save_as = setting.save_as

    def set_df(self):
        df_preprocessing = pd.DataFrame()
        data_num = len(self.starcom_data.index)

        df_preprocessing['Time'] = pd.to_datetime([t * 3 for t in range(0, data_num)], unit='s').strftime('%H:%M:%S')
        # 暫訂進流 = 出流
        df_preprocessing['Conductivity_in'] = [float(EC.split(' ')[0]) for EC in self.starcom_data['Conductivity Value']]
        df_preprocessing['Conductivity_out'] = df_preprocessing['Conductivity_in'].copy()
        # 暫訂進流 = 出流
        df_preprocessing['pH_in'] = [float(pH.split(' ')[0]) for pH in self.starcom_data['pH Value']]
        df_preprocessing['pH_out'] = df_preprocessing['pH_in'].copy()

        df_preprocessing['Current'] = np.concatenate([self.current_data[f'Current_{i+1}'] for i in range(self.cycle*2)])
        df_preprocessing['Voltage'] = [self.voltage] * data_num
        return df_preprocessing
    
    def plot_figure(self):
        pass

    def run(self, verbose=False):
        self.df_preprocessing = self.set_df()
        self.df_preprocessing.to_csv(f"./Data/{self.save_as}", index=False)
        if verbose:
            print(f"preprocessing data save as: ./Data/{self.save_as}")
