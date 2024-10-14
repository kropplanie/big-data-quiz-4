import sys
import re
import string
import functools
import requests

# Load stopwords list and valence scores at startup
def load_stopwords():
    stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
    return list(set(stopwords_list.decode().splitlines()))

def load_valence_scores():
    url = 'https://raw.githubusercontent.com/fnielsen/afinn/master/afinn/data/AFINN-en-165.txt'
    response = requests.get(url)
    return {word: int(score) for line in response.text.splitlines() for word, score in [line.split('\t')]}

# Define processing functions
def remove_stopwords(words, stopwords):
    list_ = re.sub(r"[^a-zA-Z0-9]", " ", words.lower()).split()
    return [itm for itm in list_ if itm not in stopwords]

def clean_text(text, stopwords):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return ' '.join(remove_stopwords(text, stopwords))

def decode_bytes(input_data):
    return input_data.decode('utf-8', errors='replace') if isinstance(input_data, bytes) else input_data

def get_word_valences(words, valence_scores):
    return list(map(lambda word: valence_scores.get(word.lower(), 0), words))

def calc_valence(input_data, stopwords, valence_scores):
    decoded_text = decode_bytes(input_data)
    decoded_text = re.sub(r'[\x00-\x1F\x7F]', '', decoded_text)
    cleaned_text = clean_text(decoded_text, stopwords)
    words = cleaned_text.split()
    word_valences = get_word_valences(words, valence_scores)

    total_valence, valid_count = functools.reduce(
        lambda acc, val: (acc[0] + val, acc[1] + (1 if val != 0 else 0)),
        word_valences,
        (0, 0)
    )

    return total_valence

def main():
    stopwords = load_stopwords()
    valence_scores = load_valence_scores()

    for line in sys.stdin:
        line = line.strip()
        if line:  # Only process non-empty lines
            president = line.split()[0]  # Assuming the first word is the key
            valence_score = calc_valence(line, stopwords, valence_scores)
            print(f"LongValueSum:{president}\t{valence_score}")

if __name__ == "__main__":
    main()
