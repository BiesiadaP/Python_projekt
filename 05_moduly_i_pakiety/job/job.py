from extractors.extract import CsvExtractor2
from loaders.load import JsonLoader
from transformations.transform import Deduplicator

class Job:
    def job(self, input_path, output_path):
      source_data = CsvExtractor2().extract(input_path)
      transformed_data = Deduplicator().transform(source_data)
      JsonLoader().load(transformed_data, output_path)