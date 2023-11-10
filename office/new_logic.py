import geopandas as gpd
from shapely.geometry import Point
import datetime
import json
# Load OSM network shapefile
osm_shapefile_path = 'DSA/office/TVM_FINAL_SHAPE/TVM_FINAL_SHAPE.shp'
osm_network = gpd.read_file(osm_shapefile_path)

# Define a function to find the nearest edge
def find_nearest_edge(point, osm_network):
    nearest_edge = osm_network.distance(point.geometry).idxmin()
    return nearest_edge

gps_data_path = 'DSA/office/gps_data.json'
with open(gps_data_path, 'r') as json_file:
    gps_data = json.load(json_file)
# Create a GeoDataFrame from the GPS data
geometry = [Point(data['longitude'], data['latitude']) for data in gps_data['gps_data']]
gps_gdf = gpd.GeoDataFrame(gps_data, geometry=geometry)

# Find the nearest edge for each GPS point
gps_gdf['nearest_edge'] = gps_gdf.apply(lambda row: find_nearest_edge(row, osm_network), axis=1)

# The result is a GeoDataFrame with the nearest edge for each GPS point
with open("DSA/office/output.txt",'w') as f :
    print(gps_gdf[['latitude', 'longitude', 'nearest_edge']],file=f)
