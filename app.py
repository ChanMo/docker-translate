import os
import tempfile
import subprocess as sp
from werkzeug.utils import secure_filename
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return 'Welcome to chanmo/translate'

@app.route('/list-languages')
def list_languages():
    res = sp.run(['trans', '-list-codes'], capture_output=True, check=True)
    return res.stdout.decode('utf8').strip().split('\n')

@app.route("/translate/<source>/<target>", methods=['POST'])
def translate(source, target):
    if source == target:
        return 'the source language cannot be the same as the target language.', 400

    content = request.form.get('content')
    if not content:
        return 'the content is required.', 400

    output = sp.run(['trans', f'{source}:{target}', content], capture_output=True, check=True)
    return output.stdout
