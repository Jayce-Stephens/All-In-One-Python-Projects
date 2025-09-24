
directory = {
    "2023-10-01": ["Users/austin/Photos/img001.jpg", "Users/austin/Photos/img002.jpg"],
}

def main():

    print("Welcome to the Photo Organizer!")
    count = int(input("How many photos do you want to organize? "))
    
    while(count > 0):
        count -= 1
        path = input("Enter the path to your photo directory: ")
        date = input("Enter the date the photos were taken (YYYY-MM-DD): ")
        location = input("Enter the location where the photos were taken: ")
        if date in directory:
            directory[date].append(path)
        else:
            directory[date] = [path]

    print(f"Organizing photos in directory: {path}")
    print("Photos organized successfully!")
    

    time = input("Enter a date (YYYY-MM-DD) to view photos taken on that day: ")
    photos = usrCall(time)
    print(f"Photos taken on {time}: {photos}")
     
    
def usrCall(time):
    if time in directory:
        return directory[time]
    else:
        return "No photos found for this date."


if __name__ == "__main__":
    main()