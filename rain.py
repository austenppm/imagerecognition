import random
import time
import os

def rain():
    # simulate the passage of time
    time.sleep(0.1)

    # generate a random number between 0 and 1
    rand = random.random()

    # if the number is greater than 0.75,
    # print a "." to simulate a raindrop
    if rand > 0.75:
        print(".", end="")

# run the rain simulation 10 times
for i in range(10):
    rain()

# clear the screen and print a black background
os.system("clear")
print("\033[40m")
