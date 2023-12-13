# Word Vector Embedding API

## Overview
This project presents a simple yet effective Flask-based API that leverages spaCy's NLP capabilities to generate word vector embeddings. The API provides an intuitive interface for users to input a single word and receive its corresponding vector representation, a numerical array that captures the semantic essence of the word based on its usage.

## Features
- **Single Word Vector Generation**: Accepts a single word as input and returns its vector embedding as determined by spaCy's `en_core_web_lg` model.
- **Input Validation**: Ensures robust handling of the input, allowing only a single word and returning an informative error message if multiple words are entered.
- **User-Friendly Interface**: A simple and clean web form for user input, making the process of obtaining word vectors straightforward and accessible.
- **Informative Responses**: Alongside the vector data, the API provides a clear message about the success or failure of the vector retrieval process.

## How It Works
- **User Interface**: The user accesses a web form where they can enter a word.
- **API Processing**: Upon form submission, the Flask API processes the input using spaCy to extract the word's vector embedding.
- **Validation**: The back-end validates the input to ensure it's a single word. If more than one word is detected, an error message is returned.
- **Output**: If the input is valid, the API returns the vector embedding of the word as a JSON response.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework for serving the API and handling requests.
- **spaCy**: An open-source software library for advanced Natural Language Processing, used here for generating word vector embeddings.
- **HTML/CSS**: For the front-end form and styling.

## Installation and Usage
`pip install Flask spacy`  
`python -m spacy download en_core_web_lg`

## Run
`python app.py`  
The application should now be running on `http://127.0.0.1:5000/home`
