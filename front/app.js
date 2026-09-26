// This file runs the BridgeDay front page.
// It loads lessons, login, and dashboard data.

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

// Get the Listening tab audio button.
const listeningAudioButton = document.getElementById("listening-audio-button");

// Store the button that is speaking now.
let activeAudioButton = null;

// This finds the typing text area.
const typingText = document.getElementById("typing-text");

// Find writing practice elements.
const writingTitle = document.getElementById("writing-title");
const writingInstruction = document.getElementById("writing-instruction");
const writingSentence = document.getElementById("my-sentence");

// Find the writing save button.
const saveSentenceButton = document.getElementById("save-sentence-button");

// Find the login form.
const loginForm = document.getElementById("login-form");

// Find login input fields.
const loginEmail = document.getElementById("login-email");
const loginPassword = document.getElementById("login-password");

// Find login status text.
const authStatus = document.getElementById("auth-status");

// Find the logout button.
const logoutButton = document.getElementById("logout-button");

// Find the finish lesson button.
const finishLessonButton = document.getElementById("finish-lesson-button");

// Find the next lesson button.
const nextLessonButton = document.getElementById("next-lesson-button");

// Find lesson study flow buttons.
const previousStepButton = document.getElementById("previous-step-button");
const continueStepButton = document.getElementById("continue-step-button");

// Find lesson study progress elements.
const studyStepLabel = document.getElementById("study-step-label");
const studyProgressValue = document.getElementById("study-progress-value");

// Find account elements.
const authCard = document.getElementById("auth-card");
const accountStrip = document.getElementById("account-strip");
const topUserLabel = document.getElementById("top-user-label");
// Find the session timer text.
const sessionTimer = document.getElementById("session-timer");
const passwordToggle = document.getElementById("password-toggle");

// Find dashboard elements.
const streakCount = document.getElementById("streak-count");
const weekCount = document.getElementById("week-count");
const todayCount = document.getElementById("today-count");
// Find total lesson count.
const totalCount = document.getElementById("total-count");
const weeklyMinutes = document.getElementById("weekly-minutes");
const weeklyText = document.getElementById("weekly-text");
const progressTitle = document.getElementById("progress-title");
const progressSummary = document.getElementById("progress-summary");
const progressReview = document.getElementById("progress-review");
const reviewTitle = document.getElementById("review-title");
const reviewText = document.getElementById("review-text");
// Find the review card list.
const reviewList = document.getElementById("review-list");

// Find Home dashboard elements.
const greetingTitle = document.getElementById("greeting-title");
const greetingQuestion = document.getElementById("greeting-question");
const homeLessonTitle = document.getElementById("home-lesson-title");
const homeLessonDescription = document.getElementById(
  "home-lesson-description",
);
const homeLessonLanguage = document.getElementById("home-lesson-language");
const homeLessonLevel = document.getElementById("home-lesson-level");
const homeGoalText = document.getElementById("home-goal-text");
const homeGoalFill = document.getElementById("home-goal-fill");
const continueButton = document.getElementById("continue-button");
const dailyProgressRing = document.getElementById("daily-progress-ring");
const dailyProgressPercent = document.getElementById("daily-progress-percent");
const dailyProgressCount = document.getElementById("daily-progress-count");
const weekBars = document.querySelectorAll(".week-bar");

// Set the lesson API address.
const LESSON_API_URL =
  "http://127.0.0.1:8000/api/lessons/en-a2-work-routine-001";

// Set the API base address.
const API_BASE_URL = "http://127.0.0.1:8000";

// Set the dashboard API address.
const DASHBOARD_API_URL = API_BASE_URL + "/api/dashboard";

// Set the next lesson API address.
const NEXT_LESSON_API_URL = API_BASE_URL + "/api/lessons/next";

// Set the review queue API address.
const REVIEW_API_URL = API_BASE_URL + "/api/reviews";

// Read saved local login data.
let accessToken = localStorage.getItem("bridgeday_access_token");

let currentUser = JSON.parse(
  localStorage.getItem("bridgeday_current_user") || "null",
);

// Save the lesson start time.
let lessonStartedAt = null;

// This has language information.
const languageSettings = {
  english: {
    code: "en",
    label: "English",
    comparisonLabel: "Deutsch",
    locale: "en-GB",
    levelName: "englishLevel",
    writingTitle: "My daily sentence",
    writingInstruction: "Write one sentence in English.",
    writingPlaceholder: "I study English every day.",
    saveLabel: "Save my sentence",
    savedLabel: "Sentence saved ✓",
  },
  german: {
    code: "de",
    label: "Deutsch",
    comparisonLabel: "English",
    locale: "de-DE",
    levelName: "germanLevel",
    writingTitle: "Mein Satz für heute",
    writingInstruction: "Schreibe einen Satz auf Deutsch.",
    writingPlaceholder: "Ich lerne jeden Tag Deutsch.",
    saveLabel: "Satz speichern",
    savedLabel: "Satz gespeichert ✓",
  },
};

// This starts with English.
let selectedLanguage = "english";

