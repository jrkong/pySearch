#jrkong's command line searcher

import urllib
import argparse
import webbrowser

argparser = argparse.ArgumentParser()
argparser.add_argument("-s", help="Takes a query to search for and searches it.", nargs="*")
argparser.add_argument("-e", "--engine", help="Changes the name or alias of a search engine and sets it as the search engine for the session", nargs="+")
argparser.add_argument("-d", "--domain", help="Changes the domain extention", nargs="+")
argparser.add_argument("-b", "--browser", help="Changes browser to perform search in", nargs="+")

args = argparser.parse_args()

#print available broswers
def printAvailableBrowsers(invalid):
        print("You have selected an invalid or unreigstered browser: " + invalid + ".\nHere is a list of available browsers")
        for i in webbrowser._browsers:
            print("\t"+i)
#end of printAvailableBrowsers

class Search:
    def __init__(self, searchIn = None, engineIn = "google", domainIn = "ca"):
        self.searchRaw = searchIn
        self.searchQuery = ""
        self.engine = engineIn
        self.domain = domainIn
        self.url = "";
        self.searchString = "/search?q="
    #end of constructor    

    #set search engine
    def setEngine(self, engineIn):
        self.engine = engineIn
    #end of setEngine

    #set domain engine
    def setdomain(self, domainIn):
        self.domain = domainIn
    #end of setdomain

    def buildLink(self):
        if self.engine == "amazon":
            self.searchString = "/s/keywords="
            self.searchQuery = "%20".join(self.searchRaw)
        elif self.engine == "twitter":
            self.searchQuery = " ".join(self.searchRaw)
        else:
            self.searchQuery = "+".join(self.searchRaw)
        #end of search exceptions
        self.url = "http://www." + self.engine + "." + self.domain + self.searchString + self.searchQuery
    #end of link building

    def openBrowser(self):
        try:
            browser = webbrowser.get(args.browser[0])
            browser.open_new_tab(self.url)
        except:
            printAvailableBrowsers(args.browser[0])
    #end of openBrowser()
#end of Query

searchObj = Search(args.s)
if args.engine is not None:
    searchObj.setEngine(args.engine[0])

if args.domain is not None:
    searchObj.setdomain(args.domain[0])
#end of cmd args handling

searchObj.buildLink()
searchObj.openBrowser()
