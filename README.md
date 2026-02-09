# Tiny Sentiment Classifier

A minimal, practical AI project that classifies text as **positive**, **negative**, or **neutral** using a lightweight Hugging Face model.

This project is intentionally small — perfect for beginners, job seekers, and anyone who wants a clean, real-world example of using pretrained AI models.

---

## 🚀 Features
- 10–15 lines of Python
- Uses a tiny pretrained model (no training required)
- Classifies any input text
- Clear, readable code

---

## 🧠 How It Works
The script loads a sentiment-analysis pipeline from the `transformers` library and runs inference on any text you provide. It returns:
- The predicted label  
- The confidence score  

---

## ▶️ Run It
```bash
pip install -r requirements.txt
python classifier.py

Enter text to classify: I love this project!
POSITIVE (0.999)