// Read the API language code for the selected learning track.
function getSelectedLanguageCode() {
  // Read settings for the selected track.
  const selectedSettings = languageSettings[selectedLanguage];

  // Send the API language code.
  return selectedSettings.code;
}

// This stores the daily lesson.
let currentLesson = null;

// Store the saved dashboard data.
let currentDashboard = null;

// Define the study step order.
const studySteps = [
  {
    name: "text",
    nextLabel: "Continue to Listening →",
  },
  {
    name: "listening",
    nextLabel: "Continue to Grammar →",
  },
  {
    name: "grammar",
    nextLabel: "Continue to Vocabulary →",
  },
  {
    name: "vocabulary",
    nextLabel: "Continue to Speak & Write →",
  },
  {
    name: "speaking",
    nextLabel: "",
  },
];

// Start with the text step.
let currentStudyStepIndex = 0;

// Read the saved session start time.
let sessionStartedAt =
  Number(localStorage.getItem("bridgeday_session_started_at")) || null;

// Store the browser timer.
let sessionTimerId = null;

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

// Check if the current lesson is complete.
function isCurrentLessonCompleted() {
  return (
    currentDashboard?.completed_lesson_codes?.includes(
      currentLesson?.lessonCode,
    ) || false
  );
}

// Update the lesson step buttons and progress bar.
function renderStudyFlow() {
  // Stop when lesson data is missing.
  if (!currentLesson) {
    return;
  }

  // Read the total step amount.
  const totalSteps = studySteps.length;

  // Read the current step number for people.
  const visibleStep = currentStudyStepIndex + 1;

  // Calculate progress percent.
  const progressPercent = (visibleStep / totalSteps) * 100;

  // Show the current step text.
  studyStepLabel.textContent = "Step " + visibleStep + " of " + totalSteps;

  // Update the progress bar width.
  studyProgressValue.style.width = progressPercent + "%";

  // Check saved lesson completion.
  const isCompleted = isCurrentLessonCompleted();

  // Show the next lesson only after completion.
  if (isCompleted) {
    previousStepButton.hidden = true;
    continueStepButton.hidden = true;
    finishLessonButton.hidden = true;
    nextLessonButton.hidden = false;
    return;
  }

  // Show Previous step after the first step.
  previousStepButton.hidden = currentStudyStepIndex === 0;

  // Show Continue before the last step.
  continueStepButton.hidden = currentStudyStepIndex === totalSteps - 1;

  // Show Finish only on the last step.
  finishLessonButton.hidden = currentStudyStepIndex !== totalSteps - 1;

  // Hide Next lesson before completion.
  nextLessonButton.hidden = true;

  // Update the Continue button label.
  continueStepButton.textContent = studySteps[currentStudyStepIndex].nextLabel;
}

