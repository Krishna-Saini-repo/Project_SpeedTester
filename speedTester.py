"""
Typing Speed Test

A simple Python program that measures typing speed (WPM) and accuracy. 
The user is prompted with a random sentence, and the program calculates 
time taken, words per minute, and accuracy percentage.
"""

import random
import time

def calculate_accuracy(original, typed):
    correct_chars = 0
    max_len = max(len(original), len(typed))

    for o, t in zip(original, typed):
        if o == t:
            correct_chars += 1

    accuracy = (correct_chars / max_len) * 100 if max_len > 0 else 0
    return accuracy



def main():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Typing is a fundamental skill in the digital age.",
        "Practice makes perfect when learning to code.",
        "Python is a versatile and beginner-friendly language.",
        "Keep calm and code in Python."
    ]

    sentence = random.choice(sentences)
    print("\nType this sentence exactly as shown:\n")
    print(f"> {sentence}")

    input("\nPress Enter when you're ready to start...")
    start_time = time.time()
    typed = input("\nStart typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    word_count = len(typed) / 5
    wpm = word_count / (elapsed_time / 60)
    accuracy = calculate_accuracy(sentence, typed)

    print("\n--- Results ---")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")



main()
