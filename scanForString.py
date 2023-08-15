import mmap, os, csv


def searchData(directory='./data/Bachelorette'):
    phrase=input("Search term:")
    
    for filename in os.scandir(directory):

        episodeNum = filename.name[3:5]
        seasonNum = filename.name[0:2]
        count=5
        if filename.is_file():
            filename = directory +'/'+filename.name
            print(f"Checking: {str(filename)} for {phrase} ...")
            process(filename, phrase)
            # {episodeNum},{seasonNum},{Occurance}
            with open('reults.csv','a') as f:
                write = csv.writer(f)
                write.writerow({seasonNum: 'seasons', episodeNum: 'episode', count:'count'})
                print(f"Row for {filename} added!")



def process(filename,phrase):
    with open(filename, 'rb', 0) as file:
        s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        print('Searching for: '+ phrase)
        phrase = bytes(phrase, encoding='utf-8')
        if s.find(phrase) != -1:
            print(f'Found! in {filename}')


# - Start
searchData()
