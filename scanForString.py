# The goal of this is to scan a directory for all of the txt files one at a time for a string
# then, save the findings to a csv to later be used on a graph
# CSV: season,episode,count
import os, csv


def searchData(directory: str = "./data/Bachelorette") -> None:
    '''
    Ask the user to enter a search term, then scan every file in the given directory path to generate a results.csv of the counts for each episode.
        Parameters:
            directory (str): directory path containing Bachelorette dialogue
        Returns:
            None
    '''
    phrase = input("Search term:")  # Ex: 'for the right reason'
    with open("results.csv", "a") as f:
        write = csv.writer(f)
        write.writerow({"season": "season", "episode": "episode", "count": "count"})

    for filename in os.scandir(directory):
        # Extracting Season/Episode from title Ex: 06x01_-_Week_1_(Season_6).txt
        episodeNum = filename.name[3:5]
        seasonNum = filename.name[0:2]

        if filename.is_file():
            filename = directory + "/" + filename.name

            try:
                found_count = process(filename, phrase)
                # {episodeNum},{seasonNum},{Occurance}
                with open("results.csv", "a") as f:
                    write = csv.writer(f)
                    write.writerow(
                        {
                            seasonNum: "season",
                            episodeNum: "episode",
                            found_count: "count",
                        }
                    )
                    print(f"Row for S{seasonNum}:E{episodeNum} added!")
            except:
                print("Failed to process:", filename)
                continue


def process(filepath: str, search_term: str) -> int:
    '''
    Returns the number of occurrences for the search_term at the given filepath
        Parameters:
            filepath (str): path of episode dialogue file to search
            searchTerm (int): Another decimal integer
        Returns:
            count (int): count of searchTerm occurrences in filepath.
    '''
    try:
        with open(filepath, "r") as file:
            content = file.read()
            count = content.count(search_term)
            print(f"Found: {count}")
            return count
    except Exception as e:
        print(f"Error while processing {filepath}: {e}")
        raise e