// Show one study step by its position.
function showStudyStep(stepIndex) {
  // Stop when the position is outside the step list.
  if (stepIndex < 0 || stepIndex >= studySteps.length) {
    return;
  }

  // Save the new step position.
  currentStudyStepIndex = stepIndex;

  // Read the current step name.
  const stepName = studySteps[currentStudyStepIndex].name;

  // Show the correct study content.
  showStudyArea(stepName);

  // Update buttons and progress.
  renderStudyFlow();

  // Return to the top of the lesson.
  window.scrollTo({
    top: 0,
    behavior: "smooth",
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

// Show writing practice for the selected learning track.
function renderWritingPractice() {
  // Read settings for the selected track.
  const selectedSettings = languageSettings[selectedLanguage];

  // Show the correct practice title.
  writingTitle.textContent = selectedSettings.writingTitle;

  // Show the correct practice instruction.
  writingInstruction.textContent = selectedSettings.writingInstruction;

  // Show a helpful sentence example.
  writingSentence.placeholder = selectedSettings.writingPlaceholder;

  // Clear a sentence from the previous language track.
  writingSentence.value = "";

  // Restore the normal save button label.
  saveSentenceButton.textContent = selectedSettings.saveLabel;

  // Enable the save button for the new lesson.
  saveSentenceButton.disabled = false;
}

// Load a previously saved learner sentence.
async function loadSavedWriting() {
  // Stop when the learner is signed out.
  if (!accessToken || !currentUser || !currentLesson?.lessonCode) {
    return;
  }

  // Save the current lesson code during the request.
  const lessonCode = currentLesson.lessonCode;

  try {
    // Ask the API for saved writing from this lesson.
    const response = await fetch(
      API_BASE_URL + "/api/writing/" + encodeURIComponent(lessonCode),
      {
        headers: {
          Authorization: "Bearer " + accessToken,
        },
      },
    );

    // A missing sentence is normal for a new lesson.
    if (response.status === 404) {
      return;
    }

    // Read the API response.
    const data = await response.json();

    // Stop when another API error happens.
    if (!response.ok) {
      throw new Error(data.detail || "Saved writing was not found.");
    }

    // Stop when the learner opened another lesson first.
    if (currentLesson?.lessonCode !== lessonCode) {
      return;
    }

    // Show the saved learner sentence.
    writingSentence.value = data.text;

    // Show that this sentence was saved.
    saveSentenceButton.textContent =
      languageSettings[selectedLanguage].savedLabel;
  } catch (error) {
    // Show the error only for development.
    console.error(error);
  }
}

// Save the current learner sentence.
async function saveCurrentWriting() {
  // Stop when the learner is signed out.
  if (!accessToken || !currentUser) {
    alert("Please sign in before saving your sentence.");
    return;
  }

  // Stop when lesson data is missing.
  if (!currentLesson?.lessonCode) {
    return;
  }

  // Remove extra spaces from the learner sentence.
  const cleanText = writingSentence.value.trim();

  // Ask for a real sentence.
  if (!cleanText) {
    alert("Write a sentence before saving.");
    writingSentence.focus();
    return;
  }

  // Disable repeated clicks while saving.
  saveSentenceButton.disabled = true;

  try {
    // Send the learner sentence to the API.
    const response = await fetch(API_BASE_URL + "/api/writing", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + accessToken,
      },
      body: JSON.stringify({
        lesson_code: currentLesson.lessonCode,
        text: cleanText,
      }),
    });

    // Read the API response.
    const data = await response.json();

    // Stop when the API reports an error.
    if (!response.ok) {
      throw new Error(data.detail || "Sentence was not saved.");
    }

    // Show the clean saved sentence.
    writingSentence.value = data.text;

    // Confirm the save action.
    saveSentenceButton.textContent =
      languageSettings[selectedLanguage].savedLabel;
  } catch (error) {
    // Show a safe error for the learner.
    alert(error.message);

    // Show details for development.
    console.error(error);
  } finally {
    // Allow another save.
    saveSentenceButton.disabled = false;
  }
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

  // Set the Listening tab audio language.
  listeningAudioButton.dataset.language = mainSettings.locale;

  // Show the current language on the Listening button.
  listeningAudioButton.textContent = "Listen to " + mainSettings.label;

  // This creates vocabulary cards.
  renderVocabulary(mainLesson);

  // Update writing practice for the selected track.
  renderWritingPractice();

  // Load any sentence saved for this lesson.
  loadSavedWriting();

  // This shows grammar text.
  const grammarText = document.querySelector(".grammar-content .page-help");

  grammarText.textContent = mainLesson.grammar || "Grammar will appear here.";

  // This shows listening text.
  const listeningText = document.querySelector(".listening-content .page-help");

  listeningText.textContent =
    "Listen to the sentence in " + mainSettings.label + ".";

  // Update the Home lesson card.
  renderHomeLesson();

  // Update the lesson study flow.
  renderStudyFlow();
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
    // Save the lesson code for progress.
    lessonCode: apiLesson.lesson_code,
    // Save the lesson category.
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

// Update the finish button with saved progress.
function updateFinishButton() {
  // Stop when lesson data is missing.
  if (!currentLesson) {
    return;
  }

  // Check if this lesson is complete.
  const isCompleted =
    currentDashboard?.completed_lesson_codes.includes(
      currentLesson.lessonCode,
    ) || false;

  // Show the correct button text.
  finishLessonButton.textContent = isCompleted
    ? "Lesson completed ✓"
    : "Finish lesson";

  // Disable only completed lessons.
  finishLessonButton.disabled = isCompleted;
}

// Show a greeting for the current time.
function renderGreeting() {
  // Read the current hour.
  const hour = new Date().getHours();

  // Choose the greeting text.
  if (hour < 12) {
    greetingTitle.textContent = "Good morning ☀️";
  } else if (hour < 18) {
    greetingTitle.textContent = "Good afternoon 👋";
  } else {
    greetingTitle.textContent = "Good evening 🌙";
  }

  // Read settings for the selected learning track.
  const selectedSettings = languageSettings[selectedLanguage];

  // Show the real selected learning track.
  greetingQuestion.textContent =
    "Ready for your next " + selectedSettings.label + " lesson?";
}

// Show the main learning card.
function renderHomeLesson() {
  // Stop when lesson data is missing.
  if (!currentLesson) {
    return;
  }

  // Read settings for the selected learning track.
  const lessonSettings = languageSettings[selectedLanguage];

  // Read the selected language label.
  const languageLabel = lessonSettings.label;

  // Check if this lesson is complete in this language track.
  const isCompleted =
    currentDashboard?.completed_lesson_codes.includes(
      currentLesson.lessonCode,
    ) || false;

  // Show the selected real lesson language.
  homeLessonTitle.textContent = isCompleted
    ? "Review your " + languageLabel + " lesson"
    : "Your next " + languageLabel + " lesson";

  // Show the selected real lesson message.
  homeLessonDescription.textContent = isCompleted
    ? "Review the lesson and keep your " + languageLabel + " active."
    : "Keep your " +
      languageLabel +
      " streak going with a short daily session.";

  // Show the selected track information.
  homeLessonLanguage.textContent = "▣ " + languageLabel;
  homeLessonLevel.textContent = currentLesson[lessonSettings.levelName] || "";
}

// Show the weekly bars.
function renderWeekBars() {
  // Read today in JavaScript format.
  const todayIndex = (new Date().getDay() + 6) % 7;

  // Read completed lessons today.
  const completedToday = currentDashboard?.completed_today || 0;

  // Update every bar.
  weekBars.forEach(function (bar, index) {
    // Remove old bar styles.
    bar.classList.remove("today-bar", "completed-bar");

    // Mark the current day.
    if (index === todayIndex) {
      bar.classList.add("today-bar");
    }

    // Mark a completed lesson today.
    if (index === todayIndex && completedToday > 0) {
      bar.classList.add("completed-bar");
    }
  });
}

// Show dashboard data on the page.
function renderDashboard() {
  // Show empty values without login.
  if (!currentDashboard) {
    streakCount.textContent = "0";
    weekCount.textContent = "0";
    todayCount.textContent = "0";
    totalCount.textContent = "0";
    weeklyMinutes.textContent = "0 min saved";
    weeklyText.textContent = "Sign in to see your saved progress.";
    progressTitle.textContent = "Start your first lesson";
    progressSummary.textContent = "Sign in to save study data.";
    progressReview.textContent = "No review data is available.";
    reviewTitle.textContent = "Next review";
    reviewText.textContent = "Sign in to see your review status.";
    homeGoalText.textContent = "0 / 1 lesson";
    homeGoalFill.style.width = "0%";
    dailyProgressPercent.textContent = "0%";
    dailyProgressCount.textContent = "0 lessons completed";
    dailyProgressRing.style.setProperty("--daily-percent", "0%");
    renderGreeting();
    renderHomeLesson();
    renderWeekBars();
    return;
  }

  // Change seconds to full minutes.
  const totalMinutes = Math.floor(currentDashboard.study_seconds_total / 60);

  // Read daily completion.
  const completedToday = currentDashboard.completed_today;

  // Set daily progress to zero or one hundred.
  const dailyPercent = completedToday > 0 ? 100 : 0;

  // Show real stats.
  streakCount.textContent = currentDashboard.current_streak_days;
  weekCount.textContent = currentDashboard.completed_this_week;
  todayCount.textContent = completedToday;
  totalCount.textContent = currentDashboard.total_completed_lessons;

  // Show saved total time.
  weeklyMinutes.textContent = totalMinutes + " min saved";

  // Show daily goal data.
  homeGoalText.textContent = Math.min(completedToday, 1) + " / 1 lesson";
  homeGoalFill.style.width = dailyPercent + "%";
  dailyProgressPercent.textContent = dailyPercent + "%";
  dailyProgressCount.textContent = completedToday + " lessons completed";
  dailyProgressRing.style.setProperty("--daily-percent", dailyPercent + "%");

  // Show the weekly message.
  if (currentDashboard.completed_this_week > 0) {
    weeklyText.textContent =
      "You completed " +
      currentDashboard.completed_this_week +
      " lesson(s) this week.";
  } else if (currentDashboard.total_completed_lessons > 0) {
    weeklyText.textContent =
      "New week, new start. You have " +
      currentDashboard.total_completed_lessons +
      " completed lesson(s) in total.";
  } else {
    weeklyText.textContent = "Complete your first lesson to see your progress.";
  }

  // Show Progress page data.
  progressTitle.textContent =
    currentDashboard.total_completed_lessons + " completed lesson(s)";
  progressSummary.textContent =
    "Total study time: " + totalMinutes + " minutes.";
  progressReview.textContent =
    "Reviews ready now: " + currentDashboard.reviews_due + ".";

  // Show Review page data.
  reviewTitle.textContent =
    currentDashboard.reviews_due > 0 ? "Review ready" : "No review today";

  reviewText.textContent =
    currentDashboard.reviews_due > 0
      ? "Open a lesson review when you are ready."
      : "Your next review will appear here.";

  // Update the Home dashboard.
  renderGreeting();
  renderHomeLesson();
  renderWeekBars();
}

// Show review cards from the selected learning track.
function renderReviewQueue(reviews) {
  // Remove old review cards.
  reviewList.innerHTML = "";

  // Explain the review page without login.
  if (!accessToken || !currentUser) {
    reviewTitle.textContent = "Next review";
    reviewText.textContent = "Sign in to see your review status.";
    return;
  }

  // Explain when no completed lesson has a review date.
  if (reviews.length === 0) {
    reviewTitle.textContent = "No scheduled reviews";
    reviewText.textContent =
      "Finish a lesson to create your first review schedule.";
    return;
  }

  // Count lessons ready to review now.
  const dueReviews = reviews.filter(function (review) {
    return review.is_due;
  });

  // Show the correct review summary.
  reviewTitle.textContent =
    dueReviews.length > 0 ? "Review ready" : "Upcoming reviews";

  reviewText.textContent =
    dueReviews.length > 0
      ? dueReviews.length + " lesson(s) are ready now."
      : "Your completed lessons will be ready on their review dates.";

  // Create one card for every review lesson.
  reviews.forEach(function (review) {
    // Create one review card.
    const reviewCard = document.createElement("article");
    reviewCard.className = "empty-card";

    // Create the lesson title.
    const reviewName = document.createElement("h3");
    reviewName.textContent = review.title;

    // Create lesson information.
    const reviewInfo = document.createElement("p");
    reviewInfo.textContent =
      review.language_code.toUpperCase() + " · " + review.level_code;

    // Create review date information.
    const reviewDate = document.createElement("p");

    // Format the review date for the browser language.
    const formattedDate = new Date(review.next_review_at).toLocaleDateString();

    // Show due or upcoming status.
    reviewDate.textContent = review.is_due
      ? "Ready to review now."
      : "Available on " + formattedDate + ".";

    // Create a button to open the lesson.
    const openButton = document.createElement("button");
    openButton.className = "next-button";
    openButton.type = "button";
    openButton.textContent = "Open lesson →";

    // Open this lesson in Study.
    openButton.addEventListener("click", function () {
      openReviewLesson(review.lesson_code);
    });

    // Put basic content inside the card.
    reviewCard.append(reviewName, reviewInfo, reviewDate, openButton);

    // Add a completion button only for due reviews.
    if (review.is_due) {
      // Create the review completion button.
      const completeButton = document.createElement("button");
      completeButton.className = "main-button";
      completeButton.type = "button";
      completeButton.textContent = "Complete review";

      // Complete this due review.
      completeButton.addEventListener("click", function () {
        completeReview(review.lesson_code);
      });

      // Add the completion action to the card.
      reviewCard.append(completeButton);
    }

    // Put this review card on the page.
    reviewList.append(reviewCard);
  });
}

// Load scheduled reviews for the selected learning track.
async function loadReviewQueue() {
  // Clear the review page without login.
  if (!accessToken || !currentUser) {
    renderReviewQueue([]);
    return;
  }

  try {
    // Read the selected real language track.
    const languageCode = getSelectedLanguageCode();

    // Create the filtered review address.
    const reviewUrl =
      REVIEW_API_URL + "?language_code=" + encodeURIComponent(languageCode);

    // Ask the API for scheduled reviews.
    const response = await fetch(reviewUrl, {
      headers: {
        Authorization: "Bearer " + accessToken,
      },
    });

    // Read the API response.
    const data = await response.json();

    // Stop when the API has an error.
    if (!response.ok) {
      throw new Error(data.detail || "Review data was not found.");
    }

    // Show the real review cards.
    renderReviewQueue(data.reviews);
  } catch (error) {
    // Clear old cards after an API error.
    reviewList.innerHTML = "";

    // Show a safe message.
    reviewTitle.textContent = "Review data was not found.";
    reviewText.textContent = "Please try again after checking the API.";

    // Show details for development.
    console.error(error);
  }
}

// Open one review lesson in Study.
async function openReviewLesson(lessonCode) {
  try {
    // Ask the API for the selected lesson.
    const response = await fetch(
      API_BASE_URL + "/api/lessons/" + encodeURIComponent(lessonCode),
    );

    // Read the API response.
    const lessonData = await response.json();

    // Stop when the API has an error.
    if (!response.ok) {
      throw new Error(lessonData.detail || "Lesson was not found.");
    }

    // Save the review lesson in the front.
    currentLesson = mapLessonFromApi(lessonData);

    // Start review at the Text step.
    currentStudyStepIndex = 0;

    // Render the selected lesson.
    renderLesson();

    // Show the first study step.
    showStudyStep(0);

    // Open Study.
    showPage("study");
  } catch (error) {
    // Show a safe message.
    alert(error.message);

    // Show details for development.
    console.error(error);
  }
}

// Complete one due review.
async function completeReview(lessonCode) {
  try {
    // Send the review completion to the API.
    const response = await fetch(
      REVIEW_API_URL + "/" + encodeURIComponent(lessonCode) + "/complete",
      {
        method: "POST",
        headers: {
          Authorization: "Bearer " + accessToken,
        },
      },
    );

    // Read the API response.
    const data = await response.json();

    // Stop when the API has an error.
    if (!response.ok) {
      throw new Error(data.detail || "Review was not completed.");
    }

    // Refresh dashboard review information.
    await loadDashboard();

    // Refresh the review queue.
    await loadReviewQueue();

    // Confirm the new review schedule.
    alert(
      "Review completed. Next review: " +
        new Date(data.next_review_at).toLocaleDateString(),
    );
  } catch (error) {
    // Show a safe message.
    alert(error.message);

    // Show details for development.
    console.error(error);
  }
}

// Load real dashboard data from the API.
async function loadDashboard() {
  // Clear data when the user is signed out.
  if (!accessToken || !currentUser) {
    currentDashboard = null;
    renderDashboard();
    updateFinishButton();
    // Update the guided study flow with saved progress.
    renderStudyFlow();
    return;
  }

  try {
    // Read the selected track code for the dashboard.
    const languageCode = getSelectedLanguageCode();

    // Create the filtered dashboard address.
    const dashboardUrl =
      DASHBOARD_API_URL + "?language_code=" + encodeURIComponent(languageCode);

    // Ask the API for saved progress in this track.
    const response = await fetch(dashboardUrl, {
      headers: {
        Authorization: "Bearer " + accessToken,
      },
    });

    // Check the dashboard response.
    if (!response.ok) {
      throw new Error("Dashboard data was not found.");
    }

    // Save dashboard data.
    currentDashboard = await response.json();

    // Update the page.
    renderDashboard();
    updateFinishButton();

    // Update the guided study flow with saved progress.
    renderStudyFlow();
  } catch (error) {
    // Show empty data when the API has an error.
    currentDashboard = null;
    renderDashboard();
    updateFinishButton();
    // Update the guided study flow with saved progress.
    renderStudyFlow();

    // Show the error for development.
    console.error(error);
  }
}

// Change seconds to a clock format.
function formatSessionTime(totalSeconds) {
  // Find hours.
  const hours = Math.floor(totalSeconds / 3600);

  // Find minutes.
  const minutes = Math.floor((totalSeconds % 3600) / 60);

  // Find seconds.
  const seconds = totalSeconds % 60;

  // Send a two digit clock.
  return [hours, minutes, seconds]
    .map(function (value) {
      return String(value).padStart(2, "0");
    })
    .join(":");
}

// Update the session clock.
function updateSessionTimer() {
  // Stop when no session exists.
  if (!sessionStartedAt) {
    sessionTimer.textContent = "00:00:00";
    return;
  }

  // Find time from the login moment.
  const totalSeconds = Math.floor((Date.now() - sessionStartedAt) / 1000);

  // Show the session clock.
  sessionTimer.textContent = formatSessionTime(totalSeconds);
}

// Start the session clock.
function startSessionTimer() {
  // Create a start time when needed.
  if (!sessionStartedAt) {
    sessionStartedAt = Date.now();

    localStorage.setItem(
      "bridgeday_session_started_at",
      String(sessionStartedAt),
    );
  }

  // Stop an old timer.
  clearInterval(sessionTimerId);

  // Show time now.
  updateSessionTimer();

  // Update time every second.
  sessionTimerId = setInterval(updateSessionTimer, 1000);
}

// Stop and clear the session clock.
function stopSessionTimer() {
  // Stop the browser timer.
  clearInterval(sessionTimerId);

  // Clear timer values.
  sessionTimerId = null;
  sessionStartedAt = null;

  // Remove saved session time.
  localStorage.removeItem("bridgeday_session_started_at");
}

// Update the login and account areas.
function updateAuthArea() {
  if (currentUser) {
    // Show the signed in email.
    topUserLabel.textContent = currentUser.email;

    // Hide the login card.
    authCard.hidden = true;

    // Show the top account area.
    accountStrip.hidden = false;

    // Start the session clock.
    startSessionTimer();
    return;
  }

  // Show the signed out user.
  authStatus.textContent = "Sign in to save your lessons.";

  // Show the login card.
  authCard.hidden = false;

  // Hide the top account area.
  accountStrip.hidden = true;

  // Stop the session clock.
  stopSessionTimer();
}

// Start the lesson timer.
function startLessonTimer() {
  if (!lessonStartedAt) {
    lessonStartedAt = Date.now();
  }
}

// Show or hide the password text.
function togglePasswordVisibility() {
  // Check the current password type.
  const isHidden = loginPassword.type === "password";

  // Change the password type.
  loginPassword.type = isHidden ? "text" : "password";

  // Update the button label.
  passwordToggle.setAttribute(
    "aria-label",
    isHidden ? "Hide password" : "Show password",
  );

  passwordToggle.title = isHidden ? "Hide password" : "Show password";
}

// Sign in with the API.
async function signInUser(event) {
  // Stop the page refresh.
  event.preventDefault();

  try {
    // Send login data to the API.
    const response = await fetch(API_BASE_URL + "/api/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: loginEmail.value,
        password: loginPassword.value,
      }),
    });

    // Read the API response.
    const data = await response.json();

    // Check the login response.
    if (!response.ok) {
      throw new Error(data.detail || "Login was not successful.");
    }

    // Save local login data.
    accessToken = data.access_token;
    currentUser = data.user;

    localStorage.setItem("bridgeday_access_token", accessToken);

    localStorage.setItem("bridgeday_current_user", JSON.stringify(currentUser));

    // Start a new login session.
    sessionStartedAt = Date.now();

    localStorage.setItem(
      "bridgeday_session_started_at",
      String(sessionStartedAt),
    );

    // Clear the password field.
    loginPassword.value = "";

    // Update the login area.
    updateAuthArea();
    // Load saved progress for the selected track.
    await loadDashboard();

    // Load the real next lesson for the selected track.
    await loadSelectedTrackLesson();
  } catch (error) {
    // Show a safe login error.
    authStatus.textContent = error.message;
  }
}

