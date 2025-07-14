import altair as alt
import pandas as pd

# read data from a CSV file
# url = 'https://raw.githubusercontent.com/altair-viz/altair/master/examples/data/seattle-weather.csv'
# weather_data = pd.read_csv(url)

url = 'https://gist.githubusercontent.com/officeofjane/2c3ed88c4be050d92765de912d71b7c4/raw/8abc5e19a5fac2ec63e81891d9bfdebe2d55f92c/publication-grids.csv'
df = pd.read_csv(url)

# filter the data to include only New York Times 2
df = df[df['publication'] == 'New York Times 2']

heatmap = alt.Chart(df).mark_rect(stroke=None, cornerRadius=5).encode(
    x=alt.X('col:O', axis=None),
    y=alt.Y('row:O', axis=None),
    color='id:Q'
)

text = heatmap.mark_text(baseline='middle', align='center', fill='black', fontSize=14).encode(
    text='code:O'
)

chart = (heatmap + text).properties(width=350, height=250).configure_view(strokeOpacity=0)

# display the chart
chart