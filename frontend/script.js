const API_BASE = "http://localhost:5000/api";

let selectedTopic = "random";
let likedJokes = new Set();
let totalGenerated = 0;

// Store jokes globally so we can access punchlines safely
let currentJokes = [];

// Topic pill selection
document.getElementById("topicPills").addEventListener("click", (e) => {
  const pill = e.target.closest(".pill");
  if (!pill) return;
  document.querySelectorAll(".pill").forEach(p => p.classList.remove("active"));
  pill.classList.add("active");
  selectedTopic = pill.dataset.topic;
});

async function fetchJokes() {
  const btn = document.getElementById("generateBtn");
  const section = document.getElementById("jokesSection");
  const mode = document.getElementById("modeSelect").value;
  const count = document.getElementById("countSelect").value;

  // Loading state
  btn.disabled = true;
  btn.innerHTML = `<div class="spinner"></div><span class="btn-text">Generating...</span>`;
  section.innerHTML = `<div class="placeholder"><div class="placeholder-emoji" style="animation: spin 1s linear infinite; display:inline-block">⚡</div><p>Brewing your jokes...</p></div>`;

  try {
    const params = new URLSearchParams({ topic: selectedTopic, mode, count });
    const res = await fetch(`${API_BASE}/jokes?${params}`);
    const data = await res.json();

    if (!data.success) throw new Error(data.error || "Unknown error");

    currentJokes = data.jokes; // store globally
    renderJokes(data.jokes);
    totalGenerated += data.jokes.length;
    showStats(data.jokes.length, mode);

  } catch (err) {
    section.innerHTML = `
      <div class="error-msg">
        <div style="font-size:48px">😵</div>
        <p style="margin-top:12px">Oops! ${err.message}</p>
        <p style="font-size:0.8rem; margin-top:8px; color:#666">Make sure the Flask server is running on port 5000</p>
      </div>`;
  } finally {
    btn.disabled = false;
    btn.innerHTML = `<span class="btn-icon">⚡</span><span class="btn-text">Generate Jokes!</span>`;
  }
}

function renderJokes(jokes) {
  const section = document.getElementById("jokesSection");
  section.innerHTML = `<div class="jokes-grid" id="jokesGrid"></div>`;
  const grid = document.getElementById("jokesGrid");

  jokes.forEach((joke, i) => {
    const card = document.createElement("div");
    card.className = `joke-card color-${i % 6}`;
    card.style.animationDelay = `${i * 0.08}s`;

    // Build card using DOM methods — NO inline onclick with string data
    card.innerHTML = `
      <div class="joke-number">Joke #${i + 1} · ${escapeHtml(joke.topic || 'Random')}</div>
      <div class="joke-setup">${escapeHtml(joke.setup)}</div>
      <button class="reveal-btn" data-index="${i}">👇 Reveal Punchline</button>
      <div class="joke-footer">
        <span class="source-badge ${joke.source}">${joke.source === 'ai' ? '🤖 AI' : '📰 Reddit'}</span>
        <button class="like-btn" data-liked="false" data-index="${i}" title="Like this joke">🤍</button>
      </div>
    `;

    // Attach reveal button event safely
    const revealBtn = card.querySelector(".reveal-btn");
    revealBtn.addEventListener("click", () => revealPunchline(revealBtn, i));

    // Attach like button event safely
    const likeBtn = card.querySelector(".like-btn");
    likeBtn.addEventListener("click", () => toggleLike(likeBtn, i));

    grid.appendChild(card);
  });
}

function revealPunchline(btn, index) {
  const punchline = currentJokes[index]?.punchline;
  if (!punchline) return;

  const card = btn.closest(".joke-card");

  // Remove the reveal button
  btn.remove();

  // Create punchline element safely using textContent (no XSS)
  const p = document.createElement("div");
  p.className = "joke-punchline";
  p.textContent = punchline; // safe — no HTML injection

  // Insert before footer
  const footer = card.querySelector(".joke-footer");
  card.insertBefore(p, footer);
}

function toggleLike(btn, index) {
  if (likedJokes.has(index)) {
    likedJokes.delete(index);
    btn.textContent = "🤍";
    btn.classList.remove("liked");
  } else {
    likedJokes.add(index);
    btn.textContent = "❤️";
    btn.classList.add("liked");
  }
}

function showStats(count, mode) {
  const bar = document.getElementById("statsBar");
  bar.style.display = "block";
  bar.innerHTML = `✨ Generated <strong>${count}</strong> jokes · Mode: <strong>${mode}</strong> · Total this session: <strong>${totalGenerated}</strong>`;
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}