// Sign out from the local browser.
function signOutUser() {
  // Remove local login data.
  localStorage.removeItem("bridgeday_access_token");
  localStorage.removeItem("bridgeday_current_user");

  // Clear local values.
  accessToken = null;
  currentUser = null;

  // Update the login area.
  updateAuthArea();

  // Clear dashboard data on screen.
  currentDashboard = null;
  renderDashboard();
  updateFinishButton();
}

// Save the completed lesson.
async function finishCurrentLesson() {
  // Check if the user is signed in.
  if (!accessToken || !currentUser) {
    authStatus.textContent = "Please sign in before finishing a lesson.";

    showPage("home");
    return;
  }

  // Check if the lesson exists.
  if (!currentLesson?.lessonCode) {
    return;
  }

  // Start the timer when needed.
  startLessonTimer();

  // Calculate the study time.
  const studySeconds = Math.max(
    1,
    Math.floor((Date.now() - lessonStartedAt) / 1000),
  );

  try {
    // Send completion data to the API.
    const response = await fetch(API_BASE_URL + "/api/progress/complete", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + accessToken,
      },
      body: JSON.stringify({
        // Send the lesson code.
        lesson_code: currentLesson.lessonCode,
        // Send the study time.
        study_seconds: studySeconds,
      }),
    });

    // Read the API response.
    const data = await response.json();

    // Check the completion response.
    if (!response.ok) {
      throw new Error(data.detail || "Lesson was not saved.");
    }

    // Update the finish button.
    finishLessonButton.textContent = "Lesson completed ✓";

    finishLessonButton.disabled = true;

    // Load new dashboard data.
    await loadDashboard();

    // Show Next lesson after saving completion.
    renderStudyFlow();

    // Stop the lesson timer.
    lessonStartedAt = null;

    // Show the saved message.
    alert(
      "Lesson saved. Review date: " +
        new Date(data.next_review_at).toLocaleDateString(),
    );
  } catch (error) {
    // Show a safe completion error.
    alert(error.message);
  }
}

