1. summary of print
   1) directly print something : print("Hello World")
   2) print a variable only : print(a) a = 1
   3) print many variable : print("Hello" , a) a = 'world'
   4) combine 1) and 2) : print("Hello %s" % 'World')  //  print("Hello %s" % a) a = 'World'
                          if we have more than one variable :
                          print("Day %d, %s" % (day, s)) day = 1, s = "Hello World"
   5) print the same thing for many times : print("*" * 10) -> output: **********
   6) use format : format = '%r %r %r %r' print(format, %("Hello", "World", "!", "!"))
                   print("{0},{1},{0}".format("Hello", "World"))
2. summary of file
   1) get the filename, we can use input() method or "from sys import argv"
      then, we can let script, filename = argv to get the name
   2) if we want to do compile a file, we need to open it first
      use a = open(filename) to open, we can also add arguments in open() method
   3) other methods about file
      a.read(), read the whole file
      a.readline(size), from the now file_index, read size bytes, if not assigned, read a line
      a.truncate(size), from the now file_index, delete size bytes, if not assigned, delete all 
      a.write(content), from the now file_index, write the content
      a.seek(), put the file_index to somewhere you want
      a.close(), close the file
   4) to check whether a file exist or not, we can write "from os. path import exsits" (no indent between . and path)
3. summary of input()
   1) a = input(), get what user input
   2) a = input(prompt), prompt = '>' -> > hello -> a = 'hello'
      in this way we can print some prompts before user input something
   3) what we get by input() is string type, if we want int or float, we need to transfer the type
      ex: a = int(input()), b = float(input())
4. summary of function
   1) form : def function_name(argument):
             the other lines should start with 4 indents
             two lines between function_codes and other codes
   2) use : the use and the function are in one py_file: convey the arguments and use the function
   3) we can have many return values in a function