# Python Scripting

6. Modules
https://docs.python.org/3/tutorial/modules.html#more-on-modules

<details>
<summary>Project Background</summary>
If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. This is known as creating a script. As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in several programs without copying its definition into each program.
</details>

<details>
<summary>Project Purpose</summary>
To support existing development and future skill development, the use of scripting languauges could prove useful. For example, to automate downloads of multiple box scores. Planned for usage during bet_buddy development. See bet_buddy repository for more details. 
</details>

<details>
<summary>Modules</summary>
To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents
</details>

<details>
<summary>Modules As Scripts</summary>

Example Code:
if __name__ == "__main__":
    import sys
    print(int(sys.argv[1]))
</details>
