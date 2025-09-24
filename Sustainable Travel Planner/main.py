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
ECO_ACTIVITIES = {
    "planting trees": 0.5,  # kg CO2 offset per tree
    "beach cleanup": 2.0,  # kg CO2 offset per hour
    "wildlife conservation": 1.5,  # kg CO2 offset per hour
    "community gardening": 1.0,  # kg CO2 offset per hour
    "recycling programs": 0.8,  # kg CO2 offset per hour
    "sustainable farming": 1.2  # kg CO2 offset per hour
}

def main():
    print("Let's plan your eco-friendly trip!")
    current_location = input("Enter your current location: ")
    destination = input("Enter your travel destination: ")
    travel_mode = input("Enter your preferred mode of travel (e.g., train, bus, bike): ")


    dist = distance(current_location, destination)
    print(distance(current_location, destination))
    print("Estimated CO2 emissions for your trip: ", calculate_emissions(dist[1], travel_mode), "kg CO2")
    suggest_eco_activities(calculate_emissions(dist[1], travel_mode))



def calculate_emissions(distance_km, travel_mode):
    
    rate = EMISSION_RATES.get(travel_mode.lower())
    if rate is None:
        print("Unknown travel mode. Please choose from car, bus, train, bike, or plane.")
    return distance_km * rate

def suggest_eco_activities(emission_kg):
    print("To offset your trip's carbon footprint, consider the following eco-friendly activities:")

    if emission_kg <= 0:
        print("No emissions to offset!")
        return
    else:
        for activity, count in ECO_ACTIVITIES.items():
            hours_needed = emission_kg/count # finds the number of hours needed to offset the emissions


            print(f"- {activity}: {hours_needed:.2f} hours needed to offset your CO2 emissions.")


def distance(current_location, destination):
    
    geolocator = Nominatim(user_agent="sustainable_travel_planner")
    loc1 = geolocator.geocode(current_location)
    loc2 = geolocator.geocode(destination)

    coor1 = (loc1.latitude, loc1.longitude)
    coor2 = (loc2.latitude, loc2.longitude)
    return "Distance: ", geodesic(coor1, coor2).km, "km" #function of geopy that returns the distance between two coordinates


if __name__ == "__main__":
    main()
