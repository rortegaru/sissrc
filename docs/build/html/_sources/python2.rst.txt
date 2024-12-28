Python Tutorial
===============



Python Basics
-------------

This section will get you started with using Python and you’ll be able
to learn more about whatever you want after studying it.

1.  `What is programming? <what-is-programming.md>`__
2.  `Installing Python <installing-python.md>`__
3.  `Getting started with Python <getting-started.md>`__
4.  `ThinkPython: The way of the program <the-way-of-the-program.md>`__
5.  `Variables, Booleans and None <variables.md>`__
6.  `Using functions <using-functions.md>`__
7.  `Setting up an editor <editor-setup.md>`__
8.  `If, else and elif <if.md>`__
9.  `Handy stuff with strings <handy-stuff-strings.md>`__
10. `Lists and tuples <lists-and-tuples.md>`__
11. `Loops <loops.md>`__
12. `zip and enumerate <zip-and-enumerate.md>`__
13. `Dictionaries <dicts.md>`__
14. `Defining functions <defining-functions.md>`__
15. `Writing a larger program <larger-program.md>`__
16. `What is true? <what-is-true.md>`__
17. `Files <files.md>`__
18. `Modules <modules.md>`__
19. `Exceptions <exceptions.md>`__
20. `Classes <classes.md>`__
21. `Docstrings <docstrings.md>`__


What is programming?
--------------------

**Feel free to** `skip this part <#how-to-read-this-tutorial>`__ **if
you already know everything it’s talking about.**

As a computer user you know that computers don’t have feelings. They
don’t work any faster or slower depending on if we’re angry at them or
if we’re happy. Computers can perform millions of calculations per
second, but they require us to tell them exactly what to do. If they do
something else than we want them to do the problem is usually that they
don’t understand our instructions the way we understand them.

The only big difference between programming and what you’re familiar
with already is that instead of clicking buttons to do things we write
the instructions using a **programming language**. Most programming
languages consist of English words, digits and some characters that have
special meanings.

Unlike people often think, programming is usually not complicated. Large
programs are always made of **small, simple pieces**, and those pieces
are written one by one. Programming languages are made to be used by
humans, so if there’s an easy way to do something and a difficult way to
do something, you should use the easier way.

What do I need?
^^^^^^^^^^^^^^^

First of all, **you don’t need to be good at math**. Some programmers
are good at math, some are not. Programming and math are two separate
things and being good or bad at one doesn’t mean you are automatically
good or bad at the other.

You also don’t need a powerful computer. I could do almost all of my
programming on a 12-year-old computer if I needed to. Fast computers are
nice to work with, but you don’t need them.

Programming takes time like all hobbies do. Some people learn it
quickly, and some people don’t. I don’t expect you to read this tutorial
in a couple hours and then master everything it’s talking about. Take
your time with things, and remember that I learned to program slowly.

Getting started
^^^^^^^^^^^^^^^

This tutorial uses a programming language called Python because it’s
easy to learn and we can do many different things with it. For example,
we can create our own applications that have buttons that people can
click instead of just using applications written by others.

Before we can get started with Python we need to know how to write some
of Python’s special characters with our keyboards. Unfortunately I don’t
know which keys you need to press to produce these characters because
your keyboard is probably different than mine. But the keyboard can tell
what you need to press. For example, my Finnish keyboard has a key like
this:

.. figure:: ../images/key.png
   :alt: A key on my keyboard.

   A key on my keyboard.

Here’s what the characters on this key mean:

-  I can type a number 7 by pressing this key without holding down other
   keys at the same time.
-  I can type a ``/`` character by holding down the shift key (on the
   left edge of the keyboard, between Ctrl and CapsLock) and pressing
   this key.
-  I can type a ``{`` character by holding down AltGr (on the bottom of
   the keyboard, on the right side of the spacebar) and pressing this
   key. Holding down Ctrl and Alt instead of AltGr may also work.

The only key that doesn’t have anything written on it is spacebar. It’s
the big, wide key that’s closest to you. Another key that’s used for
producing whitespace is tab, the key above CapsLock.

In this tutorial we need to know how to type these characters. We’ll
learn their meanings later.

=========== ====================================
Character   Names
=========== ====================================
``+``       plus
``-``       minus, dash
``_``       underscore
``*``       star, asterisk
``/``       forwardslash (it’s leaning forward)
``\``       backslash (it’s leaning back)
``=``       equals sign
``%``       percent sign
``.``       dot
``,``       comma
``:``       colon
``?``       question mark
``!``       exclamation mark
``<`` ``>`` less-than and greater-than signs
``'`` ``"`` single quote and double quote
``#``       hashtag
``()``      parentheses
``[]``      square brackets, brackets
``{}``      curly braces, braces, curly brackets
=========== ====================================

That may seem like many characters, but you probably know many of them
already so it shouldn’t be a problem.

How to read this tutorial
^^^^^^^^^^^^^^^^^^^^^^^^^

I’ve done my best to make this tutorial as easy to follow as possible.
Other people have commented on this and helped me improve this a lot
also. But what should you do if you have a problem with the tutorial?

1. Try the example code yourself.
2. Read the code and the explanation for it again.
3. If there’s something you haven’t seen before in the tutorial and it’s
   not explained, try to find it in the previous chapters.
4. If you can’t find what you’re looking for or you still have trouble
   understanding the tutorial or any other problems with the tutorial,
   please `tell me about it <../contact-me.md>`__. I want to improve
   this tutorial so other readers won’t have the same problem as you
   have.
5. See `Getting help <../getting-help.md>`__ if you can’t contact me for
   some reason.

You are free to combine this tutorial with other learning resources. If
this tutorial isn’t exactly what you’re looking for you don’t need to
stick with nothing but this. You can find another tutorial and mix the
tutorials however you want as long as you **make sure that you
understand everything you read**.

One of the most important things with learning to program is to **not
fear mistakes**. If you make a mistake, your computer will not break in
any way. You’ll get an error message that tells you what’s wrong and
where. Even professional programmers do mistakes and get error messages
all the time, and there’s nothing wrong with it.

If you want to know what some piece of code in this tutorial does just
**try it and see**. It’s practically impossible to break anything
accidentally with the things you will learn by reading this tutorial, so
you are free to try out all the examples however you want and change
them to do whatever you want.

Even though a good tutorial is an important part about learning to
program, you also need to learn to make your own things. Use what you
have learned, and create something with it.

But reading is boring!
^^^^^^^^^^^^^^^^^^^^^^

This chapter is probably the most boring chapter in the whole tutorial.
Other chapters contain much less text and much more code. You can also
get pretty far by just reading the code, and then reading the text only
if you don’t understand the code.

Summary
^^^^^^^

-  Now you should know what programming and programming languages are.
-  You don’t need to be good at math and you don’t need a new computer.
-  Complicated programs consist of simple pieces.
-  You don’t need to remember how to type different characters. Just
   find the character on your keyboard and press the key, holding down
   shift or AltGr as needed.
-  Make sure you understand everything you read.
-  Experiment with things freely and don’t fear mistakes.
-  Error messages are our friends.
-  Let me know if you have trouble with this tutorial.
-  Now we’re ready to `install Python <installing-python.md>`__ and `get
   started <getting-started.md>`__!


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <../README.md>`__ \| `Next <installing-python.md>`__ \| `List
of contents <../README.md#basics>`__

Installing Python
-----------------

If you want to learn to program with Python using this tutorial, you
need to try out the code examples. You can use a website like
`repl.it <https://repl.it/languages/python3>`__, but I highly recommend
installing Python. That way you don’t need to open a web browser just to
write code, and you can work without an Internet connection.

It doesn’t matter which operating system you use because Python runs
great on Windows, Mac OSX, Linux and many other operating systems.
However, installing and launching Python are done differently on
different operating systems, so just follow your operating system’s
instructions.

Let’s get started!

Downloading and installing Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Windows
```````

Installing Python on Windows is a lot like installing any other program.

1. Go to `the official Python website <https://www.python.org/>`__.

2. Move your mouse over the blue Downloads button, but don’t click it.
   Then click the button that downloads the latest version of Python.

3. Run the installer.

4. Make sure that the launcher gets installed and click Install Now.

   .. figure:: ../images/py-exe.png
      :alt: The py.exe launcher.

      The py.exe launcher.

Mac OSX
```````

At the time of writing this, Macs don’t come with a Python 3 and you
need to install it yourself. It should be like installing any other
program, but unfortunately I don’t have better instructions because I
don’t have an up-to-date Mac and I have never installed Python on a Mac.
If you would like to write better instructions, `tell
me <../contact-me.md>`__.

Linux
`````

You already have Python 3, **there’s no need to install anything**. You
may also have Python 2, but don’t try to remove it. Some of the programs
that came with your operating system are probably written in Python 2,
so removing Python 2 would break them.

Running Python
^^^^^^^^^^^^^^

Next we’ll learn to run Python on a PowerShell or terminal. There are
several other ways to run Python, but if you learn this way now it’s
going to make things easier later.

.. _windows-1:

Windows
```````

1. Open a PowerShell from your start menu or start screen.

2. Type ``py`` and press Enter. You should see something like this:

   .. figure:: ../images/powershell.png
      :alt: Python running in a PowerShell window.

      Python running in a PowerShell window.

Other operating systems
```````````````````````

1. Open a terminal. How exactly this is done depends on your operating
   system, but most operating systems have some way to search for
   programs. Search for a program called terminal and launch it.

2. Type ``python3`` and press Enter. You should see something like this:

   .. figure:: ../images/terminal.png
      :alt: Running Python on my terminal.

      Running Python on my terminal.

   Your terminal probably looks different than mine, it’s OK.

Now you can type ``exit()`` and press Enter to get out of Python. Or you
can just close the PowerShell or Terminal window.

.. _summary-1:

Summary
^^^^^^^

Now you should have Python installed, and you should be able run it.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <what-is-programming.md>`__ \| `Next <getting-started.md>`__
\| `List of contents <../README.md#basics>`__

Getting started with Python
---------------------------

`Launch Python <installing-python.md>`__.

The ``>>>`` means that Python is ready and we can enter a command. The
basic idea is really simple: we enter a command, press Enter, enter
another command, press Enter and keep going.

You probably don’t know any Python commands yet. Let’s see what happens
if we just write something and press Enter.

.. code:: python

   >>> hello
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'hello' is not defined
   >>>

Oops! That didn’t work. But like I wrote in the
`introduction <what-is-programming.md>`__, error messages are our
friends. This error message tells us what’s wrong and where, and we’ll
learn what “name ‘hello’ is not defined” means `later <variables.md>`__.

Maybe we can press Enter without typing anything?

.. code:: python

   >>>
   >>>
   >>>
   >>>

That worked. How about numbers?

.. code:: python

   >>> 123
   123
   >>> -123
   -123
   >>> 3.14
   3.14
   >>> -12.3
   -12.3
   >>>

There we go, it echoes them back.

In some countries, decimal numbers are written with a comma, like
``3,14`` instead of ``3.14``. Maybe Python knows that?

.. code:: python

   >>> 3,14
   (3, 14)
   >>>

We didn’t get an error… but ``(3, 14)`` is not at all what we expected!
So from now on, let’s use a dot with decimal numbers, because ``3.14``
worked just fine. Later we’ll learn what ``(3, 14)`` is.

Comments
^^^^^^^^

**Comments are text that don’t do anything when they’re run.** They can
be created by typing a ``#`` and then some text after it, and they are
useful when our code would be hard to understand without them.

.. code:: python

   >>> 1 + 2     # can you guess what the result is?
   3
   >>>

Again, I put a space after the ``#`` and multiple spaces before it just
to make things easier to read.

If we write a comment on a line with no code on it, the prompt changes
from ``>>>`` to ``...``. To be honest, I have no idea why it does that
and I think it would be better if it would just stay as ``>>>``. The
prompt goes back to ``>>>`` when we press Enter again.

.. code:: python

   >>> # hello there
   ...
   >>>

Strings
^^^^^^^

Strings are small pieces of text that we can use in our programs. We can
create strings by simply writing some text in quotes.

.. code:: python

   >>> 'hello'
   'hello'
   >>> 'this is a test'
   'this is a test'
   >>> 

Strings can also be written with “double quotes” instead of ‘single
quotes’. This is useful when we need to put quotes inside the string.

.. code:: python

   >>> "hello there"
   'hello there'
   >>> "it's sunny"
   "it's sunny"
   >>> 

It’s also possible to add single quotes and double quotes into the same
string, but most of the time we don’t need to do that so I’m not going
to talk about it now.

It doesn’t matter which quotes you use when the string doesn’t need to
contain any quotes. If you think that one of the quote types looks nicer
than the other or you find it faster to type, go ahead and use that.

Strings can be joined together easily with ``+`` or repeated with ``*``:

.. code:: python

   >>> "hello" + "world"
   'helloworld'
   >>> "hello" * 3
   'hellohellohello'
   >>> 

Note that a ``#`` inside a string doesn’t create a comment.

.. code:: python

   >>> "strings can contain # characters"
   'strings can contain # characters'
   >>> 

Using Python as a calculator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: diff

   ---------- WARNING: This part contains boring math. Proceed with caution. ----------

Let’s type some math stuff into Python and see what it does.

.. code:: python

   >>> 17 + 3
   20
   >>> 17 - 3
   14
   >>> 17 * 3
   51
   >>> 17 / 3
   5.666666666666667
   >>>

It’s working, Python just calculates the result and echoes it back.

I added a space on both sides of ``+``, ``-``, ``*`` and ``/``.
Everything would work without those spaces too:

.. code:: python

   >>> 4 + 2 + 1
   7
   >>> 4+2+1
   7
   >>>

However, I recommend always adding the spaces because they make the code
easier to read.

Things are calculated in the same order as in math. The parentheses
``(`` and ``)`` also work the same way.

.. code:: python

   >>> 1 + 2 * 3        # 2 * 3 is calculated first
   7
   >>> (1 + 2) * 3      # 1 + 2 is calculated first
   9
   >>>

You can also leave out spaces to show what’s calculated first. Python
ignores it, but our code will be easier to read for people.

.. code:: python

   >>> 1 + 2*3         # now it looks like 2*3 is calculated first
   7
   >>>

Python also supports many other kinds of calculations, but most of the
time you don’t need them. Actually you don’t need even these
calculations most of the time, but these calculations are probably
enough when you need to calculate something.

.. _summary-2:

Summary
^^^^^^^

-  Error messages are our friends.
-  We can enter any Python commands to the interactive ``>>>`` prompt,
   and it will echo back the result.
-  ``+``, ``-``, ``*`` and ``/`` work in Python just like in math.
-  Pieces of text starting with a ``#`` are comments and pieces of text
   in quotes are strings.
-  You can use single quotes and double quotes however you want.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <installing-python.md>`__ \|
`Next <the-way-of-the-program.md>`__ \| `List of
contents <../README.md#basics>`__

ThinkPython: The way of the program
-----------------------------------

ThinkPython is a free Python book. Its first chapter is about
programming in general. `Read it
here. <http://greenteapress.com/thinkpython2/html/thinkpython2002.html>`__.

Read the glossary also, but don’t study it too much. Some things in it
are useful to know, but I think studying it carefully would be really
boring. Also do all exercises except the last one. It’s more about math
skills than learning Python.

When you’re done reading, read the summary below and make sure you’ve
learned everything.

.. _summary-3:

Summary
^^^^^^^

-  Now you should have some kind of idea about what programming is.
-  Each value has a type, and you can find that out with
   ``type(value)``. For example, writing ``type(123)`` to the Python
   prompt does the same thing as writing ``int`` to the prompt.
-  Types and classes are the same thing (in Python 3).
-  Some of the most commonly used types are:

   -  int is short for integer. ``1`` and ``2`` are integers.
   -  float is short for floating point number. ``1.0`` and ``3.14`` are
      floats.
   -  str is short for string. ``"hello"`` and ``'hello'`` are strings.
      It doesn’t matter if you use ‘single quotes’ or “double quotes”,
      they do the same thing in Python.

More exercises
^^^^^^^^^^^^^^

1. What happens if you use + between two strings, like
   ``"hello" + "world"``? How about ``"hello" * "world"``?
2. What happens if you use + between a string and an integer, like
   ``"hello" + 3``? How about ``"hello" * 3``?
3. What happens if you use + between a float and an integer, like
   ``0.5 + 3``? How about ``0.5 * 3``?


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <getting-started.md>`__ \| `Next <variables.md>`__ \| `List of
contents <../README.md#basics>`__

Variables, Booleans and None
----------------------------

Variables
^^^^^^^^^

Variables are easy to understand. They simply **point to values**.

.. code:: python

   >>> a = 1   # create a variable called a that points to 1
   >>> b = 2   # create another variable
   >>> a       # get the value that the variable points to
   1
   >>> b
   2
   >>>

Let’s draw a diagram of these variables.

.. figure:: ../images/variables1.png
   :alt: Variable diagram

   Variable diagram

We can also change the value of a variable after setting it.

.. code:: python

   >>> a = 2    # make a point to 2 instead of 1
   >>> a
   2
   >>>

So now our diagram looks like this:

.. figure:: ../images/variables2.png
   :alt: Variable diagram

   Variable diagram

Setting a variable to another variable gets the value of the other
variable and sets the first variable to point to that value.

.. code:: python

   >>> a = 1
   >>> b = a  # this makes b point to 1, not a
   >>> a = 5
   >>> b      # b didn't change when a changed
   1
   >>>

Trying to access a variable that is not defined creates an error
message.

.. code:: python

   >>> thingy
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'thingy' is not defined
   >>>

Variables are simple to understand, but there are a few details that we
need to keep in mind:

-  Variables always point to a value, **they never point to other
   variables**. That’s why the arrows in our diagrams always go left to
   right.
-  Multiple variables can point to the same value, but one variable
   cannot point to multiple values.
-  The values that variables point to can point to other values also.
   We’ll learn more about that when we’ll talk about
   `lists <lists-and-tuples.md>`__.

Variables are an important part of most programming languages, and they
allow programmers to write much larger programs than they could write
without variables.

Variable names are case-sensitive, like many other things in Python.

.. code:: python

   >>> thing = 1
   >>> THING = 2
   >>> thIng = 3
   >>> thing
   1
   >>> THING
   2
   >>> thIng
   3
   >>>

There are also words that cannot be used as variable names because they
are reserved by Python itself and have a special meaning. They are
called **keywords**, and we can run ``help('keywords')`` to see the full
list if we want to. We’ll learn to use most of them later in this
tutorial. Trying to use a keyword as a variable name causes a syntax
error.

.. code:: python

   >>> if = 123
     File "<stdin>", line 1
       if = 123
          ^
   SyntaxError: invalid syntax
   >>>

When assigning something to a variable using a ``=``, the right side of
the ``=`` is always executed before the left side. This means that we
can do something with a variable on the right side, then assign the
result back to the same variable on the left side.

.. code:: python

   >>> a = 1
   >>> a = a + 1
   >>> a
   2
   >>>

To do something to a variable (for example, to add something to it) we
can also use ``+=``, ``-=``, ``*=`` and ``/=`` instead of ``+``, ``-``,
``*`` and ``/``. The “advanced” ``%=``, ``//=`` and ``**=`` also work.

.. code:: python

   >>> a += 2          # a = a + 2
   >>> a -= 2          # a = a - 2
   >>> a *= 2          # a = a * 2
   >>> a /= 2          # a = a / 2
   >>>

This is not limited to integers.

.. code:: python

   >>> a = 'hello'
   >>> a *= 3
   >>> a += 'world'
   >>> a
   'hellohellohelloworld'
   >>>

Now we also understand why typing hello to the prompt didn’t work in the
beginning of this tutorial. But we can assign something to a variable
called hello and then type hello:

.. code:: python

   >>> hello = 'hello there'
   >>> hello
   'hello there'
   >>>

Good and bad variable names
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variable names can be multiple characters long. They can contain
uppercase characters, numbers and some other characters, but most of the
time we should use simple, lowercase variable names. We can also use
underscores. For example, these variable names are good:

.. code:: python

   >>> magic_number = 123
   >>> greeting = "Hello World!"
   >>>

Don’t use variable names like this, **these variables are bad**:

.. code:: python

   >>> magicNumber = 3.14          # looks weird
   >>> Greeting = "Hello there!"   # also looks weird
   >>> x = "Hello again!"          # what the heck is x?
   >>>

All of these variables work just fine, but other Python programmers
don’t want you to use them. Most Python code doesn’t use variable names
that contain UpperCase letters like ``magicNumber`` and ``Greeting``, so
other people reading your code will think it looks weird if you use
them. The problem with ``x`` is that it’s too short, and people have no
idea what it is. Remember that mathematicians like figuring out what x
is, but programmers hate that.

Booleans
^^^^^^^^

There are two Boolean values, True and False. In Python, and in many
other programming languages, ``=`` is assigning and ``==`` is comparing.
``a = 1`` sets a to 1, and ``a == 1`` checks if a equals 1.

.. code:: python

   >>> a = 1
   >>> a == 1
   True
   >>> a = 2
   >>> a == 1
   False
   >>>

``a == 1`` is the same as ``(a == 1) == True``, but ``a == 1`` is more
readable, so most of the time we shouldn’t write ``== True`` anywhere.

.. code:: python

   >>> a = 1
   >>> a == 1
   True
   >>> (a == 1) == True
   True
   >>> a = 2
   >>> a == 1
   False
   >>> (a == 1) == True
   False
   >>>

None
^^^^

None is Python’s “nothing” value. It behaves just like any other value,
and it’s often used as a default value for different kinds of things.
Right now it might seem useless but we’ll find a bunch of ways to use
None later.

None’s behavior on the interactive prompt might be a bit confusing at
first:

.. code:: python

   >>> thingy = None
   >>> thingy
   >>>

That was weird! We set thingy to None, but typing ``thingy`` didn’t echo
back None.

This is because the prompt never echoes back None. That is handy,
because many things result in None, and it would be annoying to see None
coming up all the time.

If we want to see a None on the interactive prompt, we can use print.

.. code:: python

   >>> print(thingy)
   None
   >>>

Another confusing thing is that if we do something weird to None we get
error messages that talk about NoneType object. The NoneType object they
are talking about is always None. We’ll learn more about what attributes
and calling are later.

.. code:: python

   >>> None.hello    # None has no attribute 'hello'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: 'NoneType' object has no attribute 'hello'
   >>> None()        # None is not callable
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'NoneType' object is not callable
   >>>

Other comparing operators
^^^^^^^^^^^^^^^^^^^^^^^^^

So far we’ve used ``==``, but there are other operators also. This list
probably looks awfully long, but it’s actually quite easy to learn.

+----------+-----------------------------------+-----------------------+
| Usage    | Description                       | True examples         |
+==========+===================================+=======================+
| ``       | a is equal to b                   | ``1 == 1``            |
| a == b`` |                                   |                       |
+----------+-----------------------------------+-----------------------+
| ``       | a is not equal to b               | ``1 != 2``            |
| a != b`` |                                   |                       |
+----------+-----------------------------------+-----------------------+
| `        | a is greater than b               | ``2 > 1``             |
| `a > b`` |                                   |                       |
+----------+-----------------------------------+-----------------------+
| ``       | a is greater than or equal to b   | ``2 >= 1``,           |
| a >= b`` |                                   | ``1 >= 1``            |
+----------+-----------------------------------+-----------------------+
| `        | a is less than b                  | ``1 < 2``             |
| `a < b`` |                                   |                       |
+----------+-----------------------------------+-----------------------+
| ``       | a is less than or equal to b      | ``1 <= 2``,           |
| a <= b`` |                                   | ``1 <= 1``            |
+----------+-----------------------------------+-----------------------+

We can also combine multiple comparisons. This table assumes that a and
b are Booleans.

+-------+---------------------------------+---------------------------+
| Usage | Description                     | True example              |
+=======+=================================+===========================+
| `     | a is True and b is True         | ``1 == 1 and 2 == 2``     |
| `a an |                                 |                           |
| d b`` |                                 |                           |
+-------+---------------------------------+---------------------------+
| ``a o | a is True, b is True or they’re | ``False or 1 == 1``,      |
| r b`` | both True                       | ``True or True``          |
+-------+---------------------------------+---------------------------+

``not`` can be used for negations. If ``value`` is True, ``not value``
is False, and if ``value`` is False, ``not value`` is True.

There’s also ``is``, but don’t use it instead of ``==`` unless you know
what you are doing. We’ll learn more about it later.

.. _summary-4:

Summary
^^^^^^^

-  Variables have a name and a value. We can create or change variables
   with ``name = value``.
-  ``thing += stuff`` does the same thing as ``thing = thing + stuff``.
-  Use lowercase variable names and remember that programmers hate
   figuring out what x is.
-  ``=`` means assigning and ``==`` means comparing.
-  True and False are Booleans. Comparing values results in a Boolean.
-  None is a value that we’ll find useful later. When error messages say
   ``NoneType object`` they mean None.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <the-way-of-the-program.md>`__ \|
`Next <using-functions.md>`__ \| `List of
contents <../README.md#basics>`__

Using functions
---------------

Now we know how to make Python show text.

.. code:: python

   >>> 'Hello!'
   'Hello!'
   >>>

But that includes ``''``. One way to show text to the user without
``''`` is with the print function. In Python, printing doesn’t have
anything to do with physical printers, it just means showing text on the
screen.

.. code:: python

   >>> print('Hello!')
   Hello!
   >>>

Now we are ready for a classic example, which is also the first program
in many tutorials :)

