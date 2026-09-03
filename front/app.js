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

// This finds lesson elements.
const lessonTopic = document.getElementById("lesson-topic");
const lessonTitle = document.getElementById("lesson-title");
const lessonLevel = document.getElementById("lesson-level");
const primaryLanguageLabel = document.getElementById("primary-language-label");
const comparisonLanguageLabel = document.getElementById(
  "comparison-language-label",
);
const primaryText = document.getElementById("english-text");
const comparisonText = document.getElementById("german-text");
const portugueseHelp = document.getElementById("portuguese-help");
const comparisonPortugueseHelp = document.getElementById(
  "comparison-portuguese-help",
);

// This finds comparison elements.
const showComparisonButton = document.getElementById("show-german-button");
const comparisonCard = document.getElementById("german-card");

// This finds vocabulary elements.
const wordList = document.getElementById("word-list");
const wordCount = document.getElementById("word-count");

// This gets audio buttons.
const audioButtons = document.querySelectorAll(".soft-button[data-language]");

// This finds the typing text area.
const typingText = document.getElementById("typing-text");

// Set the lesson API address.
const LESSON_API_URL =
  "http://127.0.0.1:8000/api/lessons/en-a2-work-routine-001";

// This has language information.
const languageSettings = {
  english: {
    code: "en",
    label: "English",
    comparisonLabel: "Deutsch",
    locale: "en-GB",
    levelName: "englishLevel",
  },
  german: {
    code: "de",
    label: "Deutsch",
    comparisonLabel: "English",
    locale: "de-DE",
    levelName: "germanLevel",
  },
};

// This starts with English.
let selectedLanguage = "english";

// This stores the daily lesson.
let currentLesson = null;

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

  // This shows one part of the sentence.
  typingText.textContent = currentLine.slice(0, typingLetterIndex);

  // This checks if the sentence is complete.
  if (typingLetterIndex < currentLine.length) {
    typingLetterIndex += 1;
    setTimeout(writeTypingText, 55);
    return;
  }

  // This waits before the next sentence.
  setTimeout(changeTypingLine, 1800);
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

// This shows one page.
function showPage(pageName) {
  // This checks every page section.
  pageSections.forEach(function (section) {
    const isThisPage = section.classList.contains(pageName + "-page");

    // This shows or hides the page.
    section.hidden = !isThisPage;
  });

  // This checks every menu button.
  navButtons.forEach(function (button) {
    const isThisButton = button.dataset.page === pageName;

    // This updates the active style.
    button.classList.toggle("active-page", isThisButton);
  });
}

// This shows one study area.
function showStudyArea(studyName) {
  // This checks every study area.
  studyContents.forEach(function (area) {
    const isThisArea = area.classList.contains(studyName + "-content");

    // This shows or hides the area.
    area.hidden = !isThisArea;
  });

  // This checks every study button.
  studyButtons.forEach(function (button) {
    const isThisButton = button.dataset.study === studyName;

    // This updates the active style.
    button.classList.toggle("active-study-button", isThisButton);
  });
}

// This gets one language lesson.
function getLanguageLesson(languageCode) {
  // This uses reviewed text first.
  const reviewedText = currentLesson.reviewedTranslations?.[languageCode];

  // This uses automatic text when needed.
  const automaticText = currentLesson.translations?.[languageCode];

  // This sends back the best text.
  return reviewedText || automaticText;
}

// This creates vocabulary cards.
function renderVocabulary(languageLesson) {
  // This removes old words.
  wordList.innerHTML = "";

  // This gets lesson words.
  const words = languageLesson.keywords || [];

  // This shows the word amount.
  wordCount.textContent = words.length + " words";

  // This creates every word card.
  words.forEach(function (word, index) {
    // This gets the Portuguese word.
    const portugueseWord = currentLesson.keywordsPt?.[index] || "";

    // This creates one card.
    const card = document.createElement("article");
    card.className = "word-card";

    // This creates the foreign word.
    const foreignWord = document.createElement("strong");
    foreignWord.textContent = word;

    // This creates the Portuguese meaning.
    const meaning = document.createElement("span");
    meaning.textContent = portugueseWord;

    // This puts text inside the card.
    card.append(foreignWord, meaning);

    // This puts the card on the page.
    wordList.append(card);
  });
}

