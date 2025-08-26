import spacy
import stanza

# Загрузка моделей
nlp_ru = spacy.load("ru_core_news_sm")

# Инициализация stanza для финского и шведского
stanza.download('fi')
stanza.download('sv')
nlp_fi = stanza.Pipeline('fi', processors='tokenize,ner', use_gpu=False)
nlp_sv = stanza.Pipeline('sv', processors='tokenize,ner', use_gpu=False)

def extract_entities(text, lang):
    if lang == 'ru':
        doc = nlp_ru(text)
        return [(ent.text, ent.label_) for ent in doc.ents]
    elif lang == 'fi':
        doc = nlp_fi(text)
        entities = []
        for sent in doc.sentences:
            for ent in sent.ents:
                entities.append((ent.text, ent.type))
        return entities
    elif lang == 'sv':
        doc = nlp_sv(text)
        entities = []
        for sent in doc.sentences:
            for ent in sent.ents:
                entities.append((ent.text, ent.type))
        return entities
    else:
        return [("Язык не поддерживается", "N/A")]
