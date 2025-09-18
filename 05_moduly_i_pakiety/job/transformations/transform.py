class Deduplicator:
    def transform(self, df):
        return df[["Imię"]].drop_duplicates()