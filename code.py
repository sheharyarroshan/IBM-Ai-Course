pip install deep_translator
# translator.py
from deep_translator import MyMemoryTranslator

def english_to_french(text):
    translator = MyMemoryTranslator(source='en', target='fr')
    return translator.translate(text)

def french_to_english(text):
    translator = MyMemoryTranslator(source='fr', target='en')
    return translator.translate(text)

# Unit Tests
import unittest

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")
        self.assertNotEqual(result, "Hola")

    def test_french_to_english(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")
        self.assertNotEqual(result, "Hola")

if __name__ == '__main__':
    unittest.main()
# server.py
from flask import Flask, request, jsonify
from your_package.translator import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/translate/english-to-french', methods=['POST'])
def translate_english_to_french():
    data = request.json
    text = data['text']
    result = english_to_french(text)
    return jsonify({"translation": result})

@app.route('/translate/french-to-english', methods=['POST'])
def translate_french_to_english():
    data = request.json
    text = data['text']
    result = french_to_english(text)
    return jsonify({"translation": result})

if __name__ == '__main__':
    app.run(debug=True)
