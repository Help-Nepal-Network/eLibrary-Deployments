import os
from src.converter import csv2geojson
from src.converter import csv2htmltable
from src.plot_on_map import plot
import config as cfg


columns_to_include = ['Site', 'Location', 'Date', 'Funded By', 'Number of computers']

if not os.path.exists(cfg.output_dir):
    print(f"creating output directory: {cfg.output_dir}")
    os.makedirs(cfg.output_dir)


geojson  = csv2geojson(cfg.csv_file, cfg.geojson_file)
map_html = plot(geojson, save_path=cfg.geojson_html)

deployment_table = csv2htmltable(cfg.csv_file, columns_to_include, cfg.deployment_html)

with open(cfg.index_file, "r") as index:
    index_content = index.read()

with open(deployment_table, "r") as table:
    table_content = table.read()

with open(cfg.general_info, "r") as info:
    info_content = info.read()

with open(cfg.geojson_html, "r") as data:
    geojson_content = data.read()

# Inject table content into the index file
output_content = index_content.replace("<!-- ADD INFORMATIONS -->", info_content)
output_content = output_content.replace("<!-- INSERT TABLE HERE -->", table_content)
output_content = output_content.replace("<!-- DEPLOYMENT MAP -->", geojson_content)

with open(cfg.output_file, "w") as output:
    output.write(output_content)

print(f"Static HTML file generated: {cfg.output_file}")
