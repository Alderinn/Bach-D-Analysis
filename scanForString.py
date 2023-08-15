# The goal of this is to scan a directory for all of the txt files one at a time for a string
# then, save the findings to a csv to later be used on a graph
#CSV: season,episode,count
import mmap, os, csv
count=0
def searchData(directory='./data/Bachelorette'):
    phrase=input("Search term:") # Ex: 'for the right reason'
    with open('reults.csv','a') as f:
                write = csv.writer(f)
                write.writerow({'seasons': 'seasons', 'episode': 'episode', 'count':'count'})
                
    for filename in os.scandir(directory):
        #Extracting Season/Episode from title Ex: 06x01_-_Week_1_(Season_6).txt
        episodeNum = filename.name[3:5]
        seasonNum = filename.name[0:2]
        
        if filename.is_file():
            filename = directory +'/'+filename.name
            found_count = process(filename, phrase, count)
            # {episodeNum},{seasonNum},{Occurance}
            with open('reults.csv','a') as f:
                write = csv.writer(f)
                write.writerow({seasonNum: 'seasons', episodeNum: 'episode', found_count:'count'})
                print(f"Row for S{seasonNum}:E{episodeNum} added!")
def process(filename,searchTerm,count):
    # find {searchTerm} within {filename} and return {count}
        try:
            with open(filename, 'r') as file:
                content = file.read()
                found_count = content.count(searchTerm)
                print(f"Found: {found_count}")
                return found_count
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return False
# - Start
searchData()
