# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random
added_total = int(0)

def randDice():
    #for count in range(dice_rounds):
        # Write your logic to generate 2 numbers between 1 and 6 here
        num1 = int(random.randint(1,6))
        num2 = int(random.randint(1,6))

        # Sum 2 numbers
        added_total = num1 + num2

        # return sum to calling function
        return added_total
    
randDice()
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.

def main(added_total):
    dice_rounds = float(0)     
    while dice_rounds < 100:
            dice_rounds = dice_rounds + 2
            added_total += randDice()
    total_dice = added_total
    average_dice = total_dice / 100
    print(average_dice)
    
main(added_total)
