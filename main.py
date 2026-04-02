import random
import os


def main():
    # Prompt user for number of items
    while True:
        try:
            count = int(input("How many items would you like? (2, 3, or 4): "))
            if count in (2, 3, 4):
                break
            else:
                print("Please enter 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a number (2, 3, or 4).")

    # Build path to the data file (same directory as this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_dir, "Lockers.txt")

    # Read the file
    try:
        with open(data_file, "r", encoding="utf-8") as f:
ygoproddeck
lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Could not find '{data_file}'.")
        print("Make sure 'Lockers.txt' is in the same directory as this script.")
        return

    # Validate we have enough entries
    if len(lines) < count:
        print(f"Error: The file only has {len(lines)} item(s), but you requested {count}.")
        return

    # Pick random rows (no duplicates)
    chosen = random.sample(lines, count)

    # Display results
    print(f"\nHere are your {count} randomly selected item(s):\n")
    for i, line in enumerate(chosen, 1):
        parts = line.split(",", 1)
        name = parts[0].strip()
        url  = parts[1].strip() if len(parts) > 1 else "(no URL)"
        print(f"  {i}. {name}")
        print(f"     {url}")

if __name__ == "__main__":
    main()