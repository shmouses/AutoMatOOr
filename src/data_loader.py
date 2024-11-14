import pandas as pd
import os
from data_object import DataObject

class DataLoader:
    def __init__(self, folder_path, file_type, data_category, features, target, data_types, constraints):
        self.folder_path = folder_path
        self.file_type = file_type
        self.data_category = data_category
        self.features = features
        self.target = target
        self.data_types = data_types
        self.constraints = constraints
        self.files = []
        self.data_objects = []

    def load_files(self):
        data_frames = []
        for file in self.files:
            try:
                # Detect file type based on extension
                if file.endswith('.csv'):
                    data_frame = pd.read_csv(file)
                elif file.endswith('.xlsx') or file.endswith('.xls'):
                    data_frame = pd.read_excel(file, engine='openpyxl')  # Specify the engine explicitly
                elif file.endswith('.json'):
                    data_frame = pd.read_json(file)
                else:
                    raise ValueError(f"Unsupported file format: {file}")
                data_frames.append(data_frame)
            except Exception as e:
                print(f"Error loading file {file}: {e}")
                continue
        
        if data_frames:
            data_object = DataObject(data_frames, self.data_category, self.files, self.features, self.target, self.data_types, self.constraints)
            self.data_objects.append(data_object)

    def sort_files_by_timestamp(self):
        self.files.sort(key=lambda x: os.path.getmtime(x))
