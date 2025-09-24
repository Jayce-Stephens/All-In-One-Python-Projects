
def main():

    Filepath = input("Enter the path of file : ")
    find_words_frequency(Filepath)

def find_words_frequency(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    print(text)


if __name__ == "__main__":
    main()