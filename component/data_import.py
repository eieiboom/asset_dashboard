import streamlit as st
import pandas as pd
import ast
from config import D_DTYPE, D_RENAME

@st.cache_data
def load_main_data():
    df = pd.read_csv('data/npa_datatool_20250630.csv', usecols=D_DTYPE.keys(), dtype=D_DTYPE)
    
    # Rename columns for easier use
    df_fn = (
        df
        .copy()
        .rename(columns=D_RENAME)
    )
    df_fn['pty_tp'] = df_fn['pty_tp'].str.strip().str.split(' ').str[-1]
    if 'closest' in df.columns:
        df_fn['closest'] = df['closest'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    df_out = df_fn.copy()

    return df_out

@st.cache_data
def load_confidence_criteria():
    data = {
        'confidence_type': ['H1', 'H2', 'M1', 'M2', 'M3', 'L'],
        'Same village': [True, True, False, False, False, False],
        'Distance (Metro)': ['10 km', '10 km', '3 km', '3 km', '3 km', '3 km'],
        'Distance (non Metro)': ['10 km', '10 km', '10 km', '10 km', '10 km', '10 km'],
        'Land Area': ['<= 10 sq.wah', '-', '<= 10 sq.wah', '<= 10 sq.wah', '<= 30 sq.wah', '<= 100 sq.wah'],
        'Usable Area': ['<= 20 sq.m', '-', '<= 20 sq.m', '-', '-', '-']
    }
    
    return pd.DataFrame(data)

@st.cache_data
def load_map_html():
    """
    Load the HTML file containing the map.
    """
    try:
        with open("data/npa_datatool_map_20250630.html", "r", encoding="utf-8") as f:
            map_html = f.read()
        return map_html
    except FileNotFoundError:
        st.error("Map HTML file not found. Please ensure 'map.html' exists in the project directory.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the map: {str(e)}")
        return None
