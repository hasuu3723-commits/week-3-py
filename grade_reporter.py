
# Python Week 3 Assignment - Grade Reporter

scores = [72, 45, 90, 61, 38]

# Initialize counters and total
passed = 0
failed = 0
total = 0

# Loop through every score
for score in scores:
    # Calculate the grade
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # Print each score and its grade
    print(f"Score: {score} - Grade: {grade}")

    # Count passes and failures
    if score >= 50:
        passed += 1
    else:
        failed += 1

    # Add scores to the total
    total += score

# Calculate the average
average = total / len(scores)

# Display the final results
print("\n--- Grade Report ---")
print(f"Number of learners passed: {passed}")
print(f"Number of learners failed: {failed}")
print(f"Average score: {round(average, 1)}")
