import random
import platform
import math

def main():
    freq_range = [5,15]

    # Generate a random frequency within the specified range
    random_freq = random.uniform(freq_range[0], freq_range[1])

    return random_freq

if __name__ == "__main__":
    frequency = 0
    frequency = main()
    print(f"Random frequency generated: {frequency:.2f} Hz")