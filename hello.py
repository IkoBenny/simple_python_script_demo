"""When you run a Python module like

python hello.py

the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That means that by adding this code at the end of your module:you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file"""

if __name__ == "__main__":
    print("hello world")