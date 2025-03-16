import pandas as pd

class CsvExtractor2:
    def extract(self, path):
        return pd.read_csv(path)