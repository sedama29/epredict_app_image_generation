import folium
import pandas as pd
import json

# Load the data
df = pd.read_csv('C:/ePredictor/epredictor_csv/beaches.csv')

# Create a map centered on the average latitude and longitude of the data
latitude = df['latitude'].mean()
longitude = df['longitude'].mean()
m = folium.Map(location=[latitude, longitude], zoom_start=7, tiles=None)

# Add base map layers
folium.raster_layers.TileLayer(tiles='openstreetmap', name='Street Map').add_to(m)

# Load geojson for state lines
with open('C:/wamp64/www/map_enterococcus_2/data/state_lines.json') as f:
    geojson_data = json.load(f)

# Add state lines
folium.GeoJson(
    geojson_data,
    style_function=lambda feature: {
        'fillColor': '#00000000',
        'color': 'black',
        'weight': 1,
    }).add_to(m)

# Add markers for Texas Beach Watch Sites
tile_layer = folium.FeatureGroup(name='Texas Beach Watch Sites').add_to(m)

marker_list = []  # Collect marker references to manage popups
for index, row in df.iterrows():
    marker = folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(row['site_name'], max_width=300),
        tooltip=row['site_name'],
        radius=3,
        color='red',
        fill=True,
        fill_opacity=1
    ).add_to(tile_layer)
    marker_list.append(marker)

# Add layer control

# Custom JavaScript to open all popups automatically
js = """
<script>
    function toggleTooltips(map) {
        map.eachLayer(function(layer) {
            if (layer instanceof L.CircleMarker && layer.getTooltip && layer._tooltip) {
                if (map.getZoom() > 5) {
                    layer._tooltip.options.permanent = true;
                    layer.openTooltip();
                } else {
                    layer._tooltip.options.permanent = false;
                    layer.closeTooltip();
                }
            }
        });
    }

    var map = document.getElementsByClassName('folium-map')[0].__map;
    map.on('zoomend', function() {
        toggleTooltips(map);
    });

    // Initial check
    setTimeout(() => toggleTooltips(map), 1000);
</script>
"""
m.get_root().html.add_child(folium.Element(js))


# Inject JavaScript into the map

# Save the map
m.save("index_2.html")
