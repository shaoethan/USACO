ans = input("Hello! Do you want to play Facts Game? (Yes/No) ").lower()

if ans == "no":
    print("Okay, see you later!")
elif ans == "yes":
    choice = input(
        "Great, lets get started! What is the most expensive stock in the world? (Berkshire Hathaway Inc/Tesla Inc/Apple Inc").lower()
    # Most expensive stock
    if choice in ("apple inc", "tesla inc"):
        print("Nope, it was Berkshire Hathaway Inc. Restart the game to play again.")
    elif choice == "berkshire hathaway inc":
        choice = input("Right! Now, what is the largest country in the world? (China/Russia/India)").lower()

        # Largest country
        if choice in ("china", "india"):
            print("Nope, it was Russia. Restart the game to play again.")
        elif choice == "Russia" or "russia":
            choice = input(
                "Well done! I am sure you won't answer to this question! Who was the third president of India (Zakir Husain/Yahya Khan/Ram Nath Kovind)").lower()

            # Third president of India
            if choice in ("ram nath kovind", "yahya khan"):
                print("You were close! It was Zakir Husain. Restart the game to play again.")
            elif choice == "Zakir Husain" or "zakir husain":
                choice = input(
                    "Good job! You are pretty smart, huh? Try this. What is the smallest country in the world? (Vatican City/Monaco/Morocco)").lower()

                # Smallest country
                if choice in ("morocco", "monaco"):
                    print("Nope. It was hard one. It was Vatican City. Restart the game to start again.")
                elif choice == "vatican city":
                    print("Right!")
else:
    print("Invalid, please type either 'no' or 'yes'")

