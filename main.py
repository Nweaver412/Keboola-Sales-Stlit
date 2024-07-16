import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(layout="wide", page_title="Financial Dashboard")

st.title("Financial Dashboard")
left_column, right_column = st.columns([3, 2])

# ------------------------------------------------------------
# LEFT COLUMN
# ------------------------------------------------------------
with left_column:
    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Gross Profit", "4.9M", "1.7%")
    col2.metric("Cost", "3.8M", "-4.1%")
    col3.metric("Revenue", "8.8M", "0.5%")
    col4.metric("Gross Margin %", "56.4%", "-0.9%")

    CHART_HEIGHT = 400

    tablecol_left_column, left_1_column, left_2_column, left_3_column, left_4_column = st.columns([2, 1, 1, 1, 1])

    with tablecol_left_column:
        st.subheader("AC 1, PY, PL by Business/Unit")
        
        df = pd.DataFrame({
            'Business/Unit': ['Personal care', 'Hair Care Eu', 'Hair Care RoW', 'Electronics', 'Desktop PC', 'Monitors', 'Accessories'],
            'AC 1': [3.5, 0.52, 0.56, 1.39, 0.13, 0.23, 0.31],
            'PL': [3.64, 0.55, 0.59, 1.24, 0.25, 0.29, 0.41],
            'PY': [3.6, 0.73, 0.69, 3.23, 0.16, 0.25, 0.20]
        })
        custom_css = f"""
        <style>
            .stTable {{
                height: {CHART_HEIGHT}px;
                overflow-y: auto;
            }}
            .stTable thead {{
                position: sticky;
                top: 0;
                background-color: white;
            }}
            .stTable tbody {{
                overflow-y: auto;
            }}
            thead tr th:first-child {{display:none}}
            tbody th {{display:none}}
            .stTable td {{
                font-size: 0.9em;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: 150px;
            }}
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)
        st.table(df)

    with left_1_column:
        df['%var'] = ((df['AC 1'] - df['PY']) / df['PY']) * 100

        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=[f"{i}" for i in range(len(df))],
            x=df['%var'],
            orientation='h',
            textposition='outside',
            marker_color=['red' if x < 0 else 'green' for x in df['%var']],
        ))

        fig.update_layout(
            title='ΔPY',
            plot_bgcolor='lightgray', 
            xaxis_title='Value',
            yaxis_title='',
            height=CHART_HEIGHT,  # Use the same height as the table
            margin=dict(l=0, r=20, t=30, b=0),
            xaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='Gray'),
            yaxis=dict(showticklabels=False),
        )

        st.plotly_chart(fig, use_container_width=True)

    with left_2_column:
            df['%var'] = ((df['AC 1'] - df['PY']) / df['PY']) * 100

            fig = go.Figure()
            fig.add_trace(go.Bar(
                y=[f"{i}" for i in range(len(df))],
                x=df['%var'],
                orientation='h',
                textposition='outside',
                marker_color=['red' if x < 0 else 'green' for x in df['%var']],
            ))

            fig.update_layout(
                plot_bgcolor='lightgray', 
                title='ΔPL',
                xaxis_title='Value',
                yaxis_title='',
                height=CHART_HEIGHT,  # Use the same height as the table
                margin=dict(l=0, r=20, t=30, b=0),
                xaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='Gray'),
                yaxis=dict(showticklabels=False),
            )

            st.plotly_chart(fig, use_container_width=True)


    with left_3_column:
            df['%var'] = ((df['AC 1'] - df['PY']) / df['PY']) * 100

            fig = go.Figure()
            fig.add_trace(go.Bar(
                y=[f"{i}" for i in range(len(df))],
                x=df['%var'],
                orientation='h',
                textposition='outside',
                marker_color=['red' if x < 0 else 'green' for x in df['%var']],
            ))

            fig.update_layout(
                title='ΔPY%',
                xaxis_title='Value',
                yaxis_title='',
                height=CHART_HEIGHT,  # Use the same height as the table
                margin=dict(l=0, r=20, t=30, b=0),
                xaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='Gray'),
                yaxis=dict(showticklabels=False),
            )

            st.plotly_chart(fig, use_container_width=True)

    with left_4_column:
            df['%var'] = ((df['AC 1'] - df['PY']) / df['PY']) * 100

            fig = go.Figure()
            fig.add_trace(go.Bar(
                y=[f"{i}" for i in range(len(df))],
                x=df['%var'],
                orientation='h',
                textposition='outside',
                marker_color=['red' if x < 0 else 'green' for x in df['%var']],
            ))

            fig.update_layout(
                title='ΔPL%',
                xaxis_title='Value',
                yaxis_title='',
                height=CHART_HEIGHT,  # Use the same height as the table
                margin=dict(l=0, r=20, t=30, b=0),
                xaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='Gray'),
                yaxis=dict(showticklabels=False),
            )

            st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------
# RIGHT COLUMN
# ------------------------------------------------------------

with right_column:
    st.subheader("AC and PL by Month")
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
    pl_values = [7.8, -0.8, 3.8, -2.8, -4.0, 7.5, -0.6, 0.0, 0.6, 13.5, -2.5]
    py_values = [18.1, -24.2, 23.0, -22.9, -3.9, -9.9, -4.4, -21.6, 32.3, 6.2, 16.8]

    fig_acpl = go.Figure()

    fig_acpl.add_trace(go.Bar(
        x=months,
        y=pl_values,
        name='ΔPL',
        marker_color=['green' if v >= 0 else 'red' for v in pl_values],
        text=[f"{v:+.1f}%" for v in pl_values],
        textposition='outside'
    ))

    fig_acpl.add_trace(go.Bar(
        x=months,
        y=py_values,
        name='ΔPY',
        marker_color=['green' if v >= 0 else 'red' for v in py_values],
        text=[f"{v:+.1f}%" for v in py_values],
        textposition='outside'
    ))

    fig_acpl.update_layout(
        barmode='group',
        title="AC and PL by Month",
        xaxis_title="Month",
        yaxis_title="Percentage",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode="x unified"
    )

    fig_acpl.add_shape(
        type="line",
        x0=months[0],
        y0=0,
        x1=months[-1],
        y1=0,
        line=dict(color="black", width=1, dash="dot"),
    )

    st.plotly_chart(fig_acpl, use_container_width=True)

    st.markdown("---")

    st.subheader("Financial Performance")
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    values = [643.5, 666.1, 808.5, 588.6, 564.6, 595.4, 945.3, 1134.0, -18.2]

    fig_financial = go.Figure()

    fig_financial.add_trace(go.Bar(
        x=months[:len(values)],
        y=values,
        marker_color='gray',
        text=[f"{v:.1f}K" if v >= 0 else f"{v:.1f}K" for v in values],
        textposition='outside'
    ))

    st.plotly_chart(fig_financial, use_container_width=True)