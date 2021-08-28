##Identifiers in Python language

Once after the successful installation of python software, we'll slowly dive into the programming language. 

{Q} What is an **identifier** ?

[A] A name of an element in python program is called as an identifier. It can be a module name or class name or function name or variable name. 
For example: ```a = 15```. 

There are **certain rules** to be followed while defining the identifiers in our program. 
1. The only allowed characters are
    
    *  alphabet symbols (either lowercase or upper case or combination of the two)
    
    * digits (0 to 9)
    
    * underscore symbol (_)
2. Identifier should not start with the digit. For example: ```12hi = 25``` is not allowed. 

3. Identifier is case-sensitive and hence python programming language is case-sensitive. For example: ```ok, OK``` are both different. 

4. There is no length limit for identifiers. However, it is strongly recommended to use meaningful names and not too lengthy. 

5. We cannot use inbuilt reserved keywords as identifiers. For example: ```if=21``` cannot be used, whereas ```IF=21``` is valid. 

6. Identifier must not contain white spaces. 
7. There is a special meaning for identifiers starting with ```_```. 
<hr>

###Reserved Keywords: 
In python, there are some words that are reserved to represent some meaning or functionality which are known as reserved keywords. 

As of _python 3.7.7_ version, there are 35 reserved keywords available. 
They are ```['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']```

If we have a closer look at the keywords, except ```False, True, None```, all the other contains only lowercase alphabets. 
<hr>

How to check for reserved keywords ? 

Open python repl tool (python idle) and type below code snippet. 
```
>>>import keyword
>>>keyword.kwlist
```

<hr>

###Comments: 
Comments in python are to clarify the code and hence are not interpreted by Python. 
The comments in python language start with hash character ```#``` . A hash character ```#``` enclosed within the string literal is just the hash character and not a comment. 

```
# this is the comment
hello = 252  # this is another comment. 
text = "# this is not a comment" 
```

<hr>

With this information, now we are good to proceed further to develop programs.
