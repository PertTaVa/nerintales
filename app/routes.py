from flask import Blueprint, render_template, request
from src.extract_entities import extract_entities

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    entities = None
    text = ''
    lang = ''
    if request.method == 'POST':
        text = request.form.get('text')
        lang = request.form.get('lang')
        if text and lang:
            entities = extract_entities(text, lang)
    return render_template('index.html', entities=entities, text=text, lang=lang)
