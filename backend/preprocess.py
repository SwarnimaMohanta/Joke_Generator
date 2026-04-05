import json
import re

INPUT_FILE = r"C:\Users\SWARNIMA MOHANTA\OneDrive\Desktop\joke generator\backend\data\reddit_jokes.json"
OUTPUT_FILE = r"C:\Users\SWARNIMA MOHANTA\OneDrive\Desktop\joke generator\backend\data\jokes_cleaned.json"



# ---- Adult / offensive keyword filter ----
BLOCKED_WORDS = [
    # Sexual
    "sex", "sexual", "penis", "vagina", "naked", "nude", "porn", "boob",
    "breast", "ass", "butt", "cock", "dick", "pussy", "fuck", "shit",
    "bitch", "slut", "whore", "orgasm", "masturbat", "erect", "horny",
    "condom", "vibrator", "dildo", "fetish", "rape", "molest", "incest",
    "cum", "sperm", "blowjob", "handjob", "threesome", "stripper",
    "prostitut", "hooker", "kinky", "bondage", "nsfw",

    # Violence / dark
    "murder", "kill", "suicide", "dead body", "torture", "abuse",
    "drug", "cocaine", "heroin", "meth", "overdose",

    # Offensive slurs (partial match covers variants)
    "nigger", "nigga", "faggot", "retard", "tranny", "chink", "spic",
]

def is_clean(text):
    """Return True if the text contains no blocked words."""
    lower = text.lower()
    # Remove punctuation for better matching
    cleaned = re.sub(r"[^a-z0-9\s]", " ", lower)
    words = set(cleaned.split())
    for blocked in BLOCKED_WORDS:
        if blocked in cleaned:  # substring match for partial words like "masturbat"
            return False
    return True

def clean_text(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def load_and_clean():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    print(f"📦 Loaded {len(raw)} total jokes")

    cleaned = []
    skipped_empty = 0
    skipped_length = 0
    skipped_adult = 0

    for item in raw:
        title = clean_text(item.get("title", ""))
        body = clean_text(item.get("body", ""))

        # Skip if missing content
        if not title or not body:
            skipped_empty += 1
            continue

        # Skip very short or very long jokes
        if len(body) < 10 or len(body) > 600:
            skipped_length += 1
            continue

        # Skip adult/offensive content
        combined = title + " " + body
        if not is_clean(combined):
            skipped_adult += 1
            continue

        cleaned.append({
            "title": title,
            "body": body,
            "score": item.get("score", 0)
        })

    # Sort by score (best jokes first)
    cleaned.sort(key=lambda x: x["score"], reverse=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Results:")
    print(f"   Kept      : {len(cleaned)} clean jokes")
    print(f"   Skipped (adult/offensive) : {skipped_adult}")
    print(f"   Skipped (too short/long)  : {skipped_length}")
    print(f"   Skipped (empty)           : {skipped_empty}")
    print(f"\n💾 Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    load_and_clean()