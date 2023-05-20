import pytest
from Config import Config

class TestConfig(object):
    # Given
    config_path = "./Config.yaml"
    config = Config(config_path)

    def test_set_config(self):
        # When
        setting = self.config.set_config()
        # Then
        assert setting.raw_data == "20230419-MCDI10min-single.csv"
        assert setting.save_as == "20230419-MCDI10min-single_converted.csv"
        assert setting.data_interval == 3