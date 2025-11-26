# Program to calculate sum and average of scores

def calculate_sum_and_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average


if __name__ == "__main__":
    import sys
    print("=== Score Calculator (Sum & Average) ===")

    try:
        # If user gives input through command line
        if len(sys.argv) > 1:
            scores = list(map(float, sys.argv[1:]))

        else:
            # If user inputs manually
            raw_input_scores = input("Enter scores separated by space: ")
            scores = list(map(float, raw_input_scores.split()))

        print("\n=== Program Parameters ===")
        print(f"Scores entered: {scores}")

        total, average = calculate_sum_and_average(scores)

        print(f"\nSum of scores = {total}")
        print(f"Average of scores = {average:.2f}")

    except ValueError:
        print("Invalid input. Please enter only numeric values.")
        