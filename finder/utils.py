import requests

def get_location():
    resp = requests.get('http://freegeoip.app/json/')
    geodata = resp.json()
    return geodata['latitude'], geodata['longitude']

def get_barbers(latitude, longitude):
    yelp_api_key = 'dbJGI1ZLSlJTRp5idMBO6w3_eO7BVElXPoym3jSheoeopQUAugdmaK-VXVeFBvGXAGhHTrjV3DRd6bbbPTeLve90b7osiAvdYLCqw7M9YTb4Ch5IkFDEJ0_7oYIdYHYx' 
    headers = {'Authorization': f'Bearer {yelp_api_key}'}
    yelp_response = requests.get(f'https://api.yelp.com/v3/businesses/search?categories=menshair&latitude={latitude}&longitude={longitude}&sort_by=rating', headers=headers)
    return yelp_response.json()
