# Gaming Chatbot 🎮🧠

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-SentenceTransformers-orange)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)

A desktop **gaming assistant chatbot** built with Python and Tkinter.  
It uses **NLP-based semantic search** to understand user intent and provide intelligent responses about games, hardware, troubleshooting, and optimization.

---

## 📸 Screenshot

![App Screenshot](GamingScreenshot.png)

---

## 🛠 Features

- 🧠 Semantic intent detection using `SentenceTransformer (all-MiniLM-L6-v2)`
- 🎯 Smart gaming knowledge base (tips, fixes, recommendations)
- 🖥️ Clean Tkinter desktop UI (dark themed)
- ⚡ Fast local response system (no API required)
- 🔧 Hardware + performance optimization advice (GPU/CPU tuning, etc.)

---

## 🚀 How to Run

### 1. Clone the repository

git clone https://github.com/your-username/gaming-chatbot.git
cd gaming-chatbot

### 2. Install dependencies

pip install sentence-transformers torch

### 3. Run the program

python main.py

---

## 📝 Usage

- Type a gaming-related question into the input box
- The chatbot analyzes intent using NLP similarity matching
- It returns the most relevant response from its knowledge base
- Use **Send** to ask questions and **Clear Chat** to reset

---

## 📦 File Structure

gaming-chatbot/
├── main.py
├── chatbot_logic.py
├── README.md
├── requirements.txt
└── GamingScreenshot.png

---

## ⚙️ How It Works

1. User input is captured from the Tkinter GUI
2. SentenceTransformer converts text into embeddings
3. Cosine similarity is used to match intent with stored responses
4. Best-matching answer is returned instantly
5. UI updates in real time

---

## ⚡ Future Improvements

- Add larger gaming knowledge database
- Integrate live game data (patch notes / stats)
- Improve UI design with animations
- Add voice input/output
- Expand to web version

---

## 💻 Technologies

- Python 3.x
- Tkinter
- PyTorch
- SentenceTransformers
- NLP (semantic similarity)

---

## 📧 Contact

Created by **Mitsos** – feel free to contribute or open issues!
