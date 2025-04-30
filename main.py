import time
import requests
from datetime import datetime as dt
import sys
import os

GOOGLE_API_KEY = "KEY"
PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
    
def get_eta_google(origin, destination):
    origin_str = f"{origin[0]},{origin[1]}"
    destination_str = f"{destination[0]},{destination[1]}"
    departure = int(time.time())
    
    url = (
        f"https://maps.googleapis.com/maps/api/directions/json?"
        f"origin={origin_str}&destination={destination_str}"
        f"&departure_time={departure}&traffic_model=best_guess&key={GOOGLE_API_KEY}"
    )
    
    response = requests.get(url).json()
    
    if response['status'] != 'OK':
        print("Error:", response['status'], response.get('error_message'))
        return None
    
    duration = response['routes'][0]['legs'][0]['duration_in_traffic']['value']
    eta_minutes = duration // 60
    print(f"{origin} -> {destination} ETA: {eta_minutes} minutes")
    return eta_minutes

def save_data(data1, data2):
    curr_date = dt.now().date()
    curr_time = dt.now().strftime("%H:%M:%S")
    print(curr_date, curr_time)
    filename = f"{PATH}/{curr_date}_WA_travel_time.txt"
    with open(filename, 'a') as file:
        file.write(f"{curr_date},{curr_time},{data1},{data2}\n")

if __name__ == "__main__":
    site206 = [47.21389016159856, -122.46404436544215]
    site207 = [47.214403598850936, -122.46249035823517]
    site208 = [47.30709075659674, -122.2721269528852]
    eta1 = get_eta_google(site206, site208)
    eta2 = get_eta_google(site208, site207)
    save_data(eta1, eta2)
    
    # while True:
    #     try:
    #         # site206_ = snap_to_road(site206)
    #         # site207_ = snap_to_road(site207)
    #         # site208_ = snap_to_road(site208)
    #         time.sleep(60) # 1 minute
    #         eta1 = get_eta_google(site206, site208)
    #         eta2 = get_eta_google(site208, site207)
    #         save_data(eta1, eta2)
    #     except KeyboardInterrupt:
    #         print("\nStop program.")
    #         sys.exit(0)