.. code:: python

   >>> print("Hello World!")
   Hello World!
   >>>

But what exactly is print?

What are functions?
^^^^^^^^^^^^^^^^^^^

Let’s see what happens if we type ``print`` without the ``('Hello')``
part.

.. code:: python

   >>> print
   <built-in function print>
   >>>

We could also type ``print(print)``, it would do the same thing. Python
replied to us with some information about print wrapped in ``<>``.

As we can see, print is a function. Functions do something when they are
**called** by typing their name and parentheses. Inside the parentheses,
we can pass some arguments too. In ``print("hello")`` the function is
``print`` and we give it one argument, which is ``"hello"``.

Functions are easy to understand, They simply **do something when they
are called**. Functions run immediately when we call them, so the text
appears on the screen right away when we run ``print(something)``.

Sometimes people think that doing ``thingy = print('hello')`` means that
Python is going to print hello every time we type ``thingy``. But **this
is not correct**! ``print('hello')`` runs print right away, and if we
type ``thingy`` later it’s not going to run ``print('hello')`` again.

Return values
^^^^^^^^^^^^^

Now we know that ``thingy = print('hello')`` doesn’t store the
``print('hello')`` call in a variable. But what does it do then?

.. code:: python

   >>> thingy = print('hello')
   hello
   >>> print(thingy)       # thingy is now None
   None
   >>>

So doing ``thingy = print('hello')`` set ``thingy`` to None.

Here’s what happened, explained in more detail:

-  When we do ``thingy = print('hello')``, the right side is processed
   first.
-  ``print('hello')`` calls the print function with the argument
   ``'hello'``.
-  The function runs. It shows the word hello.
-  The print function **returns** None. All functions need to return
   something, and print returns None because there’s no need to return
   anything else.
-  Now the right side has been processed. ``print('hello')`` returned
   None, so we can imagine we have None instead of ``print('hello')``
   there, and the assignment now looks like ``thingy = None``.
-  ``thingy`` is now None.

Now we understand what **a return value** is. When we call the function,
Python “replaces” ``function(arguments)`` with whatever the function
returns.

Calling a function without assigning the return value to anything (e.g.
``print('hello')`` instead of ``thingy = print('hello')``) simply throws
away the return value. The interactive ``>>>`` prompt doesn’t echo the
return value back because it’s None.

Of course, ``thingy = print('hello')`` is useless compared to
``print('hello')`` because the print function always returns None and we
can do ``thingy = None`` without any printing.

Not all functions return None. The input function can be used for
getting a string from the user.

.. code:: python

   >>> stuff = input("Enter something:")
   Enter something:hello
   >>> stuff
   'hello'
   >>>

``input("Enter something:")`` showed the text ``Enter something:`` on
the screen and waited for me to type something. I typed hello and
pressed Enter. Then input returned the hello I typed as a string and it
was assigned to ``stuff``.

Usually we want to add a space after the ``:``, like this:

.. code:: python

   >>> stuff = input("Enter something: ")  # now there's space between : and where i type
   Enter something: hello
   >>>

Handy things about print
^^^^^^^^^^^^^^^^^^^^^^^^

We can also print an empty line by calling print without any arguments.

.. code:: python

   >>> print()

   >>>

In Python, ``\n`` is a newline character. Printing a string that
contains a newline character also prints a newline:

.. code:: python

   >>> print('hello\nworld')
   hello
   world
   >>>

If we want to print a real backslash, we need to **escape** it by typing
two backslashes.


   >>> print('hello\\nworld')
   hello\nworld
   >>>

We can also pass multiple arguments to the print function. We need to
separate them with commas and print will add spaces between them.

.. code:: python

   >>> print("Hello", "World!")
   Hello World!
   >>>

Unlike with ``+``, the arguments don’t need to be strings.

.. code:: python

   >>> print(42, "is an integer, and the value of pi is", 3.14)
   42 is an integer, and the value of pi is 3.14
   >>>

Variables names and built-in things
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In `the previous chapter <variables.md>`__ we learned that ``if`` is not
a valid variable name because it’s a keyword.

.. code:: python

   >>> if = 123
     File "<stdin>", line 1
       if = 123
          ^
   SyntaxError: invalid syntax
   >>>

But ``print`` and ``input`` are not keywords, so can we use them as
variable names?

.. code:: python

   >>> print = "hello"
   >>> print
   'hello'
   >>>

We can, but there’s a problem. Now we can’t even do our hello world!

.. code:: python

   >>> print("Hello World!")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object is not callable
   >>>

The error message complains that strings aren’t callable because we just
set ``print`` to the string ``'hello'`` and now we’re trying to call it
like a function. As you can see, **this is not a good idea** at all.
Most `editors <editor-setup.md>`__ display built-in functions with a
special color, so you don’t need to worry about doing this accidentally.

Exit out of Python and start it again, and ``print("Hello World!")``
should work normally.

.. _summary-5:

Summary
^^^^^^^

-  ``function()`` calls a function without any arguments, and
   ``function(1, 2, 3)`` calls a function with 1, 2 and 3 as arguments.
-  When a function is called, it does something and returns something.
-  ``function(arguments)`` is “replaced” with the return value in the
   code that called it. For example, ``stuff = function()`` calls a
   function, and then does ``stuff = the_return_value`` and the return
   value ends up in stuff.
-  Python comes with ``print`` and ``input``. They are built-in
   functions.
-  Avoid variable names that conflict with built-in functions.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <variables.md>`__ \| `Next <editor-setup.md>`__ \| `List of
contents <../README.md#basics>`__

Setting up an editor for programming
------------------------------------

An editor is a program that lets us write longer programs than we can
write on the ``>>>`` prompt. With an editor we can save the programs to
files and run them as many times as we want without writing them again.

When programmers say “editor” they don’t mean programs like Microsoft
Word or LibreOffice/OpenOffice Writer. These programs are for writing
text documents, not for programming. **Programming editors don’t support
things like bigger font sizes for titles or underlining bits of text**,
but instead they have features that are actually useful for programming,
like automatically displaying different things with different colors,
but also highlighting mistakes in the code, and coloring syntax.

If you are on Windows or Mac OSX you have probably noticed that your
Python came with an editor called IDLE. You can use IDLE, but we
recommend exploring other options first.

Which editor?
^^^^^^^^^^^^^

The choice of an editor is a very personal thing. There are many
editors, and most programmers have a favorite editor that they use for
everything and recommend to everyone.

The editors can be broadly divided into three categories:

