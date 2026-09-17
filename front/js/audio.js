// This file controls the lesson audio.
// It starts and stops browser speech for BridgeDay lessons.

// Share the lesson audio controller with app.js.
export function createLessonAudio(options) {
  // Read the buttons received from app.js.
  const textAudioButtons = options.textAudioButtons;
  const listeningAudioButton = options.listeningAudioButton;

  // Store the button that is speaking now.
  let activeAudioButton = null;

  // Get every lesson audio button.
  function getAllAudioButtons() {
    return [...textAudioButtons, listeningAudioButton];
  }

  // Reset every audio button after speech stops.
  function reset() {
    // Check every audio button.
    getAllAudioButtons().forEach(function (button) {
      // Restore the normal button label.
      button.textContent = button.dataset.listenLabel || "Listen";

      // Remove the playing style.
      button.classList.remove("audio-playing");
    });

    // Clear the active button.
    activeAudioButton = null;
  }

  // Speak text or stop the current speech.
  function speak(button, text) {
    // Stop when there is no text.
    if (!text) {
      return;
    }

    // Stop when this same button is already speaking.
    if (activeAudioButton === button) {
      // Stop browser speech now.
      window.speechSynthesis.cancel();

      // Reset all audio buttons.
      reset();
      return;
    }

    // Stop old speech from another button.
    window.speechSynthesis.cancel();

    // Reset old button styles.
    reset();

    // Create new browser speech.
    const speech = new SpeechSynthesisUtterance(text);

    // Set the browser voice language.
    speech.lang = button.dataset.language || "en-GB";

    // Save the active button.
    activeAudioButton = button;

    // Show the stop label.
    button.textContent = "Stop";

    // Add the playing style.
    button.classList.add("audio-playing");

    // Reset buttons when speech ends.
    speech.onend = reset;

    // Reset buttons when speech fails.
    speech.onerror = reset;

    // Start browser speech.
    window.speechSynthesis.speak(speech);
  }

  // Send audio actions back to app.js.
  return {
    reset,
    speak,
  };
}
