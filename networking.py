import time
import sys

text = "starting logger"

# Loop over each character in the text
for i in range(len(text)):
    # For every character, make it uppercase and print
    animated_text = text[:i] + text[i].upper() + text[i+1:]
    print(animated_text, end="\r", flush=True)
    time.sleep(0.2)  # Delay between each character capitalizing

print()  # Move to the next line after animation finishes
