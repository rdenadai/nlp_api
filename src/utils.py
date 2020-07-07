import logging
import logging.config
from unicodedata import normalize
from string import punctuation
from functools import lru_cache

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy


@lru_cache(maxsize=256)
def is_number(s):
    try:
        complex(s)  # for int, long, float and complex
    except ValueError:
        return False
    return True


@lru_cache(maxsize=256)
def get_stopwords():
    stpwords = stopwords.words("portuguese")
    punkt = [pk for pk in punctuation]
    rms = ["um", "não", "mais", "muito", "sem", "estou", "sou"]
    for rm in rms:
        del stpwords[stpwords.index(rm)]
    for rm in ["?"]:
        del punkt[punkt.index(rm)]
    return stpwords, punkt


@lru_cache(maxsize=256)
def remover_acentos(txt):
    return normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII")


def parser(phrase):
    info = []
    if len(phrase):
        phrase = remover_acentos(phrase.lower())
        for punkt in punctuation:
            phrase = phrase.replace(punkt, " ")
    for word in word_tokenize(phrase):
        if not is_number(word) and len(word) > 0:
            token = NLP_PARSER(word)[0]
            info.append(
                {
                    "word": word,
                    "stem_rslp": RSLP_STEMMER.stem(word),
                    "stem_snowball": SNOWBALL_STEMMER.stem(word),
                    "lemma": token.lemma_,
                    "type": token.pos_,
                    "is_stopword": token.is_stop,
                }
            )
    return info


gunicorn_logger = logging.getLogger("gunicorn.error")
NLP_PARSER = spacy.load("pt")
RSLP_STEMMER = nltk.stem.RSLPStemmer()
SNOWBALL_STEMMER = nltk.stem.SnowballStemmer("portuguese")
STOPWORDS, PUNCT = get_stopwords()
