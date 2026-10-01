// This file renders and submits lesson exercises.
(() => {
  // Read the area reserved for exercise practice.
  function getPracticeArea() {
    return document.getElementById("exercise-practice");
  }

  // Show one safe message in the exercise area.
  function showPracticeMessage(message) {
    // Find the exercise area.
    const practiceArea = getPracticeArea();

    // Stop safely when the area is unavailable.
    if (!practiceArea) {
      return;
    }

    // Replace old content with the current message.
    practiceArea.textContent = message;
  }

  // Render the first fill-in-the-blank exercise in a lesson.
  function render({ exercises, accessToken, dashboardApiUrl }) {
    // Find the exercise area.
    const practiceArea = getPracticeArea();

    // Stop safely when the area is unavailable.
    if (!practiceArea) {
      return;
    }

    // Clear the previous lesson exercise.
    practiceArea.replaceChildren();

    // Find the first supported exercise type.
    const exercise = exercises.find((item) => {
      return item.exercise_type === "fill_blank";
    });

    // Explain when the lesson has no practice yet.
    if (!exercise) {
      showPracticeMessage("No practice exercise for this lesson yet.");
      return;
    }

    // Explain when the student is signed out.
    if (!accessToken) {
      showPracticeMessage("Sign in to answer this exercise.");
      return;
    }

    // Save the starting time for study-time tracking.
    const startedAt = Date.now();

    // Create the exercise card.
    const card = document.createElement("article");
    card.className = "exercise-practice-card";

    // Create the exercise title.
    const title = document.createElement("h4");
    title.textContent = "Practice";
    card.append(title);

    // Show the question.
    const question = document.createElement("p");
    question.textContent = exercise.question_text;
    card.append(question);

    // Show the hint when the lesson provides one.
    if (exercise.hint_text) {
      const hint = document.createElement("p");
      hint.className = "exercise-hint";
      hint.textContent = "Hint: " + exercise.hint_text;
      card.append(hint);
    }

    // Create the answer input.
    const answerInput = document.createElement("input");
    answerInput.type = "text";
    answerInput.placeholder = "Write your answer";
    answerInput.autocomplete = "off";
    card.append(answerInput);

    // Create the answer button.
    const answerButton = document.createElement("button");
    answerButton.type = "button";
    answerButton.textContent = "Check answer";
    card.append(answerButton);

    // Create the feedback area.
    const feedback = document.createElement("p");
    feedback.className = "exercise-feedback";
    card.append(feedback);

    // Send an answer when the student clicks the button.
    answerButton.addEventListener("click", async () => {
      // Stop empty answers before calling the API.
      if (!answerInput.value.trim()) {
        feedback.textContent = "Write an answer first.";
        return;
      }

      // Disable the button while the API request runs.
      answerButton.disabled = true;
      answerButton.textContent = "Checking...";

      try {
        // Build the address for this specific exercise.
        const attemptUrl = new URL(
          "/api/exercises/" + exercise.id + "/attempts",
          dashboardApiUrl,
        );

        // Calculate how long the student spent on this exercise.
        const elapsedSeconds = Math.round((Date.now() - startedAt) / 1000);

        // Send the student's answer to the API.
        const response = await fetch(attemptUrl, {
          method: "POST",
          headers: {
            Authorization: "Bearer " + accessToken,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            answer_text: answerInput.value,
            elapsed_seconds: elapsedSeconds,
          }),
        });

        // Stop when the API cannot validate the answer.
        if (!response.ok) {
          throw new Error("Exercise answer was not saved.");
        }

        // Read the correction result.
        const result = await response.json();

        // Show success and prevent duplicate correct attempts.
        if (result.is_correct) {
          feedback.textContent = result.feedback;
          answerButton.textContent = "Correct ✓";
          answerInput.disabled = true;
          return;
        }

        // Show correction and allow another attempt.
        feedback.textContent =
          result.feedback + " Correct answer: " + result.correct_answer;

        answerButton.disabled = false;
        answerButton.textContent = "Try again";
      } catch (error) {
        // Restore the button after an API error.
        answerButton.disabled = false;
        answerButton.textContent = "Check answer";

        // Show a safe learner-facing error.
        feedback.textContent =
          "Your answer could not be checked. Please try again.";

        // Show the technical error for development.
        console.error(error);
      }
    });

    // Add the complete exercise card to the Grammar tab.
    practiceArea.append(card);
  }

  // Make the exercise feature available to app.js.
  window.BridgeDayExercises = {
    render,
  };
})();
