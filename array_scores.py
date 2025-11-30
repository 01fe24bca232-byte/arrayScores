def process_scores():
    # Fixed array of scores (change if needed)
    scores = [10, 20, 30, 40, 50]

    total = sum(scores)
    avg = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print("Sum of scores:", total)
    print("Average of scores:", avg)
    print("Maximum score:", maximum)
    print("Minimum score:", minimum)

if __name__ == "__main__":
    process_scores()