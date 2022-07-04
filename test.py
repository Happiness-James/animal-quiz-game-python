def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("incorrect answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Programming challanges")
guess1 = input("Hg is the chemical symbol of which element? ")
check_guess(guess1, "Mercury")
guess2 = input("Which email service is owned by Microsoft? ")
check_guess(guess2, "Hotmail")
guess3 = input("Which country produces the most coffee in the world?  ")
check_guess(guess3, "Brazil")
guess4 = input("What is the capital city of Spain?  ")
check_guess(guess4, "Madrid")
guess5 = input("About how many taste buds does the average human tongue have?  ")
check_guess(guess5, "10000")
guess6 = input("hich country invented tea?   ")
check_guess(guess6, "China")

print("Your Score is "+ str(score))