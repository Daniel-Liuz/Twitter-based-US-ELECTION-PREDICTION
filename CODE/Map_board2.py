import plotly.graph_objects as go
import pandas as pd

# Data
data = {
    'State Full Name': [
        'Indiana', 'Florida', 'North Carolina', 'Alabama', 'Massachusetts',
        'Rhode Island', 'Arizona', 'New York', 'Idaho', 'Utah', 'Kentucky',
        'Georgia', 'Connecticut', 'Michigan', 'South Dakota', 'Kansas',
        'Colorado', 'North Dakota', 'Iowa', 'Hawaii', 'New Hampshire',
        'West Virginia', 'Delaware', 'Mississippi', 'Tennessee', 'Oklahoma',
        'Louisiana', 'Wisconsin', 'Montana', 'Alaska', 'South Carolina',
        'Ohio', 'Washington, D.C.', 'Missouri', 'Texas', 'Maine',
        'Minnesota', 'Wyoming', 'Nevada', 'California', 'Vermont', 'Virginia',
        'Illinois', 'New Jersey', 'Maryland', 'Pennsylvania', 'Arkansas',
        'Nebraska', 'New Mexico', 'Oregon', 'Washington'
    ],
    'Republican Party': [
        0.685783, 0.630126, 0.533967, 0.782115, 0.262013, 0.363128, 0.562161,
        0.384936, 0.828954, 0.706825, 0.784219, 0.522422, 0.354527, 0.514579,
        0.774388, 0.660044, 0.387071, 0.828326, 0.63236, 0.276611, 0.468637,
        0.863382, 0.356809, 0.724405, 0.777882, 0.811434, 0.713083, 0.509357,
        0.696285, 0.653695, 0.672466, 0.612366, 0.005294, 0.655483, 0.640908,
        0.410467, 0.455344, 0.87369, 0.534735, 0.314706, 0.203614, 0.448131,
        0.419192, 0.451392, 0.281489, 0.534676, 0.785786, 0.645178, 0.448675,
        0.368841, 0.307941
    ],
    'Democratic Party': [
        0.314217, 0.369874, 0.466033, 0.217885, 0.737987, 0.636872, 0.437839,
        0.615064, 0.171046, 0.293175, 0.215781, 0.477578, 0.645473, 0.485421,
        0.225612, 0.339956, 0.612929, 0.171674, 0.36764, 0.723389, 0.531363,
        0.136618, 0.643191, 0.275595, 0.222118, 0.188566, 0.286917, 0.490643,
        0.303715, 0.346305, 0.327534, 0.387634, 0.994706, 0.344517, 0.359092,
        0.589533, 0.544656, 0.12631, 0.465265, 0.685294, 0.796386, 0.551869,
        0.580808, 0.548608, 0.718511, 0.465324, 0.214214, 0.354822, 0.551325,
        0.631159, 0.692059
    ],
    'State Abbrev': [
        'IN', 'FL', 'NC', 'AL', 'MA', 'RI', 'AZ', 'NY', 'ID', 'UT', 'KY', 'GA',
        'CT', 'MI', 'SD', 'KS', 'CO', 'ND', 'IA', 'HI', 'NH', 'WV', 'DE', 'MS',
        'TN', 'OK', 'LA', 'WI', 'MT', 'AK', 'SC', 'OH', 'DC', 'MO', 'TX', 'ME',
        'MN', 'WY', 'NV', 'CA', 'VT', 'VA', 'IL', 'NJ', 'MD', 'PA', 'AR', 'NE',
        'NM', 'OR', 'WA'
    ]
}
data = pd.DataFrame(data)

# Updated Color Scheme for Republican Party
fig_republican = go.Figure(
    data=go.Choropleth(
        locations=data["State Abbrev"],  # State Abbreviations
        locationmode="USA-states",
        z=data["Republican Party"],
        text=data["State Full Name"],
        colorscale=[  # Neutral and Nature-like color palette
            [0, "rgb(230, 240, 255)"],  # Light pastel blue
            [0.5, "rgb(120, 150, 200)"],  # Medium blue
            [1, "rgb(40, 70, 140)"]  # Deep blue
        ],
        colorbar_title="Republican Ratio"
    )
)

fig_republican.update_layout(
    title_text="Republican Party Ratio by State",
    geo=dict(
        scope="usa",
        projection=go.layout.geo.Projection(type="albers usa"),
        showlakes=True,
        lakecolor="rgb(255, 255, 255)"
    )
)

fig_republican.show()

# Updated Color Scheme for Democratic Party
fig_democratic = go.Figure(
    data=go.Choropleth(
        locations=data["State Abbrev"],  # State Abbreviations
        locationmode="USA-states",
        z=data["Democratic Party"],
        text=data["State Full Name"],
        colorscale=[  # Neutral and Nature-like color palette
            [0, "rgb(255, 235, 230)"],  # Light pastel red
            [0.5, "rgb(240, 140, 130)"],  # Medium red
            [1, "rgb(180, 50, 40)"]  # Deep red
        ],
        colorbar_title="Democratic Ratio"
    )
)

fig_democratic.update_layout(
    title_text="Democratic Party Ratio by State",
    geo=dict(
        scope="usa",
        projection=go.layout.geo.Projection(type="albers usa"),
        showlakes=True,
        lakecolor="rgb(255, 255, 255)"
    )
)

fig_democratic.show()
