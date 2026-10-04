# Traditional AI Rule-Based Chatbot

A beginner-friendly Python chatbot that answers computer science questions using a local JSON knowledge base. It uses regular-expression rules first, then TF-IDF and cosine similarity to find a close stored question. It does not use an LLM, an external AI API, deep learning, or neural networks.

## Techniques used

- **Text preprocessing:** lowercase conversion, punctuation cleanup, whitespace normalization, tokenization, and basic stop-word removal.
- **Rule-based reasoning:** hand-written IF-THEN behavior is represented by regular-expression patterns and predefined responses.
- **Knowledge representation:** categories, example questions, patterns, and answers are stored in `knowledge_base.json`.
- **Similarity matching:** scikit-learn creates TF-IDF vectors for stored questions and uses cosine similarity to rank a new question.
- **Fallback:** when no rule matches and the best similarity score is below `0.25`, the chatbot says: `Sorry, I don't understand that question yet.`

## Requirements

- Python 3.10 or newer
- Internet access for the first package installation

## Install on Windows

Open the project folder in VS Code, then open **Terminal → New Terminal**. Run these PowerShell commands from the project folder:

```powershell
python --version
python -m venv .venv
```

Activate the environment and install the packages:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, allow it for the current terminal session and retry:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

`requirements.txt` contains Gradio and scikit-learn. NLTK is not required by this version; text processing uses Python's built-in `re` module and a small local stop-word list.

## Run

With the virtual environment active, start the interface:

```powershell
python app.py
```

Open the local URL printed in the terminal, usually `http://127.0.0.1:7860`.

## Example questions

- What is artificial intelligence?
- Explain a rule-based system
- What is a Python dictionary?
- What is the difference between the internet and the web?
- How should I prepare for a viva?

The initial knowledge base contains more than 50 entries across greetings, AI, programming, data structures, databases, networks, operating systems, cybersecurity, college projects, study tips, and related topics.

## Project architecture

```text
traditional_ai_chatbot/
├── app.py                 Gradio interface
├── chatbot.py             Rule matching and TF-IDF response selection
├── nlp.py                 Text cleaning and token helpers
├── knowledge_base.json    Questions, regex patterns, categories, responses
├── requirements.txt       External Python packages
├── README.md              Setup and project guide
└── utils/
	└── helpers.py         JSON file loading helper
```

Message flow:

1. The interface passes the user's text to the chatbot.
2. The chatbot normalizes it and checks the knowledge base's regex patterns.
3. If no rule matches, it compares the text to stored questions using TF-IDF and cosine similarity.
4. It returns the closest answer if the score reaches the threshold; otherwise, it returns the fallback message.

## Limitations

This is a small educational chatbot, not a general-purpose conversational AI. It can only answer from its predefined knowledge base, and similarity matching can choose an imperfect answer. Add new entries to the JSON file to expand its subject coverage.
