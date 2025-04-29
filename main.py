import openrouteservice as ors
import time
import requests

API_KEY = "5b3ce3597851110001cf6248e897f958928948808bab68f7fef350b5"

client = ors.Client(key=API_KEY)

def get_eta(origin, destination):

    route = client.directions(
        coordinates=[origin, destination],
        profile='driving-car',
        preference='fastest',
        format='geojson'
    )
    
    time.sleep(1)
    
    eta_seconds = route['features'][0]['properties']['summary']['duration']
    eta_minutes = int(eta_seconds // 60)
    print(f"\n{origin} -> {destination}\nETA: {eta_minutes} minutes")
    return eta_minutes
    
def snap_to_road(coord):
    body = {
        "locations": coord,
        "radius": 0
    }
    
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Authorization': API_KEY,
        'Content-Type': 'application/json; charset=utf-8'
    }
    
    call = requests.post('https://api.openrouteservice.org/v2/snap/driving-car/geojson', json=body, headers=headers)

    print(call.status_code, call.reason)
    print(call.text)

def save_data(data1, data2):
    curr_datetime = None
    filename = '/{}'
    with open(filename, 'a') as file:
        file.write(f"{data1}, {data2}\n")

if __name__ == "__main__":
    site206 = [-122.46156368136903, 47.213503748392256]
    site207 = [-122.46249833281806, 47.21446807353094]
    site208 = [-122.27481709431358, 47.30403424214919]
    # site206_ = snap_to_road(site206)
    # site207_ = snap_to_road(site207)
    # site208_ = snap_to_road(site208)
    eta1 = get_eta(site206, site208)
    eta2 = get_eta(site208, site207)
    # save_data(eta1, eta2)
