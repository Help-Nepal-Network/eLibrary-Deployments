import csv
import json
import pandas as pd

def csv2geojson(csv_file, geojson_file):
    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }

    # Read the CSV file and populate the GeoJSON structure
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
        # Extract coordinates and convert to float
            try:
                gps = row['GPS'].split(', ')
                coordinates = [float(gps[1]), float(gps[0])]
            except (KeyError, IndexError, ValueError):
                coordinates = [0.0, 0.0]  # Default to (0, 0) if GPS is invalid or missing
            
            # Create a GeoJSON feature
            feature = {
                "type": "Feature",
                "properties": {
                    "site": row.get('Site', 'N/A') or ('N/A'),
                    "date": row.get('Date', 'N/A') or ('N/A'),
                    "location": row.get('Location', 'N/A') or ('N/A'),
                    "funded_by": row.get('Funded By', 'N/A') or ('N/A'),
                    "number_of_computers": row.get('Number of computers', 'N/A') or ('N/A'),
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": coordinates
                }
            }
            
            # Append feature to the GeoJSON structure
            geojson_data["features"].append(feature)

    # Write the GeoJSON data to a file
    with open(geojson_file, 'w', encoding='utf-8') as file:
        json.dump(geojson_data, file, indent=4)

    print(f"GeoJSON file has been created: {geojson_file}")
    return geojson_file



def csv2htmltable(csv_file, columns_to_include, save_path, markdown_path=''):
    df = pd.read_csv(csv_file, usecols=columns_to_include)
    
    # Save markdown table to a file
    if markdown_path != '':
        markdown_table = df.to_markdown(index=False)
        with open(markdown_path, 'w') as markdown_file:
            markdown_file.write(markdown_table)

    html_table = df.to_html(index=False)
    with open(save_path, 'w') as markdown_file:
        markdown_file.write(html_table)
    
    return save_path