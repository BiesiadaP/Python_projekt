class JsonLoader:
    def load(self, df, path):
        return df.to_json(path, orient="records", index=False, lines=True, force_ascii=False)