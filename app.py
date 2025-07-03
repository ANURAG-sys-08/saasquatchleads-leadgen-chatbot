from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load model and encoder once
model = joblib.load("lead_scoring_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Simple dummy logic
    if "name" in user_message.lower():
        reply = "Nice to meet you! What's your email?"
    elif "hello" in user_message.lower():
        reply = "Hi there! How can I assist you today?"
    else:
        reply = "Thanks for reaching out. Let me get back to you on that."

    return jsonify({'reply': reply})

# 🔮 Lead Scoring Logic
def predict_lead_score(description, industry):
    text = f"{description} {industry}"
    label_num = model.predict([text])[0]
    label = label_encoder.inverse_transform([label_num])[0]
    return label

@app.route("/score", methods=["POST"])
def score():
    data = request.json
    description = data.get("description")
    industry = data.get("industry")
    
    if not description or not industry:
        return jsonify({"error": "Missing description or industry"}), 400
    
    score = predict_lead_score(description, industry)
    return jsonify({"lead_score": score})

# ✅ Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
