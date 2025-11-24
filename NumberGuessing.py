import random

def main():
    secret = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Try to guess it.")
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: ").strip())
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts += 1

        if guess < secret:
            print("smaller number think again!!!")
        elif guess > secret:
            print("greater number think again!!!")
        else:
            print("Congratulations, You Won!!!\n", f"Number of attempts: {attempts}")
            break

if __name__ == "__main__":
    main()