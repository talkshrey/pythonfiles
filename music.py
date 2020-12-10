from psonic import *
# psonic needs to be opened before running the code
import time
min_pitch = int(input("Enter your starting pitch: "))
num = int(input("How many pitches do you want to play: "))
max_pitch = min_pitch + num*5
counter = min_pitch
counter2 = max_pitch
while counter <= max_pitch:
    play(counter)
    time.sleep(1)
    counter = counter + 5
time.sleep(1.5)
print("It's reverse time")
time.sleep(1.5)
while counter2 >= min_pitch:
    play(counter2)
    time.sleep(1)
    counter2 = counter2 - 5
