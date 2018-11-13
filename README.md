# pySearch
Simple command line python script that opens a new browser tab to search the input string

pySearch was loosely inspired by Unix's mouseless workflow.

The goal of pySearch is to bring web search capabilities to your command line so initiating a web search doesn't require taking your hand off the keyboard. The current goal is to integrate as much of the web search workflow into the command line so users can get all the keyboard interaction out of the way before taking one hand off the keyboard to use the mouse to interact with the browser.

Normally, someone working on a command line interface, to perform a web search a user would need to take one hand off the keyboard, start/navigate to their browser with their mouse (or alt+tab however they would still need to navigate to the search bar with the mouse) and then take their hand off the mouse so they can use the keyboard to type their search. pySearch simplifies this to a single command line command.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

Python

## Contributing

Please read [CONTRIBUTING.md] add here) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning


## Authors

* **Alex Kong** - *Initial work* - [pySearch]()

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.




I think we should include some long term goals for pySearch and 2 major ones that I would love to see are:

Support basic webcrawling which would allow basic searches (basic dictionary lookup would be a great test case for this) to be performed before opening a browser (think Unix man pages).

Basic browser interactivity through pySearch. The ability to navigate and control your browser using pySearch (so scrolling, selecting and opening search links, open a new tab). While it allows keyboard interactivity with the browser while inside the command line, pySearch's interactive mode shouldn't impede the user's ability to use command line commands so it should have the ability to pipe command line commands to the shell and return their output to the user.

Hopefully this is a good starting point to build our initial Readme.
