import re

from flask import Flask, request, jsonify, render_template
import spacy

nlp = spacy.load("en_core_web_lg")

app = Flask(__name__)


@app.route('/home', methods=['GET'])
def home():
    """"" This route provides the user interface for the application, displaying a simple and user-friendly form
    where users can input a word to retrieve its vector embedding."""
    return render_template('home.html')


@app.route('/calculate_embedding', methods=['POST'])
def calculate_embedding():
    """
       Extracts the vector embedding for a single word input.
       This function takes a single word submitted through a form, processes it with spaCy to obtain
       its vector representation if available, and returns the vector as a JSON response.
        If the word does not have an associated vector in the spaCy model, it returns an error message.
       """
    word = request.form['word']
    # Check if the input is more than one word
    # Ensures data integrity and handles cases where front-end validation is bypassed.
    split_text = re.split(r'\W+', word)
    if len(split_text) > 1:
        return jsonify(error="Please enter only one word."), 400
    processed_text = nlp(word)

    # Check if the token has a vector representation.

    if processed_text.has_vector:

        vector = processed_text.vector
        return jsonify({
            "word": word,
            "vector": vector.tolist(),
            "message": "Vector representation of the word successfully retrieved."
        })
    else:
        return jsonify(error=f"The word '{word}' does not have an associated vector."), 400


if __name__ == '__main__':
    app.run(debug=True)
