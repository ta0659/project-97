#importing modules
import random
import math

#Taking inputs
lower_num=int(input("Enter lower bound:"))
upper_num=int(input("Enter upper bound:"))

#generating random number between the lower and upper
x=random.randint(lower_num,upper_num)
print("\n\tYou've only",
      round(math.log(upper_num-lower_num+ 1,2)),
      "chances to guess the number\n")

#initializing the number of guesses.
count=0

#for calculation of minimum number of
#guesses depend upon range
while count < math.log(upper_num-lower_num+ 1,2):
    count+=1

#taking guesses as number
guess=int(input("Guess a number:"))

#condition testing
if x==guess:
    print("Congratulations you did it in",
          count,"try")
#Once guessed,loop will break in
elif x>guess:
    print("You guessed too small!!")
elif x<guess:
    print("You guessed too high!!")

#If guessing is more than required guesses
if count>=math.log(upper_num-lower_num+ 1,2):
    print("\nThe number is %d"%x)
    print("\tBetter Luck Next time")


