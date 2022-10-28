import random

highest = 1000
answer = random.randint(1,highest)
# print(answer)   #TODO: remove after testing
guess = 0 #initialise to any number that does not equal to answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("game over")
        break

    if guess == answer:
        print("well done you've guessed it!")
        break
    else:
        if guess > answer:
            print("guess lower")
        else:
            guess < answer
            print("Guess higher")


# if guess == answer:
#     print("well done got it first time!")
# else:
#     if guess < answer:
#         print("Guess higher")
#     else:
#         print("guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Gratzz")
#     else:
#         print("Boo")






# while guess != answer:
#     print("Incorrect, keep guessing")
#     guess = int(input())
# else:
#     print("Well done you've got it first time!")



# if guess < answer:
#     print("You guessed too low")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it!1")
#     else:
#         print("Sorry you have not guessed correctly1")
# elif guess > answer:
#     print("You guessed too high")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it!2")
#     else:
#         print("Sorry you have not guessed correctly2")
# else:
#     print("You guessed correctly")

