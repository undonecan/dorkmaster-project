## DORKMASTER

Dorkmaster is a command-line tool that utilizes Python's webbrowser and pdb modules to automate a succession of Google dorks based on user keywords. 

## ABOUT DORKMASTER

This is a personal OSINT tool designed to simplify Google dorking. It takes a list of keywords and creates dorked queries. Because it is not a traditional scraper, it significantly reduces the risk of rate limits and IP bans.

This script utilizes websites.txt and search_engines.txt, both of which are editable files. websites.txt contains the list of different domains to be used in the "site:" dork, while search_engines.txt contains a list of search engines that will be used by the webbrowser module (NOTE: not all web browsers are compatible with this program).

The default is to have the program pause via pdb.set_trace() after each query, so please familiarize yourself with the pdb debugger's simple commands (namely continue, skip, and exit). 

To forgo pdb, comment out the pdb line in main.py. This will simulate keystrokes searching each dorked query in succession. Each search is on a default 5 second timer in a separate tab.

## REQUIREMENTS

Python 3.x + standard library (urllib.parse, pdb, time, webbrowser, itertools) + pynput 
install pynput with:

pip install pynput

or

run uv add pynput

## USAGE

For easiest install, clone the repo and use uv: 

uv sync 

and 

uv run main.py

Or, once you have the source code and all dependencies are installed, navigate to the program's root folder and run it with:

python main.py

or

python3 main.py

After loading the program, input a list of comma-separated keywords listed in order of importance. The tool builds each query in the order given.

Example: 'John Doe, contractor, USA'

After each dork opens in a browser tab, the tool pauses via pdb. Review the results in the tab, then type 'c' or 'continue' to advance to the next search. Tabs stay open so you can flip back to cross-reference the dork results. The program doesn't close them.

To stop the program entirely, type 'exit' (open tabs will remain open).

### pynput mode

To advance searches automatically instead of typing 'c' each time, comment out the pdb.set_trace() line in main.py. The program will then use pynput to simulate keystrokes, advancing to the next search on a timer (5 seconds), configurable in main.py. This mode is faster but less human-looking than pdb mode; still not fully automated. 

## DISCLAIMER

This tool is intended for educational use only. I assume no liability for its misuse.

## Author: undonecan
