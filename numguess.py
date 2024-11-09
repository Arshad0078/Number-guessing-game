import random
def number_guess():
    guess_to_be_made = random.randint(0,10)
    guesses = 0
    while True:
        user_input = int(input("Guess the number"))
        guesses+=1
        if user_input==guess_to_be_made:
            print(f"you guessed the correct number in {guesses}")
            break
        elif user_input>guess_to_be_made:
            print(f"your guess is greater for number{user_input}")
        else:
            print(f"your guess is lower for number{user_input}")
number_guess()