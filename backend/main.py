print("MAIN.PY STARTED")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import joblib

from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline as hf_pipeline


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ReviewInput(BaseModel):
    review: str


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
BERT_DIR = MODEL_DIR / "bert"


print("1. Starting model loading")

logistic_model = joblib.load(
    MODEL_DIR / "logistic_regression_pipeline.pkl"
)
print("2. Logistic loaded")

naive_bayes_model = joblib.load(
    MODEL_DIR / "naive_bayes_pipeline.pkl"
)
print("3. Naive Bayes loaded")

tokenizer = AutoTokenizer.from_pretrained(BERT_DIR)
print("4. Tokenizer loaded")

bert_model = AutoModelForSequenceClassification.from_pretrained(BERT_DIR)
print("5. BERT loaded")

bert_pipeline = hf_pipeline(
    "sentiment-analysis",
    model=bert_model,
    tokenizer=tokenizer
)
print("6. BERT pipeline loaded")


def label(bert_label):
    if bert_label == "LABEL_0":
        return "Negative"
    elif bert_label == "LABEL_1":
        return "Positive"
    else:
        return "Neutral"


def output(label):
    if label == "Negative":
        return -1
    elif label == "Positive":
        return 1
    else:
        return 0


@app.post("/predict")
def predict(input: ReviewInput):

    data = input.review

    result = {
        "model1": output(logistic_model.predict([data])[0]),
        "model2": output(naive_bayes_model.predict([data])[0]),
        "model3": output(label(bert_pipeline(data)[0]["label"]))
    }

    return result