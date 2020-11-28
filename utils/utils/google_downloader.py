'''
Very simple download interface to download images from Google's Static Maps API
'''
import requests
class GoogleDownloader:
    def __init__(self, access_token):
        self.access_token = access_token
       # self.url = "https://maps.googleapis.com/maps/api/staticmap?center={},{}&zoom={}&size=400x400&maptype=satellite&key={}"
    
    def download_image(self, lat, long, zoom):
    	# url = "https://maps.googleapis.com/maps/api/staticmap?center=38.441332,-105.234751&zoom=16&size=400x400&maptype=satellite&key=AIzaSyAWWDs8NJOXX0WBdU1BNq0IssbWaLAELnI" 
	res = requests.get('https://maps.googleapis.com/maps/api/staticmap?center=38.441332,-105.234751&zoom=16&size=400x400&maptype=satellite&key=AIzaSyAWWDs8NJOXX0WBdU1BNq0IssbWaLAELnI')        
         #assert res.status_code < 400, print(f'Error - failed to download {lat}, {long}, {zoom}')
        image = plt.imread(BytesIO(res.content))
        return image
    
