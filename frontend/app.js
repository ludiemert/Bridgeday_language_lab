// This finds the German button.
const showGermanButton = document.getElementById("show-german-button");

// This finds the German card.
const germanCard = document.getElementById("german-card");

// This finds the English text.
const englishText = document.getElementById("english-text");

// This finds the German text.
const germanText = document.getElementById("german-text");

// This gets all audio buttons.
const audioButtons = document.querySelectorAll(".soft-button[data-language]");

// This shows the German card.
showGermanButton.addEventListener("click", function () {
  germanCard.hidden = false;
  showGermanButton.hidden = true;
});

// This speaks the text.
function speakText(language) {
  // This starts with English text.
  let text = englishText.textContent;

  // This changes text for German.
  if (language === "de-DE") {
    text = germanText.textContent;
  }

  // This stops old audio.
  window.speechSynthesis.cancel();

  // This creates new audio.
  const speech = new SpeechSynthesisUtterance(text);

  // This sets the audio language.
  speech.lang = language;

  // This makes the voice slower.
  speech.rate = 0.85;

  // This plays the audio.
  window.speechSynthesis.speak(speech);
}

// This adds a click action to each audio button.
audioButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // This gets the button language.
    const language = button.dataset.language;

    // This plays the correct text.
    speakText(language);
  });
});
