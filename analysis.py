import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import string, os

def process_text_document(file_path, phrase_length=2, n_most_common=10):
    # Step 1: Read the Text Document
    with open('data/'+file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Step 2: Tokenize the Text
    nltk.download('punkt')
    tokens = word_tokenize(text)
    

    # Step 3: Remove Punctuation and Lowercase
    tokens = [token.lower() for token in tokens if token.isalpha()]

    # Step 4: Calculate Phrase Frequencies
    phrases = [' '.join(tokens[i:i+phrase_length]) for i in range(len(tokens) - phrase_length + 1)]
    phrase_frequencies = Counter(phrases)

    # Step 5: Sort and Display Results
    n_most_common_phrases = phrase_frequencies.most_common(n_most_common)

    # Display the most common phrases and their frequencies
    for phrase, frequency in n_most_common_phrases:
        print(f'{phrase}: {frequency}')

    with open("outputs/"+'OUTPUT-'+str(phrase_length)+'-'+file_path, 'w', encoding='utf-8') as file:
        for phrase, frequency in n_most_common_phrases:
            file.write(f'{phrase}: {frequency}\n')

# Usage example
if __name__ == "__main__":

    directory = 'data/'
    phrase_length=int(input("Phrase Length:"))

    for filename in os.scandir(directory):
        if filename.is_file():
            process_text_document(filename.name, phrase_length, n_most_common=10)