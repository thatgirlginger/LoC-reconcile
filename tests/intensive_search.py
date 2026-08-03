import nltk
import difflib

from nltk.stem import *
from nltk.metrics.distance import jaccard_distance
from nltk.corpus import words, stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

nltk.download('words')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

from tests.searches import *

'''this module is intended to replace LoC's didyoumean API, as there is no suitable open-source or fully free alternative

however, this also contains functions to stem words and search based on those stems and their synonyms. this particular function might not be the most useful for
names or other proper nouns, since it is made primarily with subjects in mind

i'm also sure OpenRefine's API extension could potentially be of more use for something like this, but i wanted to make this for practice with nltk
and for people who would prefer '''

# helper function: remove stop words and punctuation from a string and returning a list of the output
class Helpers:
    def __init__(self, text):
        self.text = text
    
    def remove_stops(self):
        # if istype list or string, modify
        tokens = word_tokenize(self.text.lower())
        stop_words = set(stopwords.words('english'))
        return [word for word in tokens if word not in stop_words]

# split phrases; based on punctuation or space; return anything that scores above a certain mark
# sim_ratio = str(round(float(difflib.SequenceMatcher(
#                 None, original.lower(), term).ratio()), 3))

# function to stem a input list of words or individual word? should be functional for both

# spell correction using jaccard distance; build function for a single word at a time returning possible hits




#def function(something):
#   if istype string:
#       strip punctuation
#       remove_stops()
#       split string by space
#   for something in the list:
#       