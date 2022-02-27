1) pay attention to the differences between py2 and py3
    1. in py2, print needs "" only, but in py3, we have to add ()
    2. ->3)->10.Q1
2) we use # to annotate codes in py, but not // or /* in C
    1. plus + 
    2. minus -
    3. slash / (//)
    4. asterisk *
    5. percent %
    6. less-than <
    7. greater-than >
    8. less-than-equal <=
    9. greater-than-equal >=
    10. Q1: print(3+2+1-5+4%2-1/4+6), in the textbook it's answer is 7??
            at first, I think it goes wrong because "/", but it seems that "/" can handle float number 
            ok, I get it now, in py2, int-a / int-b can only get an int-c, but in py3 we can get a float-c
            -> just like the difference between even-division and division, so if we want to get a float answer in py2, 
            we need to declare the numbers as float numbers, like 2.0
            if we still want an int answer in py3, we can use //
3) in py, the result of compare operator is true or false (0 / 1)
4) in py, we don't need to declare the type of  variable,
    like a = 1.0, we don't need to write it as float a = 1.0
5) we can‘t space casually in py (unexpected indent)
6) some place operator
    1.~ -> not
    2.| -> or
    3.& -> and
7) print('{0} {0} {1:10.2f}'.format("hello", 1/3)), we use format-string to print many elements
8) in py2, if we don't want to start a new line after print, we can add a ',' at last, but in py3, we need to write as 
   print("How much do you weight?", end="")
   result: How much do you weight? 11(\n)
9) input() & raw_input()
   in py3, we use input() to get something from the users and treat what we get as a string
   in py2, raw_input() works just like input() in py3. But in py2, input() can and only receive a number and treat 
   it as int or float
   Ex: a = input("your name:") / a = input() / a = int(input())
10) pydoc:
    pydoc is a documentation generator and online help system, we can write python -m pydoc module_name in cmd to use it
    what pydoc shows have an order like this: 1. the annotation at the top of the *py file 2. all classes in this module
    3. all functions in this module 4. all variables in the module 5. the source file
11) about file_function: .+close : close the file and preserve / .+read : read the content of the file 
     .+readline read some lines of the file (in order 1 2 3 ...), need to remember line number  
     .+truncate empty the file  
     .+write(stuff) write stuff into the file
     .+seek put the file_index to a certain place -> f.seek(a, b)
12) if we want to check a file after we rewrite something, we need to close it first, because the content does not truly
    be written into the file yet.
13) split('char or string') we can use method split to cut a string by index in split
14) about function: 1. begin with def 2. : 3. no same variable name 4. indent  
15) very interesting : 
    def break_words(stuff):
    words = stuff.split(' ')
    return words
    after using a function like this, we can get many words in variablie "words", as following:
    'All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait', now words is a list
16) pop() :
    to delete an assigned element in the list
17) sorted() vs sort()
    this two function are to sort a list by dictionary-order
    but sorted() will make a new list, sort() will operate the exsiting list
18) if we want to run a .py file in terminal, we can first write "python", after we can import a python file and use 
    the functions in the file; if we want to quit, input Ctrl + d
19) in python, 'else if' in c == 'elif'
20) in choose-sentences, we can add more choose-sentence, which we call nested sentences
21) list:
    how to build up a list? 
    hairs = ['brown', 'blond','green'] / weight = [ 1, 2, 3, 4 ]
    1. if we want to get a or many elements in a list
       we can write list[1] (get the second one) / list[1:5] (get the second to fifth one) -> list[m:n] (last one n-1)
       list[-1] (get the last one element in the list) / list[1:] (get the elements from the second element)
    2. methods: 1. .append() : use it to add an element at the end of the list
                2. del : use it to delete elements 
                3. .count() : count how many times one element appear in the list
                4. alist.expend(blist) : add b to the end of a
                5. list.index(x[, start[, end]]) : return the index or fault (the first index)
                6. list.insert(index, obj) : insert element to an assigned place
                7. list.pop([index=-1]) : index = -1 -> pop the last one
                8. list.remove(obj) : remove the first matched item
                9. list.reverse() : change the order in the element
                10. list.sort(cmp=None, key=None, reverse=False):
                    reverse = True decresing order， reverse = False increasing order(default)
    3. list-operators : + : combine lists [1, 2, 3] + [4, 5, 6] / * : repeat lists [1, 2, 3] * 2
    4. check elements: 3 in [1, 2, 3] -> True
22) range()
    range(start, end, (step)), we often use range() in for-loop
23) 
    
    
    