// This shows the current lesson.
function renderLesson() {
  // This stops when the lesson is missing.
  if (!currentLesson) {
    return;
  }

  // This gets the main language settings.
  const mainSettings = languageSettings[selectedLanguage];

  // This gets the other language name.
  const comparisonLanguage =
    selectedLanguage === "english" ? "german" : "english";

  // This gets the comparison settings.
  const comparisonSettings = languageSettings[comparisonLanguage];

  // This gets the main lesson text.
  const mainLesson = getLanguageLesson(mainSettings.code);

  // This gets the comparison lesson text.
  const otherLesson = getLanguageLesson(comparisonSettings.code);

  // This stops when lesson text is missing.
  if (!mainLesson || !otherLesson) {
    lessonTitle.textContent = "Lesson text was not found.";
    return;
  }

  // This shows lesson information.
  lessonTopic.textContent = currentLesson.category
    .replace("-", " ")
    .toUpperCase();

  lessonTitle.textContent = mainLesson.title;
  lessonLevel.textContent = currentLesson[mainSettings.levelName];

  // This shows the main language card.
  primaryLanguageLabel.textContent = mainSettings.label;
  primaryText.textContent = mainLesson.text;
  portugueseHelp.textContent = currentLesson.textPt;

  // This prepares the comparison card.
  comparisonLanguageLabel.textContent = comparisonSettings.label;
  comparisonText.textContent = otherLesson.text;
  comparisonPortugueseHelp.textContent = currentLesson.textPt;

  // This prepares the comparison button.
  showComparisonButton.textContent = "Compare with " + comparisonSettings.label;

  // This hides comparison at the start.
  comparisonCard.hidden = true;
  showComparisonButton.hidden = false;

  // This updates audio languages.
  audioButtons[0].dataset.language = mainSettings.locale;
  audioButtons[1].dataset.language = comparisonSettings.locale;

  // This creates vocabulary cards.
  renderVocabulary(mainLesson);

  // This shows grammar text.
  const grammarText = document.querySelector(".grammar-content .page-help");

  grammarText.textContent = mainLesson.grammar || "Grammar will appear here.";

  // This shows listening text.
  const listeningText = document.querySelector(".listening-content .page-help");

  listeningText.textContent =
    "Listen to the sentence in " + mainSettings.label + ".";
}

// Change API data to front data.
function mapLessonFromApi(apiLesson) {
  // Find translations by language.
  const translationsByLanguage = Object.fromEntries(
    apiLesson.translations.map(function (item) {
      return [item.language_code, item];
    }),
  );

  // Create the main lesson data.
  const mainLesson = {
    title: apiLesson.title,
    text: apiLesson.text,
    grammar: apiLesson.grammar_note || "",
    keywords: apiLesson.vocabulary_items.map(function (item) {
      return item.target_word;
    }),
  };

  // Create English lesson data.
  const englishLesson =
    apiLesson.language_code === "en"
      ? mainLesson
      : {
          title: translationsByLanguage.en?.title || "",
          text: translationsByLanguage.en?.text || "",
          grammar: apiLesson.grammar_note || "",
          keywords: mainLesson.keywords,
        };

  // Create German lesson data.
  const germanLesson =
    apiLesson.language_code === "de"
      ? mainLesson
      : {
          title: translationsByLanguage.de?.title || "",
          text: translationsByLanguage.de?.text || "",
          grammar: apiLesson.grammar_note || "",
          keywords: mainLesson.keywords,
        };

  // Send data in the old front format.
  return {
    category: apiLesson.category,
    englishLevel:
      apiLesson.language_code === "en" ? apiLesson.level_code : "A2",
    germanLevel: apiLesson.language_code === "de" ? apiLesson.level_code : "A1",
    textPt: translationsByLanguage.pt?.text || "",
    keywordsPt: apiLesson.vocabulary_items.map(function (item) {
      return item.meaning_pt;
    }),
    translations: {
      en: englishLesson,
      de: germanLesson,
    },
  };
}

// Load one lesson from the API.
async function loadLesson() {
  try {
    // Ask the API for lesson data.
    const response = await fetch(LESSON_API_URL);

    // Check the API response.
    if (!response.ok) {
      throw new Error("Lesson was not found.");
    }

    // Read the API data.
    const lessonData = await response.json();

    // Change API data for the front.
    currentLesson = mapLessonFromApi(lessonData);

    // Show the lesson on screen.
    renderLesson();
  } catch (error) {
    // Show a safe error message.
    lessonTitle.textContent = "Lesson data was not found.";

    // Show the error for development.
    console.error(error);
  }
}

// This speaks a text.
function speakText(button, text) {
  // This stops old audio.
  window.speechSynthesis.cancel();

  // This creates new audio.
  const speech = new SpeechSynthesisUtterance(text);

  // This sets the voice language.
  speech.lang = button.dataset.language;

  // This makes the voice slower.
  speech.rate = 0.85;

  // This plays the audio.
  window.speechSynthesis.speak(speech);
}

// This adds page clicks.
navButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    showPage(button.dataset.page);
  });
});

// This adds study tab clicks.
studyButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    showStudyArea(button.dataset.study);
  });
});

// This adds language clicks.
languageButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // This saves the selected language.
    selectedLanguage = button.dataset.language;

    // This updates language buttons.
    languageButtons.forEach(function (languageButton) {
      const isSelected = languageButton === button;

      languageButton.classList.toggle("active-language", isSelected);
    });

    // This shows the new language lesson.
    renderLesson();
  });
});

// This shows the comparison lesson.
showComparisonButton.addEventListener("click", function () {
  comparisonCard.hidden = false;
  showComparisonButton.hidden = true;
});

// This adds audio clicks.
audioButtons.forEach(function (button, index) {
  button.addEventListener("click", function () {
    // This chooses primary or comparison text.
    const text =
      index === 0
        ? primaryText.textContent.trim()
        : comparisonText.textContent.trim();

    // This speaks the chosen text.
    speakText(button, text);
  });
});

// This starts the typing effect.
writeTypingText();

// This opens Home first.
showPage("home");

// This opens Text first.
showStudyArea("text");

// This loads the lesson file.
loadLesson();
