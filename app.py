# filepath: ai-backend/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data about you
about_me = {
    "name": "Ingrid",
    "background": "Software developer with a background in Medicine.",
    "interests": ["AI", "coding", "philosophing"],
}

@app.route("/ask", methods=["POST"])
def ask_ai():
    user_input = request.json.get("question", "").lower()
    if "name" in user_input:
        return jsonify({"response": f"My name is {about_me['name']}!"})
    elif "background" in user_input:
        return jsonify({"response": about_me["background"]})
    elif "interests" in user_input:
        return jsonify({"response": f"I love {', '.join(about_me['interests'])}!"})
    else:
        return jsonify({"response": "I'm not sure how to answer that, but feel free to ask more!"})

if __name__ == "__main__":
    app.run(debug=True)