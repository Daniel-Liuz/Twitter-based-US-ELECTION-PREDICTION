import plotly.graph_objects as go
import pandas as pd

# 数据
data = {
    "State Full Name": [
        "Indiana", "Florida", "North Carolina", "Alabama", "Massachusetts",
        "Rhode Island", "Arizona", "New York", "Idaho", "Utah", "Kentucky",
        "Georgia", "Connecticut", "Michigan", "South Dakota", "Kansas",
        "Colorado", "North Dakota", "Iowa", "Hawaii", "New Hampshire",
        "West Virginia", "Delaware", "Mississippi", "Tennessee", "Oklahoma",
        "Louisiana", "Wisconsin", "Montana", "Alaska", "South Carolina",
        "Ohio", "Washington, D.C.", "Missouri", "Texas", "Maine",
        "Minnesota", "Wyoming", "Nevada", "California", "Vermont",
        "Virginia", "Illinois", "New Jersey", "Maryland", "Pennsylvania",
        "Arkansas", "Nebraska", "New Mexico", "Oregon", "Washington"
    ],
    "Trump Votes": [
        1711713, 6109443, 2878108, 1457704, 1234783, 213021, 1574244, 3443683,
        605041, 757608, 1336227, 2661056, 731164, 2804647, 272081, 741949,
        1336921, 245943, 926653, 193169, 360031, 524191, 212546, 655094,
        1961784, 1035219, 1208233, 1689033, 220356, 141470, 1453690, 3116406,
        18669, 1675165, 6325710, 269391, 1509590, 189885, 716986, 3652701,
        119013, 1932008, 2328956, 1841876, 917443, 3336263, 750035, 358391,
        409295, 659963, 1019146
    ],
    "Harris Votes": [
        1158650, 4680748, 2688797, 769391, 2072304, 282110, 1389309, 4353005,
        274838, 487924, 700920, 2544281, 986573, 2724029, 146859, 532475,
        1682347, 111966, 706556, 312384, 383369, 208517, 285368, 404063,
        1048303, 499043, 766405, 1657714, 145534, 102969, 1014531, 2479475,
        255899, 1214456, 4734933, 322848, 1651013, 72199, 668793, 5390140,
        235371, 2143998, 2741392, 2030554, 1465766, 3112383, 391610, 265780,
        453706, 863315, 1527827
    ]
}

# 州全名与缩写映射
state_abbrev = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
    "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
    "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
    "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
    "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
    "Wisconsin": "WI", "Wyoming": "WY", "Washington, D.C.": "DC"
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 添加州缩写列
df["State Abbrev"] = df["State Full Name"].map(state_abbrev)

# 调试输出：检查映射是否成功
print("DataFrame Head:")
print(df.head())

# 设置统一的颜色刻度范围
zmin = 0
zmax = 7000000  # 根据最大票数设置上限

# 绘制 Trump Votes 热力图
fig_trump = go.Figure(
    data=go.Choropleth(
        locations=df["State Abbrev"],  # 使用州缩写
        locationmode="USA-states",
        z=df["Trump Votes"],
        text=df["State Full Name"],
        colorscale="Reds",
        colorbar_title="Trump Votes",
        zmin=zmin,
        zmax=zmax
    )
)

fig_trump.update_layout(
    title_text="Trump Votes Distribution by State",
    geo=dict(
        scope="usa",
        projection=go.layout.geo.Projection(type="albers usa"),
        showlakes=True,
        lakecolor="rgb(255, 255, 255)"
    )
)

# 显示 Trump Votes 热力图
print("Displaying Trump Votes Heatmap...")
fig_trump.show()

# 绘制 Harris Votes 热力图
fig_harris = go.Figure(
    data=go.Choropleth(
        locations=df["State Abbrev"],  # 使用州缩写
        locationmode="USA-states",
        z=df["Harris Votes"],
        text=df["State Full Name"],
        colorscale="Reds",
        colorbar_title="Harris Votes",
        zmin=zmin,
        zmax=zmax
    )
)

fig_harris.update_layout(
    title_text="Harris Votes Distribution by State",
    geo=dict(
        scope="usa",
        projection=go.layout.geo.Projection(type="albers usa"),
        showlakes=True,
        lakecolor="rgb(255, 255, 255)"
    )
)

# 显示 Harris Votes 热力图
print("Displaying Harris Votes Heatmap...")
fig_harris.show()
