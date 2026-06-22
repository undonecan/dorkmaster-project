## DORKMASTER

dork-master is a command line tool prototype that utilizes python's webbrowser and pdb modules to automate asuccession of google dorks based on user keywords. 

## ABOUT DORKMASTER

This is a personal OSINT tool designed to simplify google dorking. It takes a list of keywords and creates dorked queries. It is not a traditional scraper, and thus reduces the risk of rate-limits and IP bans.

This script utilizes websites.txt and search_engines.txt, which are editable files. Websites.txt is the list of different domains to be used in the "site:" dork, while search_engines.txt utilizes a list of search engines that will be used by the webbrowser module (NOTE: not all webbrowsser or compatible with this program).

Dork-master will puase via pdb.set_trace() after each query, so please familiarize yourself with the pdb debuggers simple commands (namely continue, skip, and exit).

## REQUIREMENTS
[ "build==1.5.0",
"packaging==26.2",
"pyproject-hooks==1.2.0",
"requests>=2.34.2",
]

besides the python3 standard library, this program requires pynput.

Navigate to the project folder and install using pip, pip3, or uv pip.
ex: pip3 dist/dorkmaster_project-0.1.0-py3-none-any.whl

## USAGE

Once installed, navigate to the program root folder and run with:
python main.py 
or
python3 main.py

After loading the program, input a list of comma-seperated keywords listed in the mater of importance.

Ex: 'John Doe, contractor, USA'

Once pdb pauses execution, contiue with by typing 'c' or 'continue.' Once you are satisfied with your search, type 'exit.'

## Author: undonecan

