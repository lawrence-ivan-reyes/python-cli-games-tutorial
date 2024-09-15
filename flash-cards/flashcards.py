# Starting Message
print("Welcome to 'Guess the Capital', where we'll be testing your Middle Eastern country knowledge. Let's begin!\n")

# Importing the JSON Module from Python3
import json

# Opening the File and Parsingh the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    print(data)

# Initializing "Total" as the Length of the "cards" Array & Setting the Base Score as 0
total = len(data["cards"])
score = 0

for i in data["cards"]:
    guess = input(i["q"] + ">")
    
    if guess == i["a"]:
        score +=1
        print(f"Correct! Current Score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current Score: {score}/{total}")

# Adding an End-Game Message
print(f"Thank you for playing! You scored a total of {score} points out of {total}.\n")

# Adding to the End-Game Message based on the User's Score
if score == total:
    print("Amazing! You're a capital wizard.")

if score > total / 2:
    print("Good job! You passed with over 50%.")

else:
    print("Grab yourself a map and start studying your capitals! Better luck for next time.")