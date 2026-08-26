// This finds all menu buttons.
const navButtons = document.querySelectorAll(".nav-button");

// This finds all page sections.
const pageSections = document.querySelectorAll(".page-section");

// This finds language buttons.
const languageButtons = document.querySelectorAll(".language-button");

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
