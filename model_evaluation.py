def accuracy_score(correct, total):
    if total == 0:
        return 0

    return correct / total


correct_predictions = 85
total_predictions = 100

accuracy = accuracy_score(
    correct_predictions,
    total_predictions
)

print(f"Accuracy: {accuracy:.2%}")