def process_scores():
    scores = [10, 20, 30, 40, 50]   # <-- Fixed values inside program

    total = sum(scores)
    avg = total / len(scores)

    print("Sum of scores:", total)
    print("Average of scores:", avg)

if __name__ == "__main__":
    process_scores()
