import streamlit as st
from ui.data_input import data_input_section
from ui.feature_target_input import feature_target_input_section
from ui.data_summary import data_summary_section
from data_loader import DataLoader
from data_curator import DataCurator
from data_object import DataObject
import os

# Set the page title and icon
st.set_page_config(page_title="Materials Process Optimizer", page_icon=":rocket:")

# Display the logo
st.image("logo.png", use_container_width=True)

# Title and description
st.title("Welcome to the Materials Process Optimizer")
st.write("Please provide the necessary information to proceed.")

# Option to use sidebar
use_sidebar = st.checkbox("Use Sidebar for Navigation", value=True)

if use_sidebar:
    input_container = st.sidebar
else:
    input_container = st

# Step 1: User inputs
folder_path, file_type, num_files, file_option, file_names, uploaded_files = data_input_section(input_container)

# Initialize data_loader variable
data_loader = None

# Step 2: Submit and process data
if input_container.button("Submit"):
    st.write("Data submitted successfully!")

    # Create a directory for uploaded files if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Load the data
    data_loader = DataLoader(
        folder_path=folder_path,
        file_type=file_type,
        data_category='time-series',  # Adjust based on your context
        features=[],  # Empty for now; will be set later
        target='',  # Empty for now; will be set later
        data_types={},  # Empty for now; will be set later
        constraints={}  # Empty for now; will be set later
    )

    if num_files == "Single":
        if file_option == "Specify file name":
            data_loader.files = [folder_path + '/' + file_names[0]]
        elif file_option == "Upload file":
            for uploaded_file in uploaded_files:
                file_path = os.path.join(folder_path, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                data_loader.files.append(file_path)
    else:
        if file_option == "Specify file names":
            data_loader.files = [folder_path + '/' + fname for fname in file_names]
        elif file_option == "Upload files":
            for uploaded_file in uploaded_files:
                file_path = os.path.join(folder_path, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                data_loader.files.append(file_path)

    data_loader.load_files()

    # Curate the data
    data_objects = data_loader.data_objects
    curator = DataCurator(data_objects)
    curator.unify_data()
    curator.stitch_data()
    curator.handle_missing_data()

    st.write("Data loading and curation completed successfully!")

    # Show summary of loaded data
    selected_index, num_rows, show_summary = data_summary_section(st, data_objects)

# Step 3: Feature and target information
features, target, data_types, constraints = feature_target_input_section(input_container)

# Ensure data_loader is not None before updating it
if data_loader:
    # Update DataLoader with feature and target information
    data_loader.features = features
    data_loader.target = target
    data_loader.data_types = data_types
    data_loader.constraints = constraints

    st.write("Feature and target information submitted successfully!")

# Display the file details and a submit button
if file_names or uploaded_files:
    input_container.write(f"Folder path: {folder_path}")
    if file_names:
        input_container.write(f"File names: {', '.join(file_names)}")
    if uploaded_files:
        input_container.write(f"Uploaded files: {', '.join([file.name for file in uploaded_files])}")
else:
    input_container.write("No file uploaded yet.")
