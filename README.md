# pySearch

pySearch is a simple command line python script that allows for seamlessly performing a web search without removing your hands off the keyboard as it opens a new browser tab to search the input string. Normally when working on a command line interface, a user would need to use their mouse to perform a web search as they would take one hand off the keyboard and navigate to their browser. Even when using ALT+TAB, users would still need to navigate to the search bar with the mouse and then return to the keyboard to type their search. 

pySearch simplifies this to a single command line command.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Software you will need
<ol>
 <li> Python - https://www.python.org/downloads/ </li>
 <li> Text Editor  - eg Visual Studio Code (if planning to edit this repo) </li>
</ol>

### Installing

Clone this Repo  

For Windows: Command Line Prompt 
        OSX: Terminal 

To run use 

python C:\Users\pySearch\pySearch.py  ( different path name where you have cloned pySearch into) 

#### Command Line Arguments 
 <ol>
 <li> -s  takes query to search</li>   
 <li> -e  changes name or alias of search engine and sets it to as search engine for session </li> 
 <li> -d  changes to domain extension </li>
 <li> -h  will provide description of command line arguments </li> 
 </ol>

## Built With

Python 3 

## Contributing

### Running the Tests
pySearch tests use the [pytest](https://docs.pytest.org) library which is not part of the default Python library. If this is the first time pytest tests are being run on the machine use `pip install -r requirements.txt` to install pytest and it's dependencies (NOTE your `pip` alias may differ based on your installation). Afterwards pySearch tests can be run with the `pytest` command when inside the pySearch directory.

### Style Enforcement with Flake8
We are using Flake8 for style guide enforcement in pySearch.
It ensures that our code does not have any linting errors and is consistent.

Before submitting any Pull Request, please ensure to complete the following steps:

Install Flake8: "python -m pip install flake8"

Run Flake8 on the whole project from the root folder: "flake8 ."
Run Flake8 on a specific file: "flake8 search.py"

A list of errors will be returned that need to be fixed, please fix them before submitting
your Pull Request!


Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

( To Be added )


## Authors

* **Alex Kong** ( https://github.com/jrkong )
* **Alexander Ponomaroff** ( https://github.com/alexander-ponomaroff )

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. (TO be added) 


## Objective 

The goal of pySearch is to bring web search capabilities to your command line so initiating a web search doesn't require taking your hand off the keyboard. The current goal is to integrate as much of the web search workflow into the command line so users can get all the keyboard interaction out of the way before taking one hand off the keyboard to use the mouse to interact with the browser.

### Specific Goals 
<ol>
 <li> Support webcrawling which would allow basic searches 
     <ul> - Basic dictionary lookup would be a great test case for this, to be performed before opening a browser (think Unix man       pages. </ul> 
 </li>
 <li> Basic browser interactivity through pySearch 
   <ul> - The ability to navigate and control your browser using pySearch (so scrolling, selecting and opening search links, open a new tab) </ul>
 </li>
 <li> pySearch's interactive mode shouldn't impede the user's ability to use command line commands 
  <ul> - While it allows keyboard interactivity with the browser while inside the command line it should have the ability to pipe command line commands to the shell and return their output to the user </ul>
 </li>
</ol>


