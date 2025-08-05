import streamlit as st

def render_metrics(filtered_df):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Total Units",
            value=len(filtered_df)
        )
    with col2:
        avg_prc = filtered_df['aprs_prc'].mean() if not filtered_df.empty else 0
        st.metric(
            label="Average Price",
            value=f"฿{avg_prc:,.0f}"
        )
    with col3:
        prc_range_max = filtered_df['aprs_prc'].max() / 1000000 if not filtered_df.empty else 0
        prc_range_min = filtered_df['aprs_prc'].min() / 1000000 if not filtered_df.empty else 0
        st.metric(
            label="prc Range",
            value=f"฿{prc_range_min:,.1f} - {prc_range_max:,.1f} M"
        )
