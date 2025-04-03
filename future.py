def play_again():
    while True:
        choice = input(" DO you want to ask another question ? (yes/no)").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Thanks for playing! goodbye!")
            return False
        else:
            print("Please type 'yes'or'no'")
            