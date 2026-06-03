# AI Website Assistant

## Project Overview

AI Website Assistant is a console-based chatbot that answers questions based on website content using Natural Language Processing (NLP).

The application scrapes website content, stores the extracted information locally, and uses a Hugging Face Question Answering model to generate relevant answers from the website data.

---

## Features

* Website content scraping
* Content cleaning and preprocessing
* AI-powered question answering
* Console-based chatbot interface
* Hugging Face NLP model integration
* Local storage using Pickle

---

## Technologies Used

* Python
* BeautifulSoup
* Requests
* HTTPX
* Hugging Face Inference API
* Pickle
* NLP (Question Answering)

---

## Project Structure

```text
AI_Website_Assistant/
│
├── chatbot.py
├── scraper.py
├── data_store.pkl
├── data_viewer.py
├── process_steps.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. The scraper extracts content from a website.
2. The extracted text is cleaned and processed.
3. The processed content is stored locally using Pickle.
4. The chatbot loads the stored website context.
5. User questions and website context are sent to the Hugging Face Question Answering API.
6. The model extracts the most relevant answer and returns it to the user.

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Website Scraper

```bash
python scraper.py
```

Enter the website URL when prompted.

---

## Run Chatbot

```bash
python chatbot.py
```

Ask questions related to the scraped website content.

---

## Example Questions

* What is BotPenguin?
* What services are provided?
* What platforms are supported?
* Does the platform support WhatsApp automation?

---

## Future Improvements

* Multi-page website crawling
* Semantic search
* Vector database integration
* Retrieval-Augmented Generation (RAG)
* Web-based frontend

---

## Author

Rahul Chauhan
