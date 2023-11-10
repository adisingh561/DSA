import geopandas as gpd
from shapely.geometry import Point

# Load the OSM network shapefile
osm_network = gpd.read_file('DSA/office/TVM_FINAL_SHAPE/TVM_FINAL_SHAPE.shp')

# Convert the list of GPS points to a GeoDataFrame
gps_data = [
    {"latitude": 8.69431, "longitude": 76.8187, "system_code_number": "865006046990777", "timestamp": "2023-11-03 00:00:00"},
    {"latitude": 8.69431, "longitude": 76.8187, "system_code_number": "865006046990777", "timestamp": "2023-11-03 00:03:00"},
    {"latitude": 8.69431, "longitude": 76.8187, "system_code_number": "865006046990777", "timestamp": "2023-11-03 00:06:00"}
]

gps_gdf = gpd.GeoDataFrame(gps_data, geometry=gpd.points_from_xy([point["longitude"] for point in gps_data], [point["latitude"] for point in gps_data]))

# Create a spatial index for efficient spatial operations
osm_sindex = osm_network.sindex

# Function to find the nearest edge to a GPS point
def find_nearest_edge(gps_point, osm_network, osm_sindex):
    # Find the index of the nearest edge using the spatial index
    nearest_edge_index = list(osm_sindex.nearest(gps_point.geometry.bounds, 1))[0]
    
    # Get the nearest edge from the OSM network
    nearest_edge = osm_network.iloc[nearest_edge_index]
    
    return nearest_edge

# Iterate through each GPS point and find the nearest edge
for index, gps_point in gps_gdf.iterrows():
    nearest_edge = find_nearest_edge(gps_point, osm_network, osm_sindex)
    
    # Do something with the nearest edge, e.g., print its information
    print(f"GPS Point {index + 1} is closest to OSM Edge:")
    print(nearest_edge)
    print('\n')
