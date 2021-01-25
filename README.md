# Kattis Solutions

## What is this?
This repository contains my solutions to the programming challenges found on [Kattis](https://open.kattis.com/).

All the solutions are accepted by Kattis. 
I strive to make the solutions as readable as I can.
But be aware that I'm using this project to learn Python and get better at solving algorithmic challenges so the solutions may not be the most Pythonic or optimal. 


## How to find the related problem?
The file name is the problem's name on Kattis.
You can find the problem by substituting [filename] with the name of the file:
https://open.kattis.com/problems/[filename]

Example:
hello.py solves the problem of
https://open.kattis.com/problems/hello


## How to run?
All these solution are solved with Python 3.6+.
You can run the solutions by passing the solution file to Python in a terminal like this:
> python hello.py

Most solutions need input.
To provide the input, run the solution like before and paste the data into the buffer like this:
> python bestcompression.py
13 3

You can also store the data in a file and redirect it to the program.
With a file called bestcompression-data.py containing "13 3", you can do it like this:
> python bestcompression.py < bestcompression-data.py


## Support of Python 2
Notice that Python 2 is not able to run these solutions because Python 2 and 3 handle `input()` differently and all solutions use it (except hello.py).
