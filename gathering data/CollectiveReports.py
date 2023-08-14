import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import string, os
import csv



def combineDatasets(file_path):
    with open('data/'+file_path, 'r', encoding='utf-8') as file:
        text = file.read()
         # Tokenize the Text
        nltk.download('punkt')
        tokens = word_tokenize(text)

        # Remove Punctuation and Lowercase
        tokens = [token.lower() for token in tokens if token.isalpha()]
        # print(f'Tokenized {file_path} successfully!')


        return tokens

def ExportCollectiveReports():
    directory = 'data/'
    collective = []
    totalwords = 0
    wrdCnt = 0
    phrase_length = int(input("Number of phrases: "))
    n_most_common = 100

    for filename in os.scandir(directory):
        if filename.is_file():
            for x in combineDatasets(filename.name):
                collective.append(x)
                wrdCnt += 1
        # print(f" {wrdCnt} words in: {filename.name}")

        totalwords = totalwords + wrdCnt


    # Calculate Phrase Frequencies
    phrases = [' '.join(collective[i:i+phrase_length]) for i in range(len(collective) - phrase_length + 1)]
    # print(f"Phrases: {phrases}")
    phrase_frequencies = Counter(phrases)
    # print(f"Phrase_Frequencies: {phrase_frequencies}")


    # Sort and Display Results
    n_most_common_phrases = phrase_frequencies.most_common(n_most_common)


    with open(f'{filename.name}.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(n_most_common_phrases)



