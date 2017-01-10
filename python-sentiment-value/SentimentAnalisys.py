'''import json for reading json formatted sentiment analysis dicts'''
import json

import sys

def start(words):
    run = True
    '''logic for checking if word in input'''
    
    try:
        with open(words, "r") as infile:
            loaded_words = json.loads(infile.read())
    except FileNotFoundError:
        print('Couldn\'t find specified file! Make sure you put the right path!\n') 
        run = False
        print('Exiting Program...')
        sys.exit(0)
    print("You can load any json formatted dict sentiment analysis! Defualt is AFINN-111.\nYou can exit the program at any time by typing \"exit\"\n")
    
    while run is True:
        words_to_anaylize = input("Check the Sentiment Value of: ")
        if words_to_anaylize.lower() in loaded_words:
            print('The Sentiment Value of {} is'.format(words_to_anaylize.lower()),
                  loaded_words[words_to_anaylize.lower()], '\n')
        elif words_to_anaylize in ['exit', 'quit', 'stop']:
            print('Exiting Program...')
            run = False
        else:
            print('Sorry {} wasn\'t found in the current index!'.format(words_to_anaylize.lower()))

def load_file():
    '''user loaded sentiment analysis files'''
    load_analysis = input("Type path to sentiment analysis file.\n(leave blank for default)")
    if load_analysis != '':
        print('Loading JSON file.\n')
        start("Word-Dicts/" + load_analysis)
    else:
        print('Loading default JSON file.\n')
        start("Word-Dicts/AFINN-111.json")

load_file()
