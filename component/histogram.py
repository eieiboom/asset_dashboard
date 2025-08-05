import streamlit as st
import plotly.express as px

def render_histogram(filtered_df, col):
    with col:
        flat_closest = filtered_df['closest'].explode()
        fig = px.histogram(flat_closest, x=flat_closest, title=f"Histogram of Neighbors Prices ({filtered_df['confidence_type'].values[0] if not filtered_df.empty else ''} confidence)")

        vline_value = filtered_df['aprs_prc'].mean() if not filtered_df.empty else None
        if vline_value:
            fig.add_vline(
                x=vline_value,
                line_dash="dash",
                line_color="red",
                annotation_text=f"Avg Price: {vline_value}",
                annotation_position="top"
            )

        fig.update_xaxes(title="Neighbors")
        fig.update_yaxes(title="Count")
        st.plotly_chart(fig, use_container_width=True)
