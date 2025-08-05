import streamlit as st
import pandas as pd
import plotly.express as px
import re

def render_confidence_criteria(df_cs: pd.DataFrame, col: st.columns, confidence_type: str=None):
    """
    Render the confidence criteria table.
    """

    with col:
        # Filter the DataFrame based on the selected confidence type
        if confidence_type:
            filtered_confidence_type = re.sub(r'\d+', '', confidence_type)
            mask = (df_cs['confidence_type'].str.contains(filtered_confidence_type))
            
            df_fn = df_cs[mask].copy().astype(str)
        else:
            df_fn = df_cs.copy().astype(str)

        df_fn = df_fn.set_index('confidence_type').T
        df_fn.index.name = "Confidence Criteria"
        # Display the criteria as a table
        if not df_fn.empty:
            styled_df = df_fn.style.set_properties(**{'text-align': 'center'})
            st.dataframe(styled_df, use_container_width=True)
        else:
            st.dataframe(df_fn, use_container_width=True)

