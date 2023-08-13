import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import string, os

def process(file_path, phrase_length=2, n_most_common=10):
    # Step 1: Read the Text Document
    with open('data/'+file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the Text
    nltk.download('punkt')
    tokens = word_tokenize(text)
    

    # Remove Punctuation and Lowercase
    tokens = [token.lower() for token in tokens if token.isalpha()]

    # Calculate Phrase Frequencies
    phrases = [' '.join(tokens[i:i+phrase_length]) for i in range(len(tokens) - phrase_length + 1)]
    phrase_frequencies = Counter(phrases)

    # Sort and Display Results
    n_most_common_phrases = phrase_frequencies.most_common(n_most_common)

    # Display the most common phrases and their frequencies
    for phrase, frequency in n_most_common_phrases:
        print(f'{phrase}: {frequency}')

    with open("outputs/"+'OUTPUT-'+str(phrase_length)+'-'+file_path, 'w', encoding='utf-8') as file:
        for phrase, frequency in n_most_common_phrases:
            file.write(f'{phrase}: {frequency}\n')
            
def ExportCollectiveReports():
    directory = 'data/'
    phrase_length=int(input("Phrase Length:"))

    for filename in os.scandir(directory):
        if filename.is_file():
            process(filename.name, phrase_length, n_most_common=10)