// Load the next lesson for the signed in user.
async function loadNextLesson() {
  // Stop when the user is not signed in.
  if (!accessToken || !currentUser) {
    authStatus.textContent = "Please sign in to open the next lesson.";

    // Return to the login area.
    showPage("home");
    return;
  }

  try {
    // Disable the button during the API request.
    nextLessonButton.disabled = true;

    // Read the selected track code.
    const languageCode = getSelectedLanguageCode();

    // Create the filtered next lesson address.
    const nextLessonUrl =
      NEXT_LESSON_API_URL +
      "?language_code=" +
      encodeURIComponent(languageCode);

    // Ask the API for the next incomplete lesson in this track.
    const response = await fetch(nextLessonUrl, {
      headers: {
        Authorization: "Bearer " + accessToken,
      },
    });

    // Read the API response.
    const lessonData = await response.json();

    // Stop when there are no new lessons.
    if (response.status === 404) {
      alert("You completed every available lesson.");
      return;
    }

    // Stop when the API has another error.
    if (!response.ok) {
      throw new Error(lessonData.detail || "Next lesson was not found.");
    }

    // Stop when the current lesson is not finished yet.
    if (lessonData.lesson_code === currentLesson?.lessonCode) {
      alert("Finish the current lesson before opening the next one.");
      return;
    }

    // Save the next lesson in the front.
    currentLesson = mapLessonFromApi(lessonData);

    // Start the new lesson at the Text step.
    currentStudyStepIndex = 0;

    // Start a new study timer.
    lessonStartedAt = Date.now();

    // Show the new lesson.
    renderLesson();

    // Show the first visible study step for the new lesson.
    showStudyStep(0);

    // Update the Finish lesson button.
    updateFinishButton();
    // Update the guided study flow with saved progress.
    renderStudyFlow();

    // Keep the user on the Study page.
    showPage("study");

    // Return to the top of the new lesson.
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  } catch (error) {
    // Show a safe error message.
    alert(error.message);

    // Show the error for development.
    console.error(error);
  } finally {
    // Enable the button after the request.
    nextLessonButton.disabled = false;
  }
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
    // Update the button after lesson loading.
    updateFinishButton();
    // Update the guided study flow with saved progress.
    renderStudyFlow();
  } catch (error) {
    // Show a safe error message.
    lessonTitle.textContent = "Lesson data was not found.";

    // Show the error for development.
    console.error(error);
  }
}

