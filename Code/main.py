def main():
    while True:
        print("\n=== GAME MENU ===")
        print("1. Typeosarus GUI")
        print("2. Rhythm Game")
        print("3. Exit")

        choice = input("Select: ")

        if choice == "1":
            print("\nLaunching Typeosarus GUI...")
            input("Press Enter to start...")
            run_typeosarus()   # GUI starts here

        elif choice == "2":
            print("\nLaunching Rhythm Game...")
            input("Press Enter to start...")
            run_rhythm_game()     # Rhythm game starts here

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()