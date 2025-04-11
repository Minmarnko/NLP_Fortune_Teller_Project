# AI-Powered Tarot Reading Using NLP and Sentiment Analysis

## Project Overview  
This project explores the use of **Natural Language Processing (NLP)** and **sentiment-aware AI models** to deliver **personalized Tarot readings**. Moving beyond static, generic predictions, our system integrates **user sentiment**, **astrological context**, and **randomized Tarot cards** to generate meaningful and emotionally aligned readings using a fine-tuned **Flan-T5 model**. Sentiment detection is handled via two **DistilBERT-based classifiers** for analyzing both user questions and generated readings.

---

## Problem Statement  
Traditional Tarot readings are often **template-based** and **lack emotional nuance**. Existing AI-based Tarot tools usually:
- Ignore user **emotions**
- Lack **astrological personalization**
- Offer **repetitive or vague** predictions

This project aims to solve these issues by combining **user sentiment**, **zodiac sign**, and **random card draws** to generate **context-aware Tarot readings** using advanced NLP techniques.

---

## Research Questions  
1. How can **sentiment-aware** NLP enhance personalization in Tarot reading generation?  
2. What is the effect of **zodiac-based conditioning** on the authenticity of AI-generated predictions?  
3. How do AI-generated Tarot readings compare to human-written ones in **coherence** and **engagement**?

---

## Dataset  

### 🧾 **Base Reference Dataset**  
- **Source:** Hugging Face `Dendory/tarot`  
- **Contains:** 78 Tarot cards (upright/reversed), interpretations by topic  
- **Limitation:** Does not include zodiac or sentiment labels

### ✨ **Custom AI-Generated Dataset**  
- **Tool Used:** Gemini 1.5 Pro API  
- **Structure:**  
  - `zodiac_sign`  
  - `question` (categorized into 6 themes: love, profession, health, family, education, money)  
  - `card1`, `card2`, `card3` (randomized)  
  - `reading` (full Tarot prediction text)  
- **Generation Method:** 12 zodiac signs × 78 cards × 6 topics × 50 questions

---

## System Workflow  
```
User Input: [Birthdate, Question]
      ↓
Zodiac Conversion: Birthdate → Zodiac Sign
      ↓
Sentiment Analysis: Fine-tuned DistilBERT classifies user question → [positive, neutral, negative]
      ↓
Random Tarot Card Draws: Select card1, card2, card3
      ↓
Tarot Reading Generation:
   Flan-T5 model takes [zodiac, question_sentiment, card1, card2, card3] → Generates reading
      ↓
Personalized Tarot Reading
      ↓
Final Sentiment Analysis on Reading:
   DistilBERT model evaluates reading's emotional tone
```

---

## Model Training  

### 🧠 **Sentiment Analysis Models (DistilBERT)**
- **Question Sentiment Model**
  - Fine-tuned `distilbert-base-uncased` on labeled user questions  
  - Labels: `positive`, `neutral`, `negative`

- **Reading Sentiment Model**
  - Fine-tuned on labeled Tarot readings to assess emotional output

### 🔮 **Tarot Reading Generator (Flan-T5)**
- Fine-tuned `flan-t5-base` model  
- Trained on the AI-generated dataset with inputs:  
  `[zodiac_sign, question, question_sentiment, card1, card2, card3] → reading`

---

## Evaluation Metrics  

| Metric Type     | Metric         | Purpose                                          |
|-----------------|----------------|--------------------------------------------------|
| Automatic       | **ROUGE**      | Measures idea/content preservation               |
| Automatic       | **BERTScore**  | Evaluates semantic similarity to human readings |
| Human-Centric   | **Likert Scale Survey** | Realism, emotional tone, personalization |
| Human-Centric   | **Sentiment Alignment** | Checks emotional coherence between input and reading |

---

## Conclusion  
This project demonstrates a novel pipeline for **sentiment- and zodiac-aware Tarot reading generation** using modern NLP techniques. By combining **Flan-T5** and **DistilBERT** with an AI-generated dataset, it delivers readings that are **emotionally aligned**, **astrologically personalized**, and **engaging**, paving the way for next-gen AI-assisted fortune-telling.