// Reset every audio button to its first state.
function resetAudioButtons() {
  // Check every audio button.
  // Join text card buttons and Listening tab button.
  const allAudioButtons = [...audioButtons, listeningAudioButton];

  // Check every audio button.
  allAudioButtons.forEach(function (audioButton) {
    // Show the first button label.
    audioButton.textContent = "Listen";

    // Remove the playing style.
    audioButton.classList.remove("audio-playing");
  });

  // Clear the active button.
  activeAudioButton = null;
}

// Speak text or stop the current speech.
function speakText(button, text) {
  // Stop when this same button is already speaking.
  if (activeAudioButton === button) {
    // Stop browser speech now.
    window.speechSynthesis.cancel();

    // Reset all audio buttons.
    resetAudioButtons();
    return;
  }

  // Stop old speech from another language card.
  window.speechSynthesis.cancel();

  // Reset old button styles.
  resetAudioButtons();

  // Create new browser speech.
  const speech = new SpeechSynthesisUtterance(text);

  // Set the voice language.
  speech.lang = button.dataset.language;

  // Make the voice slower for learning.
  speech.rate = 0.85;

  // Save the active button.
  activeAudioButton = button;

  // Show the stop action.
  button.textContent = "Stop";

  // Add the playing style.
  button.classList.add("audio-playing");

  // Reset after the speech ends.
  speech.onend = function () {
    // Reset only when this is still the active speech.
    if (activeAudioButton === button) {
      resetAudioButtons();
    }
  };

  // Reset after a browser speech error.
  speech.onerror = function () {
    // Reset only when this is still the active speech.
    if (activeAudioButton === button) {
      resetAudioButtons();
    }
  };

  // Start browser speech.
  window.speechSynthesis.speak(speech);
}

