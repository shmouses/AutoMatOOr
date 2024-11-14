1. DataObject Class:

Attributes:

data_frames: List of data frames.
data_category: Category of data (time-series or time-independent).
file_sources: List of source files.
features: List of feature columns.
target: Target column.
data_types: Dictionary mapping columns to their data types (categorical, int, float, etc.).
constraints: Dictionary mapping columns to their constraints.
agg_dataframe: A single dataframe containing all the data from data_frames.

Methods:

__init__(self, data_frames, data_category, file_sources): Initialize with data frames, data category, and file sources.
add_data_frame(self, data_frame, file_source): Add a data frame and its source file to the object.
set_features(self, features): Set feature columns.
set_target(self, target): Set target column.
set_data_types(self, data_types): Set data types for features and target.
set_constraints(self, constraints): Set constraints for features.
create_agg_dataframe(self): Combine all data frames into a single dataframe.

2. DataLoader Class:

Attributes:

folder_path: Path to the folder containing data files.
file_type: Type of files (csv, xlsx, json).
files: List of file paths.
data_objects: List of DataObject instances.

Methods:

__init__(self, folder_path, file_type): Initialize with folder path and file type.
load_files(self): Load data files based on the file type and store them in data_objects.
sort_files_by_timestamp(self): Sort the files based on timestamps in filenames.

3. DataCurator Class:

Attributes:

data_objects: List of DataObject instances to be curated.
curated_data: Curated DataObject.

Methods:

__init__(self, data_objects): Initialize with data objects.
unify_data(self): Unify or restore data from multiple sources.
stitch_data(self): Stitch data together for single and time series data.
handle_missing_data(self): Handle missing data (imputation, augmentation, correction, replacement).