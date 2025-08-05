import streamlit as st

def render_filters(df):
    st.sidebar.header("Filters")

    # Property type filter
    property_types = df['pty_tp'].unique().tolist()
    selected_property_types = st.sidebar.multiselect(
        "Select Property Types",
        options=property_types,
        default=None
    )
    mask_pty_tp = df['pty_tp'].isin(selected_property_types)

    # Project name filter
    project_names = df[mask_pty_tp]['hs_nm'].unique().tolist()
    selected_projects = st.sidebar.multiselect(
        "Select Projects",
        options=project_names,
        default=None,
        max_selections=1
    )
    mask_prj_nm = df['hs_nm'].isin(selected_projects)

    # Combine masks
    mask = mask_pty_tp & mask_prj_nm
    filtered_df = df[mask].copy()

    return filtered_df, selected_property_types, selected_projects
