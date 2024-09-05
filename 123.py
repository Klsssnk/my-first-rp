Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input()
print("Добро пожаловать на ФиПЛ," + name)
>>> 
>>> 
>>> print("Hello world")
Hello world
>>> name = input
>>> print("Добро пожаловать на ФиПЛ,"+name)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("Добро пожаловать на ФиПЛ,"+name)
TypeError: can only concatenate str (not "builtin_function_or_method") to str
