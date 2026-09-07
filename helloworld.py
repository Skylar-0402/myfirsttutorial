import random

colors = ["\033[91m","\033[92m","\033[93m","\033[94m","\033[95m","\033[96m"]
end = "\033[0m"
msg = "✨Hello World✨"

for char in msg:
    c = random.choice(colors)
    print(c + char + end, end="")
print()
print("Hello Skylar!")