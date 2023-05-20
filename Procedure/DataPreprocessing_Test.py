import pytest
import pandas as pd

from Config import Config
from Procedure.DataPreprocessing import DataPreprocessing

class TestDataPreprocessing(object):
    # Given
    config_path = "./Config.yaml"
    config = Config(config_path)
    setting = config.set_config()

    starcom_data = pd.read_excel(f"./Raw/{setting.starcom_path}", sheet_name="Preprocessing")
    current_data = pd.read_excel(f"./Raw/{setting.current_path}", sheet_name="Preprocessing")
    preprocessing = DataPreprocessing(starcom_data, current_data, setting)

    def test_set_df(self):
        # When
        df_preprocessing = self.preprocessing.set_df()
        # Then
        assert df_preprocessing.at[0, 'Time'] == '00:00:00'
        assert df_preprocessing.at[0, 'Conductivity_in'] == 1989
        assert df_preprocessing.at[0, 'Conductivity_out'] == 1989
        assert df_preprocessing.at[0, 'pH_in'] == 6.50
        assert df_preprocessing.at[0, 'pH_out'] == 6.50
        assert df_preprocessing.at[0, 'Current'] == 0.2654
        assert df_preprocessing.at[0, 'Voltage'] == 1.2


    def test_removal_efficiency(self):
        # When
        df_removal_efficiency = self.preprocessing.removal_efficiency()
        # Then  
        # assert df_removal_efficiency.at[0, "removal_efficiency"] == 

   