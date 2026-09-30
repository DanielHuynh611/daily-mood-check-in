"use strict";

const STORAGE_KEY = "daily.moodEntries.v1";
const MAX_NOTE_LENGTH = 200;
const MOODS = Object.freeze({
  very_happy: { label: "Very happy", face: "😄" },
  happy: { label: "Happy", face: "🙂" },
  neutral: { label: "Neutral", face: "😐" },
  sad: { label: "Sad", face: "🙁" },
  very_sad: { label: "Very sad", face: "😞" },
});

function localDateKey(date = new Date()) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function validEntry(value) {
  return Boolean(
    value &&
      typeof value.id === "string" &&
      /^\d{4}-\d{2}-\d{2}$/.test(value.entryDate) &&
      Object.hasOwn(MOODS, value.mood) &&
      typeof value.note === "string" &&
      value.note.length <= MAX_NOTE_LENGTH &&
      typeof value.createdAt === "string" &&
      !Number.isNaN(Date.parse(value.createdAt)),
  );
}

function readEntries() {
  const raw = window.localStorage.getItem(STORAGE_KEY);
  if (!raw) return [];

  const parsed = JSON.parse(raw);
  if (!Array.isArray(parsed)) throw new Error("Saved history has an invalid format.");
  return parsed.filter(validEntry);
}

function writeEntries(entries) {
  window.localStorage.setItem(STORAGE_KEY, JSON.stringify(entries));
}

