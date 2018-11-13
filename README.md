# pySearch

pySearch is a simple command line python script that allows for seamlessly performing a web search without removing your hands off the keyboard as it opens a new browser tab to search the input string. Normally when working on a command line interface, a user would need to use their mouse to perform a web search as they would take one hand off the keyboard and navigate to their browser. Even when using ALT+TAB, users would still need to navigate to the search bar with the mouse and then return to the keyboard to type their search. 

pySearch simplifies this to a single command line command.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Software you will need

 Python - https://www.python.org/downloads/ 
 Text Editor  - eg Visual Studio Code (if planning to edit this repo) 


### Installing

Clone this Repo  

In Command Line Prompt 

To run use 

python C:\Users\pySearch\pySearch.py  ( different path name where you have cloned pySearch into) 


## Running the tests

To be added .. 

## Built With

Python

## Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

( To Be added )


## Authors

* **Alex Kong** - *Initial work* ( https://github.com/jrkong )

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. (TO be added) 


## Goals 

The goal of pySearch is to bring web search capabilities to your command line so initiating a web search doesn't require taking your hand off the keyboard. The current goal is to integrate as much of the web search workflow into the command line so users can get all the keyboard interaction out of the way before taking one hand off the keyboard to use the mouse to interact with the browser.

### Specific Goals 

Support basic webcrawling which would allow basic searches, basic dictionary lookup would be a great test case for this, to be performed before opening a browser. (think Unix man pages)

Basic browser interactivity through pySearch. The ability to navigate and control your browser using pySearch (so scrolling, selecting and opening search links, open a new tab). While it allows keyboard interactivity with the browser while inside the command line, pySearch's interactive mode shouldn't impede the user's ability to use command line commands so it should have the ability to pipe command line commands to the shell and return their output to the user.



