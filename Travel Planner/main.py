
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

    usr_acc = input("Would you like to see accommodation options? (y/n): ")
    if usr_acc.lower() == 'y':
        accommodations = accommodation_options(destination)
        print("Here are some accommodation options:")
        for i, a in enumerate(accommodations):
            print(f"{i + 1}: {accommodations[i]}")

        
 

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

def accommodation_options(destination):
    options = {
        "Paris": ["Hotel Le Meurice", "Hotel Ritz Paris", "Hotel Plaza Athenee"],
        "New York": ["The Plaza", "The St. Regis New York", "The Langham"],
        "Tokyo": ["The Ritz-Carlton Tokyo", "Park Hyatt Tokyo", "Mandarin Oriental Tokyo"],
        "Atlanta": ["The Ritz-Carlton Atlanta", "Four Seasons Hotel Atlanta", "Loews Atlanta Hotel"],
        "Los Angeles": ["The Beverly Hills Hotel", "The Peninsula Beverly Hills", "Waldorf Astoria Beverly Hills"],
        "London": ["The Savoy", "The Langham London", "Claridge's"],
        "Gotham": ["The Iceberg Lounge", "The Narrows Hotel", "Arkham Asylum"]
    }
    return options.get(destination, ["No accommodation options available for this destination."])

if __name__ == "__main__":
    main()