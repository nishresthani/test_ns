import spacy
from langdetect import detect
import logging
 
# Create and configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger()
def language_detect(text):
    lang = detect(text)
    return lang


def extract_ner(sentence):
    lang = language_detect(sentence)
    # lang = "abc"
    try: 
        logger.info(f"detecetd language: {lang}")
        logger.info("processing NER")
        if lang=="en":
            nlp = spacy.load(lang+'_core_web_sm')
        else:
            nlp = spacy.load(lang+'_core_news_sm')
        doc = nlp(sentence)
        for ent in doc.ents:
            print(ent.text, ent.label_, ent.start_char, ent.end_char)
    except Exception as e:
        logger.error(f"language {lang} does not support")

# sentence = "Apple is looking at buying U.K. startup for $1 billion"
sentence = "ik ben Niraj Shrestha van Leuven."
extract_ner(sentence)


