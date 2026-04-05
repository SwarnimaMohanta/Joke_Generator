from flask import Flask, jsonify, request
from flask_cors import CORS
from joke_engine import get_mixed_jokes, generate_ai_jokes, get_random_jokes_from_dataset

app = Flask(__name__)
CORS(app)

TOPICS = ["animals", "food", "school", "technology", "daily life",
          "sports", "science", "office", "weather", "random"]


@app.route("/api/jokes", methods=["GET"])
def get_jokes():
    """
    GET /api/jokes?topic=animals&count=3&mode=mixed
    mode: mixed | ai | reddit
    """
    topic = request.args.get("topic", "random")
    count = int(request.args.get("count", 3))
    mode = request.args.get("mode", "mixed")

    if topic == "random":
        topic = None

    count = max(1, min(count, 6))  # clamp between 1-6

    try:
        if mode == "ai":
            jokes = generate_ai_jokes(topic=topic, count=count)
        elif mode == "reddit":
            jokes = get_random_jokes_from_dataset(n=count)
            jokes = [{"setup": j["title"], "punchline": j["body"],
                      "source": "reddit", "topic": "reddit"} for j in jokes]
        else:
            jokes = get_mixed_jokes(topic=topic, count=count)

        return jsonify({"success": True, "jokes": jokes, "count": len(jokes)})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/topics", methods=["GET"])
def get_topics():
    return jsonify({"topics": TOPICS})


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Joke Generator API is running 🎉"})

from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    app.run(debug=True, port=5000)