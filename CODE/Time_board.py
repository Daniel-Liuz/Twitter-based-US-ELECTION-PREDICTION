import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# 数据直接嵌入代码
support_data = {
    "Date": [
        "2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01",
        "2024-06-01", "2024-07-01", "2024-08-01", "2024-09-01", "2024-10-01",
        "2024-11-01", "2024-12-01"
    ],
    "Trump_Support": [45.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0, 50.5, 51.0, 51.5],
    "Harris_Support": [47.0, 46.0, 45.5, 45.0, 44.5, 44.0, 43.5, 43.0, 42.5, 42.0, 41.5, 41.0]
}

# 转换为 pandas DataFrame
df = pd.DataFrame(support_data)
df['Date'] = pd.to_datetime(df['Date'])

# 初始化 Dash 应用
app = Dash(__name__)

# 定义布局
app.layout = html.Div([
    html.H1("2024 美国总统选举支持率变化仪表盘"),
    dcc.Graph(id="support-trends-graph"),
    dcc.Slider(
        id="date-slider",
        min=0,
        max=len(df) - 1,
        value=len(df) - 1,
        marks={i: date.strftime('%Y-%m-%d') for i, date in enumerate(df['Date'])},
        step=None
    )
])

# 定义回调函数更新图表
@app.callback(
    Output("support-trends-graph", "figure"),
    Input("date-slider", "value")
)
def update_graph(selected_index):
    # 筛选滑块选择的时间范围
    filtered_df = df.iloc[:selected_index + 1]

    # 添加 Trump 的折线图
    trace_trump_line = go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["Trump_Support"],
        mode="lines+markers",
        name="Donald Trump (Line)",
        line=dict(color="red")
    )

    # 添加 Trump 的柱状图
    trace_trump_bar = go.Bar(
        x=filtered_df["Date"],
        y=filtered_df["Trump_Support"],
        name="Donald Trump (Bar)",
        marker_color="rgba(255, 0, 0, 0.5)"
    )

    # 添加 Harris 的折线图
    trace_harris_line = go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["Harris_Support"],
        mode="lines+markers",
        name="Kamala Harris (Line)",
        line=dict(color="blue")
    )

    # 添加 Harris 的柱状图
    trace_harris_bar = go.Bar(
        x=filtered_df["Date"],
        y=filtered_df["Harris_Support"],
        name="Kamala Harris (Bar)",
        marker_color="rgba(0, 0, 255, 0.5)"
    )

    layout = go.Layout(
        title="支持率变化趋势（折线图+柱状图）",
        xaxis=dict(title="日期"),
        yaxis=dict(title="支持率 (%)"),
        barmode="group",  # 设置柱状图的排列方式（分组排列）
        hovermode="closest"
    )

    return {"data": [trace_trump_line, trace_trump_bar, trace_harris_line, trace_harris_bar], "layout": layout}

# 运行 Dash 应用
if __name__ == "__main__":
    app.run_server(debug=True)
