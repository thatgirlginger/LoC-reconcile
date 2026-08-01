import nltk

nltk.download('words')
from nltk.stem import *
from nltk.metrics.distance import jaccard_distance
from nltk.corpus import words
from nltk.util import ngrams

from tests.searches import *

'''this module is intended to replace LoC's didyoumean API, as there is no suitable open-source or fully free alternative

however, this also contains functions to stem words and search based on those stems and their synonyms. this particular function might not be the most useful for
names or other proper nouns, since it is made primarily with subjects in mind

i'm also sure OpenRefine's API extension could potentially be of more use for something like this, but i wanted to make this for practice with nltk
and for people who would prefer '''

# helper function: remove stop words and punctuation from a string and returning a list of the output

# function to stem a input list of words or individual word? should be functional for both

# spell correction using jaccard distance; build function for a single word at a time returning possible hits