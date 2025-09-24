from geopy.geocoders import Nominatim
from geopy.distance import geodesic #install geopy in a virtual environment


#The Emission rates for each mode of transport (in kg CO2 per km)
#I asked chatGPT to help me with these values
EMISSION_RATES = {
    "car": 0.192,
    "bus": 0.105,
    "train": 0.041,
    "bike": 0.0,
    "plane": 0.255
}

def main():
    print("Let's plan your eco-friendly trip!")
    current_location = input("Enter your current location: ")
    destination = input("Enter your travel destination: ")
    travel_mode = input("Enter your preferred mode of travel (e.g., train, bus, bike): ")
    accommodation_type = input("Enter your preferred accommodation type (e.g., eco-lodge, hostel, hotel): ")

    dist = distance(current_location, destination)
    print(distance(current_location, destination))
    print("Estimated CO2 emissions for your trip: ", calculate_emissions(dist[1], travel_mode), "kg CO2")
    eco_activities =""


def calculate_emissions(distance_km, travel_mode):
    
    rate = EMISSION_RATES.get(travel_mode.lower())
    if rate is None:
        print("Unknown travel mode. Please choose from car, bus, train, bike, or plane.")
    return distance_km * rate
def distance(current_location, destination):
    
    geolocator = Nominatim(user_agent="sustainable_travel_planner")
    loc1 = geolocator.geocode(current_location)
    loc2 = geolocator.geocode(destination)

    coor1 = (loc1.latitude, loc1.longitude)
    coor2 = (loc2.latitude, loc2.longitude)
    return ("Distance: ", geodesic(coor1, coor2).km, "km") #function of geopy that returns the distance between two coordinates


if __name__ == "__main__":
    main()
