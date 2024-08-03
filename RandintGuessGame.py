import random

#Detecting if odd or even.
def guessing_game():
    random_num = random.randint(1, 21)
    print(random_num)
    numtype_detect = random_num % 2
    print("Guess the secret number between 1 to 20")
    if numtype_detect>0:
        print("The number is an Odd Number.")
        print('')
    else:
        print("The number is an Even Number.")
        print('')
    guess_num = 0
#Loop continues while the condition is not met
    while guess_num != random_num:
        guess_num = int(input("Enter Number: "))
        if guess_num > random_num:
            print("Choose a smaller number.")
            print('')
        elif guess_num < random_num:
            print("Choose a larger number.")
            print('')
        else:
            print("Correct! The number is ", random_num)
            print('')
#Calling the function guessing_game


guessing_game()
play_again = input("Do you want to play again (Y for yes/N for no) ?")
while play_again == 'y' or 'Y' and not("n" or "N"):
    if play_again == 'Y' or 'y':
        guessing_game()
    play_again = input("Do you want to play again (Y for yes/N for no) ?")
