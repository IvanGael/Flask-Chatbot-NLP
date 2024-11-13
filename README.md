# Flask Chatbot

This project is a simple chatbot web app built using Python, Flask, and various NLP libraries such as NLTK, SpaCy, and transformers. The chatbot uses the Huggingface `transformers` library with the `microsoft/DialoGPT-medium` model to generate responses to user inputs. It also uses NLTK and SpaCy for additional text processing.

![Demo](demo.png)

## Installation

1. **Install the required dependencies:**

    ```
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```

2. **Download NLTK data:**

    ```
    python -c "import nltk; nltk.download('punkt')"
    ```

## Usage

```
py app.py
```

## How It Works

1. **Flask Server**: The Flask web server renders the HTML template and handles incoming POST requests to generate chatbot responses.

2. **NLP Processing**:
    - **NLTK**: Used for tokenizing the input message.
    - **SpaCy**: Used for named entity recognition (NER) and part-of-speech (POS) tagging.
    - **Transformers**: The chatbot uses the Huggingface `transformers` library with the `microsoft/DialoGPT-medium` model to generate responses to user inputs.

## Examples

Here are some example messages you can try with the chatbot:

- "Hello!"
- "What is your name?"
- "Can you tell me a joke?"
- "I like cats."
- "What's the meaning of life?"




