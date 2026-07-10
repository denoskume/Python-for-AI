# ----------------------------------------
# Candidate Evaluator
# ----------------------------------------

score = 85

# Validate the score
if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")

else:
    # Determine the evaluation
    if score >= 90:
        evaluation = "Excellent"
    elif score >= 80:
        evaluation = "Very Good"
    elif score >= 70:
        evaluation = "Good"
    elif score >= 60:
        evaluation = "Average"
    else:
        evaluation = "Need Improvement"

    # Display the result
    print("---------- CANDIDATE EVALUATION ----------")
    print(f"Candidate Score : {score}")
    print(f"Evaluation      : {evaluation}")
    print("------------------------------------------")