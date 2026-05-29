

from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

def load_about():
    with open("about_me.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_answer(question, about):
    q = question.lower().strip()
    
    if any(word in q for word in ["hi", "hello", "hey", "good morning", "good afternoon"]):
        return f"Hello! I'm {about ['name']} 's profile assistant  Ask me anything about him! "
    
    if any(word in q for word in ["who", "who are you", "name", "whats your name", "who is this" ] ):
        return f"My name is {about['name']}."
    
    if any(word in q for word in ["born", "old", "how old are you",]):
         return f"I am {about['age']} years old."
     
    if any(word in q for word in ["location", "live", "from", "based", "city", "country","Where are you from"]):
        return f"I am based in {about['location']}."
    
    if any(word in q for word in ["education", "study", "degree", "school", "university", "college", "graduate"]):
        return f"🎓 {about['education']}"
    
    if any(word in q for word in ["skill", "tech", "stack", "know", "language", "tools", "technology"]):
        return f"🛠️ My skills include: {about['skills']}"

    if any(word in q for word in ["experience", "work", "job", "career", "background"]):
        return f"💼 {about['experience']}"
    
    if any(word in q for word in ["project", "built", "portfolio", "made", "created", "app"]):
        return f"🚀 My projects:\n{about['projects']}"
    
    if any(word in q for word in ["strength", "good at", "best", "strength", "advantage"]):
        return f"💪 {about['strengths']}"
    
    if any(word in q for word in ["goal", "plan", "future", "aspire", "dream", "want to"]):
        return f"🎯 {about['goals']}"

    if any(word in q for word in ["hobby", "hobbies", "free time", "interest", "fun", "outside work"]):
        return f"🎮 {about['hobbies']}"
    
    if any(word in q for word in ["contact", "email", "github", "linkedin", "reach", "connect"]):
        return f"📬 {about['contact']}"
    
    if any(word in q for word in ["available", "start", "when", "availability", "join"]):
        return f"📅 {about['availability']}"

    if any(word in q for word in ["why", "hire", "choose", "reason", "stand out", "different", "should"]):
        return f"⭐ {about['why_hire']}"
    
    if any(word in q for word in ["summary", "about", "yourself", "introduce"]):
     return f"👤 {about['summary']}"

    if any(word in q for word in ["language", "speak", "tagalog", "english"]):
     return f"🗣️ I speak: {about['languages']}"

    if any(word in q for word in ["role", "position", "title", "job title"]):
     return f"💼 I am a {about['role']}"

    return "🤔 I'm not sure about that. Try asking about my skills, projects, education, or experience!"
       
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
    app.run(host="0.0.0.0", port=10000)