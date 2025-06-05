# Adding a stopword list using nltk library

# Importing the libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Downloading the stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

# Default Stopwords
default_stopwords = set(stopwords.words('english'))
print(f"Default Stopwords: {len(default_stopwords)} words")

# Print the stopwords as a sorted list
print("List of NLTK English Stopwords:")
print(sorted(default_stopwords))