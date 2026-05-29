from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# ── Load Your Info ───────────────────────────────────────
def load_about():
    with open("about_me.json", "r") as f:
        return json.load(f)

# ── Keyword Matching Logic ───────────────────────────────
def get_answer(question, about):
    q = question.lower().strip()

    # Greetings
    if any(word in q for word in ["hi", "hello", "hey", "good morning", "good afternoon"]):
        return f"Hello! 👋 I'm {about['name']}'s portfolio chatbot. Ask me anything about him/her!"

    # Name
    if any(word in q for word in ["name", "who are you", "who is this"]):
        return f"My name is {about['name']}."

    # Age
    if "age" in q or "old" in q or "born" in q:
        return f"I am {about['age']} years old."

    # Location
    if any(word in q for word in ["location", "live", "from", "based", "city", "country"]):
        return f"I am based in {about['location']}."

    # Education
    if any(word in q for word in ["education", "study", "degree", "school", "university", "college", "graduate"]):
        return f"🎓 {about['education']}"

    # Skills
    if any(word in q for word in ["skill", "tech", "stack", "know", "language", "tools", "technology"]):
        return f"🛠️ My skills include: {about['skills']}"

    # Experience
    if any(word in q for word in ["experience", "work", "job", "career", "background"]):
        return f"💼 {about['experience']}"

    # Projects
    if any(word in q for word in ["project", "built", "portfolio", "made", "created", "app"]):
        return f"🚀 My projects:\n{about['projects']}"

    # Strengths
    if any(word in q for word in ["strength", "good at", "best", "strength", "advantage"]):
        return f"💪 {about['strengths']}"

    # Goals
    if any(word in q for word in ["goal", "plan", "future", "aspire", "dream", "want to"]):
        return f"🎯 {about['goals']}"

    # Hobbies
    if any(word in q for word in ["hobby", "hobbies", "free time", "interest", "fun", "outside work"]):
        return f"🎮 {about['hobbies']}"

    # Contact
    if any(word in q for word in ["contact", "email", "github", "linkedin", "reach", "connect"]):
        return f"📬 {about['contact']}"

    # Availability
    if any(word in q for word in ["available", "start", "when", "availability", "join"]):
        return f"📅 {about['availability']}"

    # Why hire
    if any(word in q for word in ["why", "hire", "choose", "reason", "stand out", "different"]):
        return f"⭐ {about['why_hire']}"

    # Fallback
    return "🤔 I'm not sure about that. Try asking about my skills, projects, education, or experience!"

# ── Routes ───────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    about = load_about()
    answer = get_answer(question, about)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)