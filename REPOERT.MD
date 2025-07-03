# LeadGen Chatbot & Lead Scoring Tool – Rationale Report

## 🧠 Goal

The goal was to enhance a lead generation workflow within 5 hours by focusing on:
- Improving user engagement
- Automating lead qualification

To achieve this, I implemented two complementary components:
1. A minimal chatbot interface to interact with website visitors
2. A machine learning-based lead scoring model to prioritize incoming leads

---

## 🤖 Chatbot Interface

The chatbot is implemented using HTML/CSS + Flask (no JS frameworks) to ensure simplicity and portability. It allows users to interact naturally and share key info, simulating a helpful assistant. It was designed to be lightweight, embeddable, and visually non-intrusive (toggle via cloud button).

---

## 📊 Lead Scoring Model

- **Model**: Multinomial Naive Bayes (`sklearn.naive_bayes.MultinomialNB`)
- **Task**: Classify leads into `High`, `Medium`, or `Low` based on:
  - `Company Description`
  - `Industry`
- **Reason for Model Choice**:  
  Naive Bayes is fast, effective for text classification, and works well with small datasets — making it ideal for rapid prototyping within 5 hours.

---

## 🧹 Data Preprocessing

- Combined `description` and `industry` into one string
- Used `TfidfVectorizer` for text transformation
- Encoded target labels using `LabelEncoder`
- Built a `Pipeline` for reproducibility and ease of deployment

---

## ⚙️ Performance

- Trained and tested on a small dummy dataset of ~15–20 labeled entries
- While no formal accuracy score was recorded (due to dataset size),
  predictions match expected categories well
- Easily replaceable with real labeled data for production use

---

## 💡 Why This Matters

- The chatbot increases lead engagement and form-fill conversion
- The scoring model helps sales teams focus on high-value leads
- Both tools are free of paid APIs and highly customizable

---

**Built for SaaSquatch Leads challenge. Time spent: ~5 hours total**