// This adds page clicks.
navButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // Show the selected page.
    showPage(button.dataset.page);

    // Load real reviews when Review opens.
    if (button.dataset.page === "review") {
      loadReviewQueue();
    }

    // Start the timer on the study page.
    if (button.dataset.page === "study") {
      startLessonTimer();
    }
  });
});

// Open the correct step when a study tab is clicked.
studyButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    // Find the clicked tab inside the step list.
    const stepIndex = studySteps.findIndex(function (step) {
      return step.name === button.dataset.study;
    });

    // Show that study step and update the flow buttons.
    showStudyStep(stepIndex);
  });
});

// Load the first incomplete lesson from the selected track.
async function loadSelectedTrackLesson() {
  // Stop when the user is signed out.
  if (!accessToken || !currentUser) {
    // Keep the public English preview available.
    renderLesson();
    return;
  }

  try {
    // Read the selected track code.
    const languageCode = getSelectedLanguageCode();

    // Create the filtered next lesson address.
    const nextLessonUrl =
      NEXT_LESSON_API_URL +
      "?language_code=" +
      encodeURIComponent(languageCode);

    // Ask the API for the selected track lesson.
    const response = await fetch(nextLessonUrl, {
      headers: {
        Authorization: "Bearer " + accessToken,
      },
    });

    // Read the API response.
    const lessonData = await response.json();

    // Explain when this track has no unfinished lesson.
    if (response.status === 404) {
      alert("You completed every available " + languageCode + " lesson.");
      return;
    }

    // Stop when another API error happens.
    if (!response.ok) {
      throw new Error(lessonData.detail || "Lesson was not found.");
    }

    // Save the selected real lesson.
    currentLesson = mapLessonFromApi(lessonData);

    // Return the new lesson to its first step.
    currentStudyStepIndex = 0;

    // Reset the lesson study timer.
    lessonStartedAt = Date.now();

    // Render the selected lesson.
    renderLesson();

    // Show the first visible study step for the selected lesson.
    showStudyStep(0);

    // Update completion controls.
    updateFinishButton();
    renderStudyFlow();
  } catch (error) {
    // Show the error for development.
    console.error(error);

    // Show a safe message for the learner.
    alert(error.message);
  }
}

