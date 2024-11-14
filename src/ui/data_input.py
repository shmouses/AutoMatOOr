import streamlit as st
from typing import Tuple, List

def data_input_section(input_container) -> Tuple[str, str, str, str, List[str], List[st.runtime.uploaded_file_manager.UploadedFile]]:
    """
    Collect user inputs for data file information.

    Args:
        input_container: The Streamlit container (sidebar or main) for inputs.

    Returns:
        Tuple containing folder path, file type, number of files, file option, file names, and uploaded files.
    """
    input_container.header("Step 1: Provide Data Information")
    folder_path = input_container.text_input("Path to the folder containing data files:")
    file_type = input_container.selectbox("Type of files:", ["csv", "xlsx", "json"], key="file_type")
    num_files = input_container.radio("Number of files:", ["Single", "Multiple"], key="num_files")

    file_names = []
    uploaded_files = []
    if num_files == "Single":
        file_option = input_container.radio("Choose file input method:", ["Specify file name", "Upload file"], key="file_option_single")

        if file_option == "Specify file name":
            file_name = input_container.text_input("File name (for single file):", key="single_file_name")
            file_names.append(file_name)
        elif file_option == "Upload file":
            uploaded_file = input_container.file_uploader("Choose a file", type=["csv", "xlsx", "json"], key="single_upload_file")
            if uploaded_file:
                uploaded_files.append(uploaded_file)
    else:
        file_option = input_container.radio("Choose file input method:", ["Specify file names", "Upload files"], key="file_option_multiple")

        if file_option == "Specify file names":
            num_files_specified = input_container.number_input("Number of files to specify:", min_value=1, step=1, key="num_files_specified")
            for i in range(num_files_specified):
                file_name = input_container.text_input(f"File name {i+1}:", key=f"multiple_file_name_{i}")
                file_names.append(file_name)
        elif file_option == "Upload files":
            uploaded_files = input_container.file_uploader("Choose files", type=["csv", "xlsx", "json"], accept_multiple_files=True, key="multiple_upload_files")

    return folder_path, file_type, num_files, file_option, file_names, uploaded_files
