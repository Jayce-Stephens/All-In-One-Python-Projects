
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
        directory[date] = [path]

    print(f"Organizing photos in directory: {path}")
    organize_photos(path)
    print("Photos organized successfully!")
    

    for date, photos in directory.items():
        print(f"Date: {date}")
        print(f"{date} Photos: {photos}")
     

def organize_photos(path, date=None, location=None):
    return 
    



if __name__ == "__main__":
    main()