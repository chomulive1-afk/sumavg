# Program to process an array of scores

def process_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)
    return total, average, maximum, minimum


if __name__ == "__main__":
    import sys
    print("=== Score Processing Calculator ===")

    try:
        # Case 1: User passed scores as command-line arguments
        if len(sys.argv) > 1:
            scores = list(map(float, sys.argv[1:]))
        else:
            # Case 2: Ask user to enter scores manually
            user_input = input("Enter scores separated by space: ")
            scores = list(map(float, user_input.split()))

        print("\n=== Program Parameters ===")
        print(f"Scores entered: {scores}")

        total, avg, maximum, minimum = process_scores(scores)

        print("\n=== Results ===")
        print(f"Sum of scores: {total}")
        print(f"Average of scores: {avg:.2f}")
        print(f"Maximum score: {maximum}")
        print(f"Minimum score: {minimum}")

    except ValueError:
        print("Invalid input. Please enter only numeric values.")