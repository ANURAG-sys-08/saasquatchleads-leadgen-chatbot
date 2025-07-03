

---

````markdown
# LeadGen Chatbot & Lead Scoring Tool

## 🔍 Project Description

A lightweight lead generation enhancement tool combining:

- 🤖 A minimal chatbot for engaging users and collecting info  
- 📊 A simple ML model to score leads based on company description and industry  

Built with Flask, HTML/CSS, and a Naive Bayes classifier — no external APIs required.

---

## 🚀 Features

- Chat interface that runs on any webpage
- Lead scoring API (`/score`) to rank leads as High, Medium, or Low
- Simple Flask backend + static frontend (HTML/CSS)
- Model trained on dummy data with company descriptions & industries

---

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/leadgen-chatbot.git
   cd leadgen-chatbot
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   python app.py
   ```

5. Open your browser and visit:

   ```
   http://localhost:5000
   ```

---

## 🧠 Example: Lead Scoring API

### Request

```json
POST /score
{
  "description": "AI-powered email marketing platform",
  "industry": "Marketing Technology"
}
```

### Response

```json
{
  "lead_score": "High"
}
```

---

## 📁 Project Structure

```
leadgen-chatbot/
├── app.py
├── requirements.txt
├── lead_scoring_model.pkl
├── label_encoder.pkl
├── templates/
│   └── index.html
├── static/
│   └── styles.css
└── data/
    └── sample_data.json  (optional)
```

---

## 📄 License

MIT License — feel free to fork and build on it.

---

## 👤 Author

Built by ANURAG CHUAHAN as part of a 5-hour challenge submission for enhancing SaaSquatch Leads.

```
