import pandas as pd

class DataObject:
    def __init__(self, data_frames, data_category, file_sources, features=None, target=None, data_types=None, constraints=None):
        self.data_frames = data_frames if isinstance(data_frames, list) else [data_frames]
        self.data_category = data_category
        self.file_sources = file_sources if isinstance(file_sources, list) else [file_sources]
        self.features = features or []
        self.target = target
        self.data_types = data_types or {}
        self.constraints = constraints or {}
        self.agg_dataframe = None

    def add_data_frame(self, data_frame, file_source):
        self.data_frames.append(data_frame)
        self.file_sources.append(file_source)

    def create_agg_dataframe(self):
        self.agg_dataframe = pd.concat(self.data_frames, ignore_index=True)
