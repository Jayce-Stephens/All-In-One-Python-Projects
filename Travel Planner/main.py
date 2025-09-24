
def main():
    print("Welcome to the Travel Planner!")
    destination = input("Enter your travel destination: ")
    start_date = input("Enter your start date (YYYY-MM-DD): ")
    end_date = input("Enter your end date (YYYY-MM-DD): ")

    print(f"Planning your trip to {destination} from {start_date} to {end_date}...")
    recommendations = travel_recomendations(destination)
    print("Here are some recommendations for your trip:")
    for i, c in enumerate(recommendations):
        print(f"{i + 1}: {recommendations[i]}")
        
 

    print("Trip planned successfully! Enjoy your travel!")

def travel_recomendations(destination):
    recommendations = {
        "Paris": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
        "New York": ["Statue of Liberty", "Central Park", "Times Square"],
        "Tokyo": ["Shibuya Crossing", "Tokyo Tower", "Senso-ji Temple"],
        "Atlanta": ["Georgia Aquarium", "World of Coca-Cola", "Atlanta Botanical Garden"],
        "Los Angeles": ["Hollywood Sign", "Universal Studios", "Santa Monica Pier"],
        "London": ["Big Ben", "London Eye", "Tower of London"],
        "Paris": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
        "Gotham": ["Wayne Manor", "Arkham Asylum", "Gotham City Park", "Crime Alley"]

    }
    return recommendations.get(destination, ["No recommendations available for this destination."])

if __name__ == "__main__":
    main()