The Basic Text Editors
""""""""""""""""""""""

These editors usually come with the operating system. They do not have
features like running code, auto-completion, etc. that make programming
easier. They are usually used for relatively simple text editing. Most
programmers do not use these editors for programming.

A few popular ones in this category are: - Notepad (Windows) - Gedit
(Linux) - Notepad ++ (Windows) - Nano (Linux/Mac OS)

Smart Text Editors
""""""""""""""""""

The text editors in this category have features like auto-completion,
syntax highlighting, running and debugging code, highlighting errors,
etc. They are relatively easy to learn and have the necessary features
to start your programming journey.

A few popular ones in this category are: - Visual Studio Code / VS Code
(Windows/Linux/Mac OS) - IDLE (Usually comes with Python)
(Windows/Linux/Mac OS) - Thonny (Windows/Linux/Mac OS) -
`Porcupine <https://github.com/Akuli/porcupine>`__ (created by the
author of this tutorial) (Windows/Linux/Mac OS) - Geany
(Windows/Linux/Mac OS)

**We recommend that you look into a few of these editors and install
your favorite one.**

IDEs and advanced editors
"""""""""""""""""""""""""

This category of text editors are usually professional grade pieces of
software. They are mostly proprietary and paid. They have a steep
learning curve because of how many features they have. These types of
editors are generally not preferred in the beginning stage. They are
meant to be used for writing complex and large pieces of software.

A few popular ones in this category are: - Visual Studio (Not be
confused with *Visual Studio Code*) (Windows) - Pycharm
(Windows/Linux/Mac OS) - Vim (Windows/Linux/Mac OS) - Emacs
(Windows/Linux/Mac OS)

As already mentioned, there are no “right” or “wrong” editors. The
preference of an editor is a personal choice and we recommend trying
different editors. The lists on this page don’t contain all editors, but
just a few of the most popular ones.

Editor or ``>>>`` prompt?
^^^^^^^^^^^^^^^^^^^^^^^^^

So far we have used the ``>>>`` prompt for everything. But now we also
have an editor that lets us write longer programs. So why not just
always use the editor?

The ``>>>`` prompt is meant to be used for experimenting with things.
For example, if you want to know what ``"hello" + 123`` does, just open
the prompt and run it.

If you want to write something once and then run it many times, write
the code to a file. For example, if you want to make a program that asks
the user to enter a word and then echoes it back, write a program that
does that in a file and run it as many times as you want to.

Note that if you write something like ``'hello'`` to the ``>>>`` prompt
it echoes it back, but if you make a file that contains nothing but a
``'hello'`` it won’t do anything when you run it. You need to use
``print('hello')`` instead when your code is in a file.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <using-functions.md>`__ \| `Next <if.md>`__ \| `List of
contents <../README.md#basics>`__

If, else and elif
-----------------

Using if statements
^^^^^^^^^^^^^^^^^^^

Now we know what True and False are.

.. code:: python

   >>> 1 == 1
   True
   >>> 1 == 2
   False
   >>>
   >>> its_raining = True
   >>> its_raining
   True
   >>>

But what if we want to execute different code depending on something?
That’s when ``if`` comes in.

.. code:: python

   >>> its_raining = True
   >>> if its_raining:
   ...     print("It's raining!")
   ...
   It's raining!
   >>> its_raining = False
   >>> if its_raining:
   ...     print("It's raining!")        # nothing happens
   ...
   >>>

The prompt changed from ``>>>`` to ``...``. It meant that Python was
expecting me to keep typing. When I was done, I just pressed Enter
twice. My code was executed and the prompt went back to ``>>>``.

An important thing to notice is that the line with a print is
**indented**. You can press the tab key, or if it doesn’t work just
press space a few times.

But why is that ``if its_raining`` instead of ``if(its_raining)``?

Earlier we learned that ``if`` is a **keyword**.

.. code:: python

   >>> if = 123
     File "<stdin>", line 1
       if = 123
          ^
   SyntaxError: invalid syntax
   >>>

**Functions** like ``print`` need ``()`` after their name to work. But
``if`` is **a keyword**, not a function, so it doesn’t need ``()``.
Python has separate functions and keywords because it’s possible to
create custom functions, but it’s not possible to create custom
keywords. That’s why keywords are usually used for “magic” things that
would be difficult to do with just functions.

Also note that if statements check the condition once only, so if we set
it to false later the if statement won’t notice it.

.. code:: python

   >>> its_raining = True
   >>> if its_raining:
   ...     its_raining = False
   ...     print("It's not raining, but this runs anyway.")
   ...
   It's not raining, but this runs anyway.
   >>>

Using else
^^^^^^^^^^

What if we want to print a different message if it’s not raining? We
could do something like this:

.. code:: python

   its_raining = True                  # you can change this to False
   its_not_raining = not its_raining   # False if its_raining, True otherwise

   if its_raining:
       print("It's raining!")
   if its_not_raining:
       print("It's not raining.")

Note that this code example doesn’t start with ``>>>``, so you should
`save it to a file and run the file <editor-setup.md>`__.

Now our program will print a different value depending on what the value
of ``its_raining`` is.

We can also add ``not its_raining`` directly to the second if statement:

.. code:: python

   its_raining = True

   if its_raining:
       print("It's raining!")
   if not its_raining:
       print("It's not raining.")

But we can make it even better by using ``else``.

.. code:: python

   its_raining = True

   if its_raining:
       print("It's raining!")
   else:
       print("It's not raining.")

The else part simply runs when the if statement doesn’t run. It doesn’t
check the condition again.

.. code:: python

   >>> its_raining = True
   >>> if its_raining:
   ...     its_raining = False
   ... else:
   ...     print("It's not raining, but this still doesn't run.")
   ...
   >>>

By combining ``else`` with the input function we can make a program that
asks for a password and checks if it’s correct.

.. code:: python

   print("Hello!")
   password = input("Enter your password: ")

   if password == "secret":
       print("That's correct, welcome!")
   else:
       print("Access denied.")

The program prints different things depending on what we enter:


   Hello!
   Enter your password: secret
   Welcome!


   Hello!
   Enter your password: lol
   Access denied.

Using the input function for passwords doesn’t work very well because we
can’t hide the password with asterisks. There are better ways to get a
password from the user, but you shouldn’t worry about that just yet.

Avoiding many levels of indentation with elif
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we have more than one condition to check, we could do this:

.. code:: python

   print("Hello!")
   word = input("Enter something: ")

   if word == "hi":
       print("Hi to you too!")
   else:
       if word == "hello":
           print("Hello hello!")
       else:
           if word == "howdy":
               print("Howdyyyy!")
           else:
               if word == "hey":
                   print("Hey hey hey!")
               else:
                   if word == "gday m8":
                       print("Gday 4 u 2!")
                   else:
                       print("I don't know what", word, "means.")

This code is a mess. We need to indent more every time we want to check
for more words. Here we check for 5 different words, so we have 5 levels
of indentation. If we would need to check 30 words, the code would
become really wide and it would be hard to work with.

Instead of typing ``else``, indenting more and typing an ``if`` we can
simply type ``elif``, which is short for ``else if``. Like this:

.. code:: python

   print("Hello!")
   word = input("Enter something: ")

   if word == "hi":
       print("Hi to you too!")
   elif word == "hello":
       print("Hello hello!")
   elif word == "howdy":
       print("Howdyyyy!")
   elif word == "hey":
       print("Hey hey hey!")
   elif word == "gday m8":
       print("Gday 4 u 2!")
   else:
       print("I don't know what", word, "means.")

Now the program is shorter and much easier to read.

Note that the ``elif`` parts only run if nothing before them matches,
and the ``else`` runs only when none of the ``elifs`` match. If we would
have used ``if`` instead, all possible values would be always checked
and the ``else`` part would run always except when word is
``"gday m8"``. This is why we use ``elif`` instead of ``if``.

For example, this program prints only ``hello``\ …

.. code:: python

   if 1 == 1:
       print("hello")
   elif 1 == 2:
       print("this is weird")
   else:
       print("world")

…but this prints ``hello`` *and* ``world``:

.. code:: python

   if 1 == 1:
       print("hello")
   if 1 == 2:
       print("this is weird")
   else:
       print("world")

Now the ``else`` belongs to the ``if 1 == 2`` part and **it has nothing
to do with the ``if 1 == 1`` part**. On the other hand, the elif version
**grouped the multiple ifs together** and the ``else`` belonged to all
of them. Adding a blank line makes this obvious:

.. code:: python

   if 1 == 1:
       print("hello")

   if 1 == 2:
       print("this is weird")
   else:
       print("world")

In general, adding blank lines to appropriate places is a good idea. If
you are asked to “fix code”, feel free to add missing blank lines.

.. _summary-6:

Summary
^^^^^^^

-  If a code example starts with ``>>>`` run it on the interactive
   prompt. If it doesn’t, write it to a file and run that file.
-  Indentation is important in Python.
-  Indented code under an if statement runs if the condition is true.
-  We can also add an else statement. Indented code under it will run if
   the code under the if statement does not run.
-  elif is short for else if.

Exercises
^^^^^^^^^

1. This program contains several problems. Copy-paste it to a file, then
   try to run it, fix the errors you got, try to run it again and keep
   going until it works.

   .. code:: python

      print(Hello!)
      something == input('Enter something: )
      print('You entered:' something)

2. Fix this program the same way:

   .. code:: python

      print('Hello!')
      something = input("Enter something: ")
      if something = 'hello':
          print("Hello for you too!")

      elif something = 'hi'
          print('Hi there!')
      else:
          print("I don't know what," something, "means.")

3. Write a program into a file that asks the user to write a word and
   then prints that word 1000 times. For example, if the user enters
   ``hi`` the program would reply ``hihihihihihihihi`` …

4. Add spaces between the words, so the output is like ``hi hi hi hi`` …

5. Make something that asks the user to enter two words, and prints 1000
   of each with spaces in between. For example, if the user enters
   ``hello`` and ``hi`` the program would print
   ``hello hi hello hi hello hi hello hi hello hi`` …

6. Make a program that asks for a password and prints ``Welcome!``,
   ``Access denied`` or ``You didn't enter anything`` depending on
   whether the user entered the correct password, a wrong password, or
   nothing at all by pressing Enter without typing anything.

The answers are `here <answers.md#if-else-and-elif>`__.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <editor-setup.md>`__ \| `Next <handy-stuff-strings.md>`__ \|
`List of contents <../README.md#basics>`__

Handy stuff: Strings
--------------------

Python strings are just pieces of text.

.. code:: python

   >>> our_string = "Hello World!"
   >>> our_string
   'Hello World!'
   >>>

So far we know how to add them together.

.. code:: python

   >>> "I said: " + our_string
   'I said: Hello World!'
   >>>

We also know how to repeat them multiple times.

.. code:: python

   >>> our_string * 3
   'Hello World!Hello World!Hello World!'
   >>>

Python strings are
`immutable <https://docs.python.org/3/glossary.html#term-immutable>`__.
That’s just a fancy way to say that they cannot be changed in-place, and
we need to create a new string to change them. Even
``some_string += another_string`` creates a new string. Python will
treat that as ``some_string = some_string + another_string``, so it
creates a new string but it puts it back to the same variable.

``+`` and ``*`` are nice, but what else can we do with strings?

Slicing
^^^^^^^

Slicing is really simple. It just means getting a part of the string.
For example, to get all characters between the second place between the
characters and the fifth place between the characters, we can do this:

.. code:: python

   >>> our_string[2:5]
   'llo'
   >>>

So the syntax is like ``some_string[start:end]``.

This picture explains how the slicing works:

.. figure:: ../images/slicing1.png
   :alt: Slicing with non-negative values

   Slicing with non-negative values

But what happens if we slice with negative values?

.. code:: python

   >>> our_string[-5:-2]
   'orl'
   >>>

It turns out that slicing with negative values simply starts counting
from the end of the string.

.. figure:: ../images/slicing2.png
   :alt: Slicing with negative values

   Slicing with negative values

If we don’t specify the beginning it defaults to 0, and if we don’t
specify the end it defaults to the length of the string. For example, we
can get everything except the first or last character like this:

.. code:: python

   >>> our_string[1:]
   'ello World!'
   >>> our_string[:-1]
   'Hello World'
   >>>

Remember that strings can’t be changed in-place.

.. code:: python

   >>> our_string[:5] = 'Howdy'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment
   >>>

There’s also a step argument we can give to our slices, but I’m not
going to talk about it now.

Indexing
^^^^^^^^

So now we know how slicing works. But what happens if we forget the
``:``?

.. code:: python

   >>> our_string[1]
   'e'
   >>>

That’s interesting. We got a string that is only one character long. But
the first character of ``Hello World!`` should be ``H``, not ``e``, so
why did we get an e?

Programming starts at zero. Indexing strings also starts at zero. The
first character is ``our_string[0]``, the second character is
``our_string[1]``, and so on.

.. code:: python

   >>> our_string[0]
   'H'
   >>> our_string[1]
   'e'
   >>> our_string[2]
   'l'
   >>> our_string[3]
   'l'
   >>> our_string[4]
   'o'
   >>>

So string indexes work like this:

.. figure:: ../images/indexing1.png
   :alt: Indexing with non-negative values

   Indexing with non-negative values

How about negative values?

.. code:: python

   >>> our_string[-1]
   '!'
   >>>

We got the last character.

But why didn’t that start at zero? ``our_string[-1]`` is the last
character, but ``our_string[1]`` is not the first character!

That’s because 0 and -0 are equal, so indexing with -0 would do the same
thing as indexing with 0.

Indexing with negative values works like this:

.. figure:: ../images/indexing2.png
   :alt: Indexing with negative values

   Indexing with negative values

String methods
^^^^^^^^^^^^^^

Python’s strings have many useful methods. `The official
documentation <https://docs.python.org/3/library/stdtypes.html#string-methods>`__
covers them all, but I’m going to just show some of the most commonly
used ones briefly. Python also comes with built-in documentation about
the string methods and we can run ``help(str)`` to read it. We can also
get help about one string method at a time, like ``help(str.upper)``.

Again, nothing can modify strings in-place. Most string methods return a
new string, but things like ``our_string = our_string.upper()`` still
work because the new string is assigned to the old variable.

Also note that all of these methods are used like
``our_string.stuff()``, not like ``stuff(our_string)``. The idea with
that is that our string knows how to do all these things, like
``our_string.stuff()``, we don’t need a separate function that does
these things like ``stuff(our_string)``. We’ll learn more about methods
`later <classes.md>`__.

Here’s an example with some of the most commonly used string methods:

.. code:: python

   >>> our_string.upper()
   'HELLO WORLD!'
   >>> our_string.lower()
   'hello world!'
   >>> our_string.startswith('Hello')
   True
   >>> our_string.endswith('World!')
   True
   >>> our_string.endswith('world!')  # Python is case-sensitive
   False
   >>> our_string.replace('World', 'there')
   'Hello there!'
   >>> our_string.replace('o', '@', 1)   # only replace one o
   'Hell@ World!'
   >>> '  hello 123  '.lstrip()    # left strip
   'hello 123  '
   >>> '  hello 123  '.rstrip()    # right strip
   '  hello 123'
   >>> '  hello 123  '.strip()     # strip from both sides
   'hello 123'
   >>> '  hello abc'.rstrip('cb')  # strip c's and b's from right
   '  hello a'
   >>> our_string.ljust(30, '-')
   'Hello World!------------------'
   >>> our_string.rjust(30, '-')
   '------------------Hello World!'
   >>> our_string.center(30, '-')
   '---------Hello World!---------'
   >>> our_string.count('o')   # it contains two o's
   2
   >>> our_string.index('o')   # the first o is our_string[4]
   4
   >>> our_string.rindex('o')  # the last o is our_string[7]
   7
   >>> '-'.join(['hello', 'world', 'test'])
   'hello-world-test'
   >>> 'hello-world-test'.split('-')
   ['hello', 'world', 'test']
   >>> our_string.upper()[3:].startswith('LO WOR')  # combining multiple things
   True
   >>>

The things in square brackets that the split method gave us and we gave
to the join method were lists. We’ll talk more about them
`later <lists-and-tuples.md>`__.

String formatting
^^^^^^^^^^^^^^^^^

To add a string in the middle of another string, we can do something
like this:

.. code:: python

   >>> name = 'Akuli'
   >>> 'My name is ' + name + '.'
   'My name is Akuli.'
   >>>

But that gets complicated if we have many things to add.

.. code:: python

   >>> channel = '##learnpython'
   >>> network = 'freenode'
   >>> "My name is " + name + " and I'm on the " + channel + " channel on " + network + "."
   "My name is Akuli and I'm on the ##learnpython channel on freenode."
   >>>

Instead it’s recommended to use string formatting. It means putting
other things in the middle of a string.

Python has multiple ways to format strings. One is not necessarily
better than others; they each have their own advantages and
disadvantages. In this tutorial, we will focus on f-strings, which is
the most common and usually the easiest way.

``f`` in f-strings stands for “format”, f-strings are string literals
that have an ``f`` at the beginning and curly braces containing
expressions that will be replaced with their values at runtime. To
create f-strings, you have to add an ``f`` or an ``F`` before the
opening quotes of a string.

.. code:: python

   >>> f"My name is {name} and I'm on the {channel} channel on {network}."
   "My name is Akuli and I'm on the ##learnpython channel on freenode."
   >>>

Other things
^^^^^^^^^^^^

We can use ``in`` and ``not in`` to check if a string contains another
string.

.. code:: python

   >>> our_string = "Hello World!"
   >>> "Hello" in our_string
   True
   >>> "Python" in our_string
   False
   >>> "Python" not in our_string
   True
   >>>

We can get the length of a string with the ``len`` function. The name
``len`` is short for “length”.

.. code:: python

   >>> len(our_string)   # 12 characters
   12
   >>> len('')     # no characters
   0
   >>> len('\n')    # python thinks of \n as one character
   1
   >>>

We can convert strings, integers and floats with each other with
``str``, ``int`` and ``float``. They aren’t actually functions, but they
behave a lot like functions. We’ll learn more about what they really are
`later <classes.md>`__.

.. code:: python

   >>> str(3.14)
   '3.14'
   >>> float('3.14')
   3.14
   >>> str(123)
   '123'
   >>> int('123')
   123
   >>>

Giving an invalid string to ``int`` or ``float`` produces an error
message.

.. code:: python

   >>> int('lol')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: invalid literal for int() with base 10: 'lol'
   >>> float('hello')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: could not convert string to float: 'hello'
   >>>

.. _summary-7:

Summary
^^^^^^^

-  Slicing returns a copy of a string with indexes from one index to
   another index. The indexes work like this:

   .. figure:: ../images/slicing3.png
      :alt: Slicing

      Slicing

-  Indexing returns one character of a string. Remember that we don’t
   need a ``:`` with indexing. The indexes work like this:

   .. figure:: ../images/indexing3.png
      :alt: Indexing

      Indexing

-  Python has many string methods. Use `the
   documentation <https://docs.python.org/3/library/stdtypes.html#string-methods>`__
   or ``help(str)`` when you don’t remember something about them.

-  String formatting means adding other things to the middle of a
   string. There are multiple ways to do this in Python. You should know
   how to use at least one of these ways.

-  The ``in`` keyword can be used for checking if a string contains
   another string.

-  ``len(string)`` returns string’s length.

-  We can use ``str``, ``int`` and ``float`` to convert values to
   different types.

.. _exercises-1:

Exercises
^^^^^^^^^

1. Fix this program.

   .. code:: python

      print("Hello!")
      word1 = input("Enter something: ")
      word2 = input("Enter another thing: ")
      word3 = input("Enter a third thing: ")
      word4 = input("And yet another thing: ")
      print("You entered " + word1 + ", " + word2 + ", " + word3 + " and " + word4 + ".")

2. This program is supposed to say something loudly. Fix it.

   .. code:: python

      message = input("What do you want me to say? ")
      message.upper
      print(message, "!!!")
      print(message, "!!!")
      print(message, "!!!")

3. Make a program to ask a string from the user and check if it is a
   palindrome. (Hint: A string is a palindrome if it is the same when
   reversed. Google how to reverse a string.)

The answers are `here <answers.md#handy-stuff-strings>`__.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <if.md>`__ \| `Next <lists-and-tuples.md>`__ \| `List of
contents <../README.md#basics>`__

Lists and tuples
----------------

Why should we use lists?
^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes we may end up doing something like this.

.. code:: python

   name1 = 'wub_wub'
   name2 = 'theelous3'
   name3 = 'RubyPinch'
   name4 = 'go|dfish'
   name5 = 'Nitori'

   name = input("Enter your name: ")
   if name == name1 or name == name2 or name == name3 or name == name4 or name == name5:
       print("I know you!")
   else:
       print("Sorry, I don't know who you are :(")

This code works just fine, but there’s a problem. The name check is
repetitive, and adding a new name requires adding even more repetitive,
boring checks.

Our first list
^^^^^^^^^^^^^^

Instead of adding a new variable for each name it might be better to
store all names in one variable. This means that our one variable needs
to point to multiple values. An easy way to do this is using a list:

.. code:: python

   names = ['wub_wub', 'theelous3', 'Nitori', 'RubyPinch', 'go|dfish']

Here the ``names`` variable points to a list, which then points to
strings, like this:

.. figure:: ../images/people.png
   :alt: List of names.

   List of names.

What can we do with lists?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Let’s open the ``>>>`` prompt and create a name list.

.. code:: python

   >>> names = ['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori']
   >>> names
   ['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori']
   >>>

There’s many things `we can do with strings <handy-stuff-strings.md>`__,
and some of these things also work with lists.

.. code:: python

   >>> len(names)   # len is short for length, we have 5 names
   5
   >>> names + ['Akuli']   # create a new list with me in it
   ['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori', 'Akuli']
   >>> ['theelous3', 'RubyPinch'] * 2    # repeating
   ['theelous3', 'RubyPinch', 'theelous3', 'RubyPinch']
   >>>

With strings indexing and slicing both returned a string, but with lists
we get a new list when we’re slicing and an element from the list if
we’re indexing.

.. code:: python

   >>> names[:2]    # first two names
   ['wub_wub', 'theelous3']
   >>> names[0]     # the first name
   'wub_wub'
   >>>

If we want to check if the program knows a name all we need to do is to
use the ``in`` keyword.

.. code:: python

   >>> 'lol' in names
   False
   >>> 'RubyPinch' in names
   True
   >>>

We can’t use this for checking if a list of names is a part of our name
list.

.. code:: python

   >>> ['RubyPinch', 'go|dfish'] in names
   False
   >>> ['RubyPinch'] in names
   False
   >>>

Lists have a few `useful
methods <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>`__.
Some of the most commonly used ones are append, extend and remove.
``append`` adds an item to the end of a list, ``extend`` adds multiple
items from another list and ``remove`` removes an item.

.. code:: python

   >>> names
   ['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori']
   >>> names.remove('theelous3')  # sorry theelous3
   >>> names.remove('go|dfish')   # and sorry go|dfish
   >>> names
   ['wub_wub', 'RubyPinch', 'Nitori']
   >>> names.append('Akuli')    # let's add me here
   >>> names
   ['wub_wub', 'RubyPinch', 'Nitori', 'Akuli']
   >>> names.extend(['go|dfish', 'theelous3'])  # wb guys
   >>> names
   ['wub_wub', 'RubyPinch', 'Nitori', 'Akuli', 'go|dfish', 'theelous3']
   >>>

Note that ``remove`` removes only the first match it finds.

.. code:: python

   >>> names = ['theelous3', 'go|dfish', 'theelous3']
   >>> names.remove('theelous3')
   >>> names    # the second theelous3 is still there!
   ['go|dfish', 'theelous3']
   >>>

If we need to remove all matching items we can use a simple while loop.
We’ll talk more about loops `in the next chapter <loops.md>`__.

.. code:: python

   >>> names = ['theelous3', 'go|dfish', 'theelous3']
   >>> while 'theelous3' in names:
   ...     names.remove('theelous3')
   ...
   >>> names
   ['go|dfish']
   >>>

Another useful thing about lists is **list comprehension**. It’s a handy
way to construct a list in single line. It often makes code cleaner,
shorter and easier to read.

.. code:: python

   >>> numbers = [1,2,3,4,5]
   >>> numbers_squared = [number ** 2 for number in numbers]
   >>> numbers_squared
   [1, 4, 9, 16, 25]
   >>>

Without a list comprehension, doing the same thing looks like this:

.. code:: python

   >>> numbers = [1,2,3,4,5]
   >>> numbers_squared = []
   >>> for number in numbers:
   ...     numbers_squared.append(number**2)
   >>> numbers_squared
   [1, 4, 9, 16, 25]
   >>>

We can also use slicing and indexing to change the content:

.. code:: python

   >>> names = ['theelous3', 'LOL', 'RubyPinch', 'go|dfish', 'Nitori']
   >>> names[1] = 'wub_wub'   # replace LOL with wub_wub
   >>> names
   ['theelous3', 'wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
   >>>

As you can see, **list can be changed in-place**. In other words, they
are **mutable**. Integers, floats, strings and many other built-in types
can’t, so they are **immutable**.

With `strings <handy-stuff-strings.md>`__ we did something to them and
then set the result back to the same variable, like
``message = message.strip()``. This just doesn’t work right with most
mutable things because they’re designed to be changed in-place.

.. code:: python

   >>> names = names.remove('Akuli')
   >>> print(names)     # now it's None!
   None
   >>>

This is the same thing that happened way back when `we assigned print’s
return value to a variable <using-functions.md#return-values>`__.

What is what?
^^^^^^^^^^^^^

After working with lists a while you’ll find out that they behave like
this:

.. code:: python

   >>> a = [1, 2, 3]
   >>> b = a
   >>> b.append(4)
   >>> a    # this changed also!
   [1, 2, 3, 4]
   >>>

This can be confusing at first, but it’s actually easy to explain. The
problem with this code example is the ``b = a`` line. If we draw a
picture of the variables it looks like this:

.. figure:: ../images/samelist.png
   :alt: Same list.

   Same list.

This is when the ``is`` keyword comes in. It can be used to check if two
variables point to the **same** thing.

.. code:: python

   >>> a is b
   True
   >>>

Typing ``[]`` creates a **new** list every time.

.. code:: python

   >>> [] is []
   False
   >>> [1, 2, 3] is [1, 2, 3]
   False
   >>>

If we need **a new list with similar content** we can use the ``copy``
method.

.. code:: python

   >>> a = [1, 2, 3]
   >>> b = a.copy()
   >>> b is a
   False
   >>> b.append(4)
   >>> b
   [1, 2, 3, 4]
   >>> a
   [1, 2, 3]
   >>>

If we draw a picture of our variables in this example it looks like
this:

.. figure:: ../images/differentlist.png
   :alt: Different lists.

   Different lists.

Tuples
^^^^^^

Tuples are a lot like lists, but they’re immutable so they can’t be
changed in-place. We create them like lists, but with ``()`` instead of
``[]``.

.. code:: python

   >>> thing = (1, 2, 3)
   >>> thing
   (1, 2, 3)
   >>> thing = ()
   >>> thing
   ()
   >>>

If we need to create a tuple that contains only one item we need to use
``(item,)`` instead of ``(item)`` because ``(item)`` is used in places
like ``(1 + 2) * 3``.

.. code:: python

   >>> (3)
   3
   >>> (3,)
   (3,)
   >>> (1 + 2) * 3
   9
   >>> (1 + 2,) * 3
   (3, 3, 3)
   >>>

It’s also possible to create tuples by just separating things with
commas and adding no parentheses. Personally I don’t like this feature,
but some people like to do it this way.

.. code:: python

   >>> 1, 2, 3
   (1, 2, 3)
   >>> 'hello',
   ('hello',)
   >>>

Tuples don’t have methods like append, extend and remove because they
can’t change themselves in-place.

.. code:: python

   >>> stuff = (1, 2, 3)
   >>> stuff.append(4)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: 'tuple' object has no attribute 'append'
   >>>

So, why the heck would we use tuples instead of lists? There are some
cases when we don’t want mutability, but there are also cases when
Python programmers just like to use tuples. If you want to know more
about this you can read `Ned Batchelder’s blog post about
this <http://nedbatchelder.com/blog/201608/lists_vs_tuples.html>`__.

.. _summary-8:

Summary
^^^^^^^

-  Lists are a way to store multiple values in one variable.
-  Lists can be changed in-place and they have methods that change them
   in-place, like append, extend and remove.
-  Slicing lists returns a **new** list, and indexing them returns an
   item from them.
-  ``thing = another_thing`` does not create a copy of
   ``another_thing``.
-  Tuples are like lists, but they can’t be changed in-place. They’re
   also used in different places.

Examples
^^^^^^^^

Here’s the same program we had in the beginning of this tutorial, but
using a list:

.. code:: python

   namelist = ['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori']

   name = input("Enter your name: ")
   if name in namelist:
       print("I know you!")
   else:
       print("Sorry, I don't know who you are :(")

.. _exercises-2:

Exercises
^^^^^^^^^

1. Fix this program:

   .. code:: python

      namelist = ('wub_wub', 'RubyPinch', 'go|dfish', 'Nitori')
      namelist.append('pb122')
      if 'pb122' in namelist:
          print("Now I know pb122!")

2. Fix this program.

   .. code:: python

      print("Hello!")
      name = input("Enter your name: "),
      print("Your name is " + name + ".")

3. Fix this program.

   .. code:: python

      namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
      namelist = namelist.extend('theelous3')
      if input("Enter your name: ") in namelist:
          print("I know you!")
      else:
          print("I don't know you.")

The answers are `here <answers.md#lists-and-tuples>`__.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <handy-stuff-strings.md>`__ \| `Next <loops.md>`__ \| `List of
contents <../README.md#basics>`__

Loops
-----

In programming, a **loop** means repeating something multiple times.
There are different kinds of loops:

-  `While loops <#while-loops>`__ repeat something while a condition is
   true.
-  `Until loops <#until-loops>`__ repeat something while a condition is
   false.
-  `For loops <#for-loops>`__ repeat something for each element of
   something.

We’ll talk about all of these in this tutorial.

While loops
^^^^^^^^^^^

Now we know how if statements work.

.. code:: python

   its_raining = True
   if its_raining:
       print("Oh crap, it's raining!")

While loops are really similar to if statements.

.. code:: python

   its_raining = True
   while its_raining:
       print("Oh crap, it's raining!")
       # we'll jump back to the line with the word "while" from here
   print("It's not raining anymore.")

If you’re not familiar with while loops, the program’s output may be a
bit surprising:


   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   Oh crap, it's raining!
   (much more raining)

Again, this program does not break your computer. It just prints the
same thing multiple times. We can interrupt it by pressing Ctrl+C.

In this example, ``its_raining`` was the **condition**. If something in
the while loop would have set ``its_raining`` to False, the loop would
have ended and the program would have printed
``It's not raining anymore``.

Let’s actually create a program that does just that:

.. code:: python

   its_raining = True
   while its_raining:
       print("It's raining!")
       answer = input("Or is it? (y=yes, n=no) ")
       if answer == 'y':
           print("Oh well...")
       elif answer == 'n':
           its_raining = False     # end the while loop
       else:
           print("Enter y or n next time.")
   print("It's not raining anymore.")

Running the program may look like this:


   It's raining!
   Or is it? (y=yes, n=no) i dunno
   Enter y or n next time.
   It's raining!
   Or is it? (y=yes, n=no) y
   Oh well...
   It's raining!
   Or is it? (y=yes, n=no) n
   It's not raining anymore.

The while loop doesn’t check the condition all the time, it only checks
it in the beginning.

.. code:: python

   >>> its_raining = True
   >>> while its_raining:
   ...     its_raining = False
   ...     print("It's not raining, but the while loop doesn't know it yet.")
   ...
   It's not raining, but the while loop doesn't know it yet.
   >>>

We can also interrupt a loop even if the condition is still true using
the ``break`` keyword. In this case, we’ll set condition to True and
rely on nothing but ``break`` to end the loop.

.. code:: python

   while True:
       answer = input("Is it raining? (y=yes, n=no) ")
       if answer == 'y':
           print("It's raining!")
       elif answer == 'n':
           print("It's not raining anymore.")
           break   # end the loop
       else:
           print("Enter y or n.")

The program works like this:


   Is it raining? (y=yes, n=no) who knows
   Enter y or n.
   Is it raining? (y=yes, n=no) y
   It's raining!
   Is it raining? (y=yes, n=no) n
   It's not raining anymore.

Unlike setting the condition to False, breaking the loop ends it
immediately.

.. code:: python

   >>> while True:
   ...     break
   ...     print("This is never printed.")
   ...
   >>>

Until loops
^^^^^^^^^^^

Python doesn’t have until loops. If we need an until loop, we can use
``while not``:

.. code:: python

   raining = False
   while not raining:
       print("It's not raining.")
       if input("Is it raining? (y/n) ") == 'y':
           raining = True
   print("It's raining!")

For loops
^^^^^^^^^

Let’s say we have `a list <lists-and-tuples.md>`__ of things we want to
print. To print each item in it, we could just do a bunch of prints:

.. code:: python

   stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']

   print(stuff[0])
   print(stuff[1])
   print(stuff[2])
   print(stuff[3])
   print(stuff[4])

The output of the program is like this:


   hello
   hi
   how are you doing
   im fine
   how about you

But this is only going to print five items, so if we add something to
stuff, it’s not going to be printed. Or if we remove something from
stuff, we’ll get an error saying “list index out of range”.

We could also create an index variable, and use a while loop:

.. code:: python

   >>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
   >>> length_of_stuff = len(stuff)
   >>> index = 0
   >>> while index < length_of_stuff:
   ...     print(stuff[index])
   ...     index += 1
   ...
   hello
   hi
   how are you doing
   im fine
   how about you
   >>>

But we have ``len()`` and an index variable we need to increment and a
while loop and many other things to worry about. That’s a lot of work
just for printing each item.

This is when for loops come in:

.. code:: python

   >>> for thing in stuff:
   ...     # this is repeated for each element of stuff, that is, first
   ...     # for stuff[0], then for stuff[1], etc.
   ...     print(thing)
   ...
   hello
   hi
   how are you doing
   im fine
   how about you
   >>>

Without the comments, that’s only two simple lines, and one variable.
Much better than anything else we tried before.

.. code:: python

   >>> for thing in stuff:
   ...     print(thing)
   ...
   hello
   hi
   how are you doing
   im fine
   how about you
   >>>

Note that ``for thing in stuff:`` is not same as
``for (thing in stuff):``. Here the ``in`` keyword is just a part of the
for loop and it has a different meaning than it would have if we had
``thing in stuff`` without a ``for``. Trying to do
``for (thing in stuff):`` creates an error.

Right now the while loop version might seem easier to understand for
you, but later you’ll realize that for loops are much easier to work
with than while loops and index variables, especially in large projects.
For looping is also a little bit faster than while looping with an index
variable.

For loops are not actually limited to lists. We can for loop over many
other things also, including strings and
`tuples <lists-and-tuples.md#tuples>`__. For looping over a tuple gives
us its items, and for looping over a string gives us its characters as
strings of length one.

.. code:: python

   >>> for short_string in 'abc':
   ...     print(short_string)
   ...
   a
   b
   c
   >>> for item in (1, 2, 3):
   ...     print(item)
   ...
   1
   2
   3
   >>>

If we can for loop over something, then that something is **iterable**.
Lists, tuples and strings are all iterable.

There’s only one big limitation with for looping over lists. We
shouldn’t modify the list in the for loop. If we do, the results can be
surprising:

.. code:: python

   >>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
   >>> for thing in stuff:
   ...     stuff.remove(thing)
   ...
   >>> stuff
   ['hi', 'im fine']
   >>>

Instead, we can create a copy of stuff and loop over it.

.. code:: python

   >>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
   >>> for thing in stuff.copy():
   ...     stuff.remove(thing)
   ...
   >>> stuff
   []
   >>>

Or if we just want to clear a list, we can use the ``clear`` `list
method <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>`__:

.. code:: python

   >>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
   >>> stuff.clear()
   >>> stuff
   []
   >>>

.. _summary-9:

Summary
^^^^^^^

-  A loop means repeating something multiple times.
-  While loops repeat something as long as a condition is true, and they
   check the condition only in the beginning.
-  For loops can be used for repeating something to each item in a list.
-  An iterable is something that can be for looped over.
-  The ``break`` keyword can be used to interrupt the innermost loop at
   any time.

.. _examples-1:

Examples
^^^^^^^^

Repeat something an endless amount of times.

.. code:: python

   message = input("What do you want me to say? ")
   while True:
       print(message, "!!!")

Ask the user to enter five things and print them.

.. code:: python

   things = []

   print("Enter 5 things: ")
   while len(things) < 5:
       thing = input("> ")
       things.append(thing)

   print("You entered these things:")
   for thing in things:
       print(thing)

Ask the user a bunch of questions.

.. code:: python

   questions_and_answers = [
       # [question, answer], ...
       ["What is 2+4? ", "6"],
       ["What is 2-4? ", "-2"],
       ["What is 2*4? ", "8"],
       ["What is 2/4? ", "0.5"],
       # You could add more questions, but the code that asks them
       # wouldn't need to be changed in any way.
   ]

   for qa in questions_and_answers:
       while True:
           if input(qa[0]) == qa[1]:
               print("Correct!")
               break
           else:
               print("That's not what I was thinking of... Try again.")

Store a list of names and let the user check if the program knows the
user.

.. code:: python

   # You can add names here so the program will know them automatically
   # when it starts.
   namelist = []

   print("Options:")
   print("  0      Quit")
   print("  1      Check if I know you")
   print("  2      Introduce yourself to me")
   print("  3      Make me forget you")
   print("  4      Print a list of people I know")
   print()     # print an empty line

   while True:
       option = input("Choose an option: ")

       # Things like option == 0 don't work because option is a string
       # and it needs to be compared with a string:
       #   >>> 0 == 0
       #   True
       #   >>> '0' == '0'
       #   True
       #   >>> 0 == '0'
       #   False
       if option == '0':
           print("Bye!")
           break

       elif option == '1':
           name = input("Enter your name: ")
           if name in namelist:
               print("I know you! :D")
           else:
               print("I don't know you :/")

       elif option == '2':
           name = input("Enter your name: ")
           if name in namelist:
               print("I knew you already.")
           else:
               namelist.append(name)
               print("Now I know you!")

       elif option == '3':
           name = input("Enter your name: ")
           if name in namelist:
               namelist.remove(name)
               print("Now I don't know you.")
           else:
               print("I didn't know you to begin with.")

       elif option == '4':
           if namelist == []:
               print("I don't know anybody yet.")
           else:
               for name in namelist:
                   print(f"I know {name}!")

       else:
           print("I don't understand :(")

       print()

.. _exercises-3:

Exercises
^^^^^^^^^

1. This code is supposed to print the numbers 1,2,3,4,5. Fix it.

   .. code:: python

      things = str([1, 2, 3, 4, 5])
      for thing in things:
          print(thing)

2. This code is supposed to print ``[1, 2, 3, 4, 5, 6]``. Fix it without
   changing the ``before`` list.

   .. code:: python

      before = [[1, 2], [3, 4], [5, 6]]
      after = []
      for number in before:
          after.append(number)
      print(after)

3. This program is supposed to convert everything in a list to integers
   and then calculate their sum. It should print 6 because ``1 + 2 + 3``
   is 6. Fix the program.

   .. code:: python

      input = ['1', '2', '3']

      for string in input:
          numbers = []
          numbers.append(int(string))

      result = 0
      for n in numbers:
          result + n
      print("their sum is", result)

4. This program is supposed to print ``[1, 2, 3]``. Fix it.

   .. code:: python

      numbers = ['1', '2', '3']
      for number in numbers:
          number = int(number)
      print(numbers)

5. Make a program that prints a pyramid like shown below. Ask the user
   to type the number of rows needed.

   ::

      OUTPUT for 5 rows
      1 
      1 2 
      1 2 3 
      1 2 3 4 
      1 2 3 4 5 

6. Make a program to get a pyramid like shown below where user can type
   the number of rows needed.

   ::

      OUTPUT for 5 rows
      1 2 3 4 5 
      2 3 4 5 
      3 4 5 
      4 5 
      5 

   The answers are `here <answers.md#loops>`__.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <lists-and-tuples.md>`__ \| `Next <zip-and-enumerate.md>`__ \|
`List of contents <../README.md#basics>`__

zip and enumerate
-----------------

Now we know how `for loops <loops.md#for-loops>`__ work in Python. But
for loops aren’t limited to printing each item in a list, they can do a
lot more.

To be able to understand for loop tricks we need to first know assigning
values to multiple variables at once. It works like this:

.. code:: python

   >>> a, b = 1, 2
   >>> a
   1
   >>> b
   2
   >>>

We can use ``()`` and ``[]`` around these values however we want and
everything will still work the same way. ``[]`` creates a list, and
``()`` creates a tuple.

.. code:: python

   >>> [a, b] = (1, 2)
   >>> a
   1
   >>> b
   2
   >>>

We can also have ``[]`` or ``()`` on one side but not on the other side.

.. code:: python

   >>> (a, b) = 1, 2
   >>> a
   1
   >>> b
   2
   >>>

Python created a tuple automatically.

.. code:: python

   >>> 1, 2
   (1, 2)
   >>>

If we’re for looping over a list with pairs of values in it we could do
this:

.. code:: python

   >>> items = [('a', 1), ('b', 2), ('c', 3)]
   >>> for pair in items:
   ...     a, b = pair
   ...     print(a, b)
   ...
   a 1
   b 2
   c 3
   >>>

Or we can tell the for loop to unpack it for us.

.. code:: python

   >>> for a, b in items:
   ...     print(a, b)
   ...
   a 1
   b 2
   c 3
   >>>

This feature is often used with Python’s built-in ``zip()`` and
``enumerate()`` functions.

zip
^^^

What comes to your mind when you hear the word ``zip``? A mechanism
extensively used to tie two parts of something, e.g. shirt or jacket.
Python’s ``zip()`` functions does pretty much the same, it helps us tie
corresponding items together.

.. code:: python

   >>> users = ["Tushar", "Aman", "Anurag", "Sohit"]
   >>> uids = ["usr122", "usr123", "usr124", "usr125"]
   >>> user_details = zip(uids, users)
   >>> print(list(user_details))
   [('usr122', 'Tushar'), ('usr123', 'Aman'), ('usr124', 'Anurag'), ('usr125', 'Sohit')]
   >>>

Note that ``print(user_details)`` doesn’t work as expected:


   >>> print(user_details)
   <zip object at 0x0000016938E311C0>
   >>>

This is because ``zip()`` is an iterator, i.e. lazy: it gives the items
as needed, instead of calculating them and storing them into memory all
at once like a list. So the zip object cannot show its elements before
the elements are used, because it hasn’t computed them yet.

.. code:: python

   >>> users = ["Tushar", "Aman", "Anurag", "Sohit"]
   >>> uids = ["usr122", "usr123", "usr124", "usr125"]
   >>> user_details = zip(uids, users)

If the lists are of different lengths, some items from the end of the
longer list will be ignored.

.. code:: python

   >>> users = ["Tushar", "Aman", "Anurag"]
   >>> emails = ["tushar@example.com", "aman@example.com", "anurag@example.com", "sohit@example.com"]
   >>> users_contact = zip(users, emails)
   >>> print(list(users_contact))
   [('Tushar', 'tushar@example.com'), ('Aman', 'aman@example.com'), ('Anurag', 'anurag@example.com')]
   >>>

Here the shortest list is ``users``, with length 3, so
``zip(users, emails)`` only takes the first 3 emails. We do not
recommend calling ``zip()`` with lists of different lengths, because
ignoring items is usually not what you intended to do.

Using zip in a ``for`` loop
```````````````````````````

It is very common to ``for`` loop over a ``zip()``, and unpack the
returned tuples in the ``for`` loop. This is why we introduced unpacking
in the beginning of this page. When used this way, there’s no need to
convert the result of ``zip(...)`` to a list.

.. code:: python

   >>> roll_nums = [20, 25, 28]
   >>> students = ["Joe", "Max", "Michel"]
   >>> for roll_num, student in zip(roll_nums, students):
   ...     print(f"Roll number of {student} is {roll_num}")
   ...
   Roll number of Joe is 20
   Roll number of Max is 25
   Roll number of Michel is 28
   >>>

enumerate
^^^^^^^^^

``enumerate()`` is an amazing Built-in function offered by python. When
used, gives us the index and the item combined.

.. code:: python

   >>> even_nums = [2, 4, 6, 8, 10, 12]
   >>> for index, item in enumerate(even_nums):
   ...     print(f"Index of {item} is {index}")
   ...
   Index of 2 is 0
   Index of 4 is 1
   Index of 6 is 2
   Index of 8 is 3
   Index of 10 is 4
   Index of 12 is 5
   >>>

It is also possible (but more difficult) to do this without
``enumerate()``:

.. code:: python

   >>> even_nums = [2, 4, 6, 8, 10, 12]
   >>> for index in range(0,  len(even_nums)):
   ...     print(f"Index of {even_nums[index]} is {index}")
   ...
   Index of 2 is 0
   Index of 4 is 1
   Index of 6 is 2
   Index of 8 is 3
   Index of 10 is 4
   Index of 12 is 5
   >>>

Here: \* ``range(0, len(even_nums))`` gives 0,1,2,3,4,5, with the list
length 6 excluded. These are the indexes of our list of length 6. \*
``even_nums[index]`` prints each element of ``even_nums``, because
``index`` comes from the range of all indexes into that list.

Because this is complicated to think about and easy to get wrong, it is
better to use ``enumerate()``.

.. _exercises-4:

Exercises
^^^^^^^^^

1. Create a program that works like this. Here I entered everything
   after the ``>`` prompt that the program displayed.

   ::

      Enter something, and press Enter without typing anything when you're done.
      >hello there
      >this is a test
      >it seems to work
      >
      Line 1 is: hello there
      Line 2 is: this is a test
      Line 3 is: it seems to work

2. Create a program that prints all letters from A to Z and a to z next
   to each other:

   ::

      A a
      B b
      C c
      ...
      X x
      Y y
      Z z

   Start your program like this:

   .. code:: python

      uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      lowercase = 'abcdefghijklmnopqrstuvwxyz'

   **Hint:** how do strings behave with ``zip``? Try it out on the
   ``>>>`` prompt and see.

3. Can you make it print the indexes also?

   ::

      1 A a
      2 B b
      3 C c
      ...
      24 X x
      25 Y y
      26 Z z

The answers are `here <answers.md>`__.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <loops.md>`__ \| `Next <dicts.md>`__ \| `List of
contents <../README.md#basics>`__

Dictionaries
------------

Now we know how `lists and tuples <lists-and-tuples.md>`__ work and how
to `for loop <loops.md#for-loops>`__ over them. If we make some kind of
program that needs to keep track of people’s names and favorite pets, we
can use a list for that:

.. code:: python

   names_and_pets = [
       ('horusr', 'cats'),
       ('caisa64', 'cats and dogs'),
       ('__Myst__', 'cats'),
   ]

Then to check if cats are horusr’s favorite pets we can do
``('horusr', 'cats') in names_and_pets``. Or we can add new people’s
favorite pets easily by appending new ``(name, pets)`` tuples to the
list.

But what if we need to check if we know anything about someone’s
favorite pets? ``'caisa64' in names_and_pets`` is always False because
the pet list consists of ``(name, pets)`` pairs instead of just names,
so we need to for loop over the whole pet list:

.. code:: python

   found_caisa64 = False
   for pair in names_and_pets:
       if pair[0] == 'caisa64':
           found_caisa64 = True
           break
   if found_caisa64:
       # do something

Or what if we need to find out what caisa64’s favorite pets are? That
also requires going through the whole list.

.. code:: python

   pets = None
   for pair in names_and_pets:
       if pair[0] == 'caisa64':
           pets = pair[1]
           break
   # make sure pets is not None and do something with it

As you can see, a list of ``(name, pets)`` pairs is not an ideal way to
store names and favorite pets.

What are dictionaries?
^^^^^^^^^^^^^^^^^^^^^^

A better way to store information about favorite pets might be a
dictionary:

.. code:: python

   favorite_pets = {
       'horusr': 'cats',
       'caisa64': 'cats and dogs',
       '__Myst__': 'cats',
   }

Here ``'horusr'`` and ``'caisa64'`` are **keys** in the dictionary, and
``'cats'`` and ``'cats and dogs'`` are their **values**. Dictionaries
are often named by their values. This dictionary has favorite pets as
its values so I named the variable ``favorite_pets``.

There are a few big differences between dictionaries and lists of pairs:

-  Dictionaries are not ordered. There are **no guarantees** about which
   order the ``name: pets`` pairs appear in when we do something with
   the dictionary.
-  Checking if a key is in the dictionary is simple and fast. We don’t
   need to for loop through the whole dictionary.
-  Getting the value of a key is also simple and fast.
-  We can’t have the same key in the dictionary multiple times, but
   multiple different keys can have the same value. This means that
   **multiple people can’t have the same name, but they can have the
   same favorite pets**.

But wait… this is a lot like variables are! Our variables are not
ordered, getting a value of a variable is fast and easy and we can’t
have multiple variables with the same name.

Variables are actually stored in a dictionary. We can get that
dictionary with the globals function. In this dictionary, keys are
variable names and values are what our variables point to.

.. code:: python

   >>> globals()
   {'names_and_pets': [('horusr', 'cats'),
                       ('caisa64', 'cats and dogs'),
                       ('__Myst__', 'cats')],
    'favorite_pets': {'__Myst__': 'cats',
                      'caisa64': 'cats and dogs',
                      'horusr': 'cats'},
    ...many other things we don't need to care about...
   }
   >>>

So if you have trouble remembering how dictionaries work just compare
them to variables. A dictionary is a perfect way to store these names
and favorite pets. We don’t care about which order the names and pets
were added in, it’s impossible to add the same name multiple times and
getting someone’s favorite pets is easy.

What can we do with dictionaries?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dictionaries have some similarities with lists. For example, both lists
and dictionaries have a length.

.. code:: python

   >>> len(names_and_pets)     # contains three elements
   3
   >>> len(favorite_pets)    # contains three key:value pairs
   3
   >>>

We can get a value of a key with ``the_dict[key]``. This is a lot easier
and faster than for-looping over a list of pairs.

.. code:: python

   >>> favorite_pets['caisa64']
   'cats and dogs'
   >>> favorite_pets['__Myst__']
   'cats'
   >>>

Trying to get the value of a non-existing key gives us an error.

.. code:: python

   >>> favorite_pets['Akuli']
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   KeyError: 'Akuli'
   >>>

But we can add new ``key: value`` pairs or change the values of existing
keys by doing ``the_dict[key] = value``.

.. code:: python

   >>> favorite_pets['Akuli'] = 'penguins'
   >>> favorite_pets['Akuli']
   'penguins'
   >>> favorite_pets['Akuli'] = 'dogs'
   >>> favorite_pets['Akuli']
   'dogs'
   >>> favorite_pets
   {'__Myst__': 'cats',
    'Akuli': 'dogs',
    'horusr': 'cats',
    'caisa64': 'cats and dogs'}
   >>>

For looping over a dictionary gets its keys, and checking if something
is in the dictionary checks if the dictionary has a key like that. This
can be confusing at first but you’ll get used to this.

.. code:: python

   >>> 'Akuli' in favorite_pets
   True
   >>> 'dogs' in favorite_pets
   False
   >>> for name in favorite_pets:
   ...     print(name)
   ...
   caisa64
   Akuli
   __Myst__
   horusr
   >>>

Dictionaries have a values method that we can use if we want to do
something with the values:

.. code:: python

   >>> favorite_pets.values()
   dict_values(['dogs', 'cats', 'cats and dogs', 'cats'])
   >>>

The values method returned a ``dict_values`` object. Things like this
behave a lot like lists and usually we don’t need to convert them to
lists.

.. code:: python

   >>> for pets in favorite_pets.values():
   ...     print(pets)
   ...
   dogs
   cats
   cats and dogs
   cats
   >>>

We can do things like ``list(favorite_pets.values())`` if we need a real
list for some reason, but doing that can slow down our program if the
dictionary is big. There’s also a keys method, but usually we don’t need
it because the dictionary itself behaves a lot like a list of keys.

If we need both keys and values we can use the items method with the
``for first, second in thing`` trick.

.. code:: python

   >>> favorite_pets.items()
   dict_items([('Akuli', 'dogs'),
               ('__Myst__', 'cats'),
               ('caisa64', 'cats and dogs'),
               ('horusr', 'cats')])
   >>> for name, pets in favorite_pets.items():
   ...     print("{} are {}'s favorite pets".format(pets, name))
   ...
   dogs are Akuli's favorite pets
   cats are __Myst__'s favorite pets
   cats and dogs are caisa64's favorite pets
   cats are horusr's favorite pets
   >>>

This is also useful for checking if the dictionary has a ``key: value``
pair.

.. code:: python

   >>> ('horusr', 'cats') in favorite_pets.items()
   True
   >>> ('horusr', 'dogs') in favorite_pets.items()
   False
   >>>

Limitations
^^^^^^^^^^^

Sometimes it might be handy to use lists as dictionary keys, but it just
doesn’t work. I’m not going to explain why Python doesn’t allow this
because usually we don’t need to worry about that.

.. code:: python

   >>> stuff = {['a', 'b']: 'c', ['d', 'e']: 'f'}
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: unhashable type: 'list'
   >>>

On the other hand, tuples work just fine:

.. code:: python

   >>> stuff = {('a', 'b'): 'c', ('d', 'e'): 'f'}
   >>> stuff
   {('a', 'b'): 'c', ('d', 'e'): 'f'}
   >>>

The values of a dictionary can be anything.

.. code:: python

   >>> stuff = {'a': [1, 2, 3], 'b': [4, 5, 6]}
   >>> stuff
   {'a': [1, 2, 3], 'b': [4, 5, 6]}
   >>>

.. _summary-10:

Summary
^^^^^^^

-  Dictionaries consist of ``key: value`` pairs.
-  Variables are stored in a dictionary with their names as keys, so
   dictionaries behave a lot like variables:

   -  Dictionaries are not ordered.
   -  Setting or getting the value of a key is simple and fast.
   -  Dictionaries can’t contain the same key more than once.

-  For-looping over a dictionary loops over its keys, and checking if
   something is in the dictionary checks if the dictionary has a key
   like that. The ``values()`` and ``items()`` methods return things
   that behave like lists of values or ``(key, value)`` pairs instead.

.. _examples-2:

Examples
^^^^^^^^

This program counts how many times words appear in a sentence.
``sentence.split()`` creates a list of words in the sentence, see
``help(str.split)`` for more info.

.. code:: python

   sentence = input("Enter a sentence: ")

   counts = {}     # {word: count, ...}
   for word in sentence.split():
       if word in counts:
           # we have seen this word before
           counts[word] += 1
       else:
           # this is the first time this word occurs
           counts[word] = 1

   print()     # display an empty line
   for word, count in counts.items():
       if count == 1:
           # "1 times" looks weird
           print(word, "appears once in the sentence")
       else:
           print(word, "appears", count, "times in the sentence")

Running the program might look like this:


   Enter a sentence: this is a test and this is quite long because this is a test

   is appears 3 times in the sentence
   long appears once in the sentence
   a appears 2 times in the sentence
   because appears once in the sentence
   this appears 3 times in the sentence
   quite appears once in the sentence
   and appears once in the sentence
   test appears 2 times in the sentence

**TODO:** Exercises.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <zip-and-enumerate.md>`__ \| `Next <defining-functions.md>`__
\| `List of contents <../README.md#basics>`__

Defining custom functions
-------------------------

It’s probably been a while since you read about using functions. `Read
about it again <using-functions.md>`__ if you need to.

Why should I use custom functions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Have a look at this code:

.. code:: python

   print("************")
   print("Hello World!")
   print("************")

   print("*************")
   print("Enter a word:")
   print("*************")

   word = input()

   if word == 'python':
       print("*******************")
       print("You entered Python!")
       print("*******************")
   else:
       print("**************************")
       print("You didn't enter Python :(")
       print("**************************")

Then compare it to this code:

.. code:: python

   print_box("Hello World!")
   print_box("Enter a word:")
   word = input()
   if word == 'python':
       print_box("You entered Python!")
   else:
       print_box("You didn't enter Python :(")

In this tutorial we’ll learn to define a ``print_box`` function that
prints text in a box. We can write the code for printing the box once,
and then use it multiple times anywhere in the program.

`Dividing a long program into simple functions <larger-program.md>`__
also makes the code easier to work with. If there’s a problem with the
code we can test the functions one by one and find the problem easily.

First functions
^^^^^^^^^^^^^^^

The ``pass`` keyword does nothing.

.. code:: python

   >>> pass
   >>>

Let’s use it to define a function that does nothing.

.. code:: python

   >>> def do_nothing():
   ...     pass
   ...
   >>> do_nothing
   <function do_nothing at 0x7f56b74e9598>
   >>>

Seems to be working so far, we have a function. It’s just a value that
is assigned to a variable called ``do_nothing``. You can ignore the
``0xblablabla`` stuff for now.

The ``pass`` is needed here because without it, Python doesn’t know when
the function ends and it gives us a syntax error. We don’t need the
``pass`` when our functions contain something else.

Let’s see what happens if we call our function.

.. code:: python

   >>> do_nothing()
   >>>

There we go. It did nothing at all.

Maybe we could just do something in the function instead?

.. code:: python

   >>> def print_hi():
   ...     print("Hi!")
   ...
   >>> print_hi()
   Hi!
   >>>

It’s working. How about printing a variable in the function?

.. code:: python

   >>> def print_message():
   ...     print(message)
   ...
   >>> message = "Hello World!"
   >>> print_message()
   Hello World!
   >>>

Again, it works. How about setting a variable in the function?

.. code:: python

   >>> def get_username():
   ...     username = input("Username: ")
   ...
   >>> get_username()
   Username: me
   >>> username
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'username' is not defined
   >>>

That was weird! Why didn’t that work?

Locals and globals
^^^^^^^^^^^^^^^^^^

So far we have used nothing but **global variables**. They are called
globals because the same variables are available anywhere in our
program, even in functions.

.. code:: python

   >>> a = 1
   >>> b = "hi"
   >>> c = "hello"
   >>> def print_abc():
   ...     print(a, b, c)
   ...
   >>> print_abc()
   1 hi hello
   >>>

But there are also **local variables**. They exist only **inside**
functions, and they are deleted when the function exits.

.. code:: python

   >>> def thingy():
   ...     d = "hello again, i'm a local variable"
   ...     print('inside thingy:', d)
   ...
   >>> thingy()
   inside thingy: hello again, i'm a local variable
   >>> d
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'd' is not defined
   >>>

Let’s draw a diagram of these variables:

.. figure:: ../images/locals-and-globals.png
   :alt: Locals and globals.

   Locals and globals.

However, modifying a global variable in-place from a function is easy.

.. code:: python

   >>> stuff = ['global stuff']
   >>> def add_stuff():
   ...     stuff.append('local stuff')
   ...
   >>> add_stuff()
   >>> stuff
   ['global stuff', 'local stuff']
   >>>

This only works for changing in-place, we cannot assign a new value to
the variable.

.. code:: python

   >>> def set_stuff_to_something_new():
   ...     stuff = ['more local stuff']
   ...
   >>> set_stuff_to_something_new()
   >>> stuff
   ['global stuff', 'local stuff']
   >>>

Input
^^^^^

**Note:** This section has nothing to do with the ``input`` function
that is used like ``word = input("enter something: ")``.

So far our functions seem to be really isolated from the rest of our
code, and it sucks! But they really are not as isolated as you might
think they are.

Let’s think about what the print function does. It takes an argument and
prints it. Maybe a custom function could also take an argument?

.. code:: python

   >>> def print_twice(message):
   ...     print(message)
   ...     print(message)
   ...
   >>>

Here ``message`` is an argument. When we call the function we’ll get a
local variable called message that will point to whatever we passed to
``print_twice``.

This function can be called in two ways:

-  Using a **positional argument**.

   This is the recommended way for functions that take only one or two
   arguments. I would do this in my code.

   .. code:: python

      >>> print_twice("hi")
      hi
      hi
      >>>

   When the function was running it had a local ``message`` variable
   that pointed to ``"hi"``. The function printed it twice.

   Positional arguments are great for simple things, but if our function
   takes many positional arguments it may be hard to tell which argument
   is which.

-  Using a **keyword argument**:

   .. code:: python

      >>> print_twice(message="hi")
      hi
      hi
      >>>

   The name “keyword argument” is a little bit confusing because keyword
   arguments don’t actually have anything to do with keywords (``if``,
   ``else`` etc). Keyword arguments are just a way to give names for our
   arguments.

   Keyword arguments are great when our function needs to take many
   arguments, because each argument has a name and it’s easy to see
   which argument is which.

   Also note that there are no spaces around the ``=`` sign. This is
   just a small style detail that Python programmers like to do because
   ``message = "hi"`` and ``some_function(message="hi")`` do two
   completely different things.

Now it’s time to solve our box printing problem:

.. code:: python

   def print_box(message):
       print('*' * len(message))
       print(message)
       print('*' * len(message))

Default values
^^^^^^^^^^^^^^

What if we want to print different characters instead of always printing
stars?

We could change our ``print_box`` function to take two arguments:

.. code:: python

   def print_box(message, character):
       print(character * len(message))
       print(message)
       print(character * len(message))

Then we could change our code to always call ``print_box`` with a star
as the second argument:

.. code:: python

   print_box("Hello World", "*")
   ...

But we don’t need to change our existing code. We can make the second
argument **optional** by giving it a default value.

.. code:: python

   def print_box(message, character='*'):
       print(character * len(message))
       print(message)
       print(character * len(message))

We can print a row of stars using the function without specifying a
different character in two ways:

-  Using a positional argument.

   .. code:: python

      print_box("Hello World!")

-  Using a keyword argument.

   .. code:: python

      print_box(message="Hello World!")

Or we can give it a different character in a few different ways if we
need to:

-  Using two positional arguments.

   .. code:: python

      print_box("Enter a word:", "?")

-  Using two keyword arguments.

   .. code:: python

      print_box(message="Enter a word:", character="?")
      print_box(character="?", message="Enter a word:")

-  Using one positional argument and one keyword argument.

   I would probably do this. If an argument has a default value, I like
   to use a keyword argument to change it if needed.

   .. code:: python

      print_box("Enter a word:", character="?")

   However, this doesn’t work:

   .. code:: python

      print_box(character="?", "Enter a word:")

   The problem is that we have a keyword argument before a positional
   argument. Python doesn’t allow this. We don’t need to worry about
   this, because if we accidentally call a function like this we will
   get an error message.

Output
^^^^^^

The built-in input function `returns a
value <using-functions.md#return-values>`__. Can our function return a
value too?

.. code:: python

   >>> def times_two(thing):
   ...     return thing * 2
   ...
   >>> times_two(3)
   6
   >>> times_two(5)
   10
   >>>

Yes, it can. Now typing ``times_two(3)`` to the prompt does the same
thing as typing ``6`` to the prompt.

We can call the ``times_two`` function and use the result however we
want, just like we can use built-in functions:

.. code:: python

   >>> times_two(2) + times_two(3)     # calculate 4 + 6
   10
   >>> print('2 * 5 is', times_two(5))
   2 * 5 is 10
   >>>

Note that **returning from a function ends it immediately**.

.. code:: python

   >>> def return_before_print():
   ...     return None
   ...     print("This never gets printed.")
   ...
   >>> return_before_print()
   >>>

If we don’t have any return statements or we have a return statement
that doesn’t specify what to return, our function will return None.

.. code:: python

   >>> def return_none_1():
   ...     pass
   ...
   >>> def return_none_2():
   ...     return
   ...
   >>> print(return_none_1())
   None
   >>> print(return_none_2())
   None
   >>>

Return or print?
^^^^^^^^^^^^^^^^

There are two ways to output information from functions. They can print
something or they can return something. So, should we print or return?

Most of the time **returning makes functions much easier to use**. Think
about the ``input()`` function. It asks the user to enter something, and
then the user enters something and that value is returned. If the input
function would print the value instead of returning it, things like
``name = input("Name: ")`` wouldn’t work and assigning the result to a
variable would be much more difficult. Printing things is fine when we
know that we’ll only need to print the result and we’ll never need to
assign it to a variable.

If our function returns a value we can always print it, like this:

.. code:: python

   >>> def return_hi():
   ...     return "hi"
   ...
   >>> print(return_hi())
   hi
   >>>

Common problems
^^^^^^^^^^^^^^^

Functions are easy to understand, but you need to pay attention to how
you’re calling them. Note that ``some_function`` and ``some_function()``
do two completely different things.

.. code:: python

   >>> def say_hi():
   ...     print("howdy hi")
   ...
   >>> say_hi     # just checking what it is, doesn't run anything
   <function say_hi at 0x7f997d2a8510>
   >>> say_hi()   # this runs it
   howdy hi
   >>>

Typing ``say_hi`` just gives us the value of the ``say_hi`` variable,
which is the function we defined. But ``say_hi()`` **calls** that
function, so it runs and gives us a return value. The return value is
None so the ``>>>`` prompt `doesn’t show it <variables.md#none>`__.

But we know that the print function shows None, so what happens if we
wrap the whole thing in ``print()``?

.. code:: python

   >>> print(say_hi)       # prints the function, just like plain say_hi
   <function say_hi at 0x7fd913f58488>
   >>> print(say_hi())     # runs the function and then prints the return value
   howdy hi
   None
   >>>

The ``print(say_hi())`` thing looks a bit weird at first, but it’s easy
to understand. There’s a print inside ``say_hi`` and there’s also the
print we just wrote, so two things are printed. Python first ran
``say_hi()``, and it returned None so Python did ``print(None)``. Adding
an extra ``print()`` around a function call is actually a common
mistake, and I have helped many people with this problem.

.. _examples-3:

Examples
^^^^^^^^

Ask yes/no questions.

.. code:: python

   def ask_yes_no(prompt):
       while True:
           answer = input(prompt + ' (y or n) ')
           if answer == 'y' or answer == 'Y':
               return True    # returning ends the function
           if answer == 'n' or answer == 'N':
               return False
           print("Answer 'y' or 'n'.")

   if ask_yes_no("Do you like ice cream?"):
       print("You like ice cream!")
   else:
       print("You don't like ice cream.")

Ask questions with multiple answers.

.. code:: python

   def ask_until_correct(prompt, correct_options,
                         error_message="I don't know what you meant."):
       while True:
           answer = input(prompt + ' ')
           if answer in correct_options:
               return answer
           print(error_message)


   colors = ['red', 'yellow', 'blue', 'green', 'orange', 'pink', 'black',
             'gray', 'white', 'brown']
   choice = ask_until_correct("What's your favorite color?", colors,
                              error_message="I don't know that color.")
   print(f"Your favorite color is {choice}!")

.. _summary-11:

Summary
^^^^^^^

-  Functions are a way to write code once, and then use that same code
   in multiple places.
-  Variables inside functions are **locals**, and variables outside
   functions are **globals**. Functions can access all variables, but by
   default, they can only create and change the value of local
   variables.
-  Functions can take **arguments** and they can behave differently
   depending on what arguments they get. Arguments are just local
   variables.
-  Functions can also **return** one value, like the built-in input
   function does. Returning also ends the function immediately.
-  Return a value instead of printing it if you need to do something
   with it after calling the function.
-  Remember that ``thing``, ``thing()``, ``print(thing)`` and
   ``print(thing())`` do different things.

.. _exercises-5:

Exercises
^^^^^^^^^

**There are many things to learn about functions, and I don’t expect you
to learn everything at once.** However, there are also many free
exercises about defining functions you can do.

1. What’s wrong with this code?

   .. code:: python

      def ask_name():
          name = input("Enter your name: ")

      ask_name()
      print("Your name is", name)

2. How about this code?

   .. code:: python

      def get_greeting():
          return "Hello World!"

      print(get_greeting)

3. Why does this print None after greeting the world?

   .. code:: python

      def greet(target):
          print("Hello", target)

      print(greet("World"))

4. Find more exercises about defining functions online.

Answers for the first, second and third exercise are
`here <answers.md#defining-functions>`__.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <dicts.md>`__ \| `Next <larger-program.md>`__ \| `List of
contents <../README.md#basics>`__

Writing a larger program
------------------------

Now we know enough about Python for creating a program that is actually
useful. Awesome!

In this tutorial we’ll write a program that reads questions and answers
in a text file and asks them. For example, this file would make the
program ask what “text displaying function” and “text asking function”
are:


   text displaying function = print
   text asking function = input

**Save this example file to questions.txt**, we’ll need it later.

This might seem useless to you right now, but a program like this can
actually be really useful for learning different kinds of things. I
originally wrote a program like this to study words of a foreign
language, but then I realized that I could study pretty much anything
with it.

But there are many things the program needs to do and writing it seems
really difficult and complicated! How the heck can we do this?

Write functions
^^^^^^^^^^^^^^^

Our program will need to do several different things:

1. Read the questions from a file.
2. Ask the questions.
3. Print statistics about how many questions were answered correctly and
   how many wrong.

Now everything seems much easier. We know how to do each of these steps
one by one, but doing it all at once would be difficult. In situations
like this it’s important to `define
functions <defining-functions.md>`__. We are going to write a
``read_questions`` function, an ``ask_questions`` function and a
``stats`` function.

Let’s start with the function that reads the question file:

.. code:: python

   def read_questions(filename):
       answers = {}
       with open(filename, 'r') as f:
           for line in f:
               line = line.strip()
               if line != '':
                   question, answer = line.split('=')
                   answers[question.strip()] = answer.strip()
       return answers

At this point it’s best to try out the function to see how it works. You
need to create a ``questions.txt`` file like the one in the beginning of
this tutorial if you didn’t create it already.

**TODO:** Instructions for using the -i switch.

.. code:: python

   >>> read_questions('questions.txt')
   {'text displaying function': 'print', 'text asking function': 'input'}
   >>>

If your function doesn’t work correctly it doesn’t matter, and fixing
the problem is easy because the function is so short. This is one of the
reasons why we write functions.

Next we’ll write the rest of the functions the same way, first writing
and then testing and fixing. Here are my versions of them:

.. code:: python

   def ask_questions(answers):
       correct = []
       wrong = []

       for question, answer in answers.items():
           if input(question + ' = ').strip() == answer:
               print("Correct!")
               correct.append(question)
           else:
               print(f"Wrong! The correct answer is {answer}.")
               wrong.append(question)

       return (correct, wrong)


   def stats(correct, wrong, answers):
       print("\n**** STATS ****\n")
       print("You answered", len(correct), "questions correctly and",
             len(wrong), "questions wrong.")

       if wrong:
           print("These would have been the correct answers:")
           for question in wrong:
               print(' ', question, '=', answers[question])

Note that these functions have some empty lines in them and there are
two empty lines between the functions. This makes the code a bit longer,
but it’s a lot easier to read this way.

Let’s try out the functions.

.. code:: python

   >>> answers = read_questions('questions.txt')
   >>> correct, wrong = ask_questions(answers)
   text displaying function = print
   Correct!
   text asking function = elif
   Wrong! The correct answer is input.
   >>> correct
   ['text displaying function']
   >>> wrong
   ['text asking function']
   >>> stats(correct, wrong, answers)

   **** STATS ****

   You answered 1 questions right and 1 questions wrong.
   These would have been the correct answers:
     text asking function = input
   >>>

Everything is working! Now we just need something that runs everything
because we don’t want to type this out on the ``>>>`` prompt every time.

You might have noticed that the stats function printed ``1 questions``
instead of ``1 question``, and it looks a bit weird. You can modify the
``print_stats`` function to fix this if you want to.

The main function
^^^^^^^^^^^^^^^^^

The last function in a program like this is usually called ``main`` and
it runs the program using other functions. Our main function consists of
mostly the same pieces of code that we just tried out on the ``>>>``
prompt.

.. code:: python

   def main():
       filename = input("Name of the question file: ")
       answers = read_questions(filename)
       correct, wrong = ask_questions(answers)
       stats(correct, wrong, answers)

The last thing we need to add is these two lines:

.. code:: python

   if __name__ == '__main__':
       main()

The ``__name__`` variable is set differently depending on how we run the
file, and it’s ``'__main__'`` when we run the file directly instead of
importing. So if we run the file normally it asks us the words, and if
we import it instead we can still run the functions one by one. If you
want to know more about ``__name__`` just make a file that prints it and
run it in different ways.

Now the whole program looks like this:

.. code:: python

   def read_questions(filename):
       answers = {}
       with open(filename, 'r') as f:
           for line in f:
               line = line.strip()
               if line != '':
                   question, answer = line.split('=')
                   answers[question.strip()] = answer.strip()
       return answers


   def ask_questions(answers):
       correct = []
       wrong = []

       for question, answer in answers.items():
           if input(f'{question} = ').strip() == answer:
               print("Correct!")
               correct.append(question)
           else:
               print(f"Wrong! The correct answer is {answer}.")
               wrong.append(question)

       return (correct, wrong)


   def stats(correct, wrong, answers):
       print("\n**** STATS ****\n")
       print("You answered", len(correct), "questions correctly and",
             len(wrong), "questions wrong.")

       if wrong:
           print("These would have been the correct answers:")
           for question in wrong:
               print(' ', question, '=', answers[question])


   def main():
       filename = input("Name of the question file: ")
       answers = read_questions(filename)
       correct, wrong = ask_questions(answers)
       stats(correct, wrong, answers)

   if __name__ == '__main__':
       main()

This is just the beginning. Now `you can <../LICENSE>`__ take your word
asking program and make your own version of it that suits **your**
needs. Then you can share it with your friends so they will find it
useful as well.

.. _summary-12:

Summary
^^^^^^^

-  Make multiple functions when your program needs to do multiple
   things. Each function should do one thing.
-  Try out the functions on the ``>>>`` prompt when you want to check if
   they work correctly.
-  ``__name__`` is ``'__main__'`` when the program is supposed to run,
   and something else when it’s imported.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <defining-functions.md>`__ \| `Next <what-is-true.md>`__ \|
`List of contents <../README.md#basics>`__

What is true?
-------------

Now we understand how code like this works.

.. code:: python

   message = input("Enter something: ")
   if message == '':
       print("You didn't enter anything!")
   else:
       print("You entered:", message)

But most Python programmers would write that code like this instead:

.. code:: python

   message = input("Enter something: ")
   if message:
       print("You entered:", message)
   else:
       print("You didn't enter anything!")

What the heck was that? We did ``if message``, but ``message`` was a
string, not True or False!

Python converted our message to a Boolean and then checked if the
Boolean it ended up with was True. But when will it be true?

Converting to Booleans
^^^^^^^^^^^^^^^^^^^^^^

The ``if message:`` actually did the same thing as ``if bool(message)``,
which is same as ``if bool(message) == True:``. Usually we just don’t
write the ``==True`` part anywhere because we don’t need it.

We can convert things to Booleans like Python did by doing
``bool(things)``. Let’s try that with strings.

.. code:: python

   >>> bool('hello')
   True
   >>> bool('there')
   True
   >>> bool('True')
   True
   >>> bool('False')    # this isn't special in any way
   True
   >>>

As we can see, the Boolean value of most strings is True. The only
string that has a false Boolean value is the empty string, ``''`` or
``""``:

.. code:: python

   >>> bool('')
   False
   >>>

Most other things are also treated as False if they’re empty and True if
they’re not empty.

.. code:: python

   >>> bool([1, 2, 3])
   True
   >>> bool([])
   False
   >>> bool((1, 2, 3))
   True
   >>> bool(())
   False
   >>> bool({'a': 1, 'b': 2})
   True
   >>> bool({})
   False
   >>>

None and zero are also falsy, but positive and negative numbers are
treated as True.

.. code:: python

   >>> bool(None)
   False
   >>> bool(0)
   False
   >>> bool(0.0)
   False
   >>> bool(1)
   True
   >>> bool(-1)
   True
   >>>

Most other things are also treated as True.

.. code:: python

   >>> bool(OSError)
   True
   >>> bool(print)
   True
   >>>

When and why should we use Boolean values of things?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It’s recommended to rely on the Boolean value when we’re doing something
with things like lists and tuples. This way our code will work even if
it gets a value of a different type than we expected it to get
originally.

For example, this code doesn’t work right if we give it something else
than a list. It thinks that empty tuples, strings and dictionaries
aren’t empty just because they aren’t empty lists:

.. code:: python

   >>> def is_this_empty(thing):
   ...     if thing == []:
   ...         print("It's empty!")
   ...     else:
   ...         print("It's not empty.")
   ...
   >>> is_this_empty([1, 2, 3])
   It's not empty.
   >>> is_this_empty([])
   It's empty!
   >>> is_this_empty(())
   It's not empty.
   >>> is_this_empty('')
   It's not empty.
   >>> is_this_empty({})
   It's not empty.
   >>>

We could improve the code by checking against different empty things.

.. code:: python

   >>> def is_this_empty(thing):
   ...     if thing == [] or thing == () or thing == '' or thing == {}:
   ...         print("It's empty!")
   ...     else:
   ...         print("It's not empty.")
   ...
   >>>

But Python has many other data types that can be empty and we haven’t
talked about in this tutorial. Trying to check all of them would be
pointless because functions like this already work with all of them:

.. code:: python

   >>> def is_this_empty(thing):
   ...     if thing:
   ...         print("It's not empty.")
   ...     else:
   ...         print("It's empty!")
   ...
   >>>

There’s also cases when we should not rely on the Boolean value. When
we’re doing things with numbers and None it’s best to simply compare to
None or zero. Like this:

.. code:: python

   if number != 0:
       print("number is not zero")

   if value is not None:
       print("value is not None")

Not like this:

.. code:: python

   if number:
       print("number is not zero")

   if value:
       print("value is not None")

We used ``is not`` instead of ``!=`` in the first example because the
official style guide recommends it. The reason is that it’s possible to
create a value that isn’t really None but seems like None when we
compare it with None using ``==`` or ``!=``, and we want to make sure
that we don’t treat values like that as None.

So here’s how we should check if something is None:

.. code:: python

   if not value: ...      # not good if we want to check if it's None
   if value == None: ...  # better
   if value is None: ...  # best

.. _summary-13:

Summary
^^^^^^^

-  ``if thing:`` does the same thing as ``if bool(thing):``. This also
   works with while loops and most other things that are usually used
   with Booleans.
-  ``bool()`` of most things is True, but ``bool()`` values of None,
   zero and most empty things are False.
-  Use ``is`` and ``is not`` when comparing to None, ``==`` and ``!=``
   when checking if a number is zero and rely on the Boolean value when
   checking if something is empty.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <larger-program.md>`__ \| `Next <files.md>`__ \| `List of
contents <../README.md#basics>`__

Managing files in Python
------------------------

What are files, directories and paths?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are simple thing that many computer users already know, but I’ll
go through them just to make sure you know them also.

Files
`````

-  Each file has a **name**, like ``hello.py``, ``mytext.txt`` or
   ``coolimage.png``. Usually the name ends with an **extension** that
   describes the content, like ``py`` for Python, ``txt`` for text or
   ``png`` for “portable network graphic”.
-  With just names identifying the files, it wouldn’t be possible to
   have two files with the same name. That’s why files also have a
   **location**. We’ll talk more about this in a moment.
-  Files have **content** that consists of `8-bit
   bytes <https://www.youtube.com/watch?v=Dnd28lQHquU>`__.

Directories/folders
```````````````````

Directories are a way to group files. They also have a name and a
location like files, but instead of containing data directly like files
do they contain other files and directories.

Paths
`````

Directories and files have a path, like ``C:\Users\me\hello.py``. That
just means that there’s a folder called ``C:``, and inside it there’s a
folder called ``Users``, and inside it there’s a folder called ``me``
and inside it there’s a ``hello.py``. Like this:


   C:
   └── Users
       └── me
           └── hello.py

``C:\Users\me\hello.py`` is an **absolute path**. But there are also
**relative paths**. For example, if we are in ``C:\Users``,
``me\hello.py`` is same as ``C:\Users\me\hello.py``. The place we are in
is sometimes called **current directory**, **working directory** or
**current working directory**.

So far we’ve talked about Windows paths, but not all computers run
Windows. For example, an equivalent to ``C:\Users\me\hello.py`` is
``/home/me/hello.py`` on my Ubuntu, and if I’m in ``/home``,
``me/hello.py`` is same as ``/home/me/hello.py``.


   /
   └── home
       └── me
           └── hello.py

Writing to a file
^^^^^^^^^^^^^^^^^

Let’s create a file and write a hello world to it.

.. code:: python

   >>> with open('hello.txt', 'w') as f:
   ...     print("Hello World!", file=f)
   ...
   >>>

Doesn’t seem like it did anything. But actually it created a
``hello.txt`` somewhere on our system. On Windows it’s probably in
``C:\Users\YourName``, and on most other systems it should be in
``/home/yourname``. You can open it with notepad or any other plain text
editor your system comes with by opening the folder that contains the
file and then double-clicking the file.

So how does that code work?

First of all, we open a path with ``open``, and it gives us a Python
file object that is assigned to the variable ``f``.

.. code:: python

   >>> f
   <_io.TextIOWrapper name='hello.txt' mode='w' encoding='UTF-8'>
   >>>

File objects are not the same thing as paths and filenames, so if we try
to use ``'hello.txt'`` like we used ``f`` it doesn’t work.

The first argument we passed to ``open`` was the path we wanted to
write. Our path was more like a filename than a path, so the file ended
up in the current working directory.

The second argument was ``w``. It’s short for write, and that just means
that we’ll create a new file. There’s some other modes we can use also:

+----+-------+--------------------------------------------------------+
| Mo | Short | Meaning                                                |
| de | for   |                                                        |
+====+=======+========================================================+
| `  | read  | Read from an existing file.                            |
| `r |       |                                                        |
| `` |       |                                                        |
+----+-------+--------------------------------------------------------+
| `  | write | Write to a file. **If the file exists, its old content |
| `w |       | is removed.**                                          |
| `` |       |                                                        |
+----+-------+--------------------------------------------------------+
| `  | a     | Write to the end of a file, and keep the old content.  |
| `a | ppend |                                                        |
| `` |       |                                                        |
+----+-------+--------------------------------------------------------+

But what is that ``with ourfile as f`` crap? That’s just a fancy way to
make sure that the file gets closed, no matter what happens. As we can
see, the file was indeed closed.

.. code:: python

   >>> f.closed
   True
   >>>

When we had opened the file we could just print to it. The print is just
like any other print, but we also need to specify that we want to print
to the file we opened using ``file=f``.

Reading from files
^^^^^^^^^^^^^^^^^^

After opening a file with the ``r`` mode we can for loop over it, just
like it was a list. So let’s go ahead and read everything in the file we
created to a list of lines.

.. code:: python

   >>> lines = []
   >>> with open('hello.txt', 'r') as f:
   ...     for line in f:
   ...         lines.append(line)
   ...
   >>> lines
   ['Hello World!\n']
   >>>

Trying to open a non-existent file with ``w`` or ``a`` creates the file
for us, but doing that with ``r`` gives us an error instead. We’ll learn
more about errors `later <exceptions.md>`__.

.. code:: python

   >>> with open('this-doesnt-exist.txt', 'r') as f:
   ...     print("It's working!")
   ...
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   FileNotFoundError: [Errno 2] No such file or directory: 'this-doesnt-exist.txt'
   >>>

So now we have the hello world in the ``lines`` variable, but it’s
``['Hello World!\n']`` instead of ``['Hello World!']``. So what the heck
is that ``\n`` doing there?

``\n`` means newline. Note that it needs to be a backslash, so ``/n``
doesn’t have any special meaning like ``\n`` has. When we wrote the file
with print it actually added a ``\n`` to the end of it. It’s recommended
to end the content of files with a newline character, but it’s not
necessary.

Let’s see how that works if we have more than one line in the file.

.. code:: python

   >>> with open('hello.txt', 'w') as f:
   ...     print("Hello one!", file=f)
   ...     print("Hello two!", file=f)
   ...     print("Hello three!", file=f)
   ...
   >>> lines = []
   >>> with open('hello.txt', 'r') as f:
   ...     for line in f:
   ...         lines.append(line)
   ...
   >>> lines
   ['Hello one!\n', 'Hello two!\n', 'Hello three!\n']
   >>>

There we go, each of our lines now ends with a ``\n``. When we for loop
over the file it’s divided into lines based on where the ``\n``
characters are, not based on how we printed to it.

But how to get rid of that ``\n``? `The rstrip string
method <https://docs.python.org/3/library/stdtypes.html#str.rstrip>`__
is great for this:

.. code:: python

   >>> stripped = []
   >>> for line in lines:
   ...     stripped.append(line.rstrip('\n'))
   ...
   >>> stripped
   ['Hello one!', 'Hello two!', 'Hello three!']
   >>>

It’s also possible to read lines one by one. Files have `a readline
method <https://docs.python.org/3/library/io.html#io.TextIOBase.readline>`__
that reads the next line, and returns ``''`` if we’re at the end of the
file.

.. code:: python

   >>> with open('hello.txt', 'r') as f:
   ...     first_line = f.readline()
   ...     second_line = f.readline()
   ...
   >>> first_line
   'Hello one!\n'
   >>> second_line
   'Hello two!\n'

There’s only one confusing thing about reading files. If we try to read
the same file object twice we’ll find out that it only gets read once:

.. code:: python

   >>> first = []
   >>> second = []
   >>> with open('hello.txt', 'r') as f:
   ...     for line in f:
   ...         first.append(line)
   ...     for line in f:
   ...         second.append(line)
   ...
   >>> first
   ['Hello one!\n', 'Hello two!\n', 'Hello three!\n']
   >>> second
   []
   >>>

File objects remember their position. When we tried to read the file
again it was already at the end, and there was nothing left to read. But
if we open the file again, we get a new file object that is in the
beginning and everything works.

.. code:: python

   >>> first = []
   >>> second = []
   >>> with open('hello.txt', 'r') as f:
   ...     for line in f:
   ...         first.append(line)
   ...
   >>> with open('hello.txt', 'r') as f:
   ...     for line in f:
   ...         second.append(line)
   ...
   >>> first
   ['Hello one!\n', 'Hello two!\n', 'Hello three!\n']
   >>> second
   ['Hello one!\n', 'Hello two!\n', 'Hello three!\n']
   >>>

Usually it’s best to just read the file once, and use the content we
have read from it multiple times.

If we need all of the content as a string, we can use `the read
method <https://docs.python.org/3/library/io.html#io.TextIOBase.read>`__.

.. code:: python

   >>> with open('hello.txt', 'r') as f:
   ...     full_content = f.read()
   ...
   >>> full_content
   'Hello one!\nHello two!\nHello three!\n'
   >>>

We can also open full paths, like
``open('C:\\Users\\me\\myfile.txt', 'r')``. The reason why we need to
use ``\\`` when we really mean ``\`` is that backslash has a special
meaning. There are special characters like ``\n``, and ``\\`` means an
actual backslash.


   >>> print('C:\some\name')
   C:\some
   ame
   >>> print('C:\\some\\name')
   C:\some\name
   >>>

Another way to create paths is to tell Python to escape them by adding
an ``r`` to the beginning of the string. In this case the ``r`` is short
for “raw”, not “read”.

.. code:: python

   >>> r'C:\some\name'
   'C:\\some\\name'
   >>>

If our program is not meant to be ran on Windows and the paths don’t
contain backslashes we don’t need to double anything or use ``r`` in
front of paths.

.. code:: python

   >>> print('/some/name')
   /some/name
   >>>

Doing things like ``open('C:\\Users\\me\\myfile.txt', 'r')`` is not
recommended because the code needs to be modified if someone wants to
run the program on a different computer that doesn’t have a
``C:\Users\me`` folder. Just use ``open('myfile.txt', 'r')``.

.. _examples-4:

Examples
^^^^^^^^

This program prints the contents of files:

.. code:: python

   while True:
       filename = input("Filename or path, or nothing at all to exit: ")
       if filename == '':
           break

       with open(filename, 'r') as f:
           # We could read the whole file at once, but this is
           # faster if the file is very large.
           for line in f:
               print(line.rstrip('\n'))

This program stores the user’s username and password in a file. Plain
text files are definitely not a good way to store usernames and
passwords, but this is just an example.

.. code:: python

   # Ask repeatedly until the user answers 'y' or 'n'.
   while True:
       answer = input("Have you been here before? (y/n) ")
       if answer == 'Y' or answer == 'y':
           been_here_before = True
           break
       elif answer == 'N' or answer == 'n':
           been_here_before = False
           break
       else:
           print("Enter 'y' or 'n'.")

   if been_here_before:
       # Read username and password from a file.
       with open('userinfo.txt', 'r') as f:
           username = f.readline().rstrip('\n')
           password = f.readline().rstrip('\n')

       if input("Username: ") != username:
           print("Wrong username!")
       elif input("Password: ") != password:
           print("Wrong password!")
       else:
           print("Correct username and password, welcome!")

   else:
       # Write username and password to a file.
       username = input("Username: ")
       password = input("Password: ")
       with open('userinfo.txt', 'w') as f:
           print(username, file=f)
           print(password, file=f)

       print("Done! Now run this program again and select 'y'.")


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <what-is-true.md>`__ \| `Next <modules.md>`__ \| `List of
contents <../README.md#basics>`__

Modules
-------

Let’s say we want to generate a random number between 1 and 3. The
random module is a really easy way to do this:

.. code:: python

   >>> import random
   >>> random.randint(1, 3)
   3
   >>> random.randint(1, 3)
   1
   >>> random.randint(1, 3)
   3
   >>> random.randint(1, 3)
   2
   >>> random.randint(1, 3)
   2
   >>>

That’s cool… but how does that work?

What are modules?
^^^^^^^^^^^^^^^^^

The first line in the example, ``import random``, was an **import
statement.** But what is that random thing that it gave us?

.. code:: python

   >>> random
   <module 'random' from '/usr/lib/python3.7/random.py'>
   >>>

So it’s a module, and it comes from a path… but what does all that mean?

Now open the folder that contains your ``random.py``. On my system it’s
``/usr/lib/python3.7``, but yours will probably be different. To open a
folder in your file manager you can press Windows-R on Windows or Alt+F2
on most Linux distributions, and just type your path there. I don’t have
an up-to-date copy of OSX so unfortunately I have no idea what you need
to do on OSX.

You’ll see a bunch of files and a few directories in the folder that
opens:

.. figure:: ../images/modules.png
   :alt: My Python’s modules.

   My Python’s modules.

All of these ``.py`` files can be imported like we just imported
``random.py``. In random.py, there’s a line like
``randint = something``, so we can use its randint variable with
``random.randint`` after importing it.

You’re probably wondering how a computer can generate random numbers.
The random module does different things on different operating systems,
but on most systems it reads random noise that several programs on the
computer produce and creates random numbers based on that.

Where do modules come from?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a ``random.py`` file with the following content:

.. code:: python

   import random

   print("A random number between 1 and 3:", random.randint(1, 3))

Now run the program.

.. code:: python

   Traceback (most recent call last):
     File "random.py", line 1, in <module>
       import random
     File "/home/akuli/random.py", line 4, in <module>
       print("A random number between 1 and 3:", random.randint(1, 3))
   AttributeError: 'module' object has no attribute 'randint'

But what was that? Why didn’t it work?

**TODO:** update the ``-i`` instructions.

Let’s go ahead and check what’s wrong. If you don’t use IDLE, you’ll
need to pass the ``-i`` option to Python, so if you would normally run
``python3 random.py`` you should now do ``python3 -i random.py``. This
will run the file and then give you a ``>>>`` prompt that we can use to
check what’s wrong. If you use IDLE, just run the file normally.

We should end up with the same error message, and then a ``>>>``. Like
this:

.. code:: python

   Traceback (most recent call last):
     File "random.py", line 1, in <module>
       import random
     File "/home/akuli/random.py", line 4, in <module>
       print("A random number between 1 and 3:", random.randint(1, 3))
   AttributeError: 'module' object has no attribute 'randint'
   >>>

So first of all, what is that ``random`` variable?

.. code:: python

   >>> random
   <module 'random' from '/home/akuli/random.py'>
   >>>

What the heck? It’s a module called random… but it’s not the
``random.py`` we thought it was. **Our** ``random.py`` has imported
itself!

So let’s go ahead and rename our file from ``random.py`` to something
like ``ourrandom.py`` and try again:


   A random number between 1 and 3: 3

There we go, now we don’t have our own ``random.py`` so it works.

So seems like that modules can be imported from the directory that our
Python file is in, and also from the directory that the real
``random.py`` is in. But where else can they come from?

There’s a module called **sys** that contains various things built into
Python. Actually the whole module is built-in, so there’s no ``sys.py``
anywhere. The sys module has a list that contains all places that
modules are searched from:

.. code:: python

   >>> import sys
   >>> sys
   <module 'sys' (built-in)>
   >>> sys.path
   ['',
    '/usr/lib/python37.zip',
    '/usr/lib/python3.7',
    '/usr/lib/python3.7/lib-dynload',
    '/home/akuli/.local/lib/python3.7/site-packages',
    '/usr/local/lib/python3.7/dist-packages',
    '/usr/lib/python3/dist-packages']
   >>>

So that’s where my Python finds its modules. The first thing in my
sys.path is an empty string, and in this case it means the current
working directory.

Caching modules
^^^^^^^^^^^^^^^

Let’s create a file called ``hello.py`` that contains a classic
greeting:

.. code:: python

   print("Hello World!")

Let’s go ahead and import it, and see how it works.

.. code:: python

   >>> import hello
   Hello World!
   >>>

Works as expected, but what happens if we try to import it again?

.. code:: python

   >>> import hello
   >>>

Nothing happened at all.

The reason why the module wasn’t loaded twice is simple. In a large
project with many files it’s normal to import the same module in many
files, so it gets imported multiple times. If Python would reload the
module every time it’s imported, dividing code to multiple files would
make the code run slower.

If we need to load the module again we can just exit out of Python and
launch it again.

Brief overview of the standard library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **standard library** consists of modules that Python comes with.
Here’s a very brief overview of what it can do. All of these modules can
also do other things, and you can read more about that in the official
documentation.

Random numbers
``````````````

The official documentation is
`here <https://docs.python.org/3/library/random.html>`__.

.. code:: python

   >>> import random
   >>> random.randint(1, 3)      # 1, 2 or 3
   3
   >>> colors = ['red', 'blue', 'yellow']
   >>> random.choice(colors)     # choose one color
   'red'
   >>> random.sample(colors, 2)  # choose two different colors
   ['yellow', 'red']
   >>> random.shuffle(colors)    # mix the color list in-place
   >>> colors
   ['yellow', 'red', 'blue']
   >>>

Things that are built into Python
`````````````````````````````````

The module name “sys” is short for “system”, and it contains things that
are built into Python. The official documentation is
`here <https://docs.python.org/3/library/sys.html>`__.

``sys.stdin``, ``sys.stdout`` and ``sys.stderr`` are `file
objects <files.md>`__, just like the file objects that ``open()`` gives
us.

.. code:: python

   >>> import sys
   >>> print("Hello!", file=sys.stdout)  # this is where prints go by default
   Hello!
   >>> print("Hello!", file=sys.stderr)  # use this for error messages
   Hello!
   >>> line = sys.stdin.readline()  # i will type hello and press enter
   hello
   >>> line
   'hello\n'
   >>>
   >>> # information about Python's version, behaves like a tuple
   >>> sys.version_info
   sys.version_info(major=3, minor=7, micro=3, releaselevel='final', serial=0)
   >>> sys.version_info[:3]  # this is Python 3.7.3
   (3, 7, 3)
   >>>
   >>> sys.exit()  # exit out of Python

**TODO:** why stderr instead of stdout, when to use
``sys.stdin.readline()`` instead of ``input()``

``sys.exit()`` does the same thing as ``sys.exit(0)``. The zero means
that the program succeeded, and everything’s fine. If our program has an
error we should print an error message to ``sys.stderr`` and then call
``sys.exit(1)``. Like this:

.. code:: python

   if something_went_wrong:
       # of course, we need to make real error messages more
       # informative than this example is
       print("Oh crap! Something went wrong.", file=sys.stderr)
       sys.exit(1)

Mathematics
```````````

There’s no math.py anywhere, math is a built-in module like sys. The
official documentation is
`here <https://docs.python.org/3/library/math.html>`__.

.. code:: python

   >>> import math
   >>> math
   <module 'math' (built-in)>
   >>> math.pi                  # approximate value of π
   3.141592653589793
   >>> math.sqrt(2)             # square root of 2
   1.4142135623730951
   >>> math.radians(180)        # convert degrees to radians
   3.141592653589793
   >>> math.degrees(math.pi/2)  # convert radians to degrees
   90.0
   >>> math.sin(math.pi/2)      # sin of 90 degrees or 1/2 π radians
   1.0
   >>>

Time-related things
```````````````````

The official documentation for the time module is
`here <https://docs.python.org/3/library/time.html>`__.

.. code:: python

   >>> import time
   >>> time.sleep(1)   # wait one second
   >>> time.time()     # return time in seconds since beginning of the year 1970
   1474896325.2394648
   >>> time.strftime('%d.%m.%Y %H:%M:%S')  # format current time nicely
   '07.04.2017 19:08:33'
   >>>

You are probably wondering how ``time.time()`` can be used and why its
timing starts from the beginning of 1970. ``time.time()`` is useful for
measuring time differences because we can save its return value to a
variable before doing something, and then afterwards check how much it
changed. There’s an example that does this in `the example
section <#examples>`__.

If you want to know why it starts from 1970 you can read something like
`this <http://stackoverflow.com/questions/1090869/why-is-1-1-1970-the-epoch-time>`__.
See ``help(time.strftime)`` if you want to know about more format
specifiers like ``%d``, ``%m`` etc. that ``time.strftime`` can take.

Operating system related things
```````````````````````````````

The module name “os” is short for “operating system”, and it contains
handy functions for interacting with the operating system that Python is
running on. The official documentation is
`here <https://docs.python.org/3/library/os.html>`__.

.. code:: python

   >>> import os
   >>> os.getcwd()        # short for "get current working directory"
   '/home/akuli'
   >>> os.mkdir('stuff')  # create a folder, short for "make directory"
   >>>
   >>> os.path.isfile('hello.txt')  # check if it's a file
   True
   >>> os.path.isfile('stuff')
   False
   >>> os.path.isdir('hello.txt')   # check if it's a directory
   False
   >>> os.path.isdir('stuff')
   True
   >>> os.path.exists('hello.txt')  # check if it's anything
   True
   >>> os.path.exists('stuff')
   True
   >>>
   >>> # this joins with '\\' on windows and '/' on most other systems
   >>> path = os.path.join('stuff', 'hello-world.txt')
   >>> path
   'stuff/hello-world.txt'
   >>> with open(path, 'w') as f:
   ...     # now this goes to the stuff folder we created
   ...     print("Hello World!", file=f)
   ...
   >>> os.listdir('stuff')  # create a list of everything in stuff
   ['hello-world.txt']
   >>>

.. _examples-5:

Examples
^^^^^^^^

Mix a list of things.

.. code:: python

   import random

   print("Enter things to mix, and press Enter without typing",
         "anything when you're done.")
   things = []
   while True:
       thing = input("Next thing: ")
       if thing == "":
           break
       things.append(thing)

   random.shuffle(things)

   print("After mixing:")
   for thing in things:
       print(thing)

Measure how long it takes for the user to answer a question. The
``{:.2f}`` rounds to 2 decimals, and you can find more formatting tricks
`here <https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals>`__.

.. code:: python

   import time

   start = time.time()
   answer = input("What is 1 + 2? ")
   end = time.time()
   difference = end - start

   if answer == '3':
       print(f"Correct! That took {difference:.2f} seconds.")
   else:
       print("That's not correct...")

Wait a given number of seconds.

.. code:: python

   import sys
   import time


   answer = input("How long do you want to wait in seconds? ")
   waitingtime = float(answer)
   if waitingtime < 0:
       print("Error: cannot wait a negative time.", file=sys.stderr)
       sys.exit(1)

   print("Waiting...")
   time.sleep(waitingtime)
   print("Done!")

Check what a path points to.

.. code:: python

   import os
   import sys

   print(f"You are currently in {os.getcwd()}.")

   while True:
       path = input("A path, or nothing at all to quit: ")
       if path == '':
           # We could just break out of the loop, but I'll show how
           # this can be done with sys.exit. The difference is that
           # break only breaks the innermost loop it is in, and
           # sys.exit ends the whole program.
           sys.exit()
       if os.path.isfile(path):
           print("It's a file!")
       elif os.path.isdir(path):
           print("It's a folder!")
       elif os.path.exists(path):
           # i have no idea when this code would actually run
           print("Interesting, it exists but it's not a file or a folder.")
       else:
           print("I can't find it :(", file=sys.stderr)

More modules!
^^^^^^^^^^^^^

Python’s standard library has many awesome modules and I just can’t tell
about each and every module I use here. Here’s some of my favorite
modules from the standard library. Don’t study them one by one, but look
into them when you think you might need them. When reading the
documentation it’s usually easiest to find what you are looking for by
pressing Ctrl+F in your web browser, and then typing in what you want to
search for.

-  `argparse <https://docs.python.org/3/howto/argparse.html>`__: a
   full-featured command-line argument parser
-  `collections <https://docs.python.org/3/library/collections.html>`__,
   `functools <https://docs.python.org/3/library/functools.html>`__ and
   `itertools <https://docs.python.org/3/library/itertools.html>`__:
   handy utilities
-  `configparser <https://docs.python.org/3/library/configparser.html>`__:
   load and save setting files
-  `csv <https://docs.python.org/3/library/csv.html>`__: store
   comma-separated lines in files
-  `json <https://docs.python.org/3/library/json.html>`__: yet another
   way to store data in files and strings
-  `textwrap <https://docs.python.org/3/library/textwrap.html>`__: break
   long text into multiple lines
-  `warnings <https://pymotw.com/3/warnings/>`__: like
   `exceptions <exceptions.md>`__, but they don’t interrupt the whole
   program
-  `webbrowser <https://pymotw.com/3/webbrowser/>`__: open a web browser
   from Python

There are also lots of awesome modules that don’t come with Python. You
can search for those on the `Python package
index <https://pypi.org/>`__, or PyPI for short. It’s often better to
find a library that does something difficult than to spend a lot of time
trying to do it yourself.

I recommend reading `the official documentation about installing
modules <https://docs.python.org/3/installing/>`__ from PyPI. If you’re
using Linux, then also read the “Installing into the system Python on
Linux” section at the bottom.

.. _summary-14:

Summary
^^^^^^^

-  Most modules are files on our computers, but some of them are built
   in to Python. We can use modules in our projects by importing them,
   and after that using ``modulename.variable`` to get a variable from
   the module.
-  Some of the most commonly used modules are random, sys, math, time
   and os.
-  Avoid creating ``.py`` files that have the same name as a name of a
   module you want to use.
-  Python comes with many modules, and we can install even more modules
   if we want to.

**TODO:** exercises


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <files.md>`__ \| `Next <exceptions.md>`__ \| `List of
contents <../README.md#basics>`__

Exceptions
----------

So far we have made programs that ask the user to enter a string, and we
also know how to convert that to an integer.

.. code:: python

   text = input("Enter something: ")
   number = int(text)
   print("Your number doubled:", number*2)

That works.


   Enter a number: 3
   Your number doubled: 6

But that doesn’t work if the user does not enter a number.

.. code:: python

   Enter a number: lol
   Traceback (most recent call last):
     File "/some/place/file.py", line 2, in <module>
       number = int(text)
   ValueError: invalid literal for int() with base 10: 'lol'

So how can we fix that?

What are exceptions?
^^^^^^^^^^^^^^^^^^^^

In the previous example we got a ValueError. ValueError is an
**exception**. In other words, ValueError is an error that can occur in
our program. If an exception occurs, the program will stop and we get an
error message. The interactive prompt will display an error message and
keep going.

.. code:: python

   >>> int('lol')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: invalid literal for int() with base 10: 'lol'
   >>>

Exceptions are `classes <classes.md>`__.

.. code:: python

   >>> ValueError
   <class 'ValueError'>
   >>>

We can also create exceptions. We won’t get an error message by doing
that, but we’ll use this for displaying our own error messages later.

.. code:: python

   >>> the_problem = ValueError('oh no')
   >>> the_problem
   ValueError('oh no',)
   >>>

Catching exceptions
^^^^^^^^^^^^^^^^^^^

If we need to try to do something and see if we get an exception, we can
use ``try`` and ``except``. This is also known as **catching** the
exception.

.. code:: python

   >>> try:
   ...     print(int('lol'))
   ... except ValueError:
   ...     print("Oops!")
   ...
   Oops!
   >>>

The except part doesn’t run if the try part succeeds.

.. code:: python

   >>> try:
   ...     print("Hello World!")
   ... except ValueError:
   ...     print("What the heck? Printing failed!")
   ...
   Hello World!
   >>>

ValueError is raised when something gets an invalid value, but the
value’s type is correct. In this case, ``int`` can take a string as an
argument, but the string needs to contain a number, not ``lol``. If the
type is wrong, we will get a TypeError instead.

.. code:: python

   >>> 123 + 'hello'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: unsupported operand type(s) for +: 'int' and 'str'
   >>>

Exceptions always interrupt the code even if we catch them. Here the
print never runs because it’s after the error but inside the ``try``
block. Everything after the try block runs normally.

.. code:: python

   >>> try:
   ...     123 + 'hello'
   ...     print("This doesn't get printed.")
   ... except TypeError:
   ...     print("Oops!")
   ...
   Oops!
   >>>

Does an ``except ValueError`` also catch TypeErrors?

.. code:: python

   >>> try:
   ...     print(123 + 'hello')
   ... except ValueError:
   ...     print("Oops!")
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
   TypeError: unsupported operand type(s) for +: 'int' and 'str'
   >>>

No, it doesn’t. But maybe we could except for both ValueError and
TypeError?

.. code:: python

   >>> try:
   ...     int('lol')
   ... except ValueError:
   ...     print('wrong value')
   ... except TypeError:
   ...     print('wrong type')
   ...
   wrong value
   >>> try:
   ...     123 + 'hello'
   ... except ValueError:
   ...     print('wrong value')
   ... except TypeError:
   ...     print('wrong type')
   ...
   wrong type
   >>>

Seems to be working.

We can also also catch multiple exceptions by catching `a
tuple <lists-and-tuples.md#tuples>`__ of exceptions:

.. code:: python

   >>> try:
   ...     123 + 'hello'
   ... except (ValueError, TypeError):
   ...     print('wrong value or type')
   ...
   wrong value or type
   >>> try:
   ...     int('lol')
   ... except (ValueError, TypeError):
   ...     print('wrong value or type')
   ...
   wrong value or type
   >>>

Catching ``Exception`` will catch all errors. We’ll learn more about why
it does that in a moment.

.. code:: python

   >>> try:
   ...     123 + 'hello'
   ... except Exception:
   ...     print("Oops!")
   ...
   Oops!
   >>> try:
   ...     int('lol')
   ... except Exception:
   ...     print("Oops!")
   ...
   Oops!
   >>>

It’s also possible to catch an exception and store it in a variable.
Here we are catching an exception that Python created and storing it in
``our_error``.

.. code:: python

   >>> try:
   ...     123 + 'hello'
   ... except TypeError as e:
   ...     our_error = e
   ...
   >>> our_error
   TypeError("unsupported operand type(s) for +: 'int' and 'str'",)
   >>> type(our_error)
   <class 'TypeError'>
   >>>

When should we catch exceptions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do **not** do things like this:

.. code:: python

   try:
       # many lines of code
   except Exception:
       print("Oops! Something went wrong.")

There’s many things that can go wrong in the ``try`` block. If something
goes wrong all we have is an oops message that doesn’t tell us which
line caused the problem. This makes fixing the program really annoying.
If we want to catch exceptions we need to be specific about what exactly
we want to catch and where instead of catching everything we can in the
whole program.

There’s nothing wrong with doing things like this:

.. code:: python

   try:
       with open('some file', 'r') as f:
           content = f.read()
   except OSError:     # we can't read the file but we can work without it
       content = some_default_content

Usually catching errors that the user has caused is also a good idea:

.. code:: python

   import sys

   text = input("Enter a number: ")
   try:
       number = int(text)
   except ValueError:
       print(f"'{text}' is not a number.", file=sys.stderr)
       sys.exit(1)
   print(f"Your number doubled is {(number * 2)}.")

Raising exceptions
^^^^^^^^^^^^^^^^^^

Now we know how to create exceptions and how to handle errors that
Python creates. But we can also create error messages manually. This is
known as **raising an exception** and **throwing an exception**.

Raising an exception is easy. All we need to do is to type ``raise`` and
then an exception we want to raise:

.. code:: python

   >>> raise ValueError("lol is not a number")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: lol is not a number
   >>>

Of course, we can also raise an exception from a variable.

.. code:: python

   >>> oops = ValueError("lol is not a number")
   >>> raise oops
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: lol is not a number
   >>>

If we `define a function <defining-functions.md>`__ that raises an
exception and call it we’ll notice that the error message also says
which functions we ran to get to that error.

.. code:: python

   >>> def oops():
   ...     raise ValueError("oh no!")
   ...
   >>> def do_the_oops():
   ...     oops()
   ...
   >>> do_the_oops()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 2, in do_the_oops
     File "<stdin>", line 2, in oops
   ValueError: oh no!
   >>>

If our code was in a file we would also see the line of code that raised
the error.

When should we raise exceptions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Back in `the module chapter <modules.md>`__ we learned to display error
messages by printing to ``sys.stderr`` and then calling ``sys.exit(1)``,
so when should we use that and when should we raise an exception?

Exceptions are meant for **programmers**, so if we are writing something
that other people will import we should use exceptions. If our program
is working like it should be and the **user** has done something wrong,
it’s usually better to use ``sys.stderr`` and ``sys.exit``.

Exception hierarchy
^^^^^^^^^^^^^^^^^^^

Exceptions are organized like this. I made this tree with `this
program <https://github.com/Akuli/classtree/>`__ on Python 3.7. You may
have more or less exceptions than I have if your Python is newer or
older than mine, but they should be mostly similar.


   Exception
   ├── ArithmeticError
   │   ├── FloatingPointError
   │   ├── OverflowError
   │   └── ZeroDivisionError
   ├── AssertionError
   ├── AttributeError
   ├── BufferError
   ├── EOFError
   ├── ImportError
   │   └── ModuleNotFoundError
   ├── LookupError
   │   ├── IndexError
   │   └── KeyError
   ├── MemoryError
   ├── NameError
   │   └── UnboundLocalError
   ├── OSError
   │   ├── BlockingIOError
   │   ├── ChildProcessError
   │   ├── ConnectionError
   │   │   ├── BrokenPipeError
   │   │   ├── ConnectionAbortedError
   │   │   ├── ConnectionRefusedError
   │   │   └── ConnectionResetError
   │   ├── FileExistsError
   │   ├── FileNotFoundError
   │   ├── InterruptedError
   │   ├── IsADirectoryError
   │   ├── NotADirectoryError
   │   ├── PermissionError
   │   ├── ProcessLookupError
   │   └── TimeoutError
   ├── ReferenceError
   ├── RuntimeError
   │   ├── NotImplementedError
   │   └── RecursionError
   ├── StopAsyncIteration
   ├── StopIteration
   ├── SyntaxError
   │   └── IndentationError
   │       └── TabError
   ├── SystemError
   ├── TypeError
   ├── ValueError
   │   └── UnicodeError
   │       ├── UnicodeDecodeError
   │       ├── UnicodeEncodeError
   │       └── UnicodeTranslateError
   └── Warning
       ├── BytesWarning
       ├── DeprecationWarning
       ├── FutureWarning
       ├── ImportWarning
       ├── PendingDeprecationWarning
       ├── ResourceWarning
       ├── RuntimeWarning
       ├── SyntaxWarning
       ├── UnicodeWarning
       └── UserWarning

Catching an exception also catches everything that’s under it in this
tree. For example, catching ``OSError`` catches errors that we typically
get when `processing files <files.md>`__, and catching Exception catches
all of these errors. You don’t need to remember this tree, running
``help('builtins')`` should display a larger tree that this is a part
of.

There are also a few exceptions that are not in this tree like
SystemExit and KeyboardInterrupt, but most of the time we shouldn’t
catch them. Catching Exception doesn’t catch them either.

.. _summary-15:

Summary
^^^^^^^

-  Exceptions are classes and they can be used just like all other
   classes.
-  ValueError and TypeError are some of the most commonly used
   exceptions.
-  The ``try`` and ``except`` keywords can be used for attempting to do
   something and then doing something else if we get an error. This is
   known as catching exceptions.
-  It’s possible to raise exceptions with the ``raise`` keyword. This is
   also known as throwing exceptions.
-  Raise exceptions if they are meant to be displayed for programmers
   and use ``sys.stderr`` and ``sys.exit`` otherwise.

.. _examples-6:

Examples
^^^^^^^^

Keep asking a number from the user until it’s entered correctly.

.. code:: python

   while True:
       try:
           number = int(input("Enter a number: "))
           break
       except ValueError:
           print("That's not a valid number! Try again.")

   print("Your number doubled is:", number * 2)

This program allows the user to customize the message it prints by
modifying a file the greeting is stored in, and it can create the file
for the user if it doesn’t exist already. This example also uses things
from `the file chapter <files.md>`__, `the function defining
chapter <defining-functions.md>`__ and `the module
chapter <modules.md>`__.

.. code:: python

   # These are here so you can change them to customize the program
   # easily.
   default_greeting = "Hello World!"
   filename = "greeting.txt"


   import sys

   def askyesno(question):
       while True:
           answer = input(question + ' (y or n) ')
           if answer == 'Y' or answer == 'y':
               return True
           if answer == 'N' or answer == 'n':
               return False

   def greet():
       with open(filename, 'r') as f:
           for line in f:
               print(line.rstrip('\n'))

   try:
       greet()
   except OSError:
       print(f"Cannot read '{filename}'!", file=sys.stderr)
       if askyesno("Would you like to create a default greeting file?"):
           with open(filename, 'w') as f:
               print(default_greeting, file=f)
           greet()


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <modules.md>`__ \| `Next <classes.md>`__ \| `List of
contents <../README.md#basics>`__

Defining and using custom classes
---------------------------------

When I was getting started in Python I learned to make classes for
tkinter GUI’s before I understood how they work. Everything I did with
classes worked, but I didn’t understand how. Hopefully you’ll first
learn to understand classes, and then learn to use them.

What are classes?
^^^^^^^^^^^^^^^^^

Python comes with many classes that we know already.

.. code:: python

   >>> str
   <class 'str'>
   >>> int
   <class 'int'>
   >>> list
   <class 'list'>
   >>> dict
   <class 'dict'>
   >>>

Calling these classes as if they were functions makes a new **instance**
of them. For example, ``str()`` makes a ``str`` instance, also known as
a string.

.. code:: python

   >>> str()
   ''
   >>> int()
   0
   >>> list()
   []
   >>> dict()
   {}
   >>>

We can also get an instance’s class with ``type()``:

.. code:: python

   >>> type('')
   <class 'str'>
   >>> type(0)
   <class 'int'>
   >>> type([])
   <class 'list'>
   >>> type({})
   <class 'dict'>
   >>>

Let’s say that we make a program that processes data about websites.
With a custom class, we’re not limited to ``str``, ``int`` and other
classes Python comes with. Instead we can define a Website class, and
make Websites and process information about websites directly. Defining
our own types like this is called **object-orientated programming**.

First class
^^^^^^^^^^^

In Python, ``pass`` does nothing.

.. code:: python

   >>> pass
   >>>

Let’s use it to define an empty class.

.. code:: python

   >>> class Website:
   ...     pass
   ...
   >>> Website
   <class '__main__.Website'>
   >>>

The ``pass`` is needed here, just like `when defining functions that do
nothing <defining-functions.md#first-functions>`__.

Note that I named the class ``Website``, not ``website``. This way we
know that it’s a class. Built-in classes use lowercase names (like
``str`` instead of ``Str``) because they are faster to type, but use
CapsWord names for your classes.

Now we can make a Website instance by calling the class.

.. code:: python

   >>> github = Website()
   >>> github
   <__main__.Website object at 0x7f36e4c456d8>
   >>> type(github)
   <class '__main__.Website'>
   >>>

We can say that ``github`` is “a Website instance”, “a Website object”
or “a Website”. All of these mean the same thing.

Now we can attach more information about github to our Website.

.. code:: python

   >>> github.url = 'https://github.com/'
   >>> github.founding_year = 2008
   >>> github.free_to_use = True
   >>>

We can also access the information easily.

.. code:: python

   >>> github.url
   'https://github.com/'
   >>> github.founding_year
   2008
   >>> github.free_to_use
   True
   >>>

As you can see, our Website is mutable, like lists are, not immutable
like strings are. We can change the website in-place without creating a
new Website.

``url``, ``founding_year`` and ``free_to_use`` are not variables, they
are **attributes**. More specifically, they are **instance attributes**.
The biggest difference is that we need to use a dot for setting and
getting values of attributes, but we don’t need that with variables.

Modules also use instance attributes for accessing their content. For
example, when we do ``random.randint``, ``random`` is a module instance
and ``randint`` is one of its attributes.

If we make another Website, does it have the same ``url``,
``founding_year`` and ``free_to_use``?

.. code:: python

   >>> effbot = Website()
   >>> effbot.url
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: 'Website' object has no attribute 'url'
   >>>

It doesn’t. We’d need to define the attributes for effbot also.

The attributes are stored in a dictionary called ``__dict__``. It’s not
recommended to use it for code that needs to be reliable, but it’s a
handy way to see which attributes the instance contains.

.. code:: python

   >>> github.__dict__
   {'free_to_use': True,
    'founding_year': 2008,
    'url': 'https://github.com/'}
   >>> effbot.__dict__
   {}
   >>>

Class attributes
^^^^^^^^^^^^^^^^

What happens if we set an attribute of the ``Website`` class to some
value instead of doing that to an instance?

.. code:: python

   >>> Website.is_online = True
   >>> Website.is_online
   True
   >>>

Seems to be working, but what happened to the instances?

.. code:: python

   >>> github.is_online
   True
   >>> effbot.is_online
   True
   >>>

What was that? Setting ``Website.is_online`` to a value also set
``github.is_online`` and ``effbot.is_online`` to that value!

Actually, ``is_online`` is still not in github’s or effbot’s
``__dict__``. github and effbot get that attribute directly from the
``Website`` class.

.. code:: python

   >>> github.__dict__
   {'free_to_use': True,
    'founding_year': 2008,
    'url': 'https://github.com/'}
   >>> effbot.__dict__
   {}
   >>>

``Website.is_online`` is ``Website``\ ’s class attribute, and in Python
you can access class attributes through instances also, so in this case
``github.is_online`` points to ``Website.is_online``. That can be
confusing, which is why it’s not recommended to use class attributes
like this. Use instance attributes instead,
e.g. ``github.is_online = True``.

Functions and methods
^^^^^^^^^^^^^^^^^^^^^

Let’s `define a function <defining-functions.md>`__ that prints
information about a website.

.. code:: python

   >>> def website_info(website):
   ...     print("URL:", website.url)
   ...     print("Founding year:", website.founding_year)
   ...     print("Free to use:", website.free_to_use)
   ...
   >>> website_info(github)
   URL: https://github.com/
   Founding year: 2008
   Free to use: True
   >>>

Seems to be working. We should be able to get information about all
websites, so maybe we should attach the ``website_info`` function to the
Website class?

.. code:: python

   >>> Website.info = website_info
   >>> Website.info(github)
   URL: https://github.com/
   Founding year: 2008
   Free to use: True
   >>>

It’s working, but ``Website.info(github)`` is a lot of typing, so
wouldn’t ``github.info()`` be much better?

.. code:: python

   >>> github.info()
   URL: https://github.com/
   Founding year: 2008
   Free to use: True
   >>>

What the heck happened? We didn’t define a ``github.info``, it just
magically worked!

``Website.info`` is our ``website_info`` function, so ``github.info``
should also be the same function. But ``Website.info`` takes a
``website`` argument, which we didn’t give it when we called
``github.info()``!

But is ``github.info`` the same thing as ``Website.info``?

.. code:: python

   >>> Website.info
   <function website_info at 0x7f36e4c39598>
   >>> github.info
   <bound method website_info of <__main__.Website object at 0x7f36e4c456d8>>
   >>>

It’s not.

Instead, ``github.info`` is a **method**. If we set a function as a
class attribute, the instances will have a method with the same name.
Methods are “links” to the class attribute functions. So
``Website.info(github)`` does the same thing as ``github.info()``, and
when ``github.info()`` is called it automatically gets ``github`` as an
argument.

In other words, **``Class.method(instance)`` does the same thing as
``instance.method()``**. This also works with built-in classes, for
example ``'hello'.lower()`` is same as ``str.lower('hello')``.

Defining methods when defining the class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Maybe we could define a method when we make the class instead of adding
it later?

.. code:: python

   >>> class Website:
   ...     def info(self):     # self will be github
   ...         print("URL:", self.url)
   ...         print("Founding year:", self.founding_year)
   ...         print("Free to use:", self.free_to_use)
   ...
   >>> github = Website()
   >>> github.url = 'https://github.com/'
   >>> github.founding_year = 2008
   >>> github.free_to_use = True
   >>> github.info()
   URL: https://github.com/
   Founding year: 2008
   Free to use: True
   >>>

It’s working. The ``self`` argument in ``Website.info`` was ``github``.
You could call it something else too such as ``me``, ``this`` or
``instance``, but use ``self`` instead. Other Python users have gotten
used to it, and the official style guide recommends it also.

We still need to set ``url``, ``founding_year`` and ``free_to_use``
manually. Maybe we could add a method to do that?

.. code:: python

   >>> class Website:
   ...     def initialize(self, url, founding_year, free_to_use):
   ...         self.url = url
   ...         self.founding_year = founding_year
   ...         self.free_to_use = free_to_use
   ...     def info(self):
   ...         print("URL:", self.url)
   ...         print("Founding year:", self.founding_year)
   ...         print("Free to use:", self.free_to_use)
   ...
   >>> github = Website()
   >>> github.initialize('https://github.com/', 2008, True)
   >>> github.info()
   URL: https://github.com/
   Founding year: 2008
   Free to use: True
   >>>

That works. The attributes we defined in the initialize method are also
available in the info method. We could also access them directly from
``github``, for example with ``github.url``.

But we still need to call ``github.initialize``. In Python, there’s a
“magic” method that runs when we create a new Website by calling the
Website class. It’s called ``__init__`` and it does nothing by default.
If our ``__init__`` method takes other arguments than self we can call
the class with arguments and they will be given to ``__init__``. Like
this:

.. code:: python

   >>> class Website:
   ...     def __init__(self, url, founding_year, free_to_use):
   ...         self.url = url
   ...         self.founding_year = founding_year
   ...         self.free_to_use = free_to_use
   ...     def info(self):
   ...         print("URL:", self.url)
   ...         print("Founding year:", self.founding_year)
   ...         print("Free to use:", self.free_to_use)
   ...
   >>> github = Website('https://github.com/', 2008, True)
   >>> github.info()
   URL: https://github.com/
   Founding year: 2008
   Free to use: True
   >>>

Classes have many other magic methods too, but I’m not going to cover
them in this tutorial.

When should I use classes?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Don’t do this:

.. code:: python

   class MyProgram:

       def __init__(self):
           print("Hello!")
           word = input("Enter something: ")
           print("You entered " + word + ".")


   program = MyProgram()

You should avoid using things like ``print`` and ``input`` in the
``__init__`` method. The ``__init__`` method should be simple and it
should just set things up.

Usually you shouldn’t use a class if you’re only going to make one
instance of it, and you don’t need a class either if you’re only going
to have one method. In this example ``MyProgram`` has only one method
and only one instance.

Make functions instead, or just write your code without any functions if
it’s short enough for that. This program does the same thing and it’s
much more readable:

.. code:: python

   print("Hello!")
   word = input("Enter something: ")
   print("You entered " + word + ".")

.. _summary-16:

Summary
^^^^^^^

-  Object-orientated programming is programming with custom data types.
   In Python that means using classes and instances.
-  Use CapsWords for class names and lowercase_words_with_underscores
   for other names. This makes it easy to see which objects are classes
   and which objects are instances.
-  Calling a class as if it was a function makes a new instance of it.
-  ``foo.bar = baz`` sets ``foo``\ ’s attribute ``bar`` to ``baz``.
-  Use class attributes for functions and instance attributes for other
   things.
-  Functions as class attributes can be accessed as instance methods.
   They get their instance as the first argument. Call that ``self``
   when you define the method.
-  ``__init__`` is a special method, and it’s ran when a new instance of
   a class is created. It does nothing by default.
-  Don’t use classes if your code is easier to read without them.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <exceptions.md>`__ \| `Next <docstrings.md>`__ \| `List of
contents <../README.md#basics>`__

Help and Docstrings
-------------------

In this tutorial we have used ``help()`` a few times. It’s great and you
can use it as much as you want to. For example, running ``help(str)``
displays a nice list of all string methods and explanations of what they
do, and ``help(list.extend)`` explains what extending something to a
list does.

You can get help of many other things too. For example:

.. code:: python

   >>> stuff = []
   >>> help(stuff.append)
   Help on built-in function append:

   append(object, /) method of builtins.list instance
       Append object to the end of the list.

   >>> help(print)
   Help on built-in function print in module builtins:

   print(...)
       print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

       Prints the values to a stream, or to sys.stdout by default.
       Optional keyword arguments:
       ...

Docstrings
^^^^^^^^^^

Let’s see what happens if we `define a
function <defining-functions.md>`__ and call ``help()`` on that.

.. code:: python

   >>> def thing(stuff):
   ...     return stuff * 2
   ...
   >>> help(thing)
   Help on function thing in module __main__:

   thing(stuff)
   >>>

That sucked! We have no idea about what it does based on this. All we
know is that it takes a ``stuff`` argument.

This is when documentation strings or docstrings come in. All we need to
do is to add a string to the beginning of our function and it will show
up in ``help(the_function)``. Like this:

.. code:: python

   >>> def thing(stuff):
   ...     "hello there"
   ...     return stuff * 2
   ...
   >>> help(thing)
   Help on function thing in module __main__:

   thing(stuff)
       hello there

Note that docstrings are not comments. If you add a ``# comment`` to the
beginning of the function it won’t show up in ``help()``.

Multi-line strings
^^^^^^^^^^^^^^^^^^

When we did ``help(print)``, we got more than one line of help. Maybe we
could do that in our own docstring too?

.. code:: python

   >>> def thing():
   ...     "This thing does stuff.\n\nIt always returns None."
   ...
   >>> help(thing)
   Help on function thing in module __main__:

   thing()
       This thing does stuff.

       It always returns None.
   >>>

That’s better, but how what if we want to do 5 lines of prints? Our
``"stuff\n\nstuff\nstuff"`` thing would be really long and hard to work
with. But Python has multi-line strings too. They work like this:

.. code:: python

   >>> """bla bla bla
   ...
   ... bla bla
   ... bla bla bla"""
   'bla bla bla\n\nbla bla\nbla bla bla'
   >>>

So we can write documented functions like this:

.. code:: python

   >>> def thing():
   ...     """This thing does stuff.
   ...
   ...     It always returns None.
   ...     """
   ...
   >>> help(thing)
   Help on function thing in module __main__:

   thing()
       This thing does stuff.

       It always returns None.

   >>>

It’s recommended to always use ``"""strings like this"""`` for
docstrings, even if the docstring is only one line long. This way it’s
easy to add more stuff to it later.

Documenting other stuff
^^^^^^^^^^^^^^^^^^^^^^^

Docstrings aren’t actually limited to functions. You can use them for
documenting `classes <classes.md>`__ and their methods too. For example,
let’s make a file like this and save it to ``test.py``:

.. code:: python

   """A test module.

   It contains a class and a function.
   """


   class Thing:
       """This is a test class."""

       def thingy(self):
           """This is a test method."""
           print("hello")


   def do_hello():
       """This is a test function."""
       thing = Thing()
       thing.thingy()

Then we can import it and call help on it:


   >>> import test
   >>> help(test)
   Help on module testie:

   NAME
       testie - A test module.

   DESCRIPTION
       It contains a class and a function.

   CLASSES
       builtins.object
           Thing

       class Thing(builtins.object)
        |  This is a test class.
        |
        |  Methods defined here:
        |
        |  thingy(self)
        |      This is a test method.
        |
        |  ----------------------------------------------------------------------
        |  Data descriptors defined here:
        |
        |  __dict__
        |      dictionary for instance variables (if defined)
        |
        |  __weakref__
        |      list of weak references to the object (if defined)

   FUNCTIONS
       do_hello()
           This is a test function.

   FILE
       /home/akuli/testie.py

That’s pretty cool. We just added docstrings to our code and Python made
this thing out of it.

You might be wondering what ``__weakref__`` is. You don’t need to care
about it, and I think it would be better if ``help()`` would hide it.

Popular Docstring Formats
^^^^^^^^^^^^^^^^^^^^^^^^^

There are different styles for writing docstrings. If you are
contributing to another Python project, make sure to use the same style
as rest of that project is using.

If you are starting a new project, then you can use whichever style you
want, but don’t “reinvent the wheel”; use an existing style instead
instead of making up your own. Here are some examples of popular
docstring styles to choose from:

Sphinx Style
````````````

`Sphinx <https://www.sphinx-doc.org/en/master/>`__ is the Python
documentation tool that `the official Python
documentation <https://docs.python.org/3/>`__ uses. By default, sphinx
expects you to write docstrings like this:

.. code:: python

   class Vehicles:
       """
       The Vehicles object contains lots of vehicles.
       :param arg: The arg is used for ...
       :type arg: str
       :ivar arg: This is where we store arg
       :vartype arg: str
       """

       def __init__(self, arg):
           self.arg = arg

       def cars(self, distance, destination):
           """We can't travel a certain distance in vehicles without fuels, so here's the fuels

           :param distance: The amount of distance traveled
           :type amount: int
           :param bool destinationReached: Should the fuels be refilled to cover required distance?
           :raises: :class:`RuntimeError`: Out of fuel

           :returns: A Car mileage
           :rtype: Cars
           """  
           ...

Google Style
````````````

Google Style is meant to be easier to read and use without a tool like
sphinx. Sphinx can be configured to use that with
`sphinx.ext.napoleon <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`__.

.. code:: python

   class Vehicles:
       """
       The Vehicles object contains lots of vehicles.

       Args:
           arg (str): The arg is used for...

       Attributes:
           arg (str): This is where we store arg.
       """

       def __init__(self, arg):
           self.arg = arg

       def cars(self, distance, destination):
           """We can't travel distance in vehicles without fuels, so here is the fuels

           Args:
               distance (int): The amount of distance traveled
               destination (bool): Should the fuels refilled to cover the distance?

           Raises:
               RuntimeError: Out of fuel

           Returns:
               cars: A car mileage
           """
           ...

Numpy Style
```````````

`Numpy <https://numpy.org/>`__ is a large and popular Python library,
and numpy developers have their own docstring style.

.. code:: python

   class Vehicles:
       """
       The Vehicles object contains lots of vehicles.

       Parameters
       ----------
       arg : str
           The arg is used for ...
       *args
           The variable arguments are used for ...
       **kwargs
           The keyword arguments are used for ...

       Attributes
       ----------
       arg : str
           This is where we store arg.
       """

       def __init__(self, arg):
           self.arg = arg

       def cars(self, distance, destination):
           """We can't travel distance in vehicles without fuels, so here is the fuels

           Parameters
           ----------
           distance : int
               The amount of distance traveled
           destination : bool
               Should the fuels refilled to cover the distance?

           Raises
           ------
           RuntimeError
               Out of fuel

           Returns
           -------
           cars
               A car mileage
           """
           pass

When should we use docstrings?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I recommend using docstrings when writing code that other people will
import. The ``help()`` function is awesome, so it’s good to make sure
it’s actually helpful.

If your code is not meant to be imported, docstrings are usually a good
idea anyway. Other people reading your code will understand what it’s
doing without having to read through all of the code.

.. _summary-17:

Summary
^^^^^^^

-  ``help()`` is awesome.
-  A ``"""triple-quoted string"""`` string in the beginning of a
   function, class or file is a docstring. It shows up in ``help()``.
-  Docstrings are not comments.
-  Usually it’s a good idea to add docstrings everywhere.


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`Previous <classes.md>`__ \| `Next <../advanced/datatypes.md>`__ \|
`List of contents <../README.md#basics>`__

Answers
-------

These are my answers for exercises in the chapters. If your solution
isn’t exactly like mine but it works just fine it’s ok, and you can `ask
me <../contact-me.md>`__ why I didn’t do it like you did it.

.. _thinkpython-the-way-of-the-program-1:

ThinkPython: The way of the program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. With +, the strings get added together, and with \* we get an error.
2. With + we get an error, and with \* the string is repeated multiple
   times.
3. Python calculates the result and echoes it.

.. _if-else-and-elif-1:

If, else and elif
^^^^^^^^^^^^^^^^^

1. Problems and solutions:

   -  The first line should be ``print("Hello!")`` or
      ``print('Hello!')``, not ``print(Hello!)``. ``Hello!`` is a piece
      of text, so we need to tell Python that it’s a string by putting
      quotes around it.
   -  The second line will create an error message that says that
      there’s no variable called ``something``. But we are trying to
      create it here, so we need ``=`` instead of ``==``. ``=`` is
      assigning, ``==`` is comparing.
   -  The last line should have a comma between the arguments, like
      ``print('You entered:', something)``.

2. The broken code has mostly the same issues as exercise 1. Here are
   the problems that exercise 1 doesn’t have:

   -  The if-elif-else has a blank line at a confusing place. Delete it.
   -  After deleting the code, it looks quite dense. Add a new blank
      line before the ``if``.
   -  The elif line is missing a ``:`` at the end.
   -  On the last line the comma is on the wrong side. ``"bla bla,"`` is
      a string that **contains** a comma, but ``"bla bla",`` is a string
      and a **separate** comma. In this exercise, the last line should
      be ``print("I don't know what", something, "means.")``

3. We can simply ask the word with input and print ``word * 1000``.

   .. code:: python

      word = input("Enter a word: ")
      print(word * 1000)

4. We can add a space to the word before we print it.

   .. code:: python

      word = input("Enter a word: ")
      word += " "
      print(word * 1000)

   We can also add the space right away on the first line:

   .. code:: python

      word = input("Enter a word: ") + " "
      print(word * 1000)

   Of course, there are 999 spaces between 1000 words and this will
   print 1000 spaces instead, so there will be a useless space at the
   end, but it doesn’t matter. If we really want to get rid of the
   space, we can do something like this instead:

   .. code:: python

      no_space = input("Enter a word: ")
      yes_space = no_space + " "
      print(yes_space*999 + no_space)

5. Like this:

   .. code:: python

      first = input("Enter a word: ")
      second = input("Enter another word: ")
      words = first + " " + second + " "
      print(words * 1000)

6. We can compare the word against an empty string (``""`` or ``''``) to
   check if it’s empty. In this example, the password is “seKr3t”.

   .. code:: python

      word = input("Enter your password: ")

      if word == "seKr3t":
          print("Welcome!")
      elif word == "":
          print("You didn't enter anything.")
      else:
          print("Access denied.")

   Again, this is not a good way to ask a real password from the user.

.. _handy-stuff-strings-1:

Handy stuff: Strings
^^^^^^^^^^^^^^^^^^^^

1. The program is not like you might expect it to be. It actually works
   just fine if we run it, but there’s a problem. The last line is
   really long and it’s hard to see what it does.

   The solution is string formatting. I recommend replacing the last
   line with this:

   .. code:: python

      print(f"You entered {word1}, {word2}, {word3} and {word4}.")

2. If we have a look at ``help(str.upper)`` it looks like this:

   ::

       S.upper() -> str

       Return a copy of S converted to uppercase.

   We have two problems. First of all, the broken code uses
   ``message.upper`` instead of ``message.upper()``. It also expects the
   message to magically make itself uppercased, but strings can’t be
   changed in-place so it doesn’t work.

   The solution is to do ``message.upper()`` and save the value we got
   from that to a variable:

   .. code:: python

      message = input("What do you want me to say? ")
      uppermessage = message.upper()
      print(uppermessage, "!!!")
      print(uppermessage, "!!!")
      print(uppermessage, "!!!")

   Or we can reuse the same variable name:

   .. code:: python

      message = input("What do you want me to say? ")
      message = message.upper()
      print(message, "!!!")
      print(message, "!!!")
      print(message, "!!!")

   Or we can convert the message to uppercase right away on the first
   line:

   .. code:: python

      message = input("What do you want me to say? ").upper()
      print(message, "!!!")
      print(message, "!!!")
      print(message, "!!!")

3. In the code below, ``palindrome_input[::-1]`` is the string
   ``palindrome_input`` reversed. For example, if ``palindrome_input``
   is ``"hello"``, then ``palindrome_input[::-1]`` is ``"olleh"``.

   .. code:: python

      palindrome_input = input("Enter a string: ")
      if palindrome_input == palindrome_input[::-1]:
          print("This string is a palindrome")
      else:
          print("This string is not a palindrome")

   .. rubric:: Lists and tuples
      :name: lists-and-tuples-1

4. Look carefully. The ``namelist`` is written in ``()`` instead of
   ``[]``, so it’s actually a tuple, not a list. Using confusing
   variable names is of course a bad idea, but you shouldn’t be
   surprised if someone is doing that. Replace the ``()`` with ``[]``
   and the code will work.

5. When we run the program we get a weird error:

   ::

       Hello!
       Enter your name: my name
       Traceback (most recent call last):
         File "program.py", line 3, in <module>
           print("Your name is " + name + ".")
       TypeError: Can't convert 'tuple' object to str implicitly

   So Python is trying to convert a tuple to a string. But
   ``"Your name is "`` and ``"."`` are strings, so maybe ``name`` is a
   tuple? Let’s change the last line to just ``print(name)`` so our
   program looks like this:

   .. code:: python

      print("Hello!")
      name = input("Enter your name: "),
      print(name)

   Let’s run it.

   ::

       Hello!
       Enter your name: my name
       ('my name',)

   ``name`` is indeed a tuple! The problem is the second line. Look
   carefully, there’s a comma after ``input("Enter your name: ")``.
   Python created a tuple automatically, but that’s not what we wanted.
   If we remove the comma, everything works just fine.

6. Again, the code gives us a weird error message.

   ::

       Enter your name: my name
       Traceback (most recent call last):
         File "program.py", line 3, in <module>
           if input("Enter your name: ") in namelist:
       TypeError: argument of type 'NoneType' is not iterable

   Now we need to remember that when the error messages talk about
   ``NoneType`` `they always mean None <variables.md#none>`__. So
   ``namelist`` seems to be None. Let’s make the program a bit simpler
   for working on the namelist:

   .. code:: python

      namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
      namelist = namelist.extend('theelous3')
      print(namelist)

   Now fixing the namelist is easier, so I’ll just go through the
   problems and solutions:

   -  ``namelist`` is None. It should be
      ``namelist.extend('theelous3')``, not
      ``namelist = namelist.extend('theelous3')``. See `this
      thing <using-functions.md#return-values>`__.
   -  Now the namelist is like
      ``['wub_wub', ..., 't', 'h', 'e', 'e', ...]``. Python treated
      ``'theelous3'`` like a list so it added each of its characters to
      ``namelist``. We can use ``namelist.append('theelous3')`` or
      ``namelist.extend(['theelous3'])`` instead to solve this problem.

.. _loops-1:

Loops
^^^^^

1. The problem is that ``things`` is a string because we converted it to
   a string with ``str``, so the for loop loops over the characters
   ``[``, ``1``, ``,`` and so on. Replace ``str([1, 2, 3, 4, 5])`` with
   ``[1, 2, 3, 4, 5]``.

2. The code appends each list in ``before`` to ``after``, so the
   ``number`` variable actually pointed to a list like ``[1, 2]``. An
   easy solution is to just write two for loops inside each other:

   .. code:: python

      before = [[1, 2], [3, 4], [5, 6]]
      after = []
      for sublist in before:
          for number in sublist:
              after.append(number)
      print(after)

   Lists also have an extend method that appends each item from another
   list, so we can also use that:

   .. code:: python

      before = [[1, 2], [3, 4], [5, 6]]
      after = []
      for sublist in before:
          after.extend(sublist)
      print(after)

3. The code has some empty lines in it, and they divide it nicely into
   three parts. All of these parts have some problems, so I’ll go
   through them one by one.

   The first part makes a variable called ``input``. The problem is that
   now the rest of the program `can’t use the input
   function <using-functions.md#variables-names-and-builtin-things>`__.
   It doesn’t really matter here because the rest of the program doesn’t
   use it anyway, but I still recommend using some other variable name,
   like ``inputlist``.

   The second part runs ``numbers = []`` three times. It was probably
   meant to be ran once before the loop started, like this:

   .. code:: python

      numbers = []
      for string in inputlist:
          numbers.append(int(string))

   The third part calculates ``result + n`` but throws away the value.
   It was probably supposed to do ``result += n`` instead.

4. If you run this program you’ll notice that nothing happened to the
   numbers list. The reason is that the ``number`` variable only works
   one way. It gets its values from the ``numbers`` list, but changing
   it doesn’t change the ``numbers`` list. In general, ``thing = stuff``
   changes the ``thing`` variable, and that’s it. It doesn’t change
   anything else.

   An easy solution is to just create a new list:

   .. code:: python

      numbers = ['1', '2', '3']
      converted_numbers = []
      for number in numbers:
          converted_numbers.append(int(number))
      print(converted_numbers)

5. .. code:: python

         row_count = int(input("Type the number of rows needed:")) 
         for column_count in range(1, row_count+1):
             # Print numbers from 1 to column_count
             for number in range(1, column_count+1): 
                 print(number, end=" ") 
             print()  # creates a new line for the next row

   If the user enters 5, we want to do a row with 1 column, then 2
   columns, and so on until 5 columns. That would be
   ``for column_count in range(1, 6)``, because the end of the range is
   excluded. In general, we need to specify ``row_count + 1`` so that it
   actually ends at ``row_count``. The second loop is similar.

   Usually ``print(number)`` puts a newline character at the end of the
   line, so that the next print goes to the next line. To get all
   numbers on the same line, we use a space instead of a newline
   character, but we still need ``print()`` to add a newline character
   once we have printed the entire row.

6. .. code:: python

      row_count=int(input("Type the number of rows needed:"))

      for line_number in range(1, row_count+1):
          for number in range(line_number, row_count+1):
              print(number, end=' ')
          print()

   Just like in the previous exercise, if the user enters 5, the first
   ``for`` loop gives the line numbers ``1, 2, 3, 4, 5``. For example,
   on line 2, we should print numbers from 2 to 5, as in
   ``range(2, 6)``, or in general, ``range(line_number, row_count+1)``.

Trey Hunner: zip and enumerate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Read some lines with ``input`` into a list and then enumerate it.

   .. code:: python

      print("Enter something, and press Enter without typing anything",
            "when you're done.")

      lines = []
      while True:
          line = input('>')
          if line == '':
              break
          lines.append(line)

      for index, line in enumerate(lines, start=1):
          print("Line", index, "is:", line)

2. Let’s start by trying out ``zip`` with strings:

   .. code:: python

      >>> for pair in zip('ABC', 'abc'):
      ...     print(pair)
      ...
      ('A', 'a')
      ('B', 'b')
      ('C', 'c')
      >>>

   Great, it works just like it works with lists. Now let’s create the
   letter printing program:

   .. code:: python

      uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      lowercase = 'abcdefghijklmnopqrstuvwxyz'

      for upper, lower in zip(uppercase, lowercase):
          print(upper, lower)

3. This one is a bit more difficult than the other two because we need
   to combine ``zip`` and ``enumerate``. One way to do this is to pass a
   ``zip`` result to ``enumerate``, like this:

   .. code:: python

      uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      lowercase = 'abcdefghijklmnopqrstuvwxyz'

      for index, letterpair in enumerate(zip(uppercase, lowercase), start=1):
          upper, lower = letterpair
          print(index, upper, lower)

   We can also save the zip result to a variable. I would probably do
   this.

   .. code:: python

      uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      lowercase = 'abcdefghijklmnopqrstuvwxyz'

      letterzip = zip(uppercase, lowercase)
      for index, letterpair in enumerate(letterzip, start=1):
          upper, lower = letterpair
          print(index, upper, lower)

   Another alternative is to pass an ``enumerate`` result to ``zip``.
   This is a bit more complicated, so I wouldn’t do it this way.

   .. code:: python

      uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      lowercase = 'abcdefghijklmnopqrstuvwxyz'

      for upper, indexlowerpair in zip(uppercase, enumerate(lowercase, start=1)):
          index, lower = indexlowerpair
          print(index, upper, lower)

Defining functions
^^^^^^^^^^^^^^^^^^

1. The problem with the first example is that name is a local variable.
   I explained how to fix this in `the output
   section <defining-functions.md#output>`__:

   .. code:: python

      def ask_name():
          name = input("Enter your name: ")
          return name

      print("Your name is", ask_name())

2. If you run the next example, you get something like this:

   ::

       <function get_greeting at 0xb73a0a04>

   The problem is that we print the actual ``get_greeting`` function,
   but we need to **call** it like ``get_greeting()``:

   .. code:: python

      def get_greeting():
          return "Hello World!"

      print(get_greeting())

3. See `the return or print
   section <defining-functions.md#return-or-print>`__.

   The greet function prints a greeting.

   .. code:: python

      >>> greet("World")
      Hello World
      >>>

   But it also returns None because we don’t tell it to return anything
   else.

   .. code:: python

      >>> return_value = greet("World")
      Hello World
      >>> print(return_value)
      None
      >>>

   This code from the exercise does the same thing as the code above
   does, but without a temporary ``return_value`` variable:

   .. code:: python

      >>> print(greet("World"))
      Hello World
      None
      >>>


If you have trouble with this tutorial, please `tell me about
it <../contact-me.md>`__ and I’ll make this tutorial better, or `ask for
help online <../getting-help.md>`__. If you like this tutorial, please
`give it a
star <../README.md#how-can-i-thank-you-for-writing-and-sharing-this-tutorial>`__.

You may use this tutorial freely at your own risk. See
`LICENSE <../LICENSE>`__.

`List of contents <../README.md#list-of-contents>`__
