import random
import time

print(" Welcome to the Magic 8-Ball!")
question = input("Ask me any YES/NO question: ")
print("\nThinking...")
time.sleep(3)
answers = [
    "Yes, absolutely!",
    "No way! ❌",
    "Maybe... try again later.",
    "100% true! ",
    "I doubt it."
]
print(f"🎱 Magic 8-Ball says: {random.choice(answers)}\n")