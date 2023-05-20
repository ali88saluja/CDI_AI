import pytest
from Procedure.ReadCsv import ReadCsv

class TestReadCsv(object):
    # Given
    file_path = "./Raw/20230419-MCDI10min-single.csv"
    read_csv = ReadCsv(file_path)

    def test_run(self):
        # When
        self.read_csv.run()
        # Then
        assert self.read_csv.raw_data.at[0, 'Date / Time'] == "2023/4/19 ?? 04:35:09"
        assert self.read_csv.raw_data.at[0, 'pH Value'] == "6.51 pH"
        assert self.read_csv.raw_data.at[0, 'Conductivity Value'] == "1994 uS/cm"
