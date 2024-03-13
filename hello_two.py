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