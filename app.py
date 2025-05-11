#!/usr/bin/env python
# coding: utf-8
import os
import gdown
import torch
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import random
from sklearn.decomposition import LatentDirichletAllocation
import re
import spacy
import nltk
from nltk.corpus import stopwords
from collections import Counter
from flask import Flask, request, jsonify
import numpy as np
from rake_nltk import Rake
from transformers import AutoModelForCausalLM, AutoTokenizer
from pathlib import Path
from llama_cpp import Llama
import nest_asyncio
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
nest_asyncio.apply()

# Load LLM model
MODEL_DIR = "MODEL"
MODEL_FILE = "zephyr-quiklang-3b-4k.Q5_K_M.gguf"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
MODEL_DRIVE_ID = "10rP3n6Z1GIniLBX3M7RLjqPL4CVjK2sg"

if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_DIR, exist_ok=True)
    url = f"https://drive.google.com/uc?id={MODEL_DRIVE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)
    
llm = Llama(model_path=MODEL_PATH, n_ctx=4096)

# Sentiment Analysis pipeline

device = 0 if torch.backends.mps.is_available() else -1
sentiment_pipeline = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    tokenizer="SamLowe/roberta-base-go_emotions",
    framework="pt",
    device=device
)

def get_sentiment(journal_entries: list[str]) -> list[str]:
    emotion_counts = Counter()
    for entry in journal_entries:
        results = sentiment_pipeline(entry)
        for r in results:
            emotion_counts[r['label']] += 1
    if emotion_counts:
        top_3 = [label for label, _ in emotion_counts.most_common(3)]
        return f'{top_3[0]}, {top_3[1]}, {top_3[2]}'
    return "neutral"

def get_themes(journal_entries: list[str], top_n=3) -> list[str]:
    text = " ".join(journal_entries)
    r = Rake()
    r.extract_keywords_from_text(text)
    themes = [kw for _ , kw in r.get_ranked_phrases_with_scores()[:top_n]]
    return f'{themes[0]}, {themes[1]}, {themes[2]}'

def get_empathy(user_responses, emotions):
    combined_responses = " ".join(user_responses)
    prompt = f"""<|system|>
You are a calm, soothing, relaxed therapist and spiritual guru. You give short, gentle advice based on what the user is feeling. Keep it vague, uplifting, and one sentence max. Do not thank the user or explain what you're doing.
</s>
<|user|>
Today's stories: {combined_responses}
Emotions: {emotions}

Give one short, positive suggestion that helps me stay centered or feel okay.
</s>
<|assistant|>
"""
    output = llm(
        prompt,
        max_tokens=50,
        temperature=0.6,
        top_p=0.8,
        stop=["</s>"]
    )
    raw_text = output['choices'][0]['text'].strip()
    clean_text = re.sub(r'[^\w\s.,!?\'-]', '', raw_text)
    sentences = re.findall(r'[^.!?]*[.!?]', clean_text)
    return sentences[0].strip() if sentences else clean_text

# FastAPI Setup
app = FastAPI()

class JournalRequest(BaseModel):
    entries: list[str]

@app.post("/analyze")
def analyze_journal(data: JournalRequest):
    entries = data.entries
    sentiment = get_sentiment(entries)
    themes = get_themes(entries)
    empathy = get_empathy(entries, sentiment)
    return {
        "sentiment": sentiment,
        "themes": themes,
        "empathy": empathy
    }

def run_api():
    uvicorn.run(app, host="0.0.0.0", port=$PORT)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", $PORT)))

