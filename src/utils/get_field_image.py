from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt


api = SentinelAPI('javokhirbek', 'matmex2002', 'https://apihub.copernicus.eu/apihub')

footprint = geojson_to_wkt(read_geojson('C://Users//jenia//PycharmProjects//test_agro//test.geojson'))
products = api.query(footprint)

api.to_geojson(products)
