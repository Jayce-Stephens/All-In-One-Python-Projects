
def main():
    path = input("Enter the path to your photo directory: ")
    print(f"Organizing photos in directory: {path}")
    organize_photos(path)
    print("Photos organized successfully!")
     
if __name__ == "__main__":
    main()