// Add real learning track clicks.
languageButtons.forEach(function (button) {
  button.addEventListener("click", async function () {
    // Save the selected learning track.
    selectedLanguage = button.dataset.language;

    // Update the active button style.
    languageButtons.forEach(function (languageButton) {
      const isSelected = languageButton === button;

      languageButton.classList.toggle("active-language", isSelected);
    });

    // Load progress only for the selected track.
    await loadDashboard();

    // Load the real lesson for the selected track.
    await loadSelectedTrackLesson();
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

// Add audio action for the Listening tab.
listeningAudioButton.addEventListener("click", function () {
  // Speak the current main lesson text.
  speakText(listeningAudioButton, primaryText.textContent.trim());
});

// This starts the typing effect.
writeTypingText();

// This opens Home first.
showPage("home");

// Open the first guided study step.
showStudyStep(0);

// Add login form action.
loginForm.addEventListener("submit", signInUser);

// Add logout button action.
logoutButton.addEventListener("click", signOutUser);

// Add password eye action.
passwordToggle.addEventListener("click", togglePasswordVisibility);

// Add finish lesson action.
finishLessonButton.addEventListener("click", finishCurrentLesson);

// Add next lesson action.
nextLessonButton.addEventListener("click", loadNextLesson);

// Save the learner sentence.
saveSentenceButton.addEventListener("click", saveCurrentWriting);

// Restore the normal label when the learner changes the sentence.
writingSentence.addEventListener("input", function () {
  // Read settings for the selected track.
  const selectedSettings = languageSettings[selectedLanguage];

  // Show the normal save action.
  saveSentenceButton.textContent = selectedSettings.saveLabel;
});

// Return to the previous study step.
previousStepButton.addEventListener("click", function () {
  // Open the step before the current one.
  showStudyStep(currentStudyStepIndex - 1);
});

// Continue to the next study step.
continueStepButton.addEventListener("click", function () {
  // Open the step after the current one.
  showStudyStep(currentStudyStepIndex + 1);
});

// Open Study from the Home card.
continueButton.addEventListener("click", function () {
  // Show the Study page.
  showPage("study");

  // Start the study timer.
  startLessonTimer();
});

// Show the first login state.
updateAuthArea();

// This loads the lesson file.
loadLesson();

// Load saved dashboard data.
loadDashboard();
