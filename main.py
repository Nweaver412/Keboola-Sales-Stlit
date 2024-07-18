import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

# Metric Card CSS
def metric_card(title, value, delta1, delta2):
    delta_color = "lawngreen" if float(delta1.strip('%')) > 0 else "red"
    return f"""
    <div style="
        background-color: white;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 200px;
        width: 100%;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    ">
        <h3 style="margin:0; width:100%; text-align:center; font-size:1.2em;">{title}</h3>
        <div style="font-size: 2.5em; font-weight: bold; margin: 10px 0;">{value}</div>
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: auto;
        ">
            <span style="color: {delta_color};">{delta1}</span>
            <div style="border-left: 1px solid #ccc; height: 20px; margin: 0 10px;"></div>
            <span style="color: {delta_color};">{delta2}</span>
        </div>
    </div>
    """
# Large Structure
left_col, right_col = st.columns([3, 2])

# ------------------------------------------------------------

# LEFT COLUMN

# ------------------------------------------------------------

with left_col:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(metric_card("Gross Profit", "4.9M", "+1.7%", "+17.4K"), unsafe_allow_html=True, )
    with col2:
        st.markdown(metric_card("Cost", "3.8M", "-4.1%", "-162.8K"), unsafe_allow_html=True)
    with col3:
        st.markdown(metric_card("Revenue", "8.8M", "+0.5%", "+180.9K"), unsafe_allow_html=True)
    with col4:
        st.markdown(metric_card("Gross Margin", "56.4%", "-0.9%", "-2.5pp"), unsafe_allow_html=True)

    data = {
    'Business/Unit': ['Personal care', 'Skin Care', 'Tooth Care', 'Hair Care', 'Baby Care', 'Electronics', 'Games', 'TV', 'Desktop PC', 'Monitors', 'Phones', 'Music', 'Books'],
    'AC': [3.5, 57.1, 86.2, 82.8, 2.5, 5.3, 3.1, 6.9, 10.9, 13.1, 12, 4, 5],
    'PL': [3.5, 48.0, 72.1, 87.0, 2.6, 5.2, 3.5, 4.9, 10.6, 16.4, 11.5, 3.9, 4.8],
    'PY': [3.4, 29.6, 48.9, 68.8, 2.3, 5.2, 19.6, 0.0, 29.0, 40.3, 10.3, 3.6, 4.7]
    }

    df = pd.DataFrame(data)

    df['ΔPY'] = df['AC'] - df['PY']
    df['ΔPL'] = df['AC'] - df['PL']
    df['ΔPY%'] = ((df['AC'] - df['PY']) / df['PY'] * 100).round(1)
    df['ΔPL%'] = ((df['AC'] - df['PL']) / df['PL'] * 100).round(1)

    def format_number(num):
        if pd.isna(num):
            return ""
        if abs(num) >= 1e6:
            return f"{num/1e6:.1f}M"
        elif abs(num) >= 1e3:
            return f"{num/1e3:.1f}K"
        else:
            return f"{num:.1f}"

    for col in ['AC', 'PL', 'PY', 'ΔPY', 'ΔPL']:
        df[col] = df[col].apply(format_number)

    df['ΔPY%'] = df['ΔPY%'].apply(lambda x: f"{x:+.1f}%")
    df['ΔPL%'] = df['ΔPL%'].apply(lambda x: f"{x:+.1f}%")

    def safe_float(val):
        if isinstance(val, str):
            return float(val.rstrip('KM%+-'))
        return float(val)

    fig = make_subplots(rows=len(df), cols=4, subplot_titles=['ΔPY', 'ΔPL', 'ΔPY%', 'ΔPL%'],
                    shared_xaxes=True, vertical_spacing=0.03, horizontal_spacing=0.02)

    for i, row in df.iterrows():
        for j, col in enumerate(['ΔPY', 'ΔPL', 'ΔPY%', 'ΔPL%']):
            value = safe_float(row[col])
            color = 'lawngreen' if value >= 0 else 'red'
            fig.add_trace(go.Bar(x=[value], y=[0], orientation='h', marker_color=color, showlegend=False),
                        row=i+1, col=j+1)
            fig.add_annotation(x=value, y=0, text=str(row[col]), showarrow=False, xanchor='left' if value >= 0 else 'right',
                            font=dict(color='black', size=8), row=i+1, col=j+1)

    fig.update_layout(height=500, width=600, margin=dict(l=0, r=0, t=30, b=0))
    fig.update_xaxes(showticklabels=False, showgrid=False, zeroline=False)
    fig.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)
    
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)
    st.markdown("<h2>AC, PY, PL by BusinessUnit, Division</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 4])

    with col1:
        st.table(data)

    with col2:
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------

# RIGHT COLUMN

# ------------------------------------------------------------

with right_col:
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ac_pl_data = [643.5, 566.1, 808.2, 586.6, 564.6, 599.4, 945.3, 1100.0, 400.4, 678.1, 222.2, 809.2]
    delta_pl = [46.6, -6.2, 29.3, -26.0, -4.1, 5.2, 112.5, -28.6, 12.4, -11.3, 2.5, 66.3]
    delta_py = [98.5, -180.9, 151.1, -174.7, -25.3, -29.0, 226.6, 161.0, 10.5, -67.5, -90.3, 110]
    delta_pl_percent = [7.8, -5.8, 3.8, -2.8, -0.6, 0.0, 13.5, -2.5, -4, 5.6, 7.8, 0.0]
    delta_py_percent = [18.1, -24.2, 23.0, -22.9, -3.9, -4.4, 32.3, 16.8, 6.2, -9.9, -21.6, 0.0]

    fig = make_subplots(rows=5, cols=1, shared_xaxes=True, vertical_spacing=0.02,
                        row_heights=[0.15, 0.15, 0.2, 0.2, 0.3])

    fig.add_trace(go.Scatter(x=months, y=delta_pl_percent, mode='markers+lines+text',
                             marker=dict(color=['lawngreen' if x >= 0 else 'red' for x in delta_pl_percent]),
                             text=[f"{x:+.1f}%" for x in delta_pl_percent],
                             textposition="top center"), row=1, col=1)

    fig.add_trace(go.Scatter(x=months, y=delta_py_percent, mode='markers+lines+text',
                             marker=dict(color=['lawngreen' if x >= 0 else 'red' for x in delta_py_percent]),
                             text=[f"{x:+.1f}%" for x in delta_py_percent],
                             textposition="top center"), row=2, col=1)

    fig.add_trace(go.Bar(x=months, y=delta_pl, marker_color=['lawngreen' if x >= 0 else 'red' for x in delta_pl],
                         text=[f"{x:+.1f}K" for x in delta_pl], textposition="outside"), row=3, col=1)

    fig.add_trace(go.Bar(x=months, y=delta_py, marker_color=['lawngreen' if x >= 0 else 'red' for x in delta_py],
                         text=[f"{x:+.1f}K" for x in delta_py], textposition="outside"), row=4, col=1)

    fig.add_trace(go.Bar(x=months, y=ac_pl_data, marker_color='grey',
                         text=[f"{x:.1f}K" for x in ac_pl_data], textposition="outside"), row=5, col=1)

    fig.update_layout(
        title="AC and PL by Month",
        height=800,
        showlegend=False,
        plot_bgcolor='white',
        yaxis=dict(title="ΔPL%", showgrid=False, zeroline=True),
        yaxis2=dict(title="ΔPY%", showgrid=False, zeroline=True),
        yaxis3=dict(title="ΔPL", showgrid=False, zeroline=True),
        yaxis4=dict(title="ΔPY", showgrid=False, zeroline=True),
        yaxis5=dict(title="AC/PL", showgrid=False, zeroline=True),
    )

    fig.update_xaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)    
    