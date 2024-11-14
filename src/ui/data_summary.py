import streamlit as st
from typing import Tuple, List

def initialize_session_state():
    """
    Initialize session state variables if they don't exist.
    """
    if 'selected_index' not in st.session_state:
        st.session_state.selected_index = 0
    if 'num_rows' not in st.session_state:
        st.session_state.num_rows = 10
    if 'show_summary' not in st.session_state:
        st.session_state.show_summary = False

def data_summary_section(st, data_objects: List) -> Tuple[int, int, bool]:
    """
    Display a summary of the loaded data files, allowing the user to select a file,
    control the number of rows displayed, and show/hide the summary.

    Args:
        st: The Streamlit module.
        data_objects: List of DataObject instances.

    Returns:
        Tuple containing the selected index, number of rows to display, and whether to show the summary.
    """
    st.header("Summary of Loaded Data")
    
    # Initialize session state variables
    initialize_session_state()

    # Dropdown to select a file
    file_selection = st.selectbox(
        "Select a file to view:",
        [f"Data File {i+1}" for i in range(len(data_objects))],
        index=st.session_state.selected_index,
        key="file_selection"
    )
    st.session_state.selected_index = int(file_selection.split()[-1]) - 1

    # Number input to select number of rows to display
    num_rows = st.number_input(
        "Number of rows to display:",
        min_value=5,
        max_value=100,
        value=st.session_state.num_rows,
        step=5,
        key="num_rows"
    )
    st.session_state.num_rows = num_rows

    # Checkbox to show/hide data summary
    show_summary = st.checkbox(
        'Show Data Summary',
        value=st.session_state.show_summary,
        key="show_summary_checkbox"
    )
    st.session_state.show_summary = show_summary

    # Conditional display
    if st.session_state.show_summary:
        data_object = data_objects[st.session_state.selected_index]
        st.subheader(f"Data File {st.session_state.selected_index + 1}")
        st.write(f"File Source: {data_object.file_sources[st.session_state.selected_index]}")
        st.write(f"Number of Rows: {data_object.data_frames[st.session_state.selected_index].shape[0]}")
        st.write(f"Number of Columns: {data_object.data_frames[st.session_state.selected_index].shape[1]}")
        st.write("Preview of Data:")
        st.write(data_object.data_frames[st.session_state.selected_index].head(st.session_state.num_rows))

    return st.session_state.selected_index, st.session_state.num_rows, st.session_state.show_summary
