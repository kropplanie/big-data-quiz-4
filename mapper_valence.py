#!/usr/bin/env python
import sys, re
import random
import requests
import string
import functools

stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
stopwords = list(set(stopwords_list.decode().splitlines()))


def remove_stopwords(words):
    list_ = re.sub(r"[^a-zA-Z0-9]", " ", words.lower()).split()
    return [itm for itm in list_ if itm not in stopwords]


def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return ' '.join(remove_stopwords(text))

def load_valence_scores(url):
    # load in the valence scores from the given url
    response = requests.get(url)
    return {word: int(score) for line in response.text.splitlines() for word, score in [line.split('\t')]}

def decode_bytes(input_data):
    return input_data.decode('utf-8', errors='replace') if isinstance(input_data, bytes) else input_data

def get_word_valences(words, valence_scores):
    return list(map(lambda word: valence_scores.get(word.lower(), 0), words))

def calc_valence(input_data):
    url = 'https://raw.githubusercontent.com/fnielsen/afinn/master/afinn/data/AFINN-en-165.txt'
    valence_scores = load_valence_scores(url)
    
    decoded_text = decode_bytes(input_data)  # Correctly decode input data

    # Remove non-printable characters from the decoded text
    decoded_text = re.sub(r'[\x00-\x1F\x7F]', '', decoded_text)
    
    cleaned_text = clean_text(decoded_text)  # Clean the processed text
    
    words = cleaned_text.split()  # Split cleaned text into words
    word_valences = get_word_valences(words, valence_scores)

    # Calculate the total valence using the reduce function
    total_valence, valid_count = functools.reduce(
        lambda acc, val: (acc[0] + val, acc[1] + (1 if val != 0 else 0)),
        word_valences,
        (0, 0)
    )
    
    return total_valence

def valence(text):
    return calc_valence(text)

def main(argv):
    total_word_count = 0  # Initialize total word count
    try:
        while True:
            line = clean_text(sys.stdin.readline())
            if not line:  # Check for EOF
                break
            
            valence_total = valence(line)
            total_word_count += len(line.split())  # Count words directly from the cleaned line
            
            print("LongValueSum:" + "president" + "\t" + str(valence_total))
        
        # Print the total word count as a special value
        print("__TOTAL__\t" + str(total_word_count))
        
    except EOFError:
        pass  # End of file reached
if __name__ == "__main__":
    main(sys.argv)
