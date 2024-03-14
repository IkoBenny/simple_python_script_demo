"""When you run a Python module like

python hello.py 5

$ python hello_two.py 5
hello world greeting #1
hello world greeting #2
hello world greeting #3
hello world greeting #4

the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file"""

if __name__ == "__main__":
    import hello
    import sys
    import importlib
    for num in range(1, int(sys.argv[1])):
        print("hello world greeting #" + str(num))
    importlib.import_module("hello.py")
    
""" Why this does not work:

__main__ — Top-level code environment
https://docs.python.org/3/library/__main__.html

SHORT ANSWER:


if __name__ == '__main__' code block comes in handy. 
Code within this block won’t run unless the module is executed in the top-level environment.

Putting as few statements as possible in the block below if __name__ == '__main__' can improve code clarity and correctness. 
Most often, a function named main encapsulates the program’s primary behavior:

CODE EXAMPLE:

# echo.py

import shlex
import sys

def echo(phrase: str) -> None:
   A dummy wrapper around print
   # for demonstration purposes, you can imagine that there is some
   # valuable and reusable logic inside this function
   print(phrase)

def main() -> int:
    Echo the input arguments to standard output
    phrase = shlex.join(sys.argv)
    echo(phrase)
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit


LONG ANSWER:



In Python, the special name __main__ is used for two important constructs:

1. the name of the top-level environment of the program,
which can be checked using the __name__ == '__main__' expression; and

2. the __main__.py file in Python packages.

What is the “top-level code environment”?
__main__ is the name of the environment where top-level code is run.
“Top-level code” is the first user-specified Python module that starts running. 
It’s “top-level” because it imports all other modules that the program needs. 
Sometimes “top-level code” is called an entry point to the application.

The top-level code environment can be:

the scope of an interactive prompt:

>>>
__name__
'__main__'
the Python module passed to the Python interpreter as a file argument:

python helloworld.py
Hello, world!
the Python module or package passed to the Python interpreter with the -m argument:

python -m tarfile
usage: tarfile.py [-h] [-v] (...)
Python code read by the Python interpreter from standard input:

echo "import this" | python
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
Python code passed to the Python interpreter with the -c argument:

python -c "import this"
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
In each of these situations, the top-level module’s __name__ is set to '__main__'.

"""