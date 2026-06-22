#!/usr/bin/env python3

"""
Prototype script to automate google dorks based on a list of keywords.

"""
import urllib.parse
from urllib.parse import urlencode
import pdb
import time
from pynput.keyboard import Key, Controller
import webbrowser
import itertools
from itertools import chain

"""
Loads .txt files and creates a search engine / website list.

"""

def load_engines():
    try:
        with open("search_engines.txt", "r") as r:
            lines = (line.rstrip() for line in r)
            engine_list = list(line for line in lines if line)
    except FileNotFoundError:
        engine_list = ["https://www.google.com/search?"]
    return engine_list

def load_websites():
    try:
        with open("websites.txt", "r") as r:
            lines = (line.rstrip() for line in r)
            website_list = list(line for line in lines if line)
    except FileNotFoundError:
        website_list = []
    return website_list


class MakeQueries:
    def __init__(self, word_data, sites, file_types):
        self.word_data = word_data
        self.sites = sites
        self.extensions = file_types


    def query_base(self):
        query_basic = ' '.join(self.word_data)
        query_AND = ' AND '.join(self.word_data)
        query_OR = ''.join(self.word_data[:1]) + ' AND (' + ' OR '.join(self.word_data[1:]) + ')'
        query_basic_quoted = ' '.join(f'"{words}"' for words in self.word_data)
        query_AND_quoted = ' AND '.join(f'"{words}"' for words in self.word_data)
        query_OR_quoted = ''.join(f'"{words}"' for words in self.word_data[:1]) + ' AND (' + ' OR '.join(f'"{words}"' for words in self.word_data[1:]) + ')'
        return [query_basic, query_AND, query_OR, query_basic_quoted, query_AND_quoted, query_OR_quoted]
    
    def append_site(self):    
        return [f'site:{site}' for site in self.sites]
    
    def append_file(self):
        return [f'filetype:{ext}' for ext in self.extensions]
       
    def site_query(self):
        sites = self.append_site()
        base = self.query_base()
        return [f"{s} {b}" for s, b in itertools.product(sites, base)]

    def file_types(self):
        files = self.append_file()
        base = self.query_base()
        return [f"{f} {b}" for f, b in itertools.product(files, base)]
        
    def in_text(self):
        base = self.query_base()
        return [f"intext:{b}" for b in base]
        
    def inurl_query(self):
        base = self.query_base()
        return [f"inurl:{b}" for b in base]
    
    def make_list(self):
        return list(
            self.query_base() +
            self.site_query() +
            self.file_types() +
            self.in_text() +
            self.inurl_query()
        )

def keyword_input():
    keywords = input("Enter keywords in order of importance seperated by commas(,): ")
    return [keyword.strip() for keyword in keywords.split(",")]

def make_url(query_load):
    keyboard = Controller()
    engine_list = load_engines()
    for engine in engine_list:
        for query in query_load:
            pdb.set_trace() # Execution will pause here
            query_body = {'q': query}
            search_url = engine + urlencode(query_body)
            search = webbrowser.open(search_url)
            time.sleep(5)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

 
def main():
    print("--------------DORKMASTER!!!------------------by Undonecan")

    keyword_list = keyword_input()
    sites = load_websites()
    file_types = ['".doc"', '".docx"', '".pdf"', '".xls"', '".xlsx"']

    query_setup = MakeQueries(keyword_list, sites, file_types)
    query_load = query_setup.make_list()
    
    print(f"Generated {len(query_load)} dork permutations. Launching in browser ...")
    make_url(query_load)
    
if __name__ == "__main__":
    main()

