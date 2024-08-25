import random
 
def guess(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)

while True:
    try:
       upper_limit = int(input("Please enter the upper limit: "))
       lower_limit = int(input("Please enter the lower limit: "))
       if lower_limit > upper_limit:
        print('Lower limit should not be greater than upper limit!')
        continue
       break
    except ValueError:
        print('Please enter valid numbers for limits!')

   
random_number = guess(lower_limit, upper_limit)
counter = 3
while counter > 0:
    try:
        guess_number = int(input("Please enter your guess number: "))
        difference = abs(guess_number - random_number)
        
        if difference == 0:
            print('Your guess is correct!')
            break
        elif difference <= 10:
            print('Wrong! Try again.')
        else:
            print('You were too far off. Try again.')
        
        counter -= 1

        if counter == 0:
            print(f"You have used all your attempts. The correct number was: {random_number}")

    except ValueError:
        print('Please enter a valid number!')

