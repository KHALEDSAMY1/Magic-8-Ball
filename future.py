def play_again():
    while True:
        choice = input("Do you want to ask another question ? (yes/no): ").strip().lower()
        if choice =="yes":
            return True
        elif choice == "no":
            print("Thanks for playing good bye")
            return False
        else:
            print("please type 'yes' or 'no'.")
            