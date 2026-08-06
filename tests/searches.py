# for testing: import relevant searching functions
from LoCreconcile import SearchLoC, Recon
import difflib
import pandas as pd

from intensive_search import *

sample = pd.read_csv("sample_data.csv")
test_terms = sample["term"].to_list()


for term in test_terms:
    type = "Subject"
    tsearch = Helpers(term).remove_stops()
    to_search = []
    for p in tsearch:
        to_search.append(corrections(p))