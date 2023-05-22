def main():
    """The Main Menu of the program."""
    # TODO load play from argument or user input
    while True:
        print(f"\nCurrently opened play: {None}")  # TODO
        print(f"Total number of speeches: {0}")  # TODO
        print(
            """
Main menu:
1: Open a play from a directory
2: List scenes of a character
3: Display number of speeches by characters
0: Exit"""
        )
        choice = input("Select a menu option: ")
        # TODO handle choice with match-case
        if choice == "0":
            break
        else:
            print("Error: Invalid option.")


if __name__ == "__main__":
    main()
