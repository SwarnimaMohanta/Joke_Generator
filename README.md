<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>JokeBot — README</title>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
  <style>
    :root {
      --bg: #0a0a0f;
      --surface: #111118;
      --card: #16161f;
      --border: rgba(255,255,255,0.07);
      --accent: #ff6b6b;
      --accent2: #ffd93d;
      --accent3: #6bcb77;
      --accent4: #4d96ff;
      --text: #f0f0f5;
      --muted: #7a7a9a;
      --mono: 'DM Mono', monospace;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    html { scroll-behavior: smooth; }

    body {
      font-family: 'DM Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.7;
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* === NOISE TEXTURE === */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 0;
      opacity: 0.4;
    }

    /* === HERO GLOW === */
    .hero-glow {
      position: fixed;
      top: -200px;
      left: 50%;
      transform: translateX(-50%);
      width: 800px;
      height: 500px;
      background: radial-gradient(ellipse, rgba(255,107,107,0.12) 0%, transparent 70%);
      pointer-events: none;
      z-index: 0;
    }

    /* === LAYOUT === */
    .wrapper {
      position: relative;
      z-index: 1;
      max-width: 900px;
      margin: 0 auto;
      padding: 0 24px 80px;
    }

    /* === HEADER === */
    header {
      text-align: center;
      padding: 80px 0 60px;
      animation: fadeDown 0.7s ease both;
    }

    .header-emoji {
      font-size: 72px;
      display: block;
      margin-bottom: 20px;
      animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-12px); }
    }

    h1 {
      font-family: 'Syne', sans-serif;
      font-size: clamp(2.5rem, 6vw, 4rem);
      font-weight: 800;
      background: linear-gradient(135deg, #ff6b6b, #ffd93d, #4d96ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      letter-spacing: -0.02em;
      margin-bottom: 12px;
    }

    .tagline {
      color: var(--muted);
      font-size: 1.05rem;
      font-weight: 300;
      margin-bottom: 28px;
    }

    /* === BADGES === */
    .badges {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: center;
      margin-bottom: 40px;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 999px;
      font-size: 0.75rem;
      font-family: var(--mono);
      font-weight: 500;
      border: 1px solid var(--border);
      background: var(--card);
    }
    .badge.blue { border-color: rgba(77,150,255,0.3); color: var(--accent4); }
    .badge.red  { border-color: rgba(255,107,107,0.3); color: var(--accent); }
    .badge.yellow { border-color: rgba(255,217,61,0.3); color: var(--accent2); }
    .badge.green { border-color: rgba(107,203,119,0.3); color: var(--accent3); }

    /* === DIVIDER === */
    .divider {
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--border), transparent);
      margin: 48px 0;
    }

    /* === SECTION TITLES === */
    h2 {
      font-family: 'Syne', sans-serif;
      font-size: 1.4rem;
      font-weight: 800;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    h2 .icon {
      font-size: 1.2rem;
      width: 36px;
      height: 36px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: var(--card);
      border: 1px solid var(--border);
      flex-shrink: 0;
    }

    h3 {
      font-family: 'Syne', sans-serif;
      font-size: 1rem;
      font-weight: 700;
      margin: 24px 0 10px;
      color: var(--accent2);
    }

    /* === FEATURES GRID === */
    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 14px;
      margin-bottom: 8px;
    }

    .feature-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 20px;
      transition: border-color 0.2s, transform 0.2s;
      animation: fadeUp 0.5s ease both;
    }

    .feature-card:hover {
      border-color: rgba(255,107,107,0.3);
      transform: translateY(-2px);
    }

    .feature-icon { font-size: 1.5rem; margin-bottom: 10px; }
    .feature-title { font-weight: 700; font-size: 0.9rem; margin-bottom: 4px; }
    .feature-desc { color: var(--muted); font-size: 0.82rem; line-height: 1.5; }

    /* === FILE TREE === */
    .file-tree {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      font-family: var(--mono);
      font-size: 0.85rem;
      line-height: 2;
      overflow-x: auto;
    }

    .tree-line { display: flex; align-items: center; gap: 8px; }
    .tree-folder { color: var(--accent2); font-weight: 500; }
    .tree-file { color: var(--text); }
    .tree-comment { color: var(--muted); font-size: 0.78rem; }
    .tree-indent { color: var(--border); }

    /* === CODE BLOCKS === */
    .code-block {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      overflow: hidden;
      margin: 12px 0;
    }

    .code-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 16px;
      background: rgba(255,255,255,0.03);
      border-bottom: 1px solid var(--border);
    }

    .code-lang {
      font-family: var(--mono);
      font-size: 0.72rem;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }

    .copy-btn {
      background: none;
      border: 1px solid var(--border);
      border-radius: 6px;
      color: var(--muted);
      font-size: 0.72rem;
      font-family: var(--mono);
      padding: 3px 10px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .copy-btn:hover { border-color: var(--accent4); color: var(--accent4); }
    .copy-btn.copied { border-color: var(--accent3); color: var(--accent3); }

    pre {
      padding: 18px 20px;
      overflow-x: auto;
      font-family: var(--mono);
      font-size: 0.85rem;
      line-height: 1.7;
      color: var(--text);
    }

    /* Syntax colors */
    .k { color: #c678dd; }   /* keyword */
    .s { color: #98c379; }   /* string */
    .c { color: #5c6370; font-style: italic; } /* comment */
    .n { color: #e06c75; }   /* name */
    .v { color: #d19a66; }   /* value */
    .p { color: var(--accent4); } /* prompt */

    /* === STEPS === */
    .steps { counter-reset: step; display: flex; flex-direction: column; gap: 16px; }

    .step {
      display: flex;
      gap: 16px;
      align-items: flex-start;
      padding: 20px;
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      transition: border-color 0.2s;
      animation: fadeUp 0.4s ease both;
    }
    .step:hover { border-color: rgba(77,150,255,0.2); }

    .step-num {
      counter-increment: step;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent), #ff9a3c);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Syne', sans-serif;
      font-weight: 800;
      font-size: 0.85rem;
      flex-shrink: 0;
    }

    .step-content { flex: 1; }
    .step-title { font-weight: 700; margin-bottom: 6px; font-size: 0.95rem; }
    .step-desc { color: var(--muted); font-size: 0.85rem; }

    /* === TABLE === */
    .table-wrap {
      overflow-x: auto;
      border-radius: 14px;
      border: 1px solid var(--border);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }

    thead {
      background: rgba(255,255,255,0.04);
    }

    th {
      padding: 12px 18px;
      text-align: left;
      font-family: 'Syne', sans-serif;
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
      border-bottom: 1px solid var(--border);
    }

    td {
      padding: 11px 18px;
      border-bottom: 1px solid var(--border);
      font-family: var(--mono);
      font-size: 0.82rem;
    }

    tr:last-child td { border-bottom: none; }
    tr:hover td { background: rgba(255,255,255,0.02); }

    .tag {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
    }
    .tag-get { background: rgba(107,203,119,0.15); color: var(--accent3); }
    .tag-blue { background: rgba(77,150,255,0.15); color: var(--accent4); }
    .tag-yellow { background: rgba(255,217,61,0.15); color: var(--accent2); }

    /* === TECH STACK === */
    .tech-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 12px;
    }

    .tech-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      text-align: center;
      transition: all 0.2s;
    }
    .tech-card:hover { transform: translateY(-2px); border-color: rgba(77,150,255,0.3); }
    .tech-icon { font-size: 1.8rem; margin-bottom: 8px; }
    .tech-name { font-weight: 700; font-size: 0.88rem; }
    .tech-role { color: var(--muted); font-size: 0.75rem; margin-top: 2px; }

    /* === WARNING BOX === */
    .warn-box {
      display: flex;
      gap: 12px;
      align-items: flex-start;
      padding: 16px 18px;
      background: rgba(255,217,61,0.06);
      border: 1px solid rgba(255,217,61,0.2);
      border-radius: 12px;
      margin: 16px 0;
      font-size: 0.88rem;
      color: var(--accent2);
    }
    .warn-icon { font-size: 1.1rem; flex-shrink: 0; margin-top: 1px; }

    /* === INFO BOX === */
    .info-box {
      display: flex;
      gap: 12px;
      align-items: flex-start;
      padding: 16px 18px;
      background: rgba(77,150,255,0.06);
      border: 1px solid rgba(77,150,255,0.2);
      border-radius: 12px;
      margin: 16px 0;
      font-size: 0.88rem;
      color: var(--accent4);
    }

    /* === AUTHOR === */
    .author-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 28px;
      display: flex;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }

    .author-avatar {
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent), var(--accent4));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.8rem;
      flex-shrink: 0;
    }

    .author-name {
      font-family: 'Syne', sans-serif;
      font-size: 1.2rem;
      font-weight: 800;
      margin-bottom: 4px;
    }

    .author-link {
      color: var(--accent4);
      text-decoration: none;
      font-size: 0.88rem;
      font-family: var(--mono);
      transition: color 0.2s;
    }
    .author-link:hover { color: var(--accent); }

    /* === FOOTER === */
    footer {
      text-align: center;
      padding: 40px 0 0;
      color: var(--muted);
      font-size: 0.82rem;
      border-top: 1px solid var(--border);
      margin-top: 60px;
    }

    footer .heart { color: var(--accent); }

    /* === ANIMATIONS === */
    @keyframes fadeDown {
      from { opacity: 0; transform: translateY(-20px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(16px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    /* Stagger cards */
    .feature-card:nth-child(1) { animation-delay: 0.05s; }
    .feature-card:nth-child(2) { animation-delay: 0.10s; }
    .feature-card:nth-child(3) { animation-delay: 0.15s; }
    .feature-card:nth-child(4) { animation-delay: 0.20s; }
    .feature-card:nth-child(5) { animation-delay: 0.25s; }
    .feature-card:nth-child(6) { animation-delay: 0.30s; }
    .feature-card:nth-child(7) { animation-delay: 0.35s; }

    .step:nth-child(1) { animation-delay: 0.05s; }
    .step:nth-child(2) { animation-delay: 0.10s; }
    .step:nth-child(3) { animation-delay: 0.15s; }
    .step:nth-child(4) { animation-delay: 0.20s; }
    .step:nth-child(5) { animation-delay: 0.25s; }
    .step:nth-child(6) { animation-delay: 0.30s; }
    .step:nth-child(7) { animation-delay: 0.35s; }
    .step:nth-child(8) { animation-delay: 0.40s; }

    p { color: var(--muted); font-size: 0.92rem; line-height: 1.8; margin-bottom: 12px; }

    a { color: var(--accent4); text-decoration: none; }
    a:hover { text-decoration: underline; }

    @media (max-width: 600px) {
      .features-grid { grid-template-columns: 1fr; }
      .tech-grid { grid-template-columns: repeat(2, 1fr); }
      .author-card { flex-direction: column; text-align: center; }
    }
  </style>
</head>
<body>

<div class="hero-glow"></div>

<div class="wrapper">

  <!-- HEADER -->
  <header>
    <span class="header-emoji">😂</span>
    <h1>JokeBot</h1>
    <p class="tagline">AI-powered joke generator · 100,000+ Reddit jokes · Beautiful dark UI</p>

    <div class="badges">
      <span class="badge blue">🐍 Python 3.8+</span>
      <span class="badge red">⚗️ Flask 3.0</span>
      <span class="badge yellow">🤖 Claude AI</span>
      <span class="badge green">📄 MIT License</span>
    </div>
  </header>

  <div class="divider"></div>

  <!-- FEATURES -->
  <section>
    <h2><span class="icon">✨</span> Features</h2>
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI-Generated Jokes</div>
        <div class="feature-desc">Fresh jokes created by Claude AI every single time you click generate.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">📰</div>
        <div class="feature-title">Reddit Classics</div>
        <div class="feature-desc">100,000+ real jokes from Reddit, filtered and cleaned for everyone.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🔀</div>
        <div class="feature-title">Mixed Mode</div>
        <div class="feature-desc">Combine AI creativity with Reddit's best — the best of both worlds.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Topic Filters</div>
        <div class="feature-desc">Animals, Food, Tech, School, Office, Sports, Weather and more.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">👇</div>
        <div class="feature-title">Reveal Punchline</div>
        <div class="feature-desc">Tap to dramatically reveal the punchline for maximum effect.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">❤️</div>
        <div class="feature-title">Like System</div>
        <div class="feature-desc">Save your favourite jokes during your session.</div>
      </div>
      <div class="feature-card">
        <div class="feature-icon">🌙</div>
        <div class="feature-title">Beautiful Dark UI</div>
        <div class="feature-desc">Animated gradient cards, glowing blobs, and smooth animations.</div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- FILE STRUCTURE -->
  <section>
    <h2><span class="icon">🗂️</span> Project Structure</h2>
    <div class="file-tree">
      <div class="tree-line"><span class="tree-folder">joke-generator/</span></div>
      <div class="tree-line"><span style="color:var(--muted)">├── </span><span class="tree-folder">backend/</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   ├── </span><span class="tree-file">app.py</span><span style="color:var(--muted)"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Flask REST API</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   ├── </span><span class="tree-file">joke_engine.py</span><span style="color:var(--muted)"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Joke logic (dataset + AI)</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   ├── </span><span class="tree-file">preprocess.py</span><span style="color:var(--muted)"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# One-time data cleaning</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   ├── </span><span class="tree-file" style="color:var(--accent)">.env</span><span style="color:var(--muted)"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# API key (never commit!)</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   ├── </span><span class="tree-folder">data/</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   │   ├── </span><span class="tree-file">reddit_jokes.json</span><span style="color:var(--muted)"> &nbsp;# Raw Kaggle dataset</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   │   └── </span><span class="tree-file">jokes_cleaned.json</span><span style="color:var(--muted)"># Auto-generated</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   └── </span><span class="tree-file">requirements.txt</span></div>
      <div class="tree-line"><span style="color:var(--muted)">├── </span><span class="tree-folder">frontend/</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   ├── </span><span class="tree-file">index.html</span><span style="color:var(--muted)"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Main UI</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   ├── </span><span class="tree-file">style.css</span><span style="color:var(--muted)"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Styling</span></div>
      <div class="tree-line"><span style="color:var(--muted)">│   └── </span><span class="tree-file">script.js</span><span style="color:var(--muted)"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Frontend logic</span></div>
      <div class="tree-line"><span style="color:var(--muted)">├── </span><span class="tree-file">.gitignore</span></div>
      <div class="tree-line"><span style="color:var(--muted)">└── </span><span class="tree-file">README.md</span></div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- GETTING STARTED -->
  <section>
    <h2><span class="icon">🚀</span> Getting Started</h2>
    <div class="steps">

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <div class="step-title">Clone the Repository</div>
          <div class="step-desc">Download the project to your machine.</div>
          <div class="code-block" style="margin-top:12px">
            <div class="code-header"><span class="code-lang">bash</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre><span class="p">$</span> git clone https://github.com/SwarnimaMohanta/Joke_Generator.git
<span class="p">$</span> cd Joke_Generator</pre>
          </div>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <div class="step-title">Create a Virtual Environment</div>
          <div class="step-desc">Keep dependencies isolated from your system Python.</div>
          <div class="code-block" style="margin-top:12px">
            <div class="code-header"><span class="code-lang">bash (windows)</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre><span class="p">$</span> python -m venv jokevenv
<span class="p">$</span> jokevenv\Scripts\activate</pre>
          </div>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <div class="step-title">Install Dependencies</div>
          <div class="step-desc">Install all required Python packages.</div>
          <div class="code-block" style="margin-top:12px">
            <div class="code-header"><span class="code-lang">bash</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre><span class="p">$</span> pip install -r backend/requirements.txt</pre>
          </div>
        </div>
      </div>

      <div class="step">
        <div class="step-num">4</div>
        <div class="step-content">
          <div class="step-title">Download the Dataset</div>
          <div class="step-desc">
            Get the Reddit jokes dataset from Kaggle and place it at <code style="font-family:var(--mono);color:var(--accent2);font-size:0.82rem">backend/data/reddit_jokes.json</code>
          </div>
          <div class="info-box" style="margin-top:12px">
            <span>🔗</span>
            <span>Download from: <a href="https://www.kaggle.com/datasets/averkij/reddit-jokes-dataset" target="_blank">kaggle.com/datasets/averkij/reddit-jokes-dataset</a></span>
          </div>
        </div>
      </div>

      <div class="step">
        <div class="step-num">5</div>
        <div class="step-content">
          <div class="step-title">Clean the Dataset (Run Once)</div>
          <div class="step-desc">This filters out adult, offensive, and low-quality jokes automatically.</div>
          <div class="code-block" style="margin-top:12px">
            <div class="code-header"><span class="code-lang">bash</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre><span class="p">$</span> python backend/preprocess.py</pre>
          </div>
        </div>
      </div>

      <div class="step">
        <div class="step-num">6</div>
        <div class="step-content">
          <div class="step-title">Set Up Your API Key</div>
          <div class="step-desc">Create a <code style="font-family:var(--mono);color:var(--accent2);font-size:0.82rem">backend/.env</code> file with your Anthropic API key.</div>
          <div class="code-block" style="margin-top:12px">
            <div class="code-header"><span class="code-lang">.env</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre>ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx</pre>
          </div>
          <div class="warn-box">
            <span class="warn-icon">⚠️</span>
            <span>Never commit your .env file. Get your key at <a href="https://console.anthropic.com" target="_blank" style="color:var(--accent2)">console.anthropic.com</a></span>
          </div>
        </div>
      </div>

      <div class="step">
        <div class="step-num">7</div>
        <div class="step-content">
          <div class="step-title">Start the Server</div>
          <div class="step-desc">Run the Flask API backend.</div>
          <div class="code-block" style="margin-top:12px">
            <div class="code-header"><span class="code-lang">bash</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
            <pre><span class="p">$</span> python backend/app.py

<span class="c"> * Running on http://127.0.0.1:5000 ✅</span></pre>
          </div>
        </div>
      </div>

      <div class="step">
        <div class="step-num">8</div>
        <div class="step-content">
          <div class="step-title">Open the App 🎉</div>
          <div class="step-desc">Double-click <code style="font-family:var(--mono);color:var(--accent2);font-size:0.82rem">frontend/index.html</code> in File Explorer to open it in your browser. You're done!</div>
        </div>
      </div>

    </div>
  </section>

  <div class="divider"></div>

  <!-- API ENDPOINTS -->
  <section>
    <h2><span class="icon">🔌</span> API Endpoints</h2>

    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Method</th>
            <th>Endpoint</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="tag tag-get">GET</span></td>
            <td>/api/jokes</td>
            <td style="font-family:'DM Sans',sans-serif;color:var(--muted)">Get jokes with filters</td>
          </tr>
          <tr>
            <td><span class="tag tag-get">GET</span></td>
            <td>/api/topics</td>
            <td style="font-family:'DM Sans',sans-serif;color:var(--muted)">Get available topics</td>
          </tr>
          <tr>
            <td><span class="tag tag-get">GET</span></td>
            <td>/api/health</td>
            <td style="font-family:'DM Sans',sans-serif;color:var(--muted)">Check server status</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>Query Parameters for /api/jokes</h3>

    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Options</th>
            <th>Default</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>topic</td>
            <td style="font-family:'DM Sans',sans-serif;color:var(--muted)">animals, food, technology, school, office, sports, weather, random</td>
            <td>random</td>
          </tr>
          <tr>
            <td>mode</td>
            <td style="font-family:'DM Sans',sans-serif;color:var(--muted)">mixed, ai, reddit</td>
            <td>mixed</td>
          </tr>
          <tr>
            <td>count</td>
            <td style="font-family:'DM Sans',sans-serif;color:var(--muted)">1 – 6</td>
            <td>3</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="code-block" style="margin-top:16px">
      <div class="code-header"><span class="code-lang">example request</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
      <pre>GET http://localhost:5000/api/jokes?topic=animals&mode=ai&count=3</pre>
    </div>
  </section>

  <div class="divider"></div>

  <!-- TECH STACK -->
  <section>
    <h2><span class="icon">🛠️</span> Tech Stack</h2>
    <div class="tech-grid">
      <div class="tech-card">
        <div class="tech-icon">🐍</div>
        <div class="tech-name">Python</div>
        <div class="tech-role">Backend language</div>
      </div>
      <div class="tech-card">
        <div class="tech-icon">⚗️</div>
        <div class="tech-name">Flask</div>
        <div class="tech-role">REST API server</div>
      </div>
      <div class="tech-card">
        <div class="tech-icon">🤖</div>
        <div class="tech-name">Claude API</div>
        <div class="tech-role">AI joke generation</div>
      </div>
      <div class="tech-card">
        <div class="tech-icon">🌐</div>
        <div class="tech-name">HTML/CSS/JS</div>
        <div class="tech-role">Frontend UI</div>
      </div>
      <div class="tech-card">
        <div class="tech-icon">📦</div>
        <div class="tech-name">Reddit Dataset</div>
        <div class="tech-role">100k+ jokes</div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- NOTES -->
  <section>
    <h2><span class="icon">📌</span> Important Notes</h2>
    <div class="warn-box">
      <span class="warn-icon">⚠️</span>
      <span>The <strong>backend/data/</strong> folder is excluded from Git — dataset files are too large for GitHub.</span>
    </div>
    <div class="warn-box">
      <span class="warn-icon">⚠️</span>
      <span>The <strong>.env</strong> file is excluded from Git — it contains your secret API key. Never share it.</span>
    </div>
    <div class="info-box">
      <span>ℹ️</span>
      <span>Run <strong>preprocess.py</strong> again anytime you want to re-clean the dataset with updated filters.</span>
    </div>
    <div class="info-box">
      <span>ℹ️</span>
      <span>You never need to run <strong>joke_engine.py</strong> directly — it loads automatically when app.py starts.</span>
    </div>
  </section>

  <div class="divider"></div>

  <!-- AUTHOR -->
  <section>
    <h2><span class="icon">👩‍💻</span> Author</h2>
    <div class="author-card">
      <div class="author-avatar">👩</div>
      <div>
        <div class="author-name">Swarnima Mohanta</div>
        <a class="author-link" href="https://github.com/SwarnimaMohanta" target="_blank">@SwarnimaMohanta on GitHub →</a>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <p>Built with <span class="heart">❤️</span> using Claude AI · MIT License · 2025</p>
  </footer>

</div>

<script>
  function copyCode(btn) {
    const pre = btn.closest('.code-block').querySelector('pre');
    const text = pre.innerText.replace(/^\$ /gm, '').trim();
    navigator.clipboard.writeText(text).then(() => {
      btn.textContent = 'Copied!';
      btn.classList.add('copied');
      setTimeout(() => {
        btn.textContent = 'Copy';
        btn.classList.remove('copied');
      }, 2000);
    });
  }
</script>

</body>
</html>
