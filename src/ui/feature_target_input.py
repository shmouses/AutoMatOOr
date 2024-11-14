import streamlit as st
from typing import Tuple, List, Dict

def feature_target_input_section(input_container) -> Tuple[List[str], str, Dict[str, str], Dict[str, Dict[str, float]]]:
    """
    Collect user inputs for feature and target columns, data types, and constraints.

    Args:
        input_container: The Streamlit container (sidebar or main) for inputs.

    Returns:
        Tuple containing features, target, data types, and constraints.
    """
    input_container.header("Step 2: Provide Feature and Target Information")
    features = input_container.text_area("List of feature columns (comma-separated):", key="features").split(',')
    target = input_container.text_input("Target column:", key="target")

    data_types = {}
    for i, feature in enumerate(features):
        data_type = input_container.selectbox(f"Data type for {feature}:", ["categorical", "int", "float", "series"], key=f"data_type_{i}")
        data_types[feature] = data_type
    # Ensure the key for the target is unique
    if target:
        data_types[target] = input_container.selectbox(f"Data type for {target}:", ["categorical", "int", "float", "series"], key="data_type_target")

    constraints = {}
    for i, feature in enumerate(features):
        min_value = input_container.number_input(f"Minimum value for {feature}:", value=0.0, key=f"min_value_{i}")
        max_value = input_container.number_input(f"Maximum value for {feature}:", value=1.0, key=f"max_value_{i}")
        constraints[feature] = {'min': min_value, 'max': max_value}

    return features, target, data_types, constraints
