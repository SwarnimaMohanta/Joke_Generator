import json
import random
import anthropic

# Load cleaned dataset once
with open(r"C:\Users\SWARNIMA MOHANTA\OneDrive\Desktop\joke generator\backend\data\jokes_cleaned.json", "r", encoding="utf-8") as f:
    JOKES_DB = json.load(f)

TOP_JOKES = JOKES_DB[:5000]  # Use top 5000 scored jokes

client = anthropic.Anthropic()

SUBJECTS = ["cat", "robot", "banana", "teacher", "programmer", "dog",
            "chef", "astronaut", "wifi router", "coffee machine"]

TOPICS = ["animals", "food", "school", "technology", "daily life",
          "sports", "science", "office", "weather"]


def get_random_jokes_from_dataset(n=3):
    """Pick n random jokes from the Reddit dataset."""
    picks = random.sample(TOP_JOKES, min(n, len(TOP_JOKES)))
    return [{"title": j["title"], "body": j["body"], "source": "reddit"} for j in picks]


def generate_ai_jokes(topic=None, count=3):
    """Use Claude API to generate fresh jokes based on the system prompt."""
    topic_str = topic if topic else random.choice(TOPICS)

    prompt = f"""You are a simple AI joke generator. Generate {count} different short, funny jokes.

Instructions:
- Use simple and clear English
- Keep jokes short (1-2 lines maximum)  
- Topic focus: {topic_str}
- Use wordplay, puns, or unexpected logic
- Avoid offensive, dark, or complex humor
- Use this structure: "Why did the [subject] [action]? Because [funny reason]."

Respond ONLY with a JSON array. No extra text. No markdown. Example format:
[
  {{"setup": "Why did the cat sit on the computer?", "punchline": "To keep an eye on the mouse!"}},
  {{"setup": "Why did the banana go to school?", "punchline": "Because it wanted to become a little smarter before it split!"}}
]

Generate exactly {count} jokes about: {topic_str}"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.content[0].text.strip()

    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    jokes = json.loads(raw)
    return [{"setup": j["setup"], "punchline": j["punchline"], "source": "ai", "topic": topic_str}
            for j in jokes]


def get_mixed_jokes(topic=None, count=3):
    """Return a mix: some from Reddit dataset, some AI-generated."""
    ai_count = min(2, count)
    reddit_count = count - ai_count

    result = []

    # AI jokes
    try:
        ai_jokes = generate_ai_jokes(topic=topic, count=ai_count)
        result.extend(ai_jokes)
    except Exception as e:
        print(f"AI generation failed: {e}")

    # Reddit jokes
    if reddit_count > 0:
        reddit = get_random_jokes_from_dataset(n=reddit_count)
        for r in reddit:
            result.append({
                "setup": r["title"],
                "punchline": r["body"],
                "source": "reddit",
                "topic": "reddit community"
            })

    random.shuffle(result)
    return result