print("Welcome to my anime dictionary")

tuloy=True

empty_dictionary = {}

def anime():
        for i,j in empty_dictionary.items():
                print(f"Code -- {i} Title -- {j}")

while tuloy == True:
        keys = input("input keys for this anime  ")

        value = input("Enter anime title ----->  ")

        empty_dictionary[keys] = value

        choice = input("continue adding anime?\ny - Yes\nn - No\np - Print\n").lower()

        if choice == 'y':
                print("Continuing...")
                continue
        elif choice == 'n':
                print("Program stops")
                break
        elif choice == 'p':
                anime()
                continue
        
        else:
                print("Invalid Choice")