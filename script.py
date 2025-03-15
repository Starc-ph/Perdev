import random
import time

# Function to generate a random list of numbers
def generate_numbers(count, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(count)]

# Function to write numbers to a file
def save_to_file(filename, numbers):
    with open(filename, "w") as file:
        for num in numbers:
            file.write(f"{num}\n")
    print(f"Numbers saved to {filename}")

# Function to read and display numbers from a file
def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
        return numbers
    except FileNotFoundError:
        print("File not found!")
        return []

# Function to perform a simple bubble sort
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# Main program
if __name__ == "__main__":
    print("Generating random numbers...")
    numbers = generate_numbers(10, 1, 100)
    print("Numbers:", numbers)

    # Save numbers to file
    filename = "numbers.txt"
    save_to_file(filename, numbers)

    time.sleep(1)  # Simulate processing delay

    print("\nReading numbers from file...")
    numbers = read_from_file(filename)
    print("Unsorted:", numbers)

    print("\nSorting numbers...")
    sorted_numbers = bubble_sort(numbers)
    print("Sorted:", sorted_numbers)
