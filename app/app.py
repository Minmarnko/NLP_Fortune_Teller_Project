from flask import Flask, render_template, request, jsonify
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, DistilBertTokenizerFast, DistilBertForSequenceClassification
import random

app = Flask(__name__)

# Load models
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tarot_tokenizer = T5Tokenizer.from_pretrained("tarot_model")
tarot_model = T5ForConditionalGeneration.from_pretrained("tarot_model").to(device)
tarot_model.eval()

# Load sentiment models for question and reading
sentiment_question_tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-sentiment-question")
sentiment_question_model = DistilBertForSequenceClassification.from_pretrained("distilbert-sentiment-question").to(device)
sentiment_question_model.eval()

sentiment_reading_tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-sentiment-reading")
sentiment_reading_model = DistilBertForSequenceClassification.from_pretrained("distilbert-sentiment-reading").to(device)
sentiment_reading_model.eval()

# Tarot cards list
tarot_cards = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World",
    "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups", "Five of Cups",
    "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups",
    "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups",
    "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords",
    "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords",
    "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords",
    "Queen of Swords", "King of Swords",
    "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands",
    "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands",
    "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands",
    "Queen of Wands", "King of Wands",
    "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles",
    "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles",
    "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles",
    "Queen of Pentacles", "King of Pentacles"
]

# Zodiac Sign Function
def get_zodiac_sign(month, day):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"

# -------------- ROUTES ----------------

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/draw_cards", methods=["POST"])
def draw_cards():
    # Frontend calls this to randomly draw 3 cards
    drawn_cards = random.sample(tarot_cards, 3)
    return jsonify({"drawn_cards": drawn_cards})

@app.route("/generate_reading", methods=["POST"])
def generate_reading():
    # Frontend sends birthdate, question and the 3 drawn cards
    birthdate = request.form.get("birthdate")
    question = request.form.get("question")
    card1 = request.form.get("card1")
    card2 = request.form.get("card2")
    card3 = request.form.get("card3")

    # Zodiac
    month, day = int(birthdate.split("-")[1]), int(birthdate.split("-")[2])
    zodiac = get_zodiac_sign(month, day)

    # Sentiment Prediction on the User's Question (Sentiment of the user's question)
    inputs_question = sentiment_question_tokenizer(question, return_tensors="pt", truncation=True, padding=True, max_length=128)
    inputs_question = {k: v.to(device) for k, v in inputs_question.items()}
    with torch.no_grad():
        outputs_question = sentiment_question_model(**inputs_question)
        sentiment_question = torch.argmax(outputs_question.logits, dim=1).item()
    sentiment_question_label = {0: "negative", 1: "neutral", 2: "positive"}[sentiment_question]

    # Tarot Reading Generation
    prompt = (
        f"You are a Tarot Master.\n"
        f"User Zodiac Sign: {zodiac}\n"
        f"User Sentiment: {sentiment_question_label}\n"
        f"User's Question: {question}\n"
        f"Drawn Cards: {card1}, {card2}, {card3}\n"
        f"Based on these, provide a detailed, sensitive, and inspiring Tarot Reading for each card and then a summarized sentence at the end."
    )

    encoded = tarot_tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        output = tarot_model.generate(
            input_ids=encoded["input_ids"].to(device),
            attention_mask=encoded["attention_mask"].to(device),
            max_length=1024,
            temperature=0.7,
            do_sample=True,
            top_k=20
        )
    reading = tarot_tokenizer.decode(output[0], skip_special_tokens=True)

    # Sentiment Analysis on the Generated Tarot Reading (final reading sentiment)
    inputs_reading = sentiment_reading_tokenizer(reading, return_tensors="pt", truncation=True, padding=True, max_length=128)
    inputs_reading = {k: v.to(device) for k, v in inputs_reading.items()}
    with torch.no_grad():
        outputs_reading = sentiment_reading_model(**inputs_reading)
        sentiment_reading = torch.argmax(outputs_reading.logits, dim=1).item()
    sentiment_reading_label = {0: "negative", 1: "neutral", 2: "positive"}[sentiment_reading]

    # Return the generated reading and the sentiment of the reading
    return jsonify({
        "zodiac": zodiac,
        "sentiment": sentiment_question_label,  # Sentiment of the user's question
        "reading": reading,
        "final_sentiment": sentiment_reading_label  # Sentiment of the final Tarot reading
    })

# ---------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
