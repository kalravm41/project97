import random;

chances = 5;
a = random.randint(1,9);

while chances != 0:
    b = int(input("Enter Your Guess: "));

    if a == b:
         print ("You Won")
         chances = 0
         break

    elif b>a:
        print("Try Something lesser")
        chances = chances-1

    elif b<a:
        print("Try Something Greater")
        chances = chances-1

print("You Lose The Number is " , a)        