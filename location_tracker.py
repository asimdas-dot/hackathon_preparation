import requests
import webbrowser

# Replace with your Google API Key
API_KEY = "YOUR_GOOGLE_API_KEY"

def get_location(api_key):
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    try:
        # Make a POST request to the Geolocation API
        response = requests.post(url, json={})
        if response.status_code == 200:
            location = response.json().get("location")
            if location:
                latitude = location.get("lat")
                longitude = location.get("lng")
                print(f"Latitude: {latitude}, Longitude: {longitude}")
                return latitude, longitude
        print("Failed to fetch location:", response.json())
    except Exception as e:
        print("Error:", e)

def open_in_google_maps(lat, lng):
    url = f"https://www.google.com/maps?q={lat},{lng}"
    webbrowser.open(url)

if __name__ == "__main__":
    print("Fetching location...")
    lat_lng = get_location(API_KEY)
    if lat_lng:
        print("Opening location in Google Maps...")
        open_in_google_maps(*lat_lng)

##if asim in found(asim is on way )
no longar eval globals 