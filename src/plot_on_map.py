import folium
import json

def plot(geojson_file, save_path="./output/elibrary-deployments-map.html"):
    with open(geojson_file) as f:
        geojson_data = json.load(f)

    # Create a base map
    m = folium.Map(location=[27.7, 85.3], zoom_start=7) 

    # Define a color mapping function
    def get_color(type_value):
        color_map = {
            "operational": "green",
            "not-operational": "red",
        }
        return color_map.get(type_value, "gray") 

    # Iterate through features in GeoJSON
    for feature in geojson_data["features"]:
        coordinates = feature["geometry"]["coordinates"][::-1]  # Reverse to (lat, lon)
        properties = feature["properties"]
        
        # Extract properties
        site_name = properties.get("site", "N/A")
        funded_by = properties.get("funded_by", "N/A")
        date_of_deployment = properties.get("date", "N/A")
        location_name = properties.get("location", "N/A")
        no_of_computers = properties.get("no_of_computers", "N/A")
        type_value = properties.get("type", "operational")
        
        popup_content = (
                f"<b>Site:</b> {site_name}<br>"
                f"<b>Deployed on:</b> {date_of_deployment}<br>"
                f"<b>Location:</b> {location_name}<br>"
                f"<b>No of computers:</b> {no_of_computers}<br>"
                f"<a href='#'>View Details</a><br>" # add link to deployment page/report/photos
            )
        
        popup = folium.Popup(popup_content, max_width=250)
        # Add marker with popup
        folium.Marker(
            location=coordinates,
            popup=popup,
            icon=folium.Icon(color=get_color(type_value)),
        ).add_to(m)
    m.save(save_path)
    return save_path


if __name__ == "__main__":
    # Load GeoJSON file
    geojson_file = "./output.geojson"
    plot(geojson_file)
    
    