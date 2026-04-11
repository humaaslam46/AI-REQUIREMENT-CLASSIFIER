# 🧠 AI Requirement Classifier

> An intelligent NLP-powered web application that automatically classifies software requirements into structured categories — saving time, reducing manual effort, and improving requirement engineering workflows.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat-square&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🚀 Live Demo

👉 **[Launch App](https://ai-requirement-classifier-swwi26kx5v8ynreluhfkzc.streamlit.app/)** 

---

## 📌 Overview

Software requirement classification is a critical but tedious step in requirement engineering. This project uses **Natural Language Processing (NLP)** and a **Naive Bayes classifier** trained on labeled requirement data to instantly predict the type of any given requirement.

### What it classifies:

| Code | Category | Description |
|------|----------|-------------|
| `FR` | Functional Requirement | What the system must **do** |
| `NFR` | Non-Functional Requirement | How the system must **perform** |
| `PE` | Performance Requirement | Speed, throughput, response time |
| `US` | Usability Requirement | Ease of use and accessibility |
| `A` | Assumption | Conditions assumed to be true |
| `L` | Limitation | Explicit system constraints |
| `PO` | Policy Requirement | Legal, regulatory, or organizational rules |

---

## ✨ Features

- ⚡ **Real-time prediction** — instant classification as you type
- 📊 **Confidence score** — shows model certainty for each prediction
- 📘 **Full explanations** — each category includes a plain-English description
- 🎨 **Clean interactive UI** — built with Streamlit, no setup required for end users
- 🔤 **NLP-based** — uses TF-IDF vectorization for robust text understanding
- 📂 **Category reference panel** — all 7 categories always visible on screen

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| ML Model | Naive Bayes (`MultinomialNB`) |
| Vectorizer | TF-IDF (`TfidfVectorizer`) |
| Label Encoding | `LabelEncoder` (scikit-learn) |
| Web Framework | Streamlit |
| Model Persistence | Pickle |

---

## ⚙️ How It Works

```
User Input (text)
      │
      ▼
TF-IDF Vectorizer  ──→  Converts text into numerical feature vector
      │
      ▼
Naive Bayes Model  ──→  Predicts requirement category
      │
      ▼
Label Encoder      ──→  Maps prediction back to human-readable label
      │
      ▼
Result displayed with category name, code, description & confidence score
```

1. User types or pastes a software requirement
2. Text is preprocessed and converted into a TF-IDF feature vector
3. The trained Naive Bayes model predicts the category
4. The label encoder maps the numeric prediction back to a category code
5. The UI displays the full category name, description, and confidence score

---

## 📂 Project Structure

```
AI-Requirement-Classifier/
│
├── app.py                  # Main Streamlit application
├── re_nb_model.pkl         # Trained Naive Bayes model
├── tfidf_vectorizer.pkl    # Fitted TF-IDF vectorizer
├── label_encoder.pkl       # Fitted label encoder
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ▶️ Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/your-username/AI-Requirement-Classifier.git

# 2. Navigate into the project folder
cd AI-Requirement-Classifier

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

### Requirements.txt (minimum)

```
streamlit
scikit-learn
numpy
```

---

## 📊 Example Inputs & Outputs

| Requirement Text | Predicted Category |
|-----------------|-------------------|
| *"The system shall allow users to log in using email and password."* | ✅ FR — Functional Requirement |
| *"The system must respond to all requests within 2 seconds under normal load."* | ✅ PE — Performance Requirement |
| *"The UI shall be operable by users with no technical background."* | ✅ US — Usability Requirement |
| *"The system shall be available 99.9% of the time."* | ✅ NFR — Non-Functional Requirement |
| *"We assume all users will have internet access."* | ✅ A — Assumption |
| *"All data storage must comply with GDPR regulations."* | ✅ PO — Policy Requirement |
| *"The system does not support offline mode."* | ✅ L — Limitation |

---

## 🧪 Model Details

- **Algorithm:** Multinomial Naive Bayes — well-suited for text classification tasks
- **Vectorization:** TF-IDF (Term Frequency–Inverse Document Frequency) captures word importance relative to the dataset
- **Training data:** Labeled software requirement dataset with 7 categories
- **Persistence:** Model, vectorizer, and encoder saved as `.pkl` files using Python's `pickle` module for fast loading at runtime

---

## 🗺️ Roadmap

- [x] Real-time single requirement classification
- [x] Confidence score display
- [x] Category reference panel
- [ ] Bulk classification via CSV upload
- [ ] Model accuracy improvements (SVM, BERT)
- [ ] Export results to CSV / PDF
- [ ] REST API endpoint for integration
- [ ] Support for more requirement categories
- [ ] Dark / light mode toggle

---

## 👩‍💻 Developed By

**Huma**  
AI & Machine Learning Enthusiast 🚀  
*Built as part of an NLP & Machine Learning project*

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

> ⭐ If you found this project helpful, please give it a star on GitHub — it means a lot!
