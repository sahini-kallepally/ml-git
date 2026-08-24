def accuracy_score(correct, total):
    return correct / total


correct_predictions = 85
total_predictions = 100

accuracy = accuracy_score(
    correct_predictions,
    total_predictions
)

print(f"Accuracy: {accuracy:.2%}")