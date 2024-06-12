# pip install flask nltk spacy transformers
# python -m spacy download en_core_web_sm


from flask import Flask, render_template, request, jsonify
import nltk
import spacy
from transformers import pipeline, Conversation, AutoTokenizer, AutoModelForCausalLM

# Download NLTK data
nltk.download('punkt')

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Initialize tokenizer with appropriate settings
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side='left')
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Initialize Huggingface transformers pipeline
chatbot = pipeline("conversational", model=model, tokenizer=tokenizer)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['message']
    # Create a Conversation object
    conversation = Conversation(user_input)
    # Use transformers to get the chatbot response
    response = chatbot(conversation)
    bot_response = response.generated_responses[0]
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)


