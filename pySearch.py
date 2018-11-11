#jrkong's command line searcher
import argparse
from search import Search

argparser = argparse.ArgumentParser()
argparser.add_argument("-s", action="append", help="Takes a query to search for and searches it.", nargs="*", required=True)
argparser.add_argument("-e", "--engine", help="Changes the name or alias of a search engine and sets it as the search engine for the session", nargs="+")
argparser.add_argument("-d", "--domain", help="Changes the domain extention", nargs="+")
argparser.add_argument("-b", "--browser", help="Changes browser to perform search in", nargs="+")

args = argparser.parse_args()

searchObj = Search()

searchObj.handleArgs(args)