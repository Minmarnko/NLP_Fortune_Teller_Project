# AI-Powered Tarot Reading Using NLP and Sentiment Analysis

## Project Overview  
This project explores the application of **Natural Language Processing (NLP)** and **sentiment-aware AI models** for **personalized Tarot readings**. Traditional Tarot readings rely on **human intuition and predefined interpretations**, but this research aims to **automate and personalize** the process using AI-driven text generation. By integrating **user input (questions & zodiac signs), sentiment detection (BERT), and a fine-tuned GPT-2 model**, we generate **refined and engaging Tarot readings**. The project aims to evaluate the **accuracy, engagement, personalization, and thematic coherence** of AI-generated fortune readings.

## Problem Statement  
Traditional fortune-telling methods are **static, template-based, and lack personalization**. Most existing **AI-generated Tarot readings** suffer from **generic content** due to the absence of user **sentiment adaptation** and **astrological insights**. Current models do not integrate **zodiac-based variations**, making them **less engaging** and **less believable**. This study addresses these challenges by designing an **AI-powered Tarot reading system** that adapts **predictions based on user sentiment and astrological features**.

## Research Questions  
This study aims to answer the following research questions:  
1. **How can sentiment-aware NLP models enhance the personalization of AI-generated Tarot readings?**  
2. **What is the impact of zodiac-based adaptation on the perceived authenticity of Tarot predictions?**  
3. **How does an AI-generated Tarot reading compare to human-created interpretations in terms of coherence and engagement?**  

## Dataset  
This project uses a combination of **structured Tarot reading texts, sentiment-annotated datasets, and user-specific features** to fine-tune AI models.  

### **Primary Dataset: Tarot Readings Dataset**  
- **Source:** Hugging Face ([tarot_readings.csv](https://huggingface.co/datasets/Dendory/tarot/blob/main/tarot_readings.csv))  
- **Contents:**  
  - Tarot card names (78 cards, upright and reversed)  
  - Interpretations (love, career, personal growth)  
  - General fortune-telling descriptions  

### **Extended Dataset: Personalized Tarot Dataset**  
- AI-generated dataset incorporating:  
  - **User Birth Date:** Mapped to zodiac signs for astrological context  
  - **Sentiment-Based Variations:** Tarot readings adapted for **positive, neutral, and negative moods**  
  - **Custom Fortune Templates:** AI-augmented texts for diverse and personalized readings  

### **Sentiment Analysis Training Dataset**  
- **Source:** Pre-existing sentiment-annotated datasets (for fine-tuning BERT)  
- **Purpose:** Helps classify user input sentiment before generating a reading  

## Methodology  
The proposed system follows a **structured NLP pipeline**, integrating **sentiment-aware response generation** and **astrological mappings**.  

### **1. System Workflow**  
1. **User Input:** The system receives a **question** and **zodiac sign**.  
2. **Preprocessing:** Tokenization, text cleaning, and Named Entity Recognition (NER) extract key features.  
3. **Sentiment Analysis (BERT):** Determines whether the user's tone is **positive, neutral, or negative**.  
4. **Tarot Model (Fine-tuned GPT-2):** Generates a Tarot reading tailored to **sentiment and zodiac sign**.  
5. **Output:** The final **refined Tarot reading** is presented to the user.  

### **2. Data Preprocessing**  
- **Tokenization & Cleaning:** Removing unwanted symbols, tokenizing text for AI processing  
- **Named Entity Recognition (NER):** Extracting **zodiac signs, user intent, and keywords**  
- **Sentiment Labeling:** Fine-tuning **BERT-based sentiment classifier** to label user queries  
- **Data Augmentation:** Generating **alternative Tarot readings** for model generalization  

### **3. Model Training**  
- **Sentiment Analysis Model (BERT-based classifier)**  
  - Fine-tune to classify **positive, neutral, or negative emotions**  
  - Helps adjust Tarot responses based on user sentiment  
- **Tarot Text Generation Model (Fine-tuned GPT-2)**  
  - Traine on the **Tarot Readings Dataset + Personalized Tarot Dataset**  
  - Generates **structured, meaningful, and personalized Tarot readings**  


### **5. Evaluation Metrics**  
- **Engagement Score:** Measures user interaction levels  
- **Text Coherence:** Ensures Tarot readings are fluent and logically structured  
- **Sentiment Alignment:** Checks if readings match the detected user sentiment  
- **Authenticity Perception:** Evaluates AI-generated readings vs. human-written Tarot texts  

## Conclusion  
This AI-powered Tarot reading system combines **NLP, sentiment analysis, and astrology-based modeling** to **personalize** and **enhance** fortune-telling experiences. By integrating **user sentiment and astrological influences**, this model aims to provide **engaging, context-aware, and interactive Tarot predictions**.  

---

