// This finds all menu buttons.
const navButtons = document.querySelectorAll(".nav-button");

// This finds all page sections.
const pageSections = document.querySelectorAll(".page-section");

// This finds language buttons.
const languageButtons = document.querySelectorAll(".language-button");

// This finds study buttons.
const studyButtons = document.querySelectorAll(".study-button");

// This finds study content areas.
const studyContents = document.querySelectorAll(".study-content");

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

// This finds the typing text area.
const typingText = document.getElementById("typing-text");

// These are the changing sentences.
const typingLines = [
  "English for real communication.",
  "Deutsch A1 step by step.",
  "Life and tech every day.",
  "Study, speak and grow.",
];

// This starts with the first sentence.
let typingLineIndex = 0;

// This starts with the first letter.
let typingLetterIndex = 0;

// This writes one letter at a time.
function writeTypingText() {
  // This gets the current sentence.
  const currentLine = typingLines[typingLineIndex];

  // This adds one letter.
  typingText.textContent = currentLine.slice(0, typingLetterIndex);

  // This checks if the sentence is complete.
  if (typingLetterIndex < currentLine.length) {
    typingLetterIndex += 1;

    // This writes the next letter.
    setTimeout(writeTypingText, 55);
  } else {
    // This waits before the next sentence.
    setTimeout(changeTypingLine, 1800);
  }
}

// This changes to the next sentence.
function changeTypingLine() {
  // This changes the sentence number.
  typingLineIndex += 1;

  // This goes back to the first sentence.
  if (typingLineIndex === typingLines.length) {
    typingLineIndex = 0;
  }

  // This starts with no letters.
  typingLetterIndex = 0;

  // This starts the new sentence.
  writeTypingText();
}

// This starts the typing effect.
writeTypingText();

// This shows one page.
function showPage(pageName) {
  // This checks every page section.
  pageSections.forEach(function (section) {
    // This checks the page name.
    const isThisPage = section.classList.contains(pageName + "-page");

    // This shows or hides the page.
    section.hidden = !isThisPage;
  });

  // This checks every menu button.
  navButtons.forEach(function (button) {
    // This checks the button page name.
    const isThisButton = button.dataset.page === pageName;

    // This adds or removes the active style.
    button.classList.toggle("active-page", isThisButton);
  });
}

// This adds a click action to each menu button.
navButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // This gets the page name.
    const pageName = button.dataset.page;

    // This shows the correct page.
    showPage(pageName);
  });
});

// This shows one study area.
function showStudyArea(studyName) {
  // This checks every study area.
  studyContents.forEach(function (area) {
    // This checks the area name.
    const isThisArea = area.classList.contains(studyName + "-content");

    // This shows or hides the area.
    area.hidden = !isThisArea;
  });

  // This checks every study button.
  studyButtons.forEach(function (button) {
    // This checks the button name.
    const isThisButton = button.dataset.study === studyName;

    // This adds or removes the active style.
    button.classList.toggle("active-study-button", isThisButton);
  });
}

// This adds a click action to each study button.
studyButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // This gets the study area name.
    const studyName = button.dataset.study;

    // This shows the correct study area.
    showStudyArea(studyName);
  });
});

// This changes the active language style.
languageButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // This checks every language button.
    languageButtons.forEach(function (languageButton) {
      // This removes the old active style.
      languageButton.classList.remove("active-language");
    });

    // This adds the new active style.
    button.classList.add("active-language");
  });
});

// This shows the German card.
showGermanButton.addEventListener("click", function () {
  germanCard.hidden = false;
  showGermanButton.hidden = true;
});

// This speaks the text.
function speakText(language) {
  // This starts with English text.
  let text = englishText.textContent.trim();

  // This changes text for German.
  if (language === "de-DE") {
    text = germanText.textContent.trim();
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

// This adds audio to each audio button.
audioButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // This gets the button language.
    const language = button.dataset.language;

    // This plays the correct text.
    speakText(language);
  });
});

// This opens Home first.
showPage("home");

// This opens Text first.
showStudyArea("text");
