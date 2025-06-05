# Import your library for testing
from cdstemplate import stopword_list

import nltk
import pytest
from nltk.corpus import stopwords

# Ensure stopwords are downloaded before running tests
nltk.download('stopwords', quiet=True)

@pytest.fixture
def nltk_stopwords():
    return set(stopwords.words('english'))

def test_stopwords_count(nltk_stopwords):
    # NLTK English stopwords list usually has more than 100 words
    assert len(nltk_stopwords) > 100

def test_common_stopwords(nltk_stopwords):
    for word in ['the', 'is', 'and', 'to', 'in']:
        assert word in nltk_stopwords

def test_uncommon_word_absence(nltk_stopwords):
    assert 'banana' not in nltk_stopwords