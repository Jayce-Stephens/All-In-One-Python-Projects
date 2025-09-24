from geopy.geocoders import Nominatim
from geopy.distance import geodesic #install geopy in a virtual environment


def main():
    print("Let's plan your eco-friendly trip!")
    current_location = input("Enter your current location: ")
    destination = input("Enter your travel destination: ")
    travel_mode = input("Enter your preferred mode of travel (e.g., train, bus, bike): ")
    accommodation_type = input("Enter your preferred accommodation type (e.g., eco-lodge, hostel, hotel): ")

    print(distance(current_location, destination))
    eco_activities =""


def distance(current_location, destination):
    
    geolocator = Nominatim(user_agent="sustainable_travel_planner")
    loc1 = geolocator.geocode(current_location)
    loc2 = geolocator.geocode(destination)

    coor1 = (loc1.latitude, loc1.longitude)
    coor2 = (loc2.latitude, loc2.longitude)
    return ("Distance: ", geodesic(coor1, coor2).km, "km") #function of geopy that returns the distance between two coordinates


if __name__ == "__main__":
    main()
