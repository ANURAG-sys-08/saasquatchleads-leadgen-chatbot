import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Load leads.json
with open("leads.json", "r") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Combine description + industry as features
df["text"] = df["description"] + " " + df["industry"]

# Encode target labels (cold, warm, hot)
label_encoder = LabelEncoder()
df["score_label"] = label_encoder.fit_transform(df["score"])

# Create a simple text classification pipeline
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# Train the model
model.fit(df["text"], df["score_label"])

# Save model and label encoder
joblib.dump(model, "lead_scoring_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("✅ Model trained and saved.")