function createId() {
  if (window.crypto?.randomUUID) return window.crypto.randomUUID();
  return `${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function showToast(message) {
  const toast = document.querySelector("#toast");
  if (!toast) return;
  toast.textContent = message;
  toast.hidden = false;
  window.setTimeout(() => {
    toast.hidden = true;
  }, 3600);
}

function showError(element, message) {
  if (!element) return;
  element.textContent = message;
  element.hidden = false;
}

function formatEntryDate(dateKey) {
  const date = new Date(`${dateKey}T12:00:00`);
  return new Intl.DateTimeFormat(undefined, { dateStyle: "full" }).format(date);
}

function formatSavedTime(isoDate) {
  const date = new Date(isoDate);
  return new Intl.DateTimeFormat(undefined, {
    hour: "numeric",
    minute: "2-digit",
  }).format(date);
}

function initialiseCheckIn() {
  const form = document.querySelector("#check-in-form");
  if (!form) return;

  const todayLabel = document.querySelector("#today-label");
  const note = document.querySelector("#mood-note");
  const noteCount = document.querySelector("#note-count");
  const moodError = document.querySelector("#mood-error");
  const storageError = document.querySelector("#storage-error");
  const supportMessage = document.querySelector("#support-message");
  const alreadyCheckedIn = document.querySelector("#already-checked-in");

  todayLabel.textContent = new Intl.DateTimeFormat(undefined, {
    weekday: "long",
    month: "long",
    day: "numeric",
  }).format(new Date());

  try {
    const existing = readEntries().some((entry) => entry.entryDate === localDateKey());
    if (existing) {
      form.hidden = true;
      alreadyCheckedIn.hidden = false;
    }
  } catch (error) {
    showError(storageError, "Daily could not read this browser’s saved history. You may need to clear this site’s data.");
  }

  note.addEventListener("input", () => {
    noteCount.textContent = `${note.value.length} / ${MAX_NOTE_LENGTH}`;
  });

  form.addEventListener("change", (event) => {
    if (event.target.name !== "mood") return;
    moodError.hidden = true;
    supportMessage.hidden = event.target.value !== "very_sad";
  });

  document.querySelector("#hide-support")?.addEventListener("click", () => {
    supportMessage.hidden = true;
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    storageError.hidden = true;

    const selected = form.elements.mood.value;
    if (!Object.hasOwn(MOODS, selected)) {
      moodError.hidden = false;
      document.querySelector('input[name="mood"]')?.focus();
      return;
    }

    const cleanNote = note.value.trim();
    if (cleanNote.length > MAX_NOTE_LENGTH) {
      showError(storageError, "The note must be 200 characters or fewer.");
      note.focus();
      return;
    }

    try {
      const entries = readEntries();
      if (entries.some((entry) => entry.entryDate === localDateKey())) {
        form.hidden = true;
        alreadyCheckedIn.hidden = false;
        return;
      }

      entries.push({
        id: createId(),
        entryDate: localDateKey(),
        mood: selected,
        note: cleanNote,
        createdAt: new Date().toISOString(),
      });
      writeEntries(entries);
      form.hidden = true;
      alreadyCheckedIn.hidden = false;
      alreadyCheckedIn.focus();
      showToast("Today’s check-in was saved on this device.");
    } catch (error) {
      showError(
        storageError,
        "Daily could not save this check-in. Check that browser storage is available and try again.",
      );
    }
  });
}

function makeHistoryEntry(entry) {
  const item = document.createElement("li");
  item.className = "history-entry";

  const mood = document.createElement("span");
  mood.className = "history-mood";
  mood.setAttribute("aria-hidden", "true");
  mood.textContent = MOODS[entry.mood].face;

  const content = document.createElement("div");
  const title = document.createElement("h3");
  title.textContent = MOODS[entry.mood].label;
  const meta = document.createElement("p");
  meta.className = "history-meta";
  meta.textContent = `${formatEntryDate(entry.entryDate)} · saved ${formatSavedTime(entry.createdAt)}`;
  content.append(title, meta);

  if (entry.note) {
    const note = document.createElement("p");
    note.className = "history-note";
    note.textContent = entry.note;
    content.append(note);
  }

  const remove = document.createElement("button");
  remove.className = "delete-entry";
  remove.type = "button";
  remove.dataset.entryId = entry.id;
  remove.setAttribute("aria-label", `Delete ${formatEntryDate(entry.entryDate)} check-in`);
  remove.textContent = "Delete";

  item.append(mood, content, remove);
  return item;
}

function initialiseHistory() {
  const list = document.querySelector("#history-list");
  if (!list) return;

  const empty = document.querySelector("#history-empty");
  const count = document.querySelector("#entry-count");
  const clearButton = document.querySelector("#clear-history");
  const errorRegion = document.querySelector("#history-error");
  const dialog = document.querySelector("#confirm-dialog");
  const dialogTitle = document.querySelector("#dialog-title");
  const dialogMessage = document.querySelector("#dialog-message");
  let pendingDelete = null;

  function render() {
    errorRegion.hidden = true;
    try {
      const entries = readEntries().sort((a, b) => b.createdAt.localeCompare(a.createdAt));
      list.replaceChildren(...entries.map(makeHistoryEntry));
      empty.hidden = entries.length > 0;
      clearButton.hidden = entries.length === 0;
      count.textContent = entries.length === 1 ? "1 saved check-in" : `${entries.length} saved check-ins`;
    } catch (error) {
      list.replaceChildren();
      empty.hidden = true;
      clearButton.hidden = true;
      count.textContent = "History unavailable";
      showError(errorRegion, "Daily could not read this browser’s saved history.");
    }
  }

  function openConfirmation(target) {
    pendingDelete = target;
    const deletingAll = target === "all";
    dialogTitle.textContent = deletingAll ? "Clear all history?" : "Delete this check-in?";
    dialogMessage.textContent = deletingAll
      ? "Every saved check-in in this browser will be permanently removed."
      : "This saved check-in will be permanently removed.";
    dialog.showModal();
  }

  clearButton.addEventListener("click", () => openConfirmation("all"));
  list.addEventListener("click", (event) => {
    const button = event.target.closest("[data-entry-id]");
    if (button) openConfirmation(button.dataset.entryId);
  });

  dialog.addEventListener("close", () => {
    if (dialog.returnValue !== "confirm" || !pendingDelete) {
      pendingDelete = null;
      return;
    }

    try {
      if (pendingDelete === "all") {
        window.localStorage.removeItem(STORAGE_KEY);
        showToast("Mood history was cleared.");
      } else {
        writeEntries(readEntries().filter((entry) => entry.id !== pendingDelete));
        showToast("Check-in deleted.");
      }
      render();
    } catch (error) {
      showError(errorRegion, "Daily could not update this browser’s saved history.");
    } finally {
      pendingDelete = null;
    }
  });

  window.addEventListener("storage", render);
  render();
}

document.addEventListener("DOMContentLoaded", () => {
  initialiseCheckIn();
  initialiseHistory();
});
