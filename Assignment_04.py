###  Assignment No 4 ###

"""Assignment Title : Implement Bi-gram, Tri-gram word sequence and its count in text input
data using NLTK library"""


import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def preprocess_text(text, remove_stopwords=False, remove_punctuation=True):
    """Preprocess text for n-gram analysis"""
    # Tokenize
    tokens = word_tokenize(text.lower())
    
    # Remove punctuation
    if remove_punctuation:
        tokens = [token for token in tokens if token not in string.punctuation]
    
    # Remove stopwords
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]
    
    return tokens

def generate_ngrams_with_count(text, n):
    """Generate n-grams and count their frequencies"""
    tokens = preprocess_text(text)
    ngram_list = list(ngrams(tokens, n))
    ngram_counts = Counter(ngram_list)
    return ngram_list, ngram_counts

def display_ngrams(ngram_type, ngram_list, ngram_counts, top_n=10):
    """Display n-grams and their counts"""
    print(f"\n{'='*60}")
    print(f"{'*'*15}   {ngram_type.upper()}    {'*'*15}")
    print(f"{'='*60}")
    
    print(f"\nAll {ngram_type}s generated:")
    print("-" * 40)
    for i, item in enumerate(ngram_list, 1):
        print(f"{i:2d}. {item}")
    
    print(f"\n{ngram_type.capitalize()} Frequency Count:")
    print("-" * 40)
    print(f"Total unique {ngram_type}s: {len(ngram_counts)}")
    print(f"Total {ngram_type}s: {sum(ngram_counts.values())}")
    
    print(f"\nMost frequent {ngram_type}s (Top {min(top_n, len(ngram_counts))}):")
    print("-" * 40)
    for i, (ngram, count) in enumerate(ngram_counts.most_common(top_n), 1):
        print(f"{i:2d}. {ngram} → Count: {count}")

# Sample text data
text_data = """
Earth is the third planet from the Sun in our solar system and the only known celestial 
body to support life. With a diverse range of ecosystems, it is home to a vast array of 
plant and animal species, including humans. The planet has one natural satellite, the Moon, 
which influences Earth's tides and stabilizes its axial tilt. Earth's atmosphere consists 
of nitrogen, oxygen, and trace amounts of other gases, creating a protective layer that 
supports life and regulates temperature. The planet's surface is about 71% water and 29% land, 
with the water bodies including oceans, seas, lakes, and rivers. Earth's climate varies from 
tropical to polar regions, supporting different types of ecosystems and biodiversity.
"""

print("ASSIGNMENT 4: N-GRAM ANALYSIS WITH FREQUENCY COUNTING")
print("=" * 60)
print("Analyzing Bi-gram, Tri-gram word sequences and their counts using NLTK")

# UNIGRAM ANALYSIS
print("\n" + "="*60)
print("STARTING N-GRAM ANALYSIS...")
print("="*60)

unigram_list, unigram_counts = generate_ngrams_with_count(text_data, 1)
display_ngrams("unigram", unigram_list, unigram_counts, 15)

# BIGRAM ANALYSIS
bigram_list, bigram_counts = generate_ngrams_with_count(text_data, 2)
display_ngrams("bigram", bigram_list, bigram_counts, 15)

# TRIGRAM ANALYSIS
trigram_list, trigram_counts = generate_ngrams_with_count(text_data, 3)
display_ngrams("trigram", trigram_list, trigram_counts, 15)

# SUMMARY STATISTICS
print(f"\n{'='*60}")
print("SUMMARY STATISTICS")
print(f"{'='*60}")
print(f"{'N-gram Type':<12} {'Total':<8} {'Unique':<8} {'Most Frequent':<35} {'Count':<5}")
print("-" * 70)

# Most frequent items
most_frequent_unigram = unigram_counts.most_common(1)[0] if unigram_counts else ("None", 0)
most_frequent_bigram = bigram_counts.most_common(1)[0] if bigram_counts else ("None", 0)
most_frequent_trigram = trigram_counts.most_common(1)[0] if trigram_counts else ("None", 0)

print(f"{'Unigram':<12} {len(unigram_list):<8} {len(unigram_counts):<8} {str(most_frequent_unigram[0]):<35} {most_frequent_unigram[1]:<5}")
print(f"{'Bigram':<12} {len(bigram_list):<8} {len(bigram_counts):<8} {str(most_frequent_bigram[0]):<35} {most_frequent_bigram[1]:<5}")
print(f"{'Trigram':<12} {len(trigram_list):<8} {len(trigram_counts):<8} {str(most_frequent_trigram[0]):<35} {most_frequent_trigram[1]:<5}")

print(f"\n{'='*60}")
print("ANALYSIS COMPLETE!")
print(f"{'='*60}")


'''
************    OUTPUT    ********************

***********   UNIGRAM    ************************
('Earth',)
('is',)
('the',)
('third',)
('planet',)
('from',)
('the',)
('Sun',)
('in',)
('our',)
('solar',)
('system',)
('and',)
('the',)
('only',)
('known',)
('celestial',)
('body',)
('to',)
('support',)
('life.',)
('With',)
('a',)
('diverse',)
('range',)
('of',)
('ecosystems,',)
('it',)
('is',)
('home',)
('to',)
('a',)
('vast',)
('array',)
('of',)
('plant',)
('and',)
('animal',)
('species,',)
('including',)
('humans.',)

***********   BIGRAM    ************************
('Earth', 'is')
('is', 'the')
('the', 'third')
('third', 'planet')
('planet', 'from')
('from', 'the')
('the', 'Sun')
('Sun', 'in')
('in', 'our')
('our', 'solar')
('solar', 'system')
('system', 'and')
('and', 'the')
('the', 'only')
('only', 'known')
('known', 'celestial')
('celestial', 'body')
('body', 'to')
('to', 'support')
('support', 'life.')
('life.', 'With')
('With', 'a')
('a', 'diverse')
('diverse', 'range')
('range', 'of')
('of', 'ecosystems,')
('ecosystems,', 'it')
('it', 'is')
('is', 'home')
('home', 'to')
('to', 'a')
('a', 'vast')
('vast', 'array')
('array', 'of')
('of', 'plant')
('plant', 'and')
('and', 'animal')
('animal', 'species,')
('species,', 'including')
('including', 'humans.')

***********   TRIGRAM    ************************
('Earth', 'is', 'the')
('is', 'the', 'third')
('the', 'third', 'planet')
('third', 'planet', 'from')
('planet', 'from', 'the')
('from', 'the', 'Sun')
('the', 'Sun', 'in')
('Sun', 'in', 'our')
('in', 'our', 'solar')
('our', 'solar', 'system')
('solar', 'system', 'and')
('system', 'and', 'the')
('and', 'the', 'only')
('the', 'only', 'known')
('only', 'known', 'celestial')
('known', 'celestial', 'body')
('celestial', 'body', 'to')
('body', 'to', 'support')
('to', 'support', 'life.')
('support', 'life.', 'With')
('life.', 'With', 'a')
('With', 'a', 'diverse')
('a', 'diverse', 'range')
('diverse', 'range', 'of')
('range', 'of', 'ecosystems,')
('of', 'ecosystems,', 'it')
('ecosystems,', 'it', 'is')
('it', 'is', 'home')
('is', 'home', 'to')
('home', 'to', 'a')
('to', 'a', 'vast')
('a', 'vast', 'array')
('vast', 'array', 'of')
('array', 'of', 'plant')
('of', 'plant', 'and')
('plant', 'and', 'animal')
('and', 'animal', 'species,')
('animal', 'species,', 'including')
('species,', 'including', 'humans.')

'''
