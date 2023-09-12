# Fix to serve js files as js, not as text/plain.
import mimetypes
mimetypes.add_type('application/javascript', '.js')

from flask import Flask, request, render_template
from flask_cors import CORS
from transformers import pipeline

app = Flask( __name__, static_url_path='', static_folder='dist', template_folder='dist')
CORS(app)

pipe = pipeline("translation_en_to_fi", model="Helsinki-NLP/opus-mt-en-fi")

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_api():
    max_length = 460

    data = request.json
    text = data['text']
    print(text)

    if len(text) > max_length:
        return { 'translation': 'The length of your text is ' + str(len(text)) + ', the max length for this model is 460'}
    
    result = pipe(text)
    translation = result[0]['translation_text']
    print(translation)
    
    response = {
        'translation': translation
    }
    
    return response

if __name__ == "__main__":
    app.run(debug = True)