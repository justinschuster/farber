import requests

def get_client_ip(request):
    """ Gets the clients ip address. """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location(ip):
    """ Gets the location based on the ip address """
    resp = requests.get('http://freegeoip.app/json/')
    geodata = resp.json()
    return geodata['latitude'], geodata['longitude']

def get_barbers(latitude, longitude):
    """ Returns barbers within 25 miles on latitude and longitude """
    yelp_api_key = 'dbJGI1ZLSlJTRp5idMBO6w3_eO7BVElXPoym3jSheoeopQUAugdmaK-VXVeFBvGXAGhHTrjV3DRd6bbbPTeLve90b7osiAvdYLCqw7M9YTb4Ch5IkFDEJ0_7oYIdYHYx' 
    headers = {'Authorization': f'Bearer {yelp_api_key}'}
    yelp_response = requests.get(f'https://api.yelp.com/v3/businesses/search?categories=menshair&latitude={latitude}&longitude={longitude}&sort_by=rating', headers=headers)
    return yelp_response.json()
