import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from component.data_import import load_main_data, load_confidence_criteria, load_map_html
from component.filters import render_filters
from component.metrics import render_metrics
from component.histogram import render_histogram
from component.confidence import render_confidence_criteria

# Page config
st.set_page_config(
    page_title="Real Estate Dashboard",
    page_icon="🏠",
    layout="wide"
)

# Title
st.title("🏠 Klabs Asset Dashboard")
st.markdown("---")

# Load the data
try:
    df = load_main_data()
    df_cs = load_confidence_criteria()
    map_html = load_map_html()
    
    # Use filters component
    filtered_df, selected_property_types, selected_projects = render_filters(df)

    # row1
    # Use metrics component
    st.markdown("#### Main Asset")
    render_metrics(filtered_df)
    st.markdown("---")

    # row2
    st.markdown("#### Neighbor Assets")
    col4, col5 = st.columns(2, vertical_alignment='center')
    # Use histogram component
    render_histogram(filtered_df=filtered_df, col=col4)
    
    # Use confidence criteria component
    confidence_type = filtered_df['confidence_type'].values[0] if not filtered_df.empty else None
    render_confidence_criteria(df_cs=df_cs, col=col5, confidence_type=confidence_type)
    st.markdown("---")

    # row3
    st.markdown("#### Map")
    if map_html:
        st.components.v1.html(map_html, height=600, scrolling=True)
    else:
        st.error("Map data is not available.")

except FileNotFoundError:
    st.error("Data file not found. Please make sure 'data/npa_datatool_20250630.csv' exists in the project directory.")
except Exception as e:
    st.error(f"An error occurred while loading the data: {str(e)}")
