from flask import Flask, render_template, request, jsonify
import json
import os
import re
from collections import Counter
from datetime import datetime

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "sample_data.json")

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def analyze_text(text):
    """Small transparent demo lexicon. This is not a psychological or diagnostic assessment."""
    positive = {
        "happy", "great", "good", "love", "enjoy", "excited", "success", "awesome",
        "proud", "helpful", "thankful", "amazing", "learn", "progress", "win",
        "motivated", "peaceful", "beautiful", "fun", "best", "achieved"
    }
    negative = {
        "sad", "bad", "stress", "stressed", "tired", "hate", "angry", "difficult",
        "worried", "failed", "fail", "problem", "upset", "lonely", "exhausted",
        "frustrated", "pressure", "hard", "disappointed", "anxious"
    }
    words = re.findall(r"[a-zA-Z']+", text.lower())
    pos = sum(1 for w in words if w in positive)
    neg = sum(1 for w in words if w in negative)
    if pos > neg:
        label = "Positive"
    elif neg > pos:
        label = "Negative"
    else:
        label = "Neutral"
    return {"label": label, "positive_hits": pos, "negative_hits": neg,
            "note": "Rule-based text signal only; not a reliable measure of a person's real mood or behaviour."}

TOPIC_KEYWORDS = {
    "Academics": ["study", "exam", "class", "lecture", "assignment", "project", "coding", "learn", "college", "lab"],
    "Sports & Fitness": ["cricket", "football", "gym", "run", "fitness", "match", "sports", "workout"],
    "Friends & Community": ["friend", "team", "volunteer", "community", "together", "club", "event"],
    "Arts & Entertainment": ["music", "movie", "art", "dance", "book", "film", "photo", "design"],
    "Technology": ["tech", "python", "software", "ai", "computer", "app", "programming", "robot"]
}

def topics_for(text):
    words = set(re.findall(r"[a-zA-Z']+", text.lower()))
    found = []
    for topic, keywords in TOPIC_KEYWORDS.items():
        count = sum(1 for word in keywords if word in words)
        if count:
            found.append({"topic": topic, "mentions": count})
    return found

def enrich_student(student):
    posts = []
    sentiment_counts = {"Positive": 0, "Neutral": 0, "Negative": 0}
    topic_counts = Counter()
    for post in student.get("posts", []):
        sentiment = analyze_text(post["text"])
        topics = topics_for(post["text"])
        sentiment_counts[sentiment["label"]] += 1
        for item in topics:
            topic_counts[item["topic"]] += item["mentions"]
        posts.append({**post, "sentiment": sentiment, "topics": topics})
    total = len(posts)
    return {
        **student,
        "posts": posts,
        "summary": {
            "post_count": total,
            "total_likes": sum(p.get("likes", 0) for p in posts),
            "total_comments": sum(p.get("comments", 0) for p in posts),
            "sentiment_counts": sentiment_counts,
            "topics": [{"topic": k, "mentions": v} for k, v in topic_counts.most_common()],
        }
    }

@app.route("/")
def index():
    students = load_data()
    return render_template("index.html", students=students)

@app.route("/api/student")
def student_api():
    name = request.args.get("name", "").strip().casefold()
    if not name:
        return jsonify({"error": "Enter a student name."}), 400
    students = load_data()
    matches = [enrich_student(s) for s in students if name in s["name"].casefold()]
    return jsonify({"matches": matches, "count": len(matches)})

@app.route("/api/students")
def students_api():
    return jsonify([{"name": s["name"], "course": s["course"], "year": s["year"]} for s in load_data()